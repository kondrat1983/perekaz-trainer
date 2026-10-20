"""Тварини та особливі персонажі для всіх творів. draw() пише файли й повертає шляхи."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from paper import *
from human import human, CLOTH
import animals as A
import fox as F
K = '#1E2433'
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
SHARED = {'fox': 'images/painted-fox/fox.svg', 'wolf': 'images/painted-fox/wolf.svg',
          'bear': 'images/painted-fox/bear.svg', 'dog': 'images/painted-fox/dog.svg',
          'hen': 'images/painted-fox/hen.svg', 'angel': 'images/angel.svg'}

def brows(x1, x2, y, mood, w=4):
    if mood == 'sad': return [S(f'M{x1-7} {y+2}L{x1+6} {y-4}', K, w), S(f'M{x2-6} {y-4}L{x2+7} {y+2}', K, w)]
    if mood == 'angry': return [S(f'M{x1-7} {y-4}L{x1+7} {y+3}', K, w), S(f'M{x2-7} {y+3}L{x2+7} {y-4}', K, w)]
    if mood == 'scared': return [S(f'M{x1-7} {y-2}Q{x1} {y-10} {x1+7} {y-4}', K, w), S(f'M{x2-7} {y-4}Q{x2} {y-10} {x2+7} {y-2}', K, w)]
    return [S(f'M{x1-7} {y}Q{x1} {y-5} {x1+7} {y-1}', K, w), S(f'M{x2-7} {y-1}Q{x2} {y-5} {x2+7} {y}', K, w)]

def canine(pal, mood, label):
    """Шакал / вовчиця: геометрія лиса з іншою палітрою."""
    m = {'neutral': 'sly', 'happy': 'proud', 'sad': 'scared', 'scared': 'scared', 'angry': 'sly'}[mood]
    return F.fox(pal, m, label=label)

JACKAL = dict(base='#C9A060', light='#E3C08A', dark='#9C7A40', bib='#F4E6CC', sock='#5A4630', ear='#6B4630')
JACKAL_BLUE = dict(base='#3B6FD0', light='#6A95E8', dark='#2A52A8', bib='#9DB8EE', sock='#1E2A4E', ear='#22305A')
SHEWOLF = dict(base='#8A8FA3', light='#B7BBC8', dark='#6B7086', bib='#D9DBE3', sock='#4A4E60', ear='#4A4E60')

def lion(mood):
    b = []
    b.append(P('path d="M96 380Q60 360 50 320Q74 340 100 344Z"', '#C9A060'))
    b.append(P('circle cx="46" cy="318" r="10"', '#8A5A34'))
    b.append(P('path d="M100 386Q86 300 126 246Q160 210 204 236Q230 310 216 386Z"', '#E3B060'))
    b.append(D('path d="M204 236Q230 310 216 386H196Q214 310 192 232Z"', '#C9913E'))
    b.append(P('ellipse cx="128" cy="346" rx="40" ry="42"', '#E3B060'))
    for x in (150, 184):
        b.append(P(f'rect x="{x}" y="296" width="26" height="90" rx="12"', '#E3B060'))
    import math
    pts = []
    for i in range(18):
        a = i / 18 * 2 * math.pi
        r = 92 if i % 2 == 0 else 74
        pts.append(f'{170 + r*math.cos(a):.0f} {160 + r*math.sin(a):.0f}')
    b.append(P('path d="M' + 'L'.join(pts) + 'Z"', '#B9692E'))
    b.append(P('circle cx="170" cy="160" r="56"', '#E3B060'))
    b.append(P('ellipse cx="176" cy="190" rx="30" ry="22"', '#F4E0B0', '', '2 3'))
    b.append(P('path d="M164 176h24l-12 12Z"', '#6B4630', '', '1 2'))
    b.append(eye(150, 152, 6.5)); b.append(eye(192, 152, 6.5))
    b += brows(150, 192, 138, mood)
    if mood == 'angry':
        b.append(P('path d="M160 198Q176 220 192 198Z"', '#9C3A30', '', '1 2'))
        b.append(D('path d="M164 199l4 7 4-7ZM180 199l4 7 4-7Z"', '#FFFFFF'))
    else:
        b.append(S('M164 200Q176 208 188 200', K, 3))
    return svg('0 0 300 400', 'Лев', b)

def mouse(mood):
    b = [S('M70 330Q20 320 30 270', '#C9A8A0', 4)]
    b.append(P('path d="M60 340Q60 250 150 250Q230 252 250 300Q240 344 170 346H70Z"', '#A8A6B4'))
    b.append(P('circle cx="150" cy="226" r="34"', '#A8A6B4'))
    b.append(P('circle cx="196" cy="230" r="30"', '#A8A6B4'))
    b.append(D('circle cx="150" cy="226" r="20"', '#E8A0A0'))
    b.append(P('path d="M180 260Q230 250 266 290Q240 306 200 300Z"', '#BDBBC8'))
    b.append(P('circle cx="266" cy="290" r="7"', '#E8A0A0', '', '1 2'))
    b.append(eye(228, 276, 5)); b += brows(228, 228, 264, mood, 3)[:1]
    b.append(S('M262 296l26-4M262 300l26 6', K, 1.6))
    return svg('0 0 300 400', 'Миша', b)

def bird(kind, mood):
    col = {'lark': ('#A07A52', '#C9A87A', '#F0DCC0'), 'crow': ('#2E3242', '#4A4E60', '#6B7086'),
           'eagle': ('#6B4630', '#8A5A34', '#FFFFFF')}[kind]
    b = []
    b.append(P('path d="M60 150L10 120L30 160L8 200L70 176Z"', col[0]))
    b.append(P('path d="M60 170Q120 110 210 120Q250 130 250 150Q236 190 170 196Q100 200 60 170Z"', col[1]))
    b.append(P('path d="M110 150Q120 60 200 40Q190 100 170 150Z"', col[0]))
    b.append(D('path d="M130 146Q140 90 186 64Q176 110 160 146Z"', col[1]))
    hc = col[2] if kind == 'eagle' else col[1]
    b.append(P('circle cx="236" cy="132" r="30"', hc))
    beak = '#E8B23A' if kind != 'crow' else '#2E3242'
    b.append(P('path d="M262 126L296 140L262 150Z"' if kind != 'eagle' else 'path d="M260 124Q300 126 290 160Q282 148 262 150Z"', beak, '', '2 2'))
    b.append(eye(244, 126, 6))
    b += brows(244, 244, 112, mood, 3)[:1]
    if kind == 'lark':
        b.append(P('path d="M226 104L232 84L244 104Z"', col[0], '', '1 2'))
    b.append(S('M150 196v20M170 194v22', '#E8B23A', 4))
    return svg('0 0 300 220', {'lark': 'Жайворонок', 'crow': 'Ворона', 'eagle': 'Орел'}[kind], b)

def horse(mood, color='#8A5A34', mane='#2E3242', label='Кінь'):
    b = []
    for x in (80, 110, 190, 220):
        b.append(P(f'rect x="{x}" y="250" width="22" height="130" rx="9"', color))
        b.append(D(f'rect x="{x}" y="364" width="22" height="16" rx="4"', K))
    b.append(P('path d="M50 220Q20 260 34 320Q50 280 70 250Z"', mane))
    b.append(P('ellipse cx="150" cy="240" rx="104" ry="52"', color))
    b.append(P('path d="M210 230L230 120Q250 90 284 110L296 150Q280 160 262 150L250 240Z"', color))
    b.append(P('path d="M226 130Q232 96 262 92L240 200Z"', mane))
    b.append(P('path d="M240 100L248 76L258 98Z"', color, '', '1 2'))
    b.append(P('ellipse cx="286" cy="146" rx="14" ry="10"', '#6B4630', '', '1 2'))
    b.append(eye(262, 118, 5.5))
    b += brows(262, 262, 106, mood, 3)[:1]
    return svg('0 0 300 400', label, b)

def snake(mood, color='#5E9A4C', label='Змія'):
    b = []
    b.append(P('path d="M40 360Q40 300 120 310Q200 320 200 270Q200 220 150 220Q120 220 130 190Q150 160 210 170Q250 180 240 150"', 'none'))
    b.append(S('M40 360Q40 300 120 310Q200 320 200 270Q200 220 150 220Q120 220 130 190', color, 34))
    b.append(S('M40 360Q40 300 120 310Q200 320 200 270Q200 220 150 220Q120 220 130 190', '#8CBF76', 10))
    b.append(P('ellipse cx="150" cy="168" rx="40" ry="28"', color))
    b.append(eye(138, 160, 6)); b.append(eye(166, 160, 6))
    b += brows(138, 166, 148, mood, 3)
    b.append(S('M188 176l20 4l6 -6M208 180l6 6', '#C24A3E', 2.5))
    return svg('0 0 300 400', label, b)

def dragon(mood, label='Змій'):
    g, gl, gd = '#5E9A4C', '#8CBF76', '#47783A'
    b = []
    b.append(P('path d="M60 300Q10 320 20 380Q60 340 90 340Z"', gd))
    b.append(P('path d="M110 180L40 60L150 150Z"', gd))
    b.append(P('path d="M190 170L270 50L230 180Z"', gd))
    b.append(P('path d="M70 330Q60 220 150 200Q240 210 236 330Q220 386 150 386Q80 386 70 330Z"', g))
    b.append(P('ellipse cx="150" cy="320" rx="44" ry="54"', '#E8D6A0'))
    for y in (290, 315, 340): b.append(S(f'M118 {y}H182', '#C9B27A', 3))
    for x in (100, 196): b.append(P(f'rect x="{x-14}" y="350" width="30" height="36" rx="12"', g))
    for i, dx in enumerate((-60, 0, 60)):
        hx, hy = 150 + dx, 120 - (20 if dx == 0 else 0)
        b.append(P(f'rect x="{hx-14}" y="{hy+20}" width="28" height="{200-hy}" rx="12"', g))
        b.append(P(f'ellipse cx="{hx}" cy="{hy}" rx="34" ry="28"', g))
        b.append(P(f'path d="M{hx-20} {hy-20}L{hx-14} {hy-44}L{hx-4} {hy-24}Z"', gl, '', '1 2'))
        b.append(P(f'path d="M{hx+4} {hy-24}L{hx+14} {hy-44}L{hx+20} {hy-20}Z"', gl, '', '1 2'))
        b.append(eye(hx - 12, hy - 4, 5)); b.append(eye(hx + 12, hy - 4, 5))
        b += brows(hx - 12, hx + 12, hy - 14, 'angry' if mood == 'neutral' else mood, 3)
        b.append(P(f'path d="M{hx-14} {hy+12}Q{hx} {hy+24} {hx+14} {hy+12}Z"', '#9C3A30', '', '1 2'))
    return svg('0 0 300 400', label, b)

def fish(mood, color='#E8B23A', label='Рибка'):
    b = [P('path d="M60 110L20 70L24 150Z"', '#B9821C'),
         P('path d="M50 110Q120 40 220 90Q250 110 220 130Q120 180 50 110Z"', color),
         D('path d="M110 80Q150 100 120 140Q170 110 150 72Z"', '#F6CE5B')]
    b.append(eye(200, 100, 7))
    b += brows(200, 200, 86, mood, 3)[:1]
    return svg('0 0 300 220', label, b)

def cat(mood, label='Кіт'):
    pal = dict(base='#8A8FA3', light='#B7BBC8', dark='#6B7086', bib='#FFFFFF', sock='#FFFFFF', ear='#E8A0A0')
    return F.fox(pal, {'neutral': 'sly', 'happy': 'proud'}.get(mood, 'scared'), label=label)

def ox(mood, label='Віл'):
    c = '#8A5A34'
    b = []
    for x in (70, 100, 200, 230):
        b.append(P(f'rect x="{x}" y="260" width="26" height="120" rx="10"', c))
    b.append(P('ellipse cx="150" cy="250" rx="110" ry="60"', c))
    b.append(D('ellipse cx="120" cy="230" rx="40" ry="24"', '#F1ECE2'))
    b.append(P('path d="M220 160Q170 140 176 120M280 160Q330 140 324 120"', 'none'))
    b.append(S('M220 170Q180 150 190 120M290 170Q330 150 320 120', '#F1ECE2', 10))
    b.append(P('ellipse cx="256" cy="210" rx="44" ry="48"', c))
    b.append(P('ellipse cx="262" cy="242" rx="30" ry="20"', '#D9B48A', '', '2 3'))
    b.append(eye(240, 196, 6)); b.append(eye(274, 196, 6))
    b += brows(240, 274, 182, mood, 3)
    return svg('0 0 340 400', label, b)

def waterbird(kind, mood):
    white = kind == 'swan'
    c = ('#FFFFFF', '#F1ECE2', '#D8D0C0') if white else ('#D9DBE3', '#B7BBC8', '#8A8FA3')
    b = [P('path d="M40 150Q60 210 160 210Q240 210 250 160Q200 170 160 130Q100 100 40 150Z"', c[1]),
         D('path d="M80 150Q120 130 170 160Q120 180 80 150Z"', c[2]),
         S('M210 170Q260 140 230 90Q210 50 250 30', c[0], 22),
         P('path d="M262 30L292 40L264 50Z"', '#E8B23A' if white else '#F29A5E', '', '1 2')]
    b.append(eye(254, 34, 4.5))
    return svg('0 0 300 220', 'Лебідь' if white else 'Гуска', b)

def frog(mood):
    g = '#5E9A4C'
    b = [P('ellipse cx="150" cy="150" rx="90" ry="54"', g), D('ellipse cx="150" cy="166" rx="60" ry="30"', '#C8E0A0'),
         P('circle cx="110" cy="96" r="26"', g), P('circle cx="190" cy="96" r="26"', g)]
    b.append(eye(110, 94, 10)); b.append(eye(190, 94, 10))
    b.append(S('M110 156Q150 180 190 156', K, 3))
    for x in (70, 230): b.append(P(f'ellipse cx="{x}" cy="196" rx="30" ry="12"', g))
    return svg('0 0 300 220', 'Жаба', b)

def elephant(mood):
    c = '#8A8FA3'
    b = []
    for x in (60, 100, 190, 230): b.append(P(f'rect x="{x}" y="250" width="34" height="130" rx="12"', c))
    b.append(P('ellipse cx="150" cy="230" rx="120" ry="80"', c))
    b.append(P('ellipse cx="240" cy="180" rx="56" ry="60"', c))
    b.append(P('path d="M190 150Q150 170 160 240Q200 250 214 210Z"', '#6B7086'))
    b.append(S('M280 200Q300 270 270 320Q262 330 254 318', c, 24))
    b.append(eye(262, 166, 6)); b += brows(262, 262, 152, mood, 3)[:1]
    b.append(S('M276 220l20 14', '#F1ECE2', 8))
    return svg('0 0 340 400', 'Слон', b)

def camel(mood):
    c = '#D9A86A'
    b = []
    for x in (80, 110, 200, 230): b.append(P(f'rect x="{x}" y="250" width="20" height="130" rx="8"', c))
    b.append(P('path d="M60 260Q60 200 110 196Q130 140 160 196Q180 140 210 196Q260 200 260 260Z"', c))
    b.append(S('M250 230Q280 180 270 120', c, 30))
    b.append(P('ellipse cx="286" cy="112" rx="30" ry="20"', c))
    b.append(eye(286, 104, 5)); b += brows(286, 286, 92, mood, 3)[:1]
    return svg('0 0 340 400', 'Верблюд', b)

def deer(mood):
    return horse(mood, '#B9813E', '#8A5A34', 'Олень').replace('</svg>', S('M240 96Q230 50 210 40M236 70L210 66M256 92Q270 46 290 38M262 64L286 62', '#6B4630', 6) + '\n</svg>')

def rabbit(mood):
    c = '#B7BBC8'
    b = [P('ellipse cx="140" cy="320" rx="70" ry="60"', c), P('circle cx="80" cy="330" r="16"', '#FFFFFF'),
         P('path d="M150 200Q130 100 150 60Q170 100 170 200Z"', c), P('path d="M180 200Q190 110 220 80Q220 130 196 206Z"', c),
         P('circle cx="170" cy="230" r="44"', c), D('path d="M154 190Q150 120 158 90Q164 130 164 190Z"', '#E8A0A0')]
    b.append(eye(156, 222, 6)); b.append(eye(190, 222, 6))
    b += brows(156, 190, 208, mood, 3)
    b.append(P('circle cx="176" cy="246" r="5"', '#E8A0A0', '', '1 1'))
    return svg('0 0 300 400', 'Заєць', b)

def sun(mood, moon=False):
    import math
    b = []
    if not moon:
        for i in range(12):
            a = i / 12 * 2 * math.pi
            b.append(P(f'path d="M{150+70*math.cos(a-0.12):.0f} {110+70*math.sin(a-0.12):.0f}L{150+104*math.cos(a):.0f} {110+104*math.sin(a):.0f}L{150+70*math.cos(a+0.12):.0f} {110+70*math.sin(a+0.12):.0f}Z"', '#F6CE5B'))
        b.append(P('circle cx="150" cy="110" r="66"', '#E8B23A'))
    else:
        b.append(P('path d="M170 20A90 90 0 1 0 170 200A70 70 0 1 1 170 20Z"', '#F6CE5B'))
    b.append(eye(128, 104, 6)); b.append(eye(166, 104, 6))
    b.append(S('M130 136Q148 150 166 136', K, 3))
    return svg('0 0 300 220', 'Місяць' if moon else 'Сонце', b)

def special(what, look, mood, label):
    base = dict(look)
    base.setdefault('sex', 'f'); base.setdefault('age', 'young')
    if what == 'mermaid':
        s = human(dict(base, outfit_type='dress', outfit=base.get('outfit', 'green')), mood, label)
        tail = (P('path d="M90 300Q150 330 210 300Q200 360 160 370L196 396H104L140 370Q100 360 90 300Z"', '#3F9A8A')
                + D('path d="M110 320Q150 336 190 320Q170 340 150 342Q130 340 110 320Z"', '#6ACBB8'))
        # ховаємо ноги й поділ сукні під хвостом: хвіст поверх
        return s.replace('</svg>', tail + '\n</svg>')
    if what == 'fairy':
        wings = (P('path d="M150 220Q60 120 50 200Q60 260 150 240Z"', '#9EC3E6', '', '2 3') +
                 P('path d="M150 220Q240 120 250 200Q240 260 150 240Z"', '#9EC3E6', '', '2 3'))
        s = human(dict(base, outfit_type='dress', outfit=base.get('outfit', 'blue')), mood, label)
        i = s.index('>', s.index('<svg')) + 1
        return s[:i] + '\n' + wings + s[i:]
    if what == 'elf':
        wings = (P('path d="M150 230Q80 150 70 210Q80 260 150 246Z"', '#C9A8E0', '', '2 3') +
                 P('path d="M150 230Q220 150 230 210Q220 260 150 246Z"', '#C9A8E0', '', '2 3'))
        s = human(dict(base, age='child', outfit_type='dress', outfit=base.get('outfit', 'white'), headwear='wreath'), mood, label)
        i = s.index('>', s.index('<svg')) + 1
        return s[:i] + '\n' + wings + s[i:]
    if what == 'genie':
        s = human(dict(base, sex='m', age='adult', skin='light', outfit='blue', outfit_type='tunic', headwear='turban', beard=True, hair='black'), mood, label)
        s = s.replace('#F2C9A0', '#7FAAF5').replace('#E2B48C', '#6A95E8')
        smoke = P('path d="M100 300Q150 330 200 300Q210 350 160 360Q120 370 150 396Q90 380 110 350Q80 330 100 300Z"', '#9EC3E6')
        return s.replace('</svg>', smoke + '\n</svg>')
    if what == 'witch':
        return human(dict(base, sex='f', age='old', outfit='black', outfit_type='robe', headwear='hood', item=base.get('item', 'staff'), hair='grey'), mood, label)
    if what == 'knight':
        return human(dict(base, sex='m', outfit='blue', outfit_type='armor', headwear='helmet', item=base.get('item', 'sword')), mood, label)
    if what == 'giant':
        return human(dict(base, sex='m', age='adult', outfit='brown', outfit_type='tunic', beard=True, item='hammer'), mood, label)
    if what == 'ghost':
        return svg('0 0 300 400', label, [P('path d="M80 380V160Q80 80 150 80Q220 80 220 160V380L196 356L172 380L150 356L128 380L104 356Z"', '#F1ECE2'), eye(128, 160, 7), eye(172, 160, 7)])
    if what in ('sun', 'moon'):
        return sun(mood, what == 'moon')
    return human(base, mood, label)

def crane(mood):
    b = [S('M130 200L120 380M160 200L170 380', '#4A4E60', 5),
         P('path d="M60 170Q90 120 180 130Q220 140 210 180Q180 210 110 206Q70 200 60 170Z"', '#B7BBC8'),
         P('path d="M60 170L20 200L70 196Z"', '#2E3242'),
         S('M196 150Q220 100 200 50', '#B7BBC8', 14),
         P('circle cx="204" cy="46" r="18"', '#D9DBE3'), P('circle cx="206" cy="34" r="8"', '#C24A3E', '', '1 1'),
         P('path d="M218 44L290 56L218 56Z"', '#4A4E60', '', '1 2')]
    b.append(eye(208, 44, 4.5))
    return svg('0 0 300 400', 'Журавель', b)

def lizard(mood):
    c, l = '#2E3242', '#4A4E60'
    b = [S('M40 330Q10 300 30 260', c, 18),
         P('path d="M40 330Q60 270 150 270Q240 270 270 300Q240 340 150 340Q80 344 40 330Z"', c)]
    for x in range(70, 240, 24): b.append(P(f'path d="M{x} 274L{x+10} 250L{x+20} 274Z"', l, '', '1 2'))
    for x in (90, 130, 190, 230): b.append(P(f'rect x="{x-8}" y="326" width="18" height="40" rx="6"', c))
    b.append(P('path d="M250 280Q290 270 296 300Q286 320 250 316Z"', c))
    b.append(P('circle cx="270" cy="290" r="7"', '#E8B23A', '', '1 1')); b.append(D('ellipse cx="271" cy="290" rx="2" ry="5"', K))
    return svg('0 0 300 400', 'Ящір', b)

def render(kind, look, mood, label):
    if kind == 'crane': return crane(mood)
    if kind == 'lizard': return lizard(mood)
    if kind == 'jackal':
        if mood.startswith('blue'):
            return canine(JACKAL_BLUE, {'blue': 'happy', 'bluescared': 'scared', 'bluehowl': 'happy'}[mood], label)
        return canine(JACKAL, mood, label)
    if kind == 'she-wolf': return canine(SHEWOLF, mood, label)
    if kind == 'lion': return lion(mood)
    if kind == 'mouse': return mouse(mood)
    if kind in ('lark', 'crow', 'eagle'): return bird(kind, mood)
    if kind == 'horse': return horse(mood, label=label)
    if kind == 'snake': return snake(mood, label=label)
    if kind == 'dragon': return dragon(mood, label)
    if kind == 'fish': return fish(mood, label=label)
    if kind == 'cat': return cat(mood, label)
    if kind == 'ox': return ox(mood, label)
    if kind in ('goose', 'swan'): return waterbird(kind, mood)
    if kind == 'frog': return frog(mood)
    if kind == 'elephant': return elephant(mood)
    if kind == 'camel': return camel(mood)
    if kind == 'deer': return deer(mood)
    if kind == 'rabbit': return rabbit(mood)
    if kind == 'fox': return F.fox(F.RED, {'neutral': 'sly', 'happy': 'proud'}.get(mood, 'scared'), label=label)
    if kind == 'wolf': return A.wolf('scared' if mood in ('scared', 'sad') else 'calm')
    if kind == 'bear': return A.bear()
    if kind == 'dog': return A.dog()
    return special(kind, look, mood, label)

def draw(kind, look, label, base, poses):
    poses = list(poses)
    if kind in SHARED and not poses:
        return {'img': REPO + '/' + SHARED[kind], 'poses': {}}
    open(base + '.svg', 'w').write(render(kind, look, 'neutral', label))
    res = {'img': base + '.svg', 'poses': {}}
    for p in poses:
        open(f'{base}-{p}.svg', 'w').write(render(kind, look, p, label))
        res['poses'][p] = f'{base}-{p}.svg'
    return res

if __name__ == '__main__':
    out = sys.argv[1]
    for k in ['jackal', 'she-wolf', 'lion', 'mouse', 'lark', 'crow', 'eagle', 'horse', 'snake', 'dragon', 'fish', 'cat', 'ox', 'goose', 'swan', 'frog', 'elephant', 'camel', 'deer', 'rabbit', 'mermaid', 'fairy', 'elf', 'genie', 'witch', 'knight', 'giant', 'ghost', 'sun', 'moon']:
        open(f'{out}/{k}.svg', 'w').write(render(k, {}, 'neutral', k))
