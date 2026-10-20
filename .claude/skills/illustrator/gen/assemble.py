"""План твору (plans/<id>.json) -> data/works/<id>/*.json і картинки персонажів."""
import json, os, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from human import human
import animals2
from items import ITEMS
ALIAS = {}

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
BG = {'forest': 'images/bg/forest.svg', 'glade': 'images/bg/glade.svg', 'market': 'images/painted-fox/market.svg',
      'village': 'images/bg/village.svg', 'hut': 'images/bg/hut.svg', 'palace': 'images/bg/palace.svg',
      'east': 'images/bg/east.svg', 'sea': 'images/bg/sea.svg', 'river': 'images/bg/river.svg',
      'steppe': 'images/bg/steppe.svg', 'mountains': 'images/bg/mountains.svg', 'cave': 'images/bg/cave.svg',
      'sky': 'images/bg/sky.svg', 'field': 'images/bg/field.svg', 'winter': 'images/bg/winter.svg',
      'hills-kyiv': 'images/bg/hills.svg', 'garden': 'images/bg/garden.svg', 'room': 'images/bg/room.svg'}
SHARED = {'fox': 'images/painted-fox/fox.svg', 'wolf': 'images/painted-fox/wolf.svg',
          'bear': 'images/painted-fox/bear.svg', 'dog': 'images/painted-fox/dog.svg',
          'hen': 'images/painted-fox/hen.svg', 'angel': 'images/angel.svg'}
FLY = {'lark', 'eagle', 'crow', 'sun', 'moon', 'fairy', 'angel', 'ghost', 'swan', 'goose_fly'}
SIZE = {'mouse': 22, 'lark': 20, 'crow': 24, 'frog': 22, 'rabbit': 34, 'hen': 30, 'cat': 40, 'fish': 22, 'snake': 30,
        'goose': 34, 'swan': 40, 'eagle': 34, 'fox': 52, 'jackal': 54, 'dog': 54, 'wolf': 60, 'she-wolf': 60,
        'deer': 70, 'lion': 66, 'bear': 70, 'horse': 76, 'ox': 70, 'camel': 80, 'elephant': 84, 'dragon': 84,
        'sun': 30, 'moon': 30, 'giant': 92, 'crane': 64, 'lizard': 46}

def kind_of(look):
    return look.get('animal') or look.get('what') or 'human'

def height(look):
    k = kind_of(look)
    if look.get('type') == 'human' or k in ('knight', 'witch', 'elf', 'fairy', 'mermaid', 'genie', 'ghost', 'angel'):
        return {'child': 58}.get(look.get('age'), 70)
    return SIZE.get(k, 50)

def layout(actors, chars):
    """Розставляє акторів: персонажі в ряд, предмет — біля попереднього персонажа."""
    out = []
    people = [a for a in actors if 'char' in a]
    n = len(people) or 1
    xs = {1: [42], 2: [30, 70], 3: [18, 50, 82], 4: [14, 38, 62, 86]}[min(n, 4)]
    i = 0
    last = None
    for a in actors:
        if 'char' in a:
            look = chars[a['char']]['look']
            h = height(look)
            if n >= 3: h = round(h * .85)
            e = {'char': a['char'], 'x': xs[min(i, len(xs) - 1)], 'bottom': 0, 'h': h}
            if kind_of(look) in FLY: e['bottom'] = 46; e['h'] = min(h, 30)
            if a.get('pose'): e['pose'] = a['pose']
            out.append(e); last = e; i += 1
        elif 'item' in a:
            e = {'img': a['_img'], 'alt': a['_alt'], 'x': 0, 'bottom': 4, 'h': 22}
            if last:
                e['x'] = min(92, last['x'] + 16); e['bottom'] = 18
            else:
                e['x'] = 50 if not out else 72
            out.append(e)
    return out

def build(plan_path):
    plan = json.load(open(plan_path))
    wid = plan['id']
    imgdir = f'images/{wid}'
    os.makedirs(f'{REPO}/{imgdir}', exist_ok=True)
    os.makedirs(f'{REPO}/data/works/{wid}', exist_ok=True)
    chars = {}
    for cid, c in plan['characters'].items():
        look = c['look']; k = kind_of(look)
        entry = {'name': c['name'], 'lname': c['lname'], 'acc': c['acc'], 'features': c['features']}
        poses = c.get('poses', [])
        if look.get('type') == 'human':
            entry['img'] = f'{imgdir}/{cid}.svg'
            open(f'{REPO}/{entry["img"]}', 'w').write(human(look, 'neutral', c['name']))
            entry['poses'] = {}
            for p in poses:
                path = f'{imgdir}/{cid}-{p}.svg'
                open(f'{REPO}/{path}', 'w').write(human(look, p, c['name']))
                entry['poses'][p] = path
        else:
            made = animals2.draw(k, look, c['name'], f'{REPO}/{imgdir}/{cid}', poses)
            entry['img'] = made['img'].replace(REPO + '/', '')
            entry['poses'] = {p: v.replace(REPO + '/', '') for p, v in made['poses'].items()}
        if not entry.get('poses'): entry.pop('poses', None)
        chars[cid] = entry
    looks = {cid: dict(c, look=plan['characters'][cid]['look']) for cid, c in chars.items()}
    items = {iid: (f'{imgdir}/item-{iid}.svg', desc) for iid, desc in plan.get('items', {}).items()}
    for iid, (path, desc) in items.items():
        fn = ITEMS.get(ALIAS.get(f'{wid}:{iid}', ALIAS.get(iid, iid)))
        if fn: open(f'{REPO}/{path}', 'w').write(fn(desc.split(' — ')[0][:40].capitalize()))
    def prep(actors):
        res = []
        for a in actors:
            a = dict(a)
            if 'item' in a:
                a['_img'], a['_alt'] = items[a['item']][0], items[a['item']][1][:40]
            res.append(a)
        return res
    scenes = []
    for n, s in enumerate(plan['scenes'], 1):
        sc = {'num': n, 'title': s['title']}
        if s.get('frames'):
            sc['summary'] = ' '.join(f['text'] for f in s['frames'])
        sc['bg'] = BG[s['bg']]
        sc['stage'] = layout(prep(s['stage']), looks)
        qs = {}
        for lv, q in s['questions'].items():
            q = dict(q)
            opts = []
            for o in q['options']:
                o = dict(o)
                if 'item' in o: o['img'] = items[o.pop('item')][0]
                opts.append(o)
            q['options'] = opts
            qs[lv] = q
        sc['questions'] = qs
        if s.get('frames'):
            sc['frames'] = [{'bg': BG[f.get('bg', s['bg'])], 'text': f['text'], 'actors': layout(prep(f['actors']), looks)} for f in s['frames']]
        scenes.append(sc)
    json.dump({'pairs': plan.get('pairs', []), 'scenes': scenes}, open(f'{REPO}/data/works/{wid}/scenes.json', 'w'), ensure_ascii=False, indent=2)
    open(f'{REPO}/data/works/{wid}/scenes.json', 'a').write('\n')
    json.dump(chars, open(f'{REPO}/data/works/{wid}/characters.json', 'w'), ensure_ascii=False, indent=2)
    open(f'{REPO}/data/works/{wid}/characters.json', 'a').write('\n')
    return plan, items

if __name__ == '__main__':
    for p in sys.argv[1:]:
        plan, items = build(p)
        missing = [i for i, (path, _) in items.items() if not os.path.exists(f'{REPO}/{path}')]
        print(plan['id'], 'ok; items to draw:', missing)
