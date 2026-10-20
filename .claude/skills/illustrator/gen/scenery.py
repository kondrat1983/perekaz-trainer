import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
K='#1E2433'
def B(shape, fill, extra=''): return P(shape, fill, extra, '4 5')
def hen():
    b=[]
    b.append(P('path d="M40 96Q30 60 58 52Q60 80 76 92Z"', '#B95A2E'))
    b.append(P('path d="M44 120Q40 70 96 70Q120 40 146 56Q160 90 150 120Q140 166 96 168Q50 164 44 120Z"', '#FFF8EC'))
    b.append(D('path d="M60 116Q90 140 128 120Q110 150 82 146Q64 138 60 116Z"', '#E9DCC6'))
    b.append(P('path d="M132 44Q138 30 148 38Q154 26 162 36Q172 34 166 50Z"', '#C2415A', '', '2 3'))
    b.append(P('path d="M158 62L178 70L158 76Z"', '#F2B544', '', '2 3'))
    b.append(D('path d="M150 80Q158 92 150 98Q142 90 150 80Z"', '#C2415A'))
    b.append(eye(146,62,4.5,5))
    b.append(S('M84 166v18M80 186h10M110 166v18M106 186h10', '#E8B23A', 4))
    return svg('0 0 200 200','Курка',b)
def barrel():
    b=[]
    b.append(P('path d="M44 50Q36 110 50 180H150Q164 110 156 50Z"', '#A06E44'))
    b.append(D('path d="M128 50Q140 110 132 180H150Q164 110 156 50Z"', '#8A5A34'))
    for y in (70,160):
        b.append(D(f'path d="M40 {y}Q100 {y+8} 160 {y}V{y+10}Q100 {y+18} 40 {y+10}Z"', '#6B7086'))
    b.append(P('ellipse cx="100" cy="50" rx="56" ry="14"', '#6B4630'))
    b.append(D('ellipse cx="100" cy="51" rx="48" ry="10"', '#3B6FD0'))
    b.append(D('ellipse cx="88" cy="48" rx="18" ry="4"', '#6A95E8'))
    for (x,h) in ((60,40),(96,26),(130,52)):
        b.append(D(f'rect x="{x}" y="56" width="9" height="{h}" rx="4.5"', '#3B6FD0'))
        b.append(D(f'circle cx="{x+4.5}" cy="{56+h}" r="6.5"', '#3B6FD0'))
    return svg('0 0 200 200','Діжка з фарбою',b)
def crown():
    b=[]
    b.append(P('path d="M36 150L28 62L70 104L100 46L130 104L172 62L164 150Z"', '#E8B23A'))
    b.append(D('path d="M100 46L130 104L172 62L164 150H130Q140 100 100 46Z"', '#B9821C', op='.5'))
    b.append(P('rect x="34" y="140" width="132" height="22" rx="4"', '#B9821C'))
    for (x,c) in ((70,'#2F6FD6'),(100,'#C2415A'),(130,'#2F6FD6')):
        b.append(P(f'circle cx="{x}" cy="151" r="8"', c, '', '2 2'))
    for (x,y) in ((28,62),(100,46),(172,62)):
        b.append(P(f'circle cx="{x}" cy="{y}" r="8"', '#F6CE5B', '', '2 2'))
    return svg('0 0 200 200','Корона',b)
def notes():
    b=[]
    for (x,y,s) in ((50,120,1),(110,80,1.2),(150,130,.9)):
        b.append(S(f'M{x+10*s} {y}v{-50*s}l{20*s} {8*s}', K, 5))
        b.append(P(f'ellipse cx="{x}" cy="{y}" rx="{12*s:.0f}" ry="{9*s:.0f}"', K, ' rotate(-20 %d %d)'%(x,y), '2 3'))
    return svg('0 0 200 200','Спів',b)

def sky(cols, h=250):
    out=[]; n=len(cols); step=h//n
    for i,c in enumerate(cols):
        out.append(D(f'rect x="0" y="{i*step}" width="600" height="{step+2 if i<n-1 else h-i*step}"', c))
    return out
def tree(x, y, r, trunk='#6B4630', g1='#5A8A48', g2='#6E9F5A', g3='#8CBF76'):
    o=[B(f'rect x="{x-9}" y="{y-10}" width="18" height="{400-y+10}"', trunk)]
    o.append(B(f'circle cx="{x}" cy="{y-r}" r="{r}"', g1))
    o.append(D(f'circle cx="{x-r*.25:.0f}" cy="{y-r*1.15:.0f}" r="{r*.72:.0f}"', g2))
    o.append(D(f'circle cx="{x-r*.4:.0f}" cy="{y-r*1.35:.0f}" r="{r*.32:.0f}"', g3))
    return o
def forest():
    b=sky(['#8FB8E0','#A9CBE8','#C4DCEE','#DCE9EF'])
    b.append(B('path d="M0 220Q120 170 260 200T600 190V400H0Z"', '#9CC08A'))
    for x,y,r in ((40,250,46),(160,236,40),(470,240,44),(580,250,50)): b+=tree(x,y,r,'#8A5A34','#7FAF6C','#8CBF76','#A9D493')
    b.append(B('path d="M0 290Q160 270 320 292T600 284V400H0Z"', '#6E9F5A'))
    for x,y,r in ((-10,330,60),(120,336,50),(520,332,58),(630,340,60)): b+=tree(x,y,r)
    b.append(B('path d="M0 340Q200 326 400 344T600 338V400H0Z"', '#5A8A48'))
    b.append(S('M200 364l6-12 6 12M320 372l5-10 5 10M420 360l6-12 6 12','#8CBF76',3))
    return svg('0 0 600 400','',b,' preserveAspectRatio="xMidYMax slice"')
def market():
    b=sky(['#9EC3E6','#B6D2EC','#CDE0F0','#E2ECF2'])
    # будинки
    houses=((0,150,110,'#E8D6B8','#C2415A'),(110,170,90,'#F0E2C6','#8A5A34'),(200,130,120,'#E3CBA4','#6B4630'),(320,160,100,'#F0E2C6','#9C2F45'),(420,140,100,'#E8D6B8','#6B4630'),(520,166,90,'#E3CBA4','#8A5A34'))
    for x,y,w,wall,roof in houses:
        b.append(B(f'rect x="{x+6}" y="{y}" width="{w-12}" height="{300-y}"', wall))
        b.append(B(f'path d="M{x} {y+4}L{x+w/2} {y-44}L{x+w} {y+4}Z"', roof))
        for wx in (x+20, x+w-44):
            b.append(D(f'rect x="{wx}" y="{y+26}" width="24" height="30" rx="3"', '#3A4C80'))
            b.append(D(f'rect x="{wx+3}" y="{y+29}" width="8" height="10"', '#7FAAF5', op='.6'))
    b.append(B('rect x="0" y="290" width="600" height="110"', '#B7BBC8'))
    b.append(D('rect x="0" y="290" width="600" height="10"', '#8A8FA3'))
    for i in range(12):
        b.append(D(f'rect x="{i*52+8}" y="{330+(i%2)*28}" width="34" height="14" rx="5"', '#A3A8B6'))
    # ятки
    for x,c1,c2 in ((30,'#E8B23A','#FFF8EC'),(400,'#2F6FD6','#FFF8EC')):
        b.append(B(f'rect x="{x+10}" y="250" width="150" height="56"', '#A06E44'))
        b.append(B(f'path d="M{x} 210H{x+170}L{x+180} 246H{x-10}Z"', c1))
        for k in range(4): b.append(D(f'path d="M{x+k*42+10} 210H{x+k*42+30}L{x+k*42+34} 246H{x+k*42+8}Z"', c2))
        for k in range(5): b.append(P(f'circle cx="{x+30+k*28}" cy="244" r="10"', ('#F6CE5B','#FFF8EC','#E07A45','#FFF8EC','#8CBF76')[k], '', '2 3'))
    return svg('0 0 600 400','',b,' preserveAspectRatio="xMidYMax slice"')
def glade():
    b=sky(['#2B3A67','#3A4C80','#5A6A9A','#8A7FA8'])
    b.append(B('circle cx="490" cy="70" r="30"', '#FFF3C8'))
    for x,y in ((80,40),(200,70),(330,30),(400,100),(560,140)):
        b.append(D(f'circle cx="{x}" cy="{y}" r="3"', '#FFF3C8'))
    b.append(B('path d="M0 230Q150 200 300 222T600 214V400H0Z"', '#3E6A4A'))
    for x,y,r in ((20,270,56),(120,250,46),(480,256,50),(590,268,58)): b+=tree(x,y,r,'#3A2A2A','#2F5A3C','#3E6A4A','#4E7A56')
    b.append(B('path d="M0 300Q200 286 400 302T600 296V400H0Z"', '#5A8A48'))
    # ліхтарики свята
    b.append(S('M60 150Q300 210 540 150','#1E2433',2))
    for i,x in enumerate(range(100,520,60)):
        y=150+ (60*(1-((x-300)/240)**2))*0.9
        b.append(P(f'circle cx="{x}" cy="{y+10:.0f}" r="9"', ('#F6CE5B','#E07A45','#8CBF76')[i%3], '', '2 3'))
    return svg('0 0 600 400','',b,' preserveAspectRatio="xMidYMax slice"')
def stump():
    b=[]
    b.append(P('path d="M30 100Q24 50 34 24H166Q176 50 170 100Z"', '#8A5A34'))
    b.append(D('path d="M140 24H166Q176 50 170 100H146Q156 60 140 24Z"', '#6B4630'))
    b.append(D('path d="M50 40Q46 70 52 96H62Q56 70 60 40Z"', '#A06E44'))
    b.append(P('ellipse cx="100" cy="24" rx="70" ry="16"', '#D9B48A'))
    b.append(S('M100 24m-44 0a44 9 0 1 0 88 0a44 9 0 1 0-88 0','#A06E44',2.5))
    b.append(S('M100 24m-20 0a20 4 0 1 0 40 0a20 4 0 1 0-40 0','#A06E44',2))
    return svg('0 0 200 104','Пеньок',b)
if __name__=='__main__':
  out=sys.argv[1]
  for n,f in (('stump',stump),('hen',hen),('barrel',barrel),('crown',crown),('notes',notes),('forest',forest),('market',market),('glade',glade)):
      open(f'{out}/{n}.svg','w').write(f())
