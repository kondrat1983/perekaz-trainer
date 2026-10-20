"""Переводит SVG с контурами в стиль «аплікація з паперу».

Каждый залитый кусок теряет контур и получает под собой тень-копию
(#1E2433, прозрачность .2, сдвиг вправо-вниз). Тонкие линии без заливки
(брови, рот, прожилки) остаются полосками того же цвета. Градиенты
заменяются плоским средним цветом: бумага не бывает градиентной.

Запуск: python3 -I .claude/skills/illustrator/paperize.py images/a.svg [images/b.svg ...] [--every-piece]\n--every-piece: тень у каждого залитого куска, для фонов, где контуров нет.
Файлы перезаписываются на месте.
"""
import re
import sys
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
SHAPES = {'path', 'rect', 'circle', 'ellipse', 'polygon'}
SHADOW = '#1E2433'
INK = '#1E2433'


def tag(el):
    return el.tag.split('}')[-1]


def mix(colors):
    rgb = [tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for c in colors]
    return '#%02X%02X%02X' % tuple(sum(v[i] for v in rgb) // len(rgb) for i in range(3))


def flat_gradients(root):
    flat = {}
    for grad in root.iter():
        if tag(grad) in ('linearGradient', 'radialGradient'):
            stops = [s.get('stop-color') for s in grad if tag(s) == 'stop' and s.get('stop-color', '').startswith('#')]
            opaque = [s for s in grad if tag(s) == 'stop' and s.get('stop-opacity') in (None, '1')]
            # Градиент-свечение (с прозрачностью) оставляем: это свет, а не бумага.
            if stops and len(opaque) == len([s for s in grad if tag(s) == 'stop']):
                flat[grad.get('id')] = mix(stops)
    return flat


def shadow_offset(root):
    box = root.get('viewBox', '0 0 300 400').split()
    width = float(box[2])
    return (4, 5) if width >= 400 else (3, 4)


def covers_canvas(el, root):
    box = [float(v) for v in root.get('viewBox').split()]
    return tag(el) == 'rect' and float(el.get('width', 0)) >= box[2] and float(el.get('height', 0)) >= box[3] * 0.7


def lerp(a, b, t):
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02X%02X%02X' % tuple(round(x + (y - x) * t) for x, y in zip(ca, cb))


def band_sky(root, bands=4):
    """Вертикальный градиент неба режем на полосы цветной бумаги."""
    grads = {g.get('id'): g for g in root.iter() if tag(g) == 'linearGradient'}
    for parent in root.iter():
        for i, el in enumerate(list(parent)):
            fill = el.get('fill') or ''
            if not (tag(el) == 'rect' and fill.startswith('url(#') and covers_canvas(el, root)):
                continue
            grad = grads.get(fill[5:-1])
            if grad is None or grad.get('x1', '0') != grad.get('x2', '0'):
                continue
            stops = [(float(s.get('offset', 0)), s.get('stop-color')) for s in grad if tag(s) == 'stop']
            width, height = el.get('width'), float(el.get('height'))
            def color_at(t):
                for (o1, c1), (o2, c2) in zip(stops, stops[1:]):
                    if o1 <= t <= o2:
                        return lerp(c1, c2, (t - o1) / ((o2 - o1) or 1))
                return stops[-1][1] if t > stops[-1][0] else stops[0][1]
            parent.remove(el)
            for k in range(bands):
                rect = ET.Element(el.tag, {'x': '0', 'y': '%g' % (height * k / bands), 'width': width,
                                           'height': '%g' % (height / bands + 1), 'fill': color_at((k + .5) / bands)})
                parent.insert(i + k, rect)
            return


def convert(path, every_piece=False):
    """every_piece: тень у каждого залитого куска (фоны без контуров)."""
    tree = ET.parse(path)
    root = tree.getroot()
    flat = flat_gradients(root)
    dx, dy = shadow_offset(root)

    def walk(parent, inherited):
        children = list(parent)
        offset = 0
        for i, el in enumerate(children):
            name = tag(el)
            ctx = dict(inherited)
            for key in ('stroke', 'stroke-width', 'fill'):
                if el.get(key) is not None:
                    ctx[key] = el.get(key)
            if name == 'g':
                walk(el, ctx)
                for attr in ('stroke', 'stroke-width'):
                    el.attrib.pop(attr, None)
                continue
            if name not in SHAPES:
                continue
            fill = ctx.get('fill')
            if fill and fill.startswith('url(#'):
                gid = fill[5:-1]
                if gid in flat:
                    fill = flat[gid]
                    el.set('fill', fill)
            stroke = ctx.get('stroke')
            if fill == 'none' or (fill is None and ctx.get('stroke') not in (None, 'none')):
                # Тонкая полоска бумаги: цвет и толщина явные, контур группы больше не наследуется.
                el.set('stroke', stroke if stroke and stroke != 'none' else INK)
                el.set('stroke-width', ctx.get('stroke-width') or '2.5')
                continue
            had_outline = stroke not in (None, 'none')
            el.set('stroke', 'none')
            el.attrib.pop('stroke-width', None)
            tiny = name == 'circle' and float(el.get('r', 99)) < 4
            if not (had_outline or every_piece) or tiny or covers_canvas(el, root) or (fill or '').startswith('url('):
                continue
            shadow = ET.Element(el.tag, {k: v for k, v in el.attrib.items() if k not in ('id', 'class')})
            shadow.set('fill', SHADOW)
            shadow.set('opacity', '%.2f' % (0.2 * float(el.get('opacity', '1'))))
            shadow.set('transform', ('translate(%d %d) ' % (dx, dy) + el.get('transform', '')).strip())
            parent.insert(i + offset, shadow)
            offset += 1

    band_sky(root)
    walk(root, {'stroke': root.get('stroke'), 'stroke-width': root.get('stroke-width'), 'fill': root.get('fill')})
    for attr in ('stroke', 'stroke-width'):
        root.attrib.pop(attr, None)
    text = ET.tostring(root, encoding='unicode')
    text = re.sub(r'\s+/>', '/>', text)
    open(path, 'w', encoding='utf-8').write(text + '\n')


if __name__ == '__main__':
    every = '--every-piece' in sys.argv
    for file in [a for a in sys.argv[1:] if a.endswith('.svg')]:
        convert(file, every)
        print('paper:', file)
