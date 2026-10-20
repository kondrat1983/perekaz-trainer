import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
RED=dict(base='#E07A45',light='#F29A5E',dark='#B95A2E',bib='#FFF8EC',sock='#3A2A2A',ear='#5A3A2A')
BLUE=dict(base='#3B6FD0',light='#6A95E8',dark='#2A52A8',bib='#9DB8EE',sock='#1E2A4E',ear='#22305A')

def fox(pal, mood='sly', crown=False, head_rot=0, burrs=False, drips=False, label='Лис Микита'):
    b=[]
    c=pal
    # хвіст
    b.append(P('path d="M128 378Q40 384 34 300Q30 230 84 196Q100 250 116 290Q126 330 150 352Z"', c['base']))
    b.append(D('path d="M60 230Q50 270 70 320Q60 270 84 214Z"', c['light']))
    b.append(P('path d="M84 196Q56 212 46 246Q62 238 74 236Q80 216 92 206Z"', c['bib'], '', '2 3'))
    # тулуб
    b.append(P('path d="M112 384Q94 300 128 242Q160 196 204 226Q232 300 218 384Z"', c['base']))
    b.append(D('path d="M204 226Q232 300 218 384H196Q214 300 190 222Z"', c['dark']))
    b.append(P('ellipse cx="132" cy="344" rx="38" ry="42"', c['base']))
    b.append(D('path d="M104 330Q112 304 140 300Q118 316 112 346Z"', c['light']))
    # груди
    b.append(P('path d="M156 226Q200 236 208 300Q194 334 172 304Q158 270 156 226Z"', c['bib'], '', '2 3'))
    # передні лапи
    for x in (152,184):
        b.append(P(f'rect x="{x}" y="296" width="22" height="90" rx="10"', c['base']))
        b.append(D(f'rect x="{x}" y="352" width="22" height="34" rx="10"', c['sock']))
    if drips:
        for (x,y,h) in ((122,250,30),(206,262,24),(100,320,26),(150,330,20)):
            b.append(D(f'rect x="{x}" y="{y}" width="7" height="{h}" rx="3.5"', c['light']))
            b.append(D(f'circle cx="{x+3.5}" cy="{y+h+3}" r="5"', c['light']))
    if burrs:
        for (x,y) in ((118,282),(196,250),(70,280),(140,370)):
            b.append(P(f'circle cx="{x}" cy="{y}" r="7"', '#6B4630', '', '2 3'))
            b.append(S(f'M{x-9} {y}h18M{x} {y-9}v18M{x-6} {y-6}l12 12M{x+6} {y-6}l-12 12', '#6B4630', 2))
    # голова
    h=[]
    h.append(P('path d="M136 158L126 92L178 140Z"', c['base']))
    h.append(D('path d="M140 148L134 110L164 140Z"', c['ear']))
    h.append(P('path d="M188 138L216 80L232 156Z"', c['base']))
    h.append(D('path d="M196 138L214 98L222 150Z"', c['ear']))
    h.append(P('path d="M128 182Q134 140 180 138Q220 138 238 174L274 194Q268 212 242 216Q212 238 172 230Q130 222 128 182Z"', c['base']))
    h.append(D('path d="M140 160Q150 144 176 142Q150 154 146 178Z"', c['light']))
    h.append(P('path d="M146 206Q190 244 244 214Q222 240 182 240Q154 234 146 206Z"', c['bib'], '', '2 3'))
    h.append(P('circle cx="270" cy="196" r="8"', '#1E2433', '', '2 3'))
    h.append(D('circle cx="268" cy="193" r="2.4"', '#FFFFFF'))
    if mood=='sly':
        h.append(eye(184,174,6,7)); h.append(eye(216,170,5.5,6.5))
        h.append(S('M172 160Q184 156 194 164','#1E2433',4)); h.append(S('M206 158Q216 152 226 158','#1E2433',4))
        h.append(S('M232 214Q246 222 260 208','#1E2433',3))
    elif mood=='scared':
        h.append(eye(184,174,7.5,8.5)); h.append(eye(216,170,7,8))
        h.append(S('M174 156Q182 148 192 154','#1E2433',4)); h.append(S('M208 150Q218 146 224 154','#1E2433',4))
        h.append(P('ellipse cx="250" cy="218" rx="6" ry="7"','#1E2433','', '2 3'))
    elif mood=='proud':
        # очі напівзаплющені, задоволений
        h.append(S('M176 176Q184 170 192 176','#1E2433',4)); h.append(S('M208 172Q216 166 224 172','#1E2433',4))
        h.append(S('M174 160Q184 154 194 158','#1E2433',3.5)); h.append(S('M206 154Q216 148 226 152','#1E2433',3.5))
        h.append(S('M232 212Q246 222 262 206','#1E2433',3))
        h.append(D('circle cx="196" cy="198" r="7"','#E8A0A0',op='.6'))
    elif mood=='howl':
        h.append(S('M176 176Q184 170 192 176','#1E2433',4)); h.append(S('M208 172Q216 166 224 172','#1E2433',4))
        h.append(S('M174 160Q184 156 194 162','#1E2433',3.5)); h.append(S('M206 156Q216 152 226 158','#1E2433',3.5))
        h.append(P('ellipse cx="248" cy="216" rx="9" ry="11"','#1E2433','', '2 3'))
        h.append(D('ellipse cx="248" cy="221" rx="5" ry="4"','#C2415A'))
        for i,(x,y) in enumerate(((270,140),(286,116),(262,104))):
            h.append(S(f'M{x} {y}v-18','#1E2433',3)); h.append(P(f'ellipse cx="{x-5}" cy="{y}" rx="7" ry="5"','#1E2433','', '2 2'))
    if crown:
        h.append(P('path d="M160 128L156 92L172 108L182 86L194 106L210 90L206 128Z"', '#E8B23A'))
        h.append(D('path d="M160 120H206V128H160Z"', '#B9821C'))
        h.append(D('circle cx="183" cy="114" r="5"', '#C2415A'))
    b.append(f'<g transform="rotate({head_rot} 190 220)">' + ''.join(h) + '</g>')
    return svg('0 0 300 400', label, b)

if __name__=='__main__':
  out=sys.argv[1]
  open(out+'/fox.svg','w').write(fox(RED))
  open(out+'/fox-blue.svg','w').write(fox(BLUE, 'scared', burrs=True, drips=True))
  open(out+'/fox-king.svg','w').write(fox(BLUE, 'proud', crown=True, head_rot=-6))
  open(out+'/fox-howl.svg','w').write(fox(BLUE, 'howl', crown=True, head_rot=-22))
