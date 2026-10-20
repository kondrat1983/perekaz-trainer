"""Предмети 200x200 у стилі аплікації. ITEMS[назва] -> функція."""
import sys, math
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
from scenery import barrel as _barrel, crown as _crown, hen as _hen
K = '#1E2433'
def V(label, b): return svg('0 0 200 200', label, b)
GOLD = ('#F6CE5B', '#E8B23A', '#B9821C')

def book(l='Книжка'):
    return V(l, [P('path d="M100 60Q60 40 20 50V160Q60 150 100 170Z"', '#FFFFFF'), P('path d="M100 60Q140 40 180 50V160Q140 150 100 170Z"', '#F1ECE2'),
                 D('path d="M96 60H104V170H96Z"', '#C24A3E'), S('M36 80Q60 74 86 84M36 100Q60 94 86 104M114 84Q140 74 164 80M114 104Q140 94 164 100', '#8A8FA3', 3)])
def bread(l='Паляниця'):
    return V(l, [P('ellipse cx="100" cy="120" rx="80" ry="50"', '#C98A3E'), D('ellipse cx="90" cy="108" rx="60" ry="30"', '#E0A85A'),
                 S('M60 100Q100 80 140 100M70 120Q100 104 130 120', '#9C6A2E', 4)])
def sprout(l='Паросток'):
    return V(l, [P('path d="M40 170Q100 140 160 170V190H40Z"', '#8A5A34'), S('M100 170V90', '#5E9A4C', 6),
                 P('path d="M100 120Q60 110 50 70Q90 80 100 120Z"', '#8CBF76'), P('path d="M100 100Q140 90 150 50Q110 60 100 100Z"', '#6E9F5A')])
def cabbage(l='Капуста'):
    return V(l, [P('circle cx="100" cy="110" r="70"', '#8CBF76'), D('circle cx="100" cy="110" r="46"', '#B8DCA0'), D('circle cx="100" cy="110" r="24"', '#D6EEC4'),
                 S('M100 40V180M40 110Q100 80 160 110', '#6E9F5A', 3)])
def potato(l='Картопля'):
    return V(l, [S('M100 90V30M100 60L70 40M100 50L130 30', '#5E9A4C', 5), P('ellipse cx="70" cy="40" rx="16" ry="10"', '#8CBF76'), P('ellipse cx="130" cy="30" rx="16" ry="10"', '#8CBF76'),
                 D('rect x="0" y="90" width="200" height="110"', '#8A5A34'), P('ellipse cx="60" cy="140" rx="34" ry="24"', '#D9B48A'), P('ellipse cx="140" cy="150" rx="30" ry="22"', '#D9B48A'),
                 S('M100 90L60 130M100 90L140 140', '#C9A87A', 3)])
def mirror(l='Дзеркало'):
    return V(l, [P('rect x="88" y="130" width="24" height="60" rx="8"', '#B9821C'), P('circle cx="100" cy="86" r="66"', '#E8B23A'), D('circle cx="100" cy="86" r="52"', '#C8E0F8'),
                 D('path d="M70 60Q80 44 100 40Q80 60 76 86Z"', '#FFFFFF', op='.8')])
def mosquito(l='Комар'):
    return V(l, [P('ellipse cx="100" cy="110" rx="34" ry="12"', '#6B7086'), P('circle cx="140" cy="104" r="12"', '#6B7086'), S('M150 106L186 112', K, 2),
                 P('ellipse cx="90" cy="80" rx="22" ry="34"', '#C8E0F8', ' rotate(-30 90 80)'), P('ellipse cx="110" cy="80" rx="20" ry="30"', '#DCEBF8', ' rotate(20 110 80)'),
                 S('M80 120L60 160M100 122L96 166M120 120L134 164', K, 2.5)])
def meat(l='Шматок м’яса'):
    return V(l, [P('path d="M40 120Q40 60 110 60Q170 64 170 120Q160 170 100 170Q40 168 40 120Z"', '#C24A3E'), D('path d="M60 110Q80 80 120 84Q90 100 80 130Z"', '#E07A6A'),
                 P('rect x="150" y="70" width="40" height="16" rx="8"', '#F1ECE2', ' rotate(-30 150 78)')])
def throne(l='Трон'):
    return V(l, [P('rect x="50" y="20" width="100" height="120" rx="10"', '#8A8FA3'), P('rect x="36" y="110" width="128" height="34" rx="6"', '#B7BBC8'),
                 P('rect x="44" y="140" width="22" height="50"', '#6B7086'), P('rect x="134" y="140" width="22" height="50"', '#6B7086'), D('rect x="66" y="40" width="68" height="60" rx="8"', '#C24A3E')])
def lamp(l='Лампа'):
    return V(l, [P('path d="M30 130Q30 90 90 90Q130 90 150 110L190 90L170 130Q140 150 30 130Z"', GOLD[1]), D('path d="M60 92Q90 60 120 92Z"', GOLD[2]),
                 P('ellipse cx="90" cy="150" rx="40" ry="10"', GOLD[2]), D('path d="M60 110Q90 100 120 110"', 'none'), S('M60 110Q90 100 120 110', GOLD[0], 4),
                 P('path d="M90 60q-8-14 0-24q8 10 0 24Z"', '#F29A5E', '', '1 2')])
def ring(l='Перстень'):
    return V(l, [S('M100 80m-46 0a46 46 0 1 0 92 0a46 46 0 1 0-92 0', GOLD[2], 18), S('M100 80m-46 0a46 46 0 1 0 92 0a46 46 0 1 0-92 0', GOLD[1], 10),
                 P('path d="M76 40L100 10L124 40L100 56Z"', '#C24A3E'), D('path d="M90 34L100 20L104 36Z"', '#EE8597')])
def coins(l='Монети'):
    b = []
    for x, y in ((60, 150), (100, 156), (140, 150), (80, 124), (120, 124), (100, 96)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="26"', GOLD[1])); b.append(D(f'circle cx="{x}" cy="{y}" r="16"', GOLD[0]))
    return V(l, b)
def gems(l='Самоцвіти'):
    b = [P('ellipse cx="100" cy="140" rx="90" ry="34"', '#B7BBC8'), D('ellipse cx="100" cy="132" rx="76" ry="24"', '#D9DBE3')]
    for x, y, c in ((60, 120, '#C24A3E'), (100, 110, '#2F6FD6'), (140, 120, '#5E9A4C'), (80, 100, '#E8B23A'), (120, 98, '#9C7CC4')):
        b.append(P(f'path d="M{x} {y-22}L{x+16} {y}L{x} {y+16}L{x-16} {y}Z"', c, '', '2 3'))
        b.append(D(f'path d="M{x} {y-18}L{x+6} {y-4}L{x-4} {y}Z"', '#FFFFFF', op='.6'))
    return V(l, b)
def grain(l='Зернятко'):
    return V(l, [P('ellipse cx="100" cy="100" rx="40" ry="70"', '#E8B23A', ' rotate(20 100 100)'), S('M90 40Q110 100 110 160', GOLD[2], 4)])
def egg(l='Яйце'):
    return V(l, [P('path d="M100 20Q160 20 164 110Q164 180 100 180Q36 180 36 110Q40 20 100 20Z"', '#F6CE5B'), D('path d="M70 60Q80 40 100 36Q80 60 76 90Z"', '#FFFFFF', op='.8'),
                 S('M44 110L70 96L90 116L110 96L130 116L156 100', '#C24A3E', 5)])
def herd(l='Череда'):
    b = []
    for x, y, s in ((60, 120, .8), (130, 130, .9), (90, 160, 1)):
        b.append(P(f'ellipse cx="{x}" cy="{y}" rx="{40*s}" ry="{22*s}"', '#8A5A34'))
        b.append(D(f'ellipse cx="{x-8}" cy="{y-4}" rx="{14*s}" ry="{9*s}"', '#F1ECE2'))
        b.append(P(f'circle cx="{x+40*s}" cy="{y-14*s}" r="{14*s}"', '#8A5A34'))
        b.append(S(f'M{x+32*s} {y-26*s}l-6 -10M{x+48*s} {y-26*s}l6 -10', '#F1ECE2', 3))
    return V(l, b)
def doves(l='Голуби з тіста'):
    b = []
    for x, flip in ((64, 1), (136, -1)):
        b.append(P(f'path d="M{x-40*flip} 130Q{x} 80 {x+30*flip} 110Q{x+44*flip} 100 {x+40*flip} 90Q{x+30*flip} 80 {x+20*flip} 92Q{x} 60 {x-30*flip} 110Z"', '#E0B87A'))
        b.append(D(f'circle cx="{x+30*flip}" cy="92" r="3"', K))
    return V(l, b)
def sapling(l='Саджанець'):
    return V(l, [P('path d="M60 160H140L130 196H70Z"', '#A06E44'), S('M100 160V70', '#8A5A34', 7), P('circle cx="100" cy="60" r="40"', '#6E9F5A'), D('circle cx="90" cy="50" r="22"', '#8CBF76')])
def apple(l='Золоте яблуко'):
    return V(l, [P('path d="M100 60Q160 30 170 100Q170 170 100 176Q30 170 30 100Q40 30 100 60Z"', GOLD[1]), D('path d="M60 80Q70 60 90 62Q70 80 66 110Z"', GOLD[0]),
                 S('M100 60Q104 40 110 30', '#6B4630', 5), P('path d="M110 40Q140 20 150 40Q130 54 110 40Z"', '#6E9F5A', '', '1 2')])
def rope(l='Аркан'):
    return V(l, [S('M40 160Q20 100 70 80Q130 60 120 120Q110 160 160 150', '#C9A87A', 10), S('M160 150m-24 0a24 18 0 1 0 48 0a24 18 0 1 0-48 0', '#C9A87A', 8)])
def casket(l='Скринька'):
    return V(l, [P('rect x="30" y="80" width="140" height="90" rx="8"', GOLD[1]), P('path d="M30 90Q100 30 170 90Z"', GOLD[0]), D('rect x="90" y="100" width="20" height="24" rx="4"', GOLD[2]),
                 P('ellipse cx="100" cy="58" rx="14" ry="18"', '#FFFFFF', '', '2 2')])
def tassel(l='Китичка'):
    b = [P('circle cx="100" cy="50" r="18"', GOLD[2])]
    for x in range(70, 131, 10):
        b.append(S(f'M100 64Q{x} 120 {x} 180', GOLD[1], 6))
    return V(l, b)
ITEMS = {k: v for k, v in globals().items() if callable(v) and not k.startswith('_') and k not in ('V', 'P', 'D', 'S', 'svg', 'eye')}
ITEMS['barrel'] = lambda l='Бочка': _barrel()
ITEMS['crown'] = lambda l='Корона': _crown()
ITEMS['hen'] = lambda l='Курка': _hen()

def basket(l='Кошик'):
    return V(l, [S('M40 100Q100 20 160 100', '#8A5A34', 8), P('path d="M30 100H170L150 180H50Z"', '#A06E44'),
                 S('M36 124H164M42 150H158', '#6B4630', 3), S('M70 100L76 178M100 100V180M130 100L124 178', '#6B4630', 3)])
def walls(l='Мури міста'):
    b = [P('rect x="10" y="80" width="180" height="110"', '#C9B27A')]
    for x in range(10, 190, 30): b.append(P(f'rect x="{x}" y="60" width="18" height="24"', '#C9B27A'))
    b.append(P('path d="M80 190V130Q100 106 120 130V190Z"', '#6B4630'))
    for y in (110, 140, 170): b.append(S(f'M10 {y}H70M130 {y}H190', '#A08A5A', 2))
    return V(l, b)
def well(l='Криниця'):
    return V(l, [P('rect x="90" y="20" width="10" height="110"', '#8A5A34'), P('path d="M40 20H170L150 4H60Z"', '#6B4630'),
                 S('M95 40H150V80', '#6B4630', 3), P('rect x="140" y="80" width="20" height="24" rx="3"', '#8A8FA3'),
                 P('path d="M40 110H160V190H40Z"', '#A06E44'), S('M40 136H160M40 162H160', '#6B4630', 3), D('ellipse cx="100" cy="110" rx="60" ry="8"', '#2F4580')])
def bush(l='Кущ калини'):
    b = [S('M100 190V120M100 150L70 110M100 140L130 100', '#6B4630', 6)]
    for x, y in ((60, 90), (100, 70), (140, 90), (80, 120), (124, 120)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="34"', '#5E9A4C'))
    for x, y in ((70, 110), (78, 104), (86, 112), (120, 84), (128, 92), (112, 92), (100, 130), (108, 136), (92, 136)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="7"', '#C24A3E', '', '1 1'))
    return V(l, b)
def beads(l='Намисто'):
    b = []
    for i in range(14):
        a = math.pi * (0.1 + 0.8 * i / 13)
        b.append(P(f'circle cx="{100-80*math.cos(a):.0f}" cy="{40+110*math.sin(a):.0f}" r="12"', '#C24A3E', '', '1 2'))
        b.append(D(f'circle cx="{97-80*math.cos(a):.0f}" cy="{37+110*math.sin(a):.0f}" r="3"', '#FFFFFF', op='.7'))
    return V(l, b)
def house(l='Хата'):
    return V(l, [P('rect x="30" y="90" width="140" height="90"', '#F4EFE6'), P('path d="M14 96Q100 10 186 96Z"', '#C9A15A'),
                 P('rect x="48" y="112" width="34" height="30"', '#3F5BA8'), P('rect x="112" y="118" width="32" height="62"', '#8A5A34')])
def millstones(l='Жорна'):
    return V(l, [P('ellipse cx="100" cy="150" rx="80" ry="26"', '#8A8FA3'), P('rect x="20" y="120" width="160" height="30"', '#8A8FA3'),
                 P('ellipse cx="100" cy="120" rx="80" ry="26"', '#B7BBC8'), D('ellipse cx="100" cy="120" rx="14" ry="5"', '#6B7086'),
                 P('rect x="150" y="70" width="12" height="50" rx="5"', '#8A5A34')])
def cloth(l='Рушник'):
    b = [P('rect x="30" y="20" width="140" height="170"', '#FFFFFF')]
    for y in (40, 160):
        for x in range(42, 160, 24):
            b.append(D(f'path d="M{x} {y}l10-10l10 10l-10 10Z"', '#C24A3E'))
        b.append(D(f'rect x="30" y="{y+16}" width="140" height="4"', '#2E3242'))
    for x in range(34, 170, 10): b.append(S(f'M{x} 190v8', '#C24A3E', 2))
    return V(l, b)
def rocks(l='Скелі'):
    return V(l, [P('path d="M10 190L40 90L80 120L110 50L150 110L190 80V190Z"', '#8A8FA3'), D('path d="M110 50L150 110L130 190H100Z"', '#6B7086', op='.6'),
                 D('path d="M40 90L60 100L50 190H30Z"', '#B7BBC8', op='.6')])
def castle(l='Замок'):
    b = [P('rect x="40" y="80" width="120" height="110"', '#D9DBE3')]
    for x in (20, 150):
        b.append(P(f'rect x="{x}" y="50" width="34" height="140"', '#C9CCD6')); b.append(P(f'path d="M{x-6} 52L{x+17} 10L{x+40} 52Z"', '#3F5BA8'))
    for x in range(40, 160, 22): b.append(P(f'rect x="{x}" y="66" width="14" height="16"', '#D9DBE3'))
    b.append(P('path d="M80 190V140Q100 118 120 140V190Z"', '#6B4630'))
    return V(l, b)
def baby(l='Немовля'):
    return V(l, [P('path d="M40 120Q40 80 100 80Q170 80 170 120Q170 170 100 170Q40 170 40 120Z"', '#FFFFFF'), S('M60 110Q100 140 150 110M70 140Q100 160 140 140', '#9EC3E6', 4),
                 P('circle cx="70" cy="96" r="30"', '#F2C9A0'), S('M58 94q4 -4 8 0M76 94q4 -4 8 0M64 108q6 4 12 0', '#1E2433', 2.5), D('circle cx="62" cy="104" r="5"', '#E8A0A0', op='.6')])
def sword_anvil(l='Меч у ковадлі'):
    return V(l, [P('path d="M30 190L50 150H150L170 190Z"', '#8A8FA3'), P('path d="M40 110H170Q160 140 130 140V150H70V140Q40 140 40 110Z"', '#4A4E60'),
                 P('path d="M94 112L106 112L104 20L100 8L96 20Z"', '#D9DBE3'), P('rect x="76" y="20" width="48" height="10" rx="4"', '#E8B23A'),
                 P('rect x="94" y="0" width="12" height="22" rx="4"', '#8A5A34'), D('rect x="99" y="30" width="2" height="76"', '#FFFFFF', op='.7')])
def golden_arrow(l='Золота стріла'):
    return V(l, [P('path d="M20 170L160 30L166 36L26 176Z"', '#E8B23A'), P('path d="M150 20L190 10L180 50Z"', '#F6CE5B'),
                 P('path d="M20 170L10 150L36 160ZM20 170L40 190L30 164Z"', '#C24A3E')])
def target(l='Мішень'):
    b = []
    for r, c in ((84, '#FFFFFF'), (64, '#C24A3E'), (44, '#FFFFFF'), (24, '#C24A3E')):
        b.append(P(f'circle cx="100" cy="100" r="{r}"', c, '', '2 3'))
    b.append(S('M100 100L150 40', '#8A5A34', 5))
    return V(l, b)
def rags(l='Лахміття'):
    return V(l, [P('path d="M40 40H160L150 180L130 160L110 186L90 160L70 186L50 166Z"', '#8A7A62'),
                 P('rect x="70" y="70" width="30" height="26"', '#A06E44', '', '1 2'), P('rect x="110" y="110" width="26" height="24"', '#6B7086', '', '1 2')])
ITEMS.update({k: v for k, v in dict(basket=basket, walls=walls, well=well, bush=bush, beads=beads, house=house, millstones=millstones, cloth=cloth,
              rocks=rocks, castle=castle, baby=baby, sword_anvil=sword_anvil, golden_arrow=golden_arrow, target=target, rags=rags).items()})

def town(l='Місто'):
    b = [P('path d="M0 190Q100 120 200 190Z"', '#6E9F5A')]
    for x, h in ((40, 50), (80, 70), (120, 56), (150, 44)):
        b.append(P(f'rect x="{x}" y="{150-h}" width="30" height="{h}"', '#C9A06A'))
        b.append(P(f'path d="M{x-4} {152-h}L{x+15} {130-h}L{x+34} {152-h}Z"', '#8A5A34'))
    for x in range(20, 190, 12): b.append(D(f'rect x="{x}" y="140" width="8" height="30" rx="3"', '#8A5A34'))
    return V(l, b)
def boat(l='Човен'):
    return V(l, [D('rect x="0" y="140" width="200" height="60"', '#4A7CC4'), P('path d="M10 120H190Q170 170 100 170Q30 170 10 120Z"', '#8A5A34'),
                 D('path d="M20 124H180Q176 134 170 140H30Q24 134 20 124Z"', '#A06E44'), S('M140 40L120 160', '#6B4630', 5)])
def chest(l='Скриня'):
    return V(l, [P('rect x="30" y="80" width="140" height="100" rx="6"', '#8A5A34'), P('path d="M30 90Q100 40 170 90Z"', '#A06E44'),
                 D('rect x="30" y="110" width="140" height="10"', '#E8B23A'), P('rect x="88" y="100" width="24" height="30" rx="4"', '#E8B23A'),
                 P('circle cx="70" cy="70" r="10"', '#C24A3E', '', '1 1'), P('circle cx="130" cy="66" r="10"', '#2F6FD6', '', '1 1')])
def redoubt(l='Редут'):
    return V(l, [P('path d="M10 190L40 110H160L190 190Z"', '#A08A5A'), D('path d="M40 110H160L170 130H30Z"', '#8A7A42'),
                 P('path d="M70 110V70H130V110Z"', '#C9A87A'), P('path d="M62 72L100 40L138 72Z"', '#8A7A42'), S('M100 40V10', '#6B4630', 4), P('path d="M100 10H130L100 24Z"', '#3F5BA8')])
def figure(l='Фігура зі смоляних бочок'):
    b = [S('M60 190L90 20M140 190L110 20M70 120H130M78 70H122', '#6B4630', 6)]
    for i, y in enumerate((170, 140, 110, 80, 50)):
        w = 50 - i * 6
        b.append(P(f'rect x="{100-w/2}" y="{y-22}" width="{w}" height="24" rx="6"', '#4A4E60'))
    return V(l, b)
def torch(l='Смолоскип'):
    return V(l, [P('rect x="90" y="80" width="20" height="110" rx="6"', '#8A5A34'), P('path d="M84 80H116L112 60H88Z"', '#4A4E60'),
                 P('path d="M100 0Q140 40 120 64H80Q60 40 100 0Z"', '#F29A5E'), D('path d="M100 24Q118 46 110 62H90Q84 46 100 24Z"', '#F6CE5B')])
def mace(l='Булава'):
    b = [P('rect x="92" y="80" width="16" height="110" rx="6"', '#6B4630'), P('circle cx="100" cy="60" r="40"', '#8A8FA3')]
    for a in range(0, 360, 45):
        x, y = 100 + 48 * math.cos(math.radians(a)), 60 + 48 * math.sin(math.radians(a))
        b.append(P(f'circle cx="{x:.0f}" cy="{y:.0f}" r="9"', '#6B7086', '', '1 1'))
    b.append(D('circle cx="88" cy="48" r="10"', '#B7BBC8'))
    return V(l, b)
def anvil(l='Ковадло'):
    return V(l, [P('path d="M30 190L50 150H150L170 190Z"', '#8A8FA3'), P('path d="M30 100H180Q170 136 136 136V150H70V136Q36 136 30 100Z"', '#4A4E60'),
                 P('rect x="120" y="30" width="12" height="70" rx="4"', '#8A5A34', ' rotate(30 126 60)'), P('rect x="120" y="20" width="44" height="22" rx="4"', '#6B7086', ' rotate(30 126 60)')])
def gate(l='Ворота'):
    return V(l, [P('rect x="10" y="40" width="40" height="150"', '#4A4E60'), P('rect x="150" y="40" width="40" height="150"', '#4A4E60'),
                 P('path d="M50 190V90Q100 40 150 90V190Z"', '#2E3242'), S('M60 100V190M80 80V190M100 70V190M120 80V190M140 100V190', '#6B7086', 4)])
def wall(l='Стіна фортеці'):
    b = []
    for x in range(10, 190, 24): b.append(P(f'path d="M{x} 190V50L{x+11} 34L{x+22} 50V190Z"', '#A06E44'))
    b.append(D('rect x="80" y="90" width="30" height="16"', '#2E3242'))
    return V(l, b)
def arrow(l='Стріла'):
    return V(l, [P('path d="M20 170L160 30L166 36L26 176Z"', '#8A5A34'), P('path d="M150 20L190 10L180 50Z"', '#8A8FA3'), P('path d="M20 170L10 150L36 160ZM20 170L40 190L30 164Z"', '#F1ECE2')])
def bag(l='Торбинка'):
    return V(l, [P('path d="M60 60Q40 120 50 170Q100 190 150 170Q160 120 140 60Z"', '#C9A87A'), S('M60 64Q100 76 140 64', '#8A5A34', 6),
                 P('ellipse cx="100" cy="56" rx="30" ry="10"', '#E8C46A')])
def kysil(l='Діжа з киселем'):
    return V(l, [P('path d="M40 70H160L150 180H50Z"', '#A06E44'), S('M44 100H156M48 150H152', '#6B4630', 4), P('ellipse cx="100" cy="70" rx="60" ry="14"', '#E3C9A0'),
                 S('M120 70L150 10', '#8A5A34', 6)])
def honey(l='Мед'):
    return V(l, [P('path d="M30 100H170Q160 170 100 170Q40 170 30 100Z"', '#3F5BA8'), P('ellipse cx="100" cy="100" rx="70" ry="16"', '#E8B23A'),
                 D('path d="M90 100q-4 30 6 40q6-30 -6-40Z"', '#E8B23A')])
def books(l='Книжки'):
    b = []
    for i, (c, w) in enumerate((('#C24A3E', 150), ('#3F5BA8', 130), ('#5E9A4C', 140), ('#E8B23A', 120))):
        y = 160 - i * 30
        b.append(P(f'rect x="{100-w/2}" y="{y}" width="{w}" height="28" rx="4"', c))
        b.append(D(f'rect x="{100-w/2+6}" y="{y+4}" width="{w-12}" height="4"', '#FFFFFF', op='.6'))
    return V(l, b)
def willow(l='Верба'):
    b = [P('path d="M90 190L96 90H104L110 190Z"', '#6B4630'), P('ellipse cx="100" cy="80" rx="70" ry="50"', '#8CBF76')]
    for x in range(40, 170, 14):
        b.append(S(f'M{x} 80Q{x+4} 130 {x} 160', '#6E9F5A', 4))
    return V(l, b)
def wagon(l='Віз'):
    return V(l, [P('path d="M20 100H180L170 140H30Z"', '#A06E44'), S('M30 110H170', '#6B4630', 3),
                 P('circle cx="60" cy="150" r="26"', '#6B4630'), D('circle cx="60" cy="150" r="8"', '#A06E44'),
                 P('circle cx="150" cy="150" r="26"', '#6B4630'), D('circle cx="150" cy="150" r="8"', '#A06E44'),
                 D('rect x="0" y="160" width="200" height="40"', '#8CBF76', op='.85')])
def flowers(l='Квіти'):
    b = []
    for x, c in ((40, '#C24A3E'), (80, '#F6CE5B'), (120, '#9C7CC4'), (160, '#FFFFFF')):
        b.append(S(f'M{x} 190V110', '#5E9A4C', 4))
        for dx, dy in ((0, -14), (12, -4), (-12, -4), (8, 10), (-8, 10)):
            b.append(P(f'circle cx="{x+dx}" cy="{100+dy}" r="8"', c, '', '1 1'))
        b.append(D(f'circle cx="{x}" cy="100" r="5"', '#E8B23A'))
    return V(l, b)
ITEMS.update(dict(town=town, boat=boat, gift=chest, chest=chest, redoubt=redoubt, figure=figure, torch=torch, mace=mace, anvil=anvil,
                  gate=gate, wall=wall, arrow=arrow, bag=bag, kysil=kysil, honey=honey, books=books, willow=willow, wagon=wagon, flowers=flowers,
                  kalyna=bush))
ITEMS['small-town'] = walls

def oven(l='Піч'):
    return V(l, [P('path d="M20 190V60Q100 30 180 60V190Z"', '#F4EFE6'), P('path d="M60 190V130Q100 96 140 130V190Z"', '#2E3242'),
                 D('path d="M74 160Q100 140 126 160V190H74Z"', '#F29A5E'), P('ellipse cx="100" cy="156" rx="22" ry="12"', '#C98A3E'),
                 S('M40 80Q60 70 70 86M140 80Q150 66 166 80', '#C24A3E', 3)])
def appletree(l='Яблуня'):
    b = [P('path d="M88 190L94 110H106L112 190Z"', '#6B4630'), P('circle cx="100" cy="80" r="70"', '#5E9A4C'), D('circle cx="80" cy="64" r="36"', '#8CBF76')]
    for x, y in ((60, 80), (90, 50), (130, 70), (110, 110), (70, 120), (140, 110)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="10"', '#C24A3E', '', '1 2'))
    return V(l, b)
def pillow(l='Перина'):
    b = [P('path d="M20 110Q20 70 60 74H140Q180 70 180 110Q180 160 140 156H60Q20 160 20 110Z"', '#FFFFFF'), D('path d="M40 100Q100 90 160 100"', 'none'),
         S('M40 100Q100 86 160 100', '#D8D0C0', 3)]
    for x, y in ((40, 40), (80, 20), (130, 36), (170, 20), (110, 10)):
        b.append(S(f'M{x-8} {y}H{x+8}M{x} {y-8}V{y+8}M{x-6} {y-6}L{x+6} {y+6}M{x+6} {y-6}L{x-6} {y+6}', '#9EC3E6', 2.5))
    return V(l, b)
def goldrain(l='Золотий дощ'):
    b = []
    for i in range(22):
        x, y = (i * 37) % 190 + 6, (i * 53) % 170 + 10
        b.append(P(f'circle cx="{x}" cy="{y}" r="9"', '#E8B23A', '', '1 2')); b.append(D(f'circle cx="{x-2}" cy="{y-2}" r="3"', '#F6CE5B'))
    return V(l, b)
def tar(l='Смола'):
    return V(l, [P('path d="M30 70H170L156 170Q100 190 44 170Z"', '#2E3242'), P('ellipse cx="100" cy="70" rx="70" ry="16"', '#1E2433'),
                 D('path d="M70 70q-6 40 6 60q6-40 -6-60ZM130 70q-4 30 6 46q4-30 -6-46Z"', '#1E2433'), S('M30 70Q10 40 40 30M170 70Q190 40 160 30', '#4A4E60', 5)])
def pumpkin(l='Гарбуз'):
    return V(l, [P('ellipse cx="100" cy="120" rx="84" ry="62"', '#E07A45'), D('ellipse cx="70" cy="120" rx="24" ry="58"', '#F29A5E'), D('ellipse cx="130" cy="120" rx="24" ry="58"', '#F29A5E'),
                 S('M100 60Q104 40 116 30', '#5E9A4C', 7), P('path d="M110 50Q140 30 160 50Q136 66 110 50Z"', '#6E9F5A', '', '1 2')])
def carriage(l='Карета'):
    return V(l, [P('path d="M40 140Q30 50 100 40Q170 50 160 140Z"', '#E8B23A'), D('path d="M70 110Q66 70 100 64Q134 70 130 110Z"', '#9EC3E6'),
                 P('path d="M90 40L100 18L110 40Z"', '#B9821C'), P('circle cx="60" cy="160" r="26"', '#B9821C'), D('circle cx="60" cy="160" r="8"', '#F6CE5B'),
                 P('circle cx="140" cy="160" r="26"', '#B9821C'), D('circle cx="140" cy="160" r="8"', '#F6CE5B')])
def clock(l='Годинник'):
    b = [P('rect x="60" y="20" width="80" height="170" rx="10"', '#8A5A34'), P('circle cx="100" cy="70" r="36"', '#F1ECE2')]
    for a in range(0, 360, 30):
        b.append(D(f'circle cx="{100+28*math.cos(math.radians(a)):.0f}" cy="{70+28*math.sin(math.radians(a)):.0f}" r="2.5"', '#1E2433'))
    b += [S('M100 70V44M100 70V48', '#1E2433', 4), S('M100 70L102 46', '#C24A3E', 2.5), D('circle cx="100" cy="150" r="14"', '#E8B23A'), S('M100 106V140', '#B9821C', 3)]
    return V(l, b)
def slipper(l='Кришталевий черевичок'):
    return V(l, [P('path d="M20 140Q20 100 60 104Q100 110 130 80Q160 60 180 90Q180 130 150 140Z"', '#C8E0F8'), D('path d="M40 120Q80 120 120 96"', 'none'),
                 S('M40 120Q90 118 130 92', '#FFFFFF', 4), P('path d="M150 140L156 176H168L170 140Z"', '#9EC3E6'), D('circle cx="150" cy="96" r="6"', '#FFFFFF')])
def oranges(l='Помаранчі'):
    b = [P('ellipse cx="100" cy="160" rx="90" ry="24"', '#D9DBE3')]
    for x, y in ((60, 130), (100, 126), (140, 130), (80, 100), (120, 100)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="24"', '#E07A45')); b.append(D(f'circle cx="{x-8}" cy="{y-8}" r="7"', '#F29A5E'))
    return V(l, b)
def fireplace(l='Камін'):
    return V(l, [P('rect x="20" y="30" width="160" height="160"', '#B98E5E'), P('rect x="10" y="30" width="180" height="20"', '#8A5A34'),
                 P('path d="M50 190V100Q100 70 150 100V190Z"', '#2E3242'), P('path d="M100 110Q130 140 120 186H80Q70 140 100 110Z"', '#F29A5E'),
                 D('path d="M100 140Q114 160 108 186H92Q86 160 100 140Z"', '#F6CE5B')])
def cherry(l='Вишня'):
    b = [S('M100 190V80M100 120L70 90M100 110L130 80', '#6B4630', 6), P('circle cx="100" cy="70" r="50"', '#5E9A4C')]
    for x, y in ((80, 70), (110, 56), (120, 90), (90, 100)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="9"', '#9C2F45', '', '1 1'))
    return V(l, b)
def cannon(l='Гармата'):
    return V(l, [P('path d="M30 110L170 60L180 90L40 140Z"', '#4A4E60'), P('circle cx="175" cy="75" r="18"', '#2E3242'), D('circle cx="175" cy="75" r="9"', '#1E2433'),
                 P('circle cx="70" cy="150" r="32"', '#8A5A34'), D('circle cx="70" cy="150" r="10"', '#6B4630')])
def cannonball(l='Ядро'):
    return V(l, [P('circle cx="110" cy="100" r="60"', '#2E3242'), D('circle cx="90" cy="80" r="16"', '#6B7086'), S('M20 110H44M10 80H40M20 140H46', '#B7BBC8', 5)])
def swamp(l='Болото'):
    return V(l, [P('ellipse cx="100" cy="140" rx="96" ry="40"', '#6B5A3A'), D('ellipse cx="90" cy="134" rx="60" ry="20"', '#8A7A52'),
                 S('M30 130V80M40 130V70M170 140V90M160 140V84', '#5E9A4C', 4), P('ellipse cx="34" cy="74" rx="5" ry="14"', '#8A5A34'), P('ellipse cx="166" cy="84" rx="5" ry="14"', '#8A5A34')])
def statue(l='Статуя'):
    return V(l, [P('rect x="60" y="160" width="80" height="30"', '#B7BBC8'), P('rect x="84" y="80" width="32" height="80" rx="10"', '#D9DBE3'),
                 P('circle cx="100" cy="60" r="24"', '#D9DBE3'), D('path d="M108 40A24 24 0 0 1 110 82Q120 60 108 40Z"', '#B7BBC8')])
def ship(l='Корабель'):
    return V(l, [P('path d="M10 130H190L160 180H40Z"', '#8A5A34'), S('M100 130V10', '#6B4630', 5),
                 P('path d="M104 20Q160 60 104 110Z"', '#FFFFFF'), P('path d="M96 30Q50 70 96 116Z"', '#F1ECE2'), P('path d="M100 10H130L100 22Z"', '#C24A3E')])
def potion(l='Зілля'):
    return V(l, [P('path d="M86 30H114V70Q160 90 156 140Q150 186 100 186Q50 186 44 140Q40 90 86 70Z"', '#9C7CC4'),
                 D('path d="M60 130Q100 150 140 130Q140 176 100 178Q60 176 60 130Z"', '#6B4C9A'), P('rect x="82" y="16" width="36" height="18" rx="4"', '#8A5A34'),
                 D('path d="M64 100Q70 86 84 84Q72 100 72 116Z"', '#FFFFFF', op='.6')])
def knife(l='Ніж'):
    return V(l, [P('path d="M40 160L150 50Q170 40 166 60L60 176Z"', '#D9DBE3'), P('path d="M20 180L50 150L66 166L36 196Z"', '#8A5A34')])
def moonbeam(l='Місячне світло'):
    return V(l, [D('path d="M60 0H120L180 200H40Z"', '#FFF3C8', op='.85'), D('path d="M80 0H100L130 200H90Z"', '#FFFFFF', op='.6')])
def lily(l='Лілія'):
    b = [S('M100 190V90', '#5E9A4C', 5), P('path d="M100 190Q60 160 70 130Q90 160 100 170Z"', '#6E9F5A')]
    for a in (-60, -20, 20, 60):
        b.append(P(f'path d="M100 90Q90 40 100 20Q110 40 100 90Z"', '#FFFFFF', f' rotate({a} 100 90)'))
    b.append(D('circle cx="100" cy="86" r="8"', '#E8B23A'))
    return V(l, b)
def poppy(l='Мак'):
    b = [S('M100 190V100', '#5E9A4C', 5)]
    for a in (0, 90, 180, 270):
        b.append(P('ellipse cx="100" cy="64" rx="34" ry="26"', '#EE8597', f' rotate({a} 100 90)'))
    b.append(P('circle cx="100" cy="90" r="16"', '#2E3242', '', '1 1'))
    return V(l, b)
def lilybed(l='Клумба з ліліями'):
    b = [P('ellipse cx="100" cy="170" rx="94" ry="26"', '#8A5A34')]
    for x in (40, 80, 120, 160):
        b.append(S(f'M{x} 170V100', '#5E9A4C', 4))
        for a in (-40, 0, 40):
            b.append(P(f'path d="M{x} 100Q{x-8} 70 {x} 56Q{x+8} 70 {x} 100Z"', '#FFFFFF', f' rotate({a} {x} 100)'))
    return V(l, b)
def fakeflowers(l='Штучні квіти'):
    b = []
    for x, c in ((50, '#C24A3E'), (100, '#9C7CC4'), (150, '#E8B23A')):
        b.append(S(f'M{x} 190L{x} 100', '#8A8FA3', 3))
        b.append(P(f'path d="M{x} 70L{x+24} 90L{x+14} 120L{x-14} 120L{x-24} 90Z"', c))
        b.append(D(f'circle cx="{x}" cy="98" r="7"', '#FFFFFF', op='.7'))
    return V(l, b)
def bug(l='Срібний жучок'):
    return V(l, [S('M100 10V70', '#D9DBE3', 1.5), P('ellipse cx="100" cy="120" rx="40" ry="50"', '#B7BBC8'), D('path d="M100 74V170"', 'none'), S('M100 76V168', '#6B7086', 3),
                 P('circle cx="100" cy="72" r="18"', '#8A8FA3'), S('M64 110L36 96M64 130L34 134M136 110L164 96M136 130L166 134', '#6B7086', 3),
                 D('ellipse cx="84" cy="104" rx="8" ry="14"', '#FFFFFF', op='.6')])
def snow(l='Завірюха'):
    b = []
    for i in range(16):
        x, y = (i * 47) % 180 + 10, (i * 71) % 170 + 14
        b.append(S(f'M{x-9} {y}H{x+9}M{x} {y-9}V{y+9}M{x-6} {y-6}L{x+6} {y+6}M{x+6} {y-6}L{x-6} {y+6}', '#FFFFFF', 3))
    b.append(S('M10 60Q80 30 190 70M10 130Q100 100 190 140', '#C8E0F8', 6))
    return V(l, b)
ITEMS.update(dict(oven=oven, appletree=appletree, pillow=pillow, gold=goldrain, tar=tar, pumpkin=pumpkin, carriage=carriage, clock=clock,
                  slipper=slipper, oranges=oranges, fireplace=fireplace, cherry=cherry, cannon=cannon, cannonball=cannonball, swamp=swamp,
                  statue=statue, ship=ship, potion=potion, knife=knife, moonbeam=moonbeam, lily=lily, poppy=poppy, lilybed=lilybed,
                  fakeflowers=fakeflowers, bug=bug, snow=snow))
