import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
K='#1E2433'
def wolf(mood='scared'):
    g=dict(base='#8A8FA3',light='#B7BBC8',dark='#6B7086',bib='#D9DBE3')
    b=[]
    # хвіст опущений
    b.append(P('path d="M110 360Q60 372 40 384Q30 360 64 340Q90 330 116 332Z"', g['dark']))
    # тулуб масивний
    b.append(P('path d="M96 386Q80 290 120 226Q160 180 214 214Q244 300 226 386Z"', g['base']))
    b.append(D('path d="M214 214Q244 300 226 386H204Q222 300 200 210Z"', g['dark']))
    b.append(P('ellipse cx="122" cy="340" rx="44" ry="46"', g['base']))
    b.append(D('path d="M90 326Q98 298 128 292Q104 312 98 344Z"', g['light']))
    # грива-комір
    b.append(P('path d="M130 222L150 260L162 230L178 268L190 232L204 262L214 226Q180 200 130 222Z"', g['light']))
    for x in (150,188):
        b.append(P(f'rect x="{x}" y="290" width="26" height="96" rx="12"', g['base']))
        b.append(D(f'rect x="{x+4}" y="292" width="6" height="80" rx="3"', g['light']))
    h=[]
    h.append(P('path d="M134 160L136 112L170 144Z"', g['dark']))
    h.append(P('path d="M196 142L214 100L224 158Z"', g['dark']))
    h.append(P('path d="M126 196Q128 150 176 144Q214 142 232 170L282 190Q284 214 252 222Q214 246 170 238Q128 232 126 196Z"', g['base']))
    h.append(D('path d="M138 172Q150 152 178 148Q152 162 146 190Z"', g['light']))
    h.append(P('path d="M152 214Q196 250 252 222Q226 248 186 248Q160 242 152 214Z"', g['bib'], '', '2 3'))
    h.append(P('ellipse cx="280" cy="192" rx="9" ry="8"', K, '', '2 3'))
    h.append(D('circle cx="277" cy="189" r="2.4"', '#FFFFFF'))
    if mood=='scared':
        h.append(eye(184,180,7.5,8.5)); h.append(eye(216,176,7,8))
        h.append(S('M172 164Q180 154 192 160','#1E2433',4.5)); h.append(S('M208 156Q218 150 226 160','#1E2433',4.5))
        h.append(S('M236 226Q248 220 262 228Q248 234 236 226','#1E2433',3))
    else:
        h.append(eye(184,180,6,7)); h.append(eye(216,176,5.5,6.5))
        h.append(S('M172 168Q184 160 194 166','#1E2433',4.5)); h.append(S('M206 160Q218 156 228 162','#1E2433',4.5))
        h.append(S('M236 226Q250 230 262 222','#1E2433',3))
    b.append('<g transform="rotate(4 190 220)">'+''.join(h)+'</g>')
    return svg('0 0 300 400','Вовк',b)

def bear():
    c=dict(base='#8A5A34',light='#A06E44',dark='#6B4630',muz='#D9B48A')
    b=[]
    b.append(P('ellipse cx="116" cy="372" rx="38" ry="16"', c['dark']))
    b.append(P('ellipse cx="190" cy="372" rx="38" ry="16"', c['dark']))
    b.append(P('path d="M70 300Q60 190 150 170Q240 190 232 300Q228 372 150 376Q74 372 70 300Z"', c['base']))
    b.append(D('path d="M200 186Q240 220 232 300Q228 360 186 372Q222 300 200 186Z"', c['dark']))
    b.append(D('path d="M86 230Q100 196 130 186Q104 214 98 260Z"', c['light']))
    b.append(P('ellipse cx="152" cy="298" rx="46" ry="54"', c['muz']))
    # лапи
    b.append(P('rect x="40" y="196" width="40" height="92" rx="20"', c['base'], ' rotate(18 60 200)'))
    b.append(P('rect x="222" y="200" width="40" height="88" rx="20"', c['base'], ' rotate(-24 242 204)'))
    h=[]
    h.append(P('circle cx="104" cy="98" r="24"', c['base'])); h.append(D('circle cx="104" cy="98" r="12"', c['dark']))
    h.append(P('circle cx="200" cy="98" r="24"', c['base'])); h.append(D('circle cx="200" cy="98" r="12"', c['dark']))
    h.append(P('ellipse cx="152" cy="140" rx="66" ry="58"', c['base']))
    h.append(D('path d="M100 120Q112 90 146 84Q114 104 108 140Z"', c['light']))
    h.append(P('ellipse cx="152" cy="164" rx="30" ry="24"', c['muz'], '', '2 3'))
    h.append(P('ellipse cx="152" cy="152" rx="12" ry="8"', K, '', '2 2'))
    h.append(D('circle cx="148" cy="149" r="2.4"', '#FFFFFF'))
    h.append(S('M152 160v10M140 172Q152 180 164 172','#1E2433',3))
    h.append(eye(126,128,6,7)); h.append(eye(178,128,6,7))
    h.append(S('M114 112Q124 106 134 112','#1E2433',4)); h.append(S('M170 112Q180 106 190 112','#1E2433',4))
    b.append('<g transform="rotate(-5 152 160)">'+''.join(h)+'</g>')
    return svg('0 0 300 400','Ведмідь',b)

def dog():
    c=dict(base='#D9B48A',light='#F0D4AE',dark='#A07A52',ear='#6B4630')
    b=[]
    b.append(P('path d="M96 330Q50 300 56 250Q76 290 106 304Z"', c['dark']))
    b.append(P('path d="M98 386Q86 300 122 250Q156 214 200 240Q226 310 214 386Z"', c['base']))
    b.append(D('path d="M200 240Q226 310 214 386H194Q210 310 188 236Z"', c['dark']))
    b.append(P('ellipse cx="126" cy="346" rx="36" ry="40"', c['base']))
    b.append(D('ellipse cx="120" cy="300" rx="16" ry="12"', c['ear']))
    for x in (150,182):
        b.append(P(f'rect x="{x}" y="300" width="22" height="86" rx="10"', c['base']))
        b.append(D(f'rect x="{x}" y="364" width="22" height="22" rx="10"', c['light']))
    h=[]
    h.append(P('path d="M136 196Q156 236 182 256Q236 260 250 226Q262 196 240 178Q220 160 186 162Q148 164 136 196Z"', c['base']))
    h.append(P('path d="M206 196Q252 190 268 210Q272 236 240 240Q214 236 206 196Z"', c['light'], '', '2 3'))
    h.append(P('ellipse cx="266" cy="208" rx="9" ry="7"', K, '', '2 2'))
    h.append(D('circle cx="263" cy="206" r="2.2"', '#FFFFFF'))
    # гавкає: відкритий рот
    h.append(P('path d="M226 232Q252 234 262 226Q258 252 236 252Q224 248 226 232Z"', K, '', '2 2'))
    h.append(D('path d="M232 244Q244 252 254 244Q246 254 236 252Z"', '#E8A0A0'))
    h.append(eye(206,190,6,7))
    h.append(S('M194 176L216 180','#1E2433',4.5))
    # вухо звисає
    h.append(P('path d="M166 170Q130 166 128 214Q140 236 160 222Q170 196 166 170Z"', c['ear']))
    b.append('<g transform="rotate(-6 190 230)">'+''.join(h)+'</g>')
    # нашийник
    b.append(P('path d="M150 252Q186 274 214 256L216 270Q186 288 150 266Z"', '#2F6FD6', '', '2 3'))
    b.append(D('circle cx="184" cy="278" r="6"', '#E8B23A'))
    # лінії гавкоту
    b.append(S('M276 238l16 6M274 252l18 14M270 266l12 18','#1E2433',3))
    return svg('0 0 300 400','Пес',b)

if __name__=='__main__':
  out=sys.argv[1]
  open(out+'/wolf.svg','w').write(wolf('scared'))
  open(out+'/bear.svg','w').write(bear())
  open(out+'/dog.svg','w').write(dog())
