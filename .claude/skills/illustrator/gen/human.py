import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
K = '#1E2433'
SKIN = {'light': ('#F2C9A0', '#E2B48C'), 'tan': ('#D9A57A', '#C08A5E'), 'dark': ('#8D5A3B', '#734528')}
HAIR = {'black': '#2A2530', 'brown': '#6B4630', 'blond': '#E8C46A', 'red': '#C2632E', 'grey': '#9A9DAA', 'white': '#ECEAE4'}
CLOTH = {  # світло, база, тінь
    'red': ('#E07A6A', '#C24A3E', '#9C3A30'), 'blue': ('#6A85CF', '#3F5BA8', '#2F4580'),
    'green': ('#8CBF76', '#5E9A4C', '#47783A'), 'yellow': ('#F6CE5B', '#E8B23A', '#B9821C'),
    'purple': ('#9C7CC4', '#6B4C9A', '#523A78'), 'brown': ('#A06E44', '#8A5A34', '#6B4630'),
    'grey': ('#B7BBC8', '#8A8FA3', '#6B7086'), 'white': ('#FFFFFF', '#F1ECE2', '#D8D0C0'),
    'black': ('#4A4E60', '#2E3242', '#1E2433'), 'orange': ('#F29A5E', '#E07A45', '#B95A2E'),
}

def face(cx, cy, r, mood, sex, age, skin):
    o = []
    ey = cy - r * .05
    dx = r * .36
    er = 4.6 if age != 'child' else 5.4
    if mood == 'happy':
        o.append(S(f'M{cx-dx-6} {ey}Q{cx-dx} {ey-7} {cx-dx+6} {ey}', K, 4))
        o.append(S(f'M{cx+dx-6} {ey}Q{cx+dx} {ey-7} {cx+dx+6} {ey}', K, 4))
    else:
        o.append(eye(cx - dx, ey, er + (1.4 if mood == 'scared' else 0)))
        o.append(eye(cx + dx, ey, er + (1.4 if mood == 'scared' else 0)))
    by = ey - r * .3
    if mood == 'sad':
        brows = (f'M{cx-dx-8} {by+2}Q{cx-dx} {by+1} {cx-dx+7} {by-5}', f'M{cx+dx-7} {by-5}Q{cx+dx} {by+1} {cx+dx+8} {by+2}')
    elif mood == 'angry':
        brows = (f'M{cx-dx-8} {by-4}L{cx-dx+8} {by+4}', f'M{cx+dx-8} {by+4}L{cx+dx+8} {by-4}')
    elif mood == 'scared':
        brows = (f'M{cx-dx-8} {by-1}Q{cx-dx} {by-10} {cx-dx+8} {by-4}', f'M{cx+dx-8} {by-4}Q{cx+dx} {by-10} {cx+dx+8} {by-1}')
    else:
        brows = (f'M{cx-dx-8} {by}Q{cx-dx} {by-6} {cx-dx+8} {by-1}', f'M{cx+dx-8} {by-1}Q{cx+dx} {by-6} {cx+dx+8} {by}')
    bc = K if True else K
    for b in brows: o.append(S(b, bc, 3.5))
    my = cy + r * .42
    if mood == 'happy':
        o.append(P(f'path d="M{cx-12} {my-3}Q{cx} {my+12} {cx+12} {my-3}Z"', '#9C3A30', '', '1 2'))
    elif mood == 'sad':
        o.append(S(f'M{cx-9} {my+4}Q{cx} {my-4} {cx+9} {my+4}', K, 3))
        o.append(D(f'path d="M{cx+dx+2} {ey+8}q-4 8 0 12q4-4 0-12Z"', '#7FAAF5'))
    elif mood == 'angry':
        o.append(S(f'M{cx-10} {my+3}L{cx+10} {my+1}', K, 3.5))
    elif mood == 'scared':
        o.append(P(f'ellipse cx="{cx}" cy="{my+2}" rx="6" ry="8"', '#9C3A30', '', '1 2'))
    else:
        o.append(S(f'M{cx-9} {my}Q{cx} {my+7} {cx+9} {my}', K, 3))
    if mood in ('happy', 'neutral') and (sex == 'f' or age == 'child'):
        o.append(D(f'circle cx="{cx-dx-6}" cy="{my-6}" r="7"', '#E8A0A0', op='.6'))
        o.append(D(f'circle cx="{cx+dx+6}" cy="{my-6}" r="7"', '#E8A0A0', op='.6'))
    o.append(D(f'path d="M{cx+2} {cy+r*.05}q5 8 0 11"', 'none'))
    o.append(S(f'M{cx+1} {cy+r*.08}q5 7 -1 10', skin[1], 3))
    return o

def held(item, x, y):
    o = []
    if item == 'sword':
        o.append(P(f'path d="M{x-5} {y-10}L{x+5} {y-10}L{x+3} {y-120}L{x} {y-132}L{x-3} {y-120}Z"', '#D9DBE3'))
        o.append(P(f'rect x="{x-18}" y="{y-14}" width="36" height="8" rx="3"', '#B9821C'))
        o.append(D(f'rect x="{x-1}" y="{y-118}" width="2" height="100"', '#FFFFFF', op='.7'))
    elif item == 'spear':
        o.append(P(f'rect x="{x-3}" y="{y-150}" width="6" height="210" rx="3"', '#8A5A34'))
        o.append(P(f'path d="M{x} {y-182}L{x+10} {y-150}H{x-10}Z"', '#B7BBC8'))
    elif item == 'staff':
        o.append(P(f'path d="M{x-4} {y+80}L{x-2} {y-120}Q{x+14} {y-140} {x+18} {y-118}Q{x+6} {y-126} {x+4} {y-110}L{x+4} {y+80}Z"', '#8A5A34'))
    elif item == 'bow':
        o.append(S(f'M{x+10} {y-90}Q{x+56} {y} {x+10} {y+90}', '#8A5A34', 7))
        o.append(S(f'M{x+10} {y-90}L{x+10} {y+90}', '#F1ECE2', 1.6))
    elif item == 'lamp':
        o.append(P(f'path d="M{x-30} {y+6}Q{x-30} {y-18} {x} {y-18}Q{x+24} {y-18} {x+30} {y-8}L{x+52} {y-20}L{x+40} {y}Q{x+20} {y+12} {x-30} {y+6}Z"', '#E8B23A'))
        o.append(D(f'path d="M{x-18} {y-16}Q{x} {y-34} {x+10} {y-16}Z"', '#B9821C'))
        o.append(D(f'path d="M{x+50} {y-22}q4 -12 0 -20q8 10 0 20Z"', '#F29A5E'))
    elif item == 'basket':
        o.append(S(f'M{x-26} {y}Q{x} {y-40} {x+26} {y}', '#8A5A34', 5))
        o.append(P(f'path d="M{x-32} {y}H{x+32}L{x+24} {y+34}H{x-24}Z"', '#A06E44'))
        o.append(S(f'M{x-28} {y+12}H{x+28}M{x-26} {y+24}H{x+26}', '#6B4630', 2.5))
    elif item == 'spindle':
        o.append(P(f'path d="M{x-2} {y-50}L{x+2} {y-50}L{x+4} {y+30}L{x} {y+44}L{x-4} {y+30}Z"', '#A06E44'))
        o.append(P(f'ellipse cx="{x}" cy="{y}" rx="10" ry="16"', '#F1ECE2'))
    elif item == 'book':
        o.append(P(f'rect x="{x-24}" y="{y-30}" width="44" height="56" rx="4"', '#C24A3E'))
        o.append(D(f'rect x="{x+12}" y="{y-28}" width="6" height="52"', '#F1ECE2'))
    elif item == 'flower':
        o.append(S(f'M{x} {y+20}L{x+2} {y-50}', '#5E9A4C', 4))
        for dx, dy in ((0, -64), (12, -54), (-12, -54), (8, -42), (-8, -42)):
            o.append(P(f'circle cx="{x+dx}" cy="{y+dy}" r="8"', '#C24A3E', '', '1 2'))
        o.append(D(f'circle cx="{x}" cy="{y-52}" r="6"', '#F6CE5B'))
    elif item == 'shield':
        o.append(P(f'path d="M{x-34} {y-40}H{x+34}V{y}Q{x+34} {y+40} {x} {y+56}Q{x-34} {y+40} {x-34} {y}Z"', '#3F5BA8'))
        o.append(D(f'path d="M{x-6} {y-36}H{x+6}V{y+48}H{x-6}ZM{x-30} {y-6}H{x+30}V{y+6}H{x-30}Z"', '#F6CE5B'))
    elif item == 'bucket':
        o.append(S(f'M{x-22} {y}Q{x} {y-30} {x+22} {y}', K, 3))
        o.append(P(f'path d="M{x-24} {y}H{x+24}L{x+18} {y+40}H{x-18}Z"', '#8A8FA3'))
        o.append(D(f'ellipse cx="{x}" cy="{y+1}" rx="22" ry="5"', '#4A7CC4'))
    elif item == 'hammer':
        o.append(P(f'rect x="{x-4}" y="{y-60}" width="8" height="90" rx="3"', '#8A5A34'))
        o.append(P(f'rect x="{x-24}" y="{y-80}" width="48" height="24" rx="4"', '#6B7086'))
    return o

def hat(kind, cx, cy, r, c, hair):
    o = []
    top = cy - r
    if kind == 'crown':
        o.append(P(f'path d="M{cx-30} {top+8}L{cx-34} {top-34}L{cx-16} {top-14}L{cx} {top-40}L{cx+16} {top-14}L{cx+34} {top-34}L{cx+30} {top+8}Z"', '#E8B23A'))
        o.append(D(f'rect x="{cx-30}" y="{top}" width="60" height="8"', '#B9821C'))
        o.append(D(f'circle cx="{cx}" cy="{top-10}" r="5"', '#C24A3E'))
    elif kind == 'hat':
        o.append(P(f'ellipse cx="{cx}" cy="{top+14}" rx="{r+22}" ry="10"', c[2]))
        o.append(P(f'path d="M{cx-r*.7} {top+14}Q{cx-r*.7} {top-40} {cx} {top-42}Q{cx+r*.7} {top-40} {cx+r*.7} {top+14}Z"', c[1]))
        o.append(D(f'rect x="{cx-r*.7}" y="{top+2}" width="{r*1.4}" height="8"', c[2]))
    elif kind == 'cap':
        o.append(P(f'path d="M{cx-r} {top+22}Q{cx-r} {top-16} {cx} {top-18}Q{cx+r} {top-16} {cx+r} {top+22}Z"', c[1]))
        o.append(P(f'path d="M{cx-r-4} {top+24}H{cx+r+4}V{top+12}H{cx-r-4}Z"', '#ECEAE4'))
    elif kind == 'kerchief':
        o.append(P(f'path d="M{cx-r-8} {cy+10}Q{cx-r-6} {top-10} {cx} {top-12}Q{cx+r+6} {top-10} {cx+r+8} {cy+10}Q{cx+r-6} {top+16} {cx} {top+14}Q{cx-r+6} {top+16} {cx-r-8} {cy+10}Z"', c[1]))
        for dx in (-20, 0, 20):
            o.append(D(f'circle cx="{cx+dx}" cy="{top+2}" r="4"', '#FFFFFF', op='.8'))
        o.append(P(f'path d="M{cx-12} {cy+r-2}L{cx} {cy+r+14}L{cx+12} {cy+r-2}Z"', c[2]))
    elif kind == 'wreath':
        for i, dx in enumerate(range(-int(r), int(r) + 1, 14)):
            col = ('#C24A3E', '#E8B23A', '#3F5BA8', '#FFFFFF')[i % 4]
            o.append(P(f'circle cx="{cx+dx}" cy="{top+8-abs(dx)*0.25:.0f}" r="9"', col, '', '1 2'))
        o.append(S(f'M{cx+r-4} {top+14}q10 30 4 70M{cx+r+2} {top+14}q14 26 12 60', '#C24A3E', 3))
    elif kind == 'helmet':
        o.append(P(f'path d="M{cx-r-4} {cy-2}Q{cx-r-4} {top-14} {cx} {top-16}Q{cx+r+4} {top-14} {cx+r+4} {cy-2}H{cx+r-6}Q{cx+r-8} {top+20} {cx} {top+18}Q{cx-r+8} {top+20} {cx-r+6} {cy-2}Z"', '#B7BBC8'))
        o.append(P(f'path d="M{cx-3} {top-34}L{cx+3} {top-34}L{cx+3} {top-14}L{cx-3} {top-14}Z"', '#8A8FA3'))
        o.append(D(f'path d="M{cx-r+2} {top+6}Q{cx-r} {top-4} {cx-r*.5} {top-10}Q{cx-r*.7} {top+2} {cx-r+8} {top+12}Z"', '#FFFFFF', op='.6'))
    elif kind == 'hood':
        o.append(P(f'path d="M{cx-r-12} {cy+r+6}Q{cx-r-16} {top-24} {cx} {top-26}Q{cx+r+16} {top-24} {cx+r+12} {cy+r+6}Q{cx+r-2} {cy-10} {cx} {top+8}Q{cx-r+2} {cy-10} {cx-r-12} {cy+r+6}Z"', c[1]))
    elif kind == 'turban':
        o.append(P(f'path d="M{cx-r-6} {top+18}Q{cx-r-10} {top-34} {cx} {top-36}Q{cx+r+10} {top-34} {cx+r+6} {top+18}Q{cx} {top+6} {cx-r-6} {top+18}Z"', '#FFFFFF'))
        o.append(S(f'M{cx-r} {top}Q{cx} {top-16} {cx+r} {top}', '#D8D0C0', 4))
        o.append(P(f'circle cx="{cx}" cy="{top-4}" r="7"', '#C24A3E', '', '1 2'))
    elif kind == 'veil':
        o.append(P(f'path d="M{cx-r-6} {cy+60}Q{cx-r-12} {top-14} {cx} {top-16}Q{cx+r+12} {top-14} {cx+r+6} {cy+60}L{cx+r-4} {cy}Q{cx} {top+4} {cx-r+4} {cy}Z"', '#FFFFFF'), )
        o.append(P(f'path d="M{cx-20} {top-4}L{cx-14} {top-20}L{cx} {top-8}L{cx+14} {top-20}L{cx+20} {top-4}Z"', '#E8B23A'))
    return o

def human(look, mood='neutral', label=''):
    sex, age = look.get('sex', 'm'), look.get('age', 'adult')
    skin = SKIN[look.get('skin', 'light')]
    hair = HAIR[look.get('hair', 'brown')]
    c = CLOTH[look.get('outfit', 'blue')]
    ot = look.get('outfit_type', 'shirt')
    hw = look.get('headwear', 'none')
    item = look.get('item', 'none')
    b = []
    # голова
    r = {'child': 46, 'young': 42, 'adult': 40, 'old': 40}[age]
    cx, cy = 150, 112
    sh = 186  # плечі
    # волосся ззаду
    if sex == 'f' and hw not in ('kerchief', 'hood', 'helmet'):
        b.append(P(f'path d="M{cx-r-8} {cy-10}Q{cx-r-14} {cy+r+70} {cx-r+6} {cy+r+84}H{cx+r-6}Q{cx+r+14} {cy+r+70} {cx+r+8} {cy-10}Z"', hair))
    # ноги
    legc = c[2] if ot not in ('dress', 'robe') else skin[1]
    if ot in ('shirt', 'tunic', 'coat', 'armor', 'rags'):
        pants = '#4A4E60' if ot != 'armor' else '#6B7086'
        b.append(P('rect x="118" y="300" width="28" height="80" rx="8"', pants))
        b.append(P('rect x="154" y="300" width="28" height="80" rx="8"', pants))
        b.append(P('path d="M112 372H148V390H108Q106 378 112 372Z"', '#3A2A2A'))
        b.append(P('path d="M152 372H188Q194 378 192 390H152Z"', '#3A2A2A'))
    else:
        b.append(P('rect x="126" y="340" width="18" height="40" rx="6"', skin[0]))
        b.append(P('rect x="156" y="340" width="18" height="40" rx="6"', skin[0]))
        b.append(P('path d="M120 376H146V390H116Z"', '#3A2A2A'))
        b.append(P('path d="M154 376H180L184 390H154Z"', '#3A2A2A'))
    # тулуб
    if ot == 'dress':
        b.append(P(f'path d="M116 {sh}Q150 {sh-12} 184 {sh}L222 350Q150 366 78 350Z"', c[1]))
        b.append(D(f'path d="M168 {sh}L184 {sh}L222 350Q206 356 190 358Z"', c[2]))
        b.append(D(f'path d="M84 340Q150 356 216 340L222 350Q150 366 78 350Z"', c[0]))
        b.append(D(f'path d="M128 {sh+4}H172L166 {sh+40}H134Z"', '#FFFFFF', op='.9'))
    elif ot == 'robe':
        b.append(P(f'path d="M112 {sh}Q150 {sh-12} 188 {sh}L206 382H94Z"', c[1]))
        b.append(D(f'path d="M168 {sh}L188 {sh}L206 382H182Z"', c[2]))
        b.append(D(f'rect x="104" y="262" width="92" height="12"', c[2]))
        b.append(D(f'path d="M146 {sh-4}H154V382H146Z"', c[0]))
    else:
        bottom = {'coat': 334, 'rags': 316}.get(ot, 308)
        b.append(P(f'path d="M110 {sh}Q150 {sh-12} 190 {sh}L196 {bottom}H104Z"', c[1]))
        b.append(D(f'path d="M170 {sh}L190 {sh}L196 {bottom}H178Z"', c[2]))
        if ot == 'armor':
            b.append(D(f'path d="M120 {sh+10}H180L176 260Q150 272 124 260Z"', '#B7BBC8'))
            b.append(D(f'path d="M126 {sh+16}H146L144 250Q132 248 128 244Z"', '#FFFFFF', op='.6'))
            for yy in (276, 292):
                b.append(D(f'rect x="106" y="{yy}" width="88" height="5"', c[2]))
        elif ot == 'rags':
            b.append(D(f'path d="M104 {bottom}L114 {bottom+12}L126 {bottom}L138 {bottom+12}L150 {bottom}L162 {bottom+12}L174 {bottom}L186 {bottom+12}L196 {bottom}Z"', c[1]))
            b.append(P('rect x="124" y="232" width="22" height="20" rx="3"', '#A06E44', '', '1 2'))
        else:
            b.append(D(f'rect x="106" y="{bottom-46}" width="88" height="10"', c[2]))
            if ot == 'shirt':
                b.append(D(f'path d="M138 {sh-2}H162L156 {sh+40}H144Z"', '#FFFFFF', op='.8'))
                for yy in range(sh + 8, sh + 40, 10):
                    b.append(D(f'circle cx="150" cy="{yy}" r="2.4"', '#C24A3E'))
    # руки
    arm_l = 'rotate(14 118 192)'
    arm_r = 'rotate(-14 182 192)'
    hand_r = (214, 288)
    if mood == 'happy' and item == 'none':
        arm_r = 'rotate(-140 182 192)'
        hand_r = None
    if item != 'none':
        arm_r = 'rotate(-34 182 192)'
        hand_r = (232, 266)
    if mood == 'scared':
        arm_l = 'rotate(150 118 192)'
    b.append(P('rect x="104" y="186" width="26" height="92" rx="13"', c[1], ' ' + arm_l))
    b.append(P('rect x="170" y="186" width="26" height="92" rx="13"', c[1], ' ' + arm_r))
    b.append(P('circle cx="117" cy="276" r="12"', skin[0], ' ' + arm_l))
    b.append(P('circle cx="183" cy="276" r="12"', skin[0], ' ' + arm_r))
    if hand_r and item != 'none':
        b += held(item, *hand_r)
    # шия, голова
    b.append(D(f'rect x="{cx-11}" y="{cy+r-14}" width="22" height="26"', skin[1]))
    if hw == 'hood':
        b += hat('hood', cx, cy, r, c, hair)
    b.append(P(f'circle cx="{cx}" cy="{cy}" r="{r}"', skin[0]))
    b.append(D(f'path d="M{cx+r*.5} {cy-r*.85}A{r} {r} 0 0 1 {cx+r*.4} {cy+r*.9}Q{cx+r*.95} {cy} {cx+r*.5} {cy-r*.85}Z"', skin[1]))
    # вуха
    b.append(P(f'ellipse cx="{cx-r+1}" cy="{cy+4}" rx="7" ry="10"', skin[0], '', '2 2'))
    b.append(P(f'ellipse cx="{cx+r-1}" cy="{cy+4}" rx="7" ry="10"', skin[0], '', '2 2'))
    # волосся спереду
    if hw not in ('kerchief', 'hood', 'helmet', 'turban', 'veil'):
        if age == 'old' and sex == 'm':
            b.append(P(f'path d="M{cx-r-2} {cy}Q{cx-r} {cy-r*.6} {cx-r*.6} {cy-r*.55}Q{cx-r*.7} {cy-r*.2} {cx-r+4} {cy+8}Z"', hair, '', '1 2'))
            b.append(P(f'path d="M{cx+r+2} {cy}Q{cx+r} {cy-r*.6} {cx+r*.6} {cy-r*.55}Q{cx+r*.7} {cy-r*.2} {cx+r-4} {cy+8}Z"', hair, '', '1 2'))
        else:
            b.append(P(f'path d="M{cx-r-3} {cy+6}Q{cx-r-6} {cy-r-10} {cx+4} {cy-r-6}Q{cx+r+8} {cy-r} {cx+r+3} {cy+4}Q{cx+r-8} {cy-r*.55} {cx+6} {cy-r*.62}Q{cx-6} {cy-r*.3} {cx-r*.6} {cy-r*.45}Q{cx-r+4} {cy-r*.2} {cx-r-3} {cy+6}Z"', hair, '', '2 3'))
            if sex == 'f' and age == 'child' and hw == 'none':
                b.append(P(f'path d="M{cx-r-2} {cy+10}Q{cx-r-26} {cy+40} {cx-r-14} {cy+80}Q{cx-r-4} {cy+50} {cx-r+6} {cy+20}Z"', hair))
                b.append(P(f'path d="M{cx+r+2} {cy+10}Q{cx+r+26} {cy+40} {cx+r+14} {cy+80}Q{cx+r+4} {cy+50} {cx+r-6} {cy+20}Z"', hair))
    if look.get('beard'):
        b.append(P(f'path d="M{cx-r+6} {cy+6}Q{cx-r+4} {cy+r+44} {cx} {cy+r+54}Q{cx+r-4} {cy+r+44} {cx+r-6} {cy+6}Q{cx+r-10} {cy+r*.7} {cx} {cy+r*.72}Q{cx-r+10} {cy+r*.7} {cx-r+6} {cy+6}Z"', hair))
        b.append(P(f'path d="M{cx-18} {cy+r*.32}Q{cx} {cy+r*.2} {cx+18} {cy+r*.32}Q{cx+10} {cy+r*.48} {cx} {cy+r*.4}Q{cx-10} {cy+r*.48} {cx-18} {cy+r*.32}Z"', hair, '', '1 2'))
    b += face(cx, cy, r, mood, sex, age, skin)
    if hw not in ('none', 'hood'):
        b += hat(hw, cx, cy, r, c, hair)
    tilt = {'sad': 6, 'happy': -5, 'scared': 3, 'angry': -2}.get(mood, -3)
    scale = {'child': .84, 'old': .96}.get(age, 1)
    body = ''.join(b)
    g = f'<g transform="translate(150 392) scale({scale}) translate(-150 -392)">{body}</g>'
    return svg('0 0 300 400', label, [g]).replace('<g transform="translate(150 392) scale(1) translate(-150 -392)">', '<g>')

if __name__ == '__main__':
    import json
    out = sys.argv[1]
    samples = {
        'h-king': dict(sex='m', age='old', hair='grey', outfit='purple', outfit_type='robe', headwear='crown', beard=True, item='staff'),
        'h-girl': dict(sex='f', age='child', hair='blond', outfit='blue', outfit_type='dress', headwear='none', item='basket'),
        'h-knight': dict(sex='m', age='young', hair='brown', outfit='blue', outfit_type='armor', headwear='helmet', item='sword'),
        'h-cossack': dict(sex='m', age='adult', skin='tan', hair='black', outfit='red', outfit_type='coat', headwear='hat', item='spear'),
        'h-woman': dict(sex='f', age='adult', hair='brown', outfit='green', outfit_type='dress', headwear='wreath', item='flower'),
        'h-aladdin': dict(sex='m', age='young', skin='tan', hair='black', outfit='orange', outfit_type='tunic', headwear='turban', item='lamp'),
        'h-poor': dict(sex='f', age='young', hair='red', outfit='grey', outfit_type='rags', headwear='kerchief', item='bucket'),
        'h-robin': dict(sex='m', age='young', hair='red', outfit='green', outfit_type='tunic', headwear='hood', item='bow'),
    }
    moods = ['neutral', 'happy', 'sad', 'angry', 'scared']
    for i, (n, look) in enumerate(samples.items()):
        open(f'{out}/{n}.svg', 'w').write(human(look, moods[i % 5], n))
