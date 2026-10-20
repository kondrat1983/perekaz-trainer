import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from paper import *
from scenery import sky, tree, B, forest as forest_fn
K='#1E2433'
SVG=lambda b: svg('0 0 600 400','',b,' preserveAspectRatio="xMidYMax slice"')
DAY=['#8FB8E0','#A9CBE8','#C4DCEE','#DCE9EF']
def hut_house(x,y,s=1,wall='#F4EFE6',roof='#C9A15A'):
    o=[B(f'rect x="{x}" y="{y}" width="{150*s}" height="{90*s}"',wall)]
    o.append(B(f'path d="M{x-20*s} {y+6*s}Q{x+75*s} {y-90*s} {x+170*s} {y+6*s}Z"',roof))
    o.append(D(f'path d="M{x-20*s} {y+6*s}Q{x+75*s} {y-30*s} {x+170*s} {y+6*s}L{x+170*s} {y+14*s}Q{x+75*s} {y-22*s} {x-20*s} {y+14*s}Z"','#A88340'))
    o.append(B(f'rect x="{x+22*s}" y="{y+22*s}" width="{34*s}" height="{30*s}"','#3F5BA8'))
    o.append(D(f'rect x="{x+24*s}" y="{y+24*s}" width="{12*s}" height="{12*s}"','#7FAAF5',op='.7'))
    o.append(B(f'rect x="{x+92*s}" y="{y+30*s}" width="{34*s}" height="{60*s}"','#8A5A34'))
    return o
def village():
    b=sky(DAY)
    b.append(B('path d="M0 230Q160 200 330 226T600 214V400H0Z"','#9CC08A'))
    b+=hut_house(60,210,1)
    b+=hut_house(380,226,.8,'#F4EFE6','#B98E48')
    for x,y,r in ((290,250,40),(560,250,46)): b+=tree(x,y,r)
    b.append(B('path d="M0 300Q200 286 400 304T600 296V400H0Z"','#6E9F5A'))
    for x in range(0,600,30): b.append(D(f'rect x="{x}" y="292" width="8" height="34" rx="3"','#A06E44'))
    b.append(D('rect x="0" y="300" width="600" height="6"','#8A5A34'))
    b.append(D('circle cx="520" cy="70" r="26"','#F6CE5B'))
    return SVG(b)
def hut():
    b=[D('rect x="0" y="0" width="600" height="400"','#EDE3CF')]
    b.append(D('rect x="0" y="0" width="600" height="60"','#D9CBB0'))
    for x in (0,200,400): b.append(B(f'rect x="{x}" y="40" width="200" height="14"','#8A5A34'))
    b.append(B('rect x="60" y="110" width="120" height="100" rx="6"','#3F5BA8'))
    b.append(D('rect x="68" y="118" width="50" height="40"','#9EC3E6'))
    b.append(D('rect x="122" y="118" width="50" height="40"','#9EC3E6'))
    b.append(B('path d="M380 90H560V320H380Z"','#F4EFE6'))
    b.append(B('path d="M400 230H540V320H400Z"','#E3D7C2'))
    b.append(B('path d="M430 260Q470 220 510 260V320H430Z"','#2E3242'))
    b.append(D('path d="M450 300Q470 270 490 300Z"','#F29A5E'))
    for x in range(390,560,24): b.append(D(f'circle cx="{x}" cy="104" r="5"','#C24A3E'))
    b.append(D('rect x="0" y="300" width="600" height="100"','#B98E5E'))
    for y in (320,350,380): b.append(D(f'rect x="0" y="{y}" width="600" height="3"','#A07A4E'))
    b.append(B('path d="M220 210H320V230H220Z"','#C24A3E'))
    b.append(S('M222 214H318M222 224H318','#FFFFFF',2))
    return SVG(b)
def palace():
    b=sky(['#9EC3E6','#B6D2EC','#CDE0F0','#E2ECF2'])
    b.append(B('rect x="140" y="110" width="320" height="200"','#D9DBE3'))
    for x in (100,460):
        b.append(B(f'rect x="{x}" y="80" width="60" height="230"','#C9CCD6'))
        b.append(B(f'path d="M{x-8} 82L{x+30} 20L{x+68} 82Z"','#3F5BA8'))
        b.append(D(f'rect x="{x+20}" y="120" width="20" height="34" rx="10"','#2E3242'))
    for x in range(140,461,32): b.append(B(f'rect x="{x}" y="94" width="20" height="18"','#D9DBE3'))
    b.append(B('path d="M260 310V230Q300 186 340 230V310Z"','#6B4630'))
    for x in (180,380): b.append(D(f'rect x="{x}" y="150" width="34" height="50" rx="17"','#2E3242'))
    b.append(B('path d="M290 110V60L330 72L290 84"','#C24A3E'))
    b.append(B('path d="M0 300Q300 286 600 300V400H0Z"','#6E9F5A'))
    b.append(D('path d="M260 310H340L380 400H220Z"','#C9B27A'))
    return SVG(b)
def east():
    b=sky(['#E8A87A','#F0C08A','#F6D6A0','#FBE6BE'])
    b.append(D('circle cx="480" cy="90" r="34"','#FFF3C8'))
    for x,w,h in ((20,120,150),(150,100,120),(420,140,160)):
        b.append(B(f'rect x="{x}" y="{300-h}" width="{w}" height="{h}"','#E3C9A0'))
        b.append(D(f'rect x="{x+w*.3}" y="{320-h}" width="{w*.18}" height="{h*.2}" rx="{w*.09}"','#6B4630'))
    b.append(B('rect x="260" y="150" width="120" height="150"','#F0DDBC'))
    b.append(B('path d="M262 152Q320 40 378 152Z"','#3F9A8A'))
    b.append(B('path d="M316 70h8v-20h-8Z"','#E8B23A'))
    b.append(B('rect x="390" y="90" width="22" height="210"','#F0DDBC'))
    b.append(B('path d="M388 92Q401 50 414 92Z"','#3F9A8A'))
    b.append(B('path d="M0 296H600V400H0Z"','#E3C9A0'))
    b.append(D('path d="M0 296H600V306H0Z"','#C9A97A'))
    b.append(S('M70 300Q60 240 80 200M80 200q-30 0-46 14M80 200q30-6 44 8M80 200q-12-26-34-30M80 200q16-24 38-24','#5E9A4C',6))
    return SVG(b)
def sea():
    b=sky(['#7FAAF5','#9EC3E6','#BCD6EE','#D6E6F2'])
    b.append(D('circle cx="110" cy="80" r="30"','#FFF3C8'))
    for i,(y,c) in enumerate(((200,'#3F6FB8'),(240,'#2F5A9C'),(290,'#244A84'),(340,'#1E3C6E'))):
        b.append(B(f'path d="M0 {y}Q75 {y-12} 150 {y}T300 {y}T450 {y}T600 {y}V400H0Z"',c))
        b.append(S(f'M{40+i*70} {y+16}q16-8 32 0M{330+i*40} {y+22}q16-8 32 0','#FFFFFF',2.5))
    b.append(B('path d="M430 360Q520 320 600 330V400H410Z"','#E8D6A0'))
    return SVG(b)
def steppe():
    b=sky(['#7FAAF5','#9EC3E6','#C4DCEE','#F0E6C8'])
    b.append(D('circle cx="480" cy="80" r="28"','#F6CE5B'))
    b.append(B('path d="M0 240Q150 226 300 236T600 230V400H0Z"','#C9B27A'))
    b.append(B('path d="M0 290Q200 276 400 292T600 286V400H0Z"','#B89A5E'))
    b.append(B('path d="M380 240Q430 180 480 240Z"','#A08A5A'))
    for x in range(20,600,40):
        b.append(S(f'M{x} 330q4-20 0-34M{x+8} 330q6-18 12-26','#8A7A42',2.5))
    return SVG(b)
def mountains():
    b=sky(DAY)
    b.append(B('path d="M-20 270L120 90L240 250L360 60L520 260L620 140V400H-20Z"','#8A8FA3'))
    b.append(D('path d="M120 90L150 130L130 128L112 140L96 122Z"','#FFFFFF'))
    b.append(D('path d="M360 60L396 108L370 104L350 118L330 98Z"','#FFFFFF'))
    b.append(D('path d="M360 60L520 260H440Z"','#6B7086',op='.6'))
    b.append(B('path d="M0 300Q200 270 400 300T600 290V400H0Z"','#6E9F5A'))
    return SVG(b)
def cave():
    b=[D('rect x="0" y="0" width="600" height="400"','#3A3442')]
    b.append(B('path d="M0 0H600V120Q520 60 420 90Q300 30 180 90Q80 60 0 120Z"','#4E4658'))
    for x,h in ((80,60),(200,40),(330,70),(470,50)):
        b.append(B(f'path d="M{x-14} 60L{x} {60+h}L{x+14} 60Z"','#5E5468'))
    b.append(B('path d="M0 300Q300 270 600 300V400H0Z"','#4E4658'))
    for x,y in ((120,320),(300,340),(480,316)):
        b.append(B(f'path d="M{x-20} {y}L{x} {y-30}L{x+20} {y}Z"','#7FAAF5'))
    b.append(D('path d="M240 300Q300 250 360 300Z"','#F6CE5B',op='.25'))
    return SVG(b)
def field():
    b=sky(DAY)
    b.append(D('circle cx="500" cy="70" r="28"','#F6CE5B'))
    b.append(B('path d="M0 220Q300 200 600 220V400H0Z"','#8CBF76'))
    b.append(B('path d="M0 260Q300 240 600 262V400H0Z"','#E8C46A'))
    for row,y in enumerate((280,310,345,380)):
        for x in range(-10,610,26):
            xx=x+(row%2)*13
            b.append(S(f'M{xx} {y+20}L{xx+2} {y-6}','#B9821C',2.5))
            b.append(D(f'ellipse cx="{xx+2}" cy="{y-10}" rx="4" ry="9"','#E8B23A'))
    return SVG(b)
def hills():
    b=sky(DAY)
    b.append(B('path d="M0 190Q90 120 180 170Q260 110 350 160Q440 100 600 170V400H0Z"','#6E9F5A'))
    b.append(D('path d="M0 190Q90 120 180 170L170 200Q90 150 0 210Z"','#8CBF76'))
    for x,y,r in ((80,200,26),(260,190,24),(470,180,28)): b+=tree(x,y,r)
    b.append(B('path d="M0 236Q300 220 600 232V400H0Z"','#5E9A4C'))
    b.append(B('path d="M0 300Q150 280 300 296T600 290V400H0Z"','#4A7CC4'))
    b.append(S('M60 330h40M240 350h60M420 326h50','#FFFFFF',2.5))
    return SVG(b)
def garden():
    b=sky(DAY)
    b.append(B('path d="M0 250Q300 230 600 250V400H0Z"','#8CBF76'))
    for x,y,r in ((60,280,50),(200,270,44),(420,276,48),(560,284,52)):
        b+=tree(x,y,r)
        for dx,dy in ((-r*.4,-r*1.1),(r*.3,-r*.8),(0,-r*1.5)):
            b.append(P(f'circle cx="{x+dx:.0f}" cy="{y+dy:.0f}" r="7"','#C24A3E','', '1 2'))
    b.append(B('path d="M0 320Q300 304 600 322V400H0Z"','#6E9F5A'))
    for x in range(30,600,70):
        b.append(P(f'circle cx="{x}" cy="350" r="7"','#F6CE5B','', '1 2'))
    return SVG(b)
def night_forest():
    b=sky(['#2B3A67','#3A4C80','#5A6A9A','#8A7FA8'])
    b.append(B('circle cx="490" cy="70" r="30"','#FFF3C8'))
    for x,y in ((80,40),(200,70),(330,30),(400,100),(560,140)): b.append(D(f'circle cx="{x}" cy="{y}" r="3"','#FFF3C8'))
    b.append(B('path d="M0 230Q150 200 300 222T600 214V400H0Z"','#3E6A4A'))
    for x,y,r in ((20,270,56),(120,250,46),(480,256,50),(590,268,58)): b+=tree(x,y,r,'#3A2A2A','#2F5A3C','#3E6A4A','#4E7A56')
    b.append(B('path d="M0 300Q200 286 400 302T600 296V400H0Z"','#5A8A48'))
    return SVG(b)
out=sys.argv[1]
fns=dict(village=village,hut=hut,palace=palace,east=east,sea=sea,steppe=steppe,mountains=mountains,cave=cave,field=field,hills=hills,garden=garden,forest=forest_fn,glade=night_forest)
for n,f in fns.items(): open(f'{out}/{n}.svg','w').write(f())
