# Сборщик SVG в стиле аплікації: P() кусок с тенью, D() кусок без тени, S() полоска.
SH='#1E2433'
def P(shape, fill, extra='', off='3 4', op='.2'):
    return f'<{shape} fill="{SH}" opacity="{op}" transform="translate({off}){extra}"/><{shape} fill="{fill}"{(" transform=\"" + extra.strip() + "\"") if extra else ""}/>'
def D(shape, fill, extra='', op=None):
    o=f' opacity="{op}"' if op else ''
    t=f' transform="{extra.strip()}"' if extra else ''
    return f'<{shape} fill="{fill}"{o}{t}/>'
def S(d, color, w=3):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def eye(x,y,r=6,ry=None):
    ry=ry or r+1
    return (P(f'ellipse cx="{x}" cy="{y}" rx="{r}" ry="{ry}"','#FFFFFF','', '2 3')
      + D(f'ellipse cx="{x+1.5}" cy="{y+1}" rx="{r*.62:.1f}" ry="{ry*.66:.1f}"',SH)
      + D(f'circle cx="{x-0.5}" cy="{y-1.8}" r="{max(1.6,r*.3):.1f}"','#FFFFFF'))
def svg(vb, label, body, extra_attr=''):
    lab = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{lab}{extra_attr}>\n' + '\n'.join(body) + '\n</svg>\n'
