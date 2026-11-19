import re
BLUE,ORANGE='#3b6ea5','#f47c20'
def pct(x): return f'{x:.2f}'.rstrip('0').rstrip('.')+'%'
def fig(cid,title,sub,body,src,legend=''):
    return f'''
  <figure class="dchart" id="{cid}">
    <figcaption><span class="dc-title">{title}</span><span class="dc-sub">{sub}</span></figcaption>
{legend}{body}
    <p class="dc-src">{src}</p>
  </figure>
'''
def legend(items):
    return '    <div class="dc-legend">'+''.join(f'<span class="dc-key"><i class="{c}" style="background:{col}"></i>{t}</span>' for t,col,c in items)+'</div>\n'
def bars(rows,scale,ref=None):
    """rows: (label,small,value,display,cls,title). ref: (value,label)"""
    o=['    <div class="dc-rows">']
    if ref:
        rp=pct(ref[0]/scale*100)
        o.append(f'      <span></span><div class="dc-reflab"><span style="left:{rp};transform:translateX(-100%);padding-right:0.35rem;">{ref[1]}</span></div>')
    for lab,small,v,disp,cls,tt in rows:
        w=v/scale*100
        sm=f'<small>{small}</small>' if small else ''
        refd=f'<span class="dc-ref" style="left:{pct(ref[0]/scale*100)}"></span>' if ref else ''
        o.append(f'      <span class="dc-lab">{lab}{sm}</span><div class="dc-track" title="{tt}">{refd}<span class="dc-bar {cls}" style="left:0;width:{pct(w)}"></span><span class="dc-val" style="left:{pct(w)}">{disp}</span></div>')
    o.append('    </div>')
    return '\n'.join(o)
def ranges(rows,scale):
    o=['    <div class="dc-rows">']
    for lab,small,lo,hi,disp,tt in rows:
        a,b=lo/scale*100,hi/scale*100
        sm=f'<small>{small}</small>' if small else ''
        o.append(f'      <span class="dc-lab">{lab}{sm}</span><div class="dc-track" title="{tt}"><span class="dc-bar rng" style="left:{pct(a)};width:{pct(b-a)}"></span><span class="dc-val" style="left:{pct(b)}">{disp}</span></div>')
    o.append('    </div>')
    return '\n'.join(o)
def diverging(rows,lo,hi):
    span=hi-lo; z=-lo/span*100
    o=['    <div class="dc-rows">']
    for lab,small,v,disp,tt in rows:
        w=abs(v)/span*100
        sm=f'<small>{small}</small>' if small else ''
        if v>=0:
            bar=f'<span class="dc-bar hi" style="left:{pct(z)};width:{pct(w)}"></span><span class="dc-val" style="left:{pct(z+w)}">{disp}</span>'
        else:
            bar=f'<span class="dc-bar neg" style="left:{pct(z-w)};width:{pct(w)}"></span><span class="dc-val l" style="left:{pct(z-w)}">{disp}</span>'
        o.append(f'      <span class="dc-lab">{lab}{sm}</span><div class="dc-track" title="{tt}"><span class="dc-zero" style="left:{pct(z)}"></span>{bar}</div>')
    o.append('    </div>')
    return '\n'.join(o)
def lines(xs,xlabels,series,ymax,yticks,thr,xcap):
    """series: (name,color,values,endlabel)"""
    n=len(xs); X=lambda i:i/(n-1)*100; Y=lambda v:100-v/ymax*100
    o=['    <div class="dc-plot">']
    for t in yticks:
        o.append(f'      <span class="dc-grid" style="top:{pct(Y(t))}"></span><span class="dc-yt" style="top:{pct(Y(t))}">{t}x</span>')
    o.append(f'      <span class="dc-thr" style="top:{pct(Y(thr[0]))}"></span><span class="dc-thrlab" style="top:{pct(Y(thr[0]))}">{thr[1]}</span>')
    o.append('      <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">')
    for name,col,vals,_ in series:
        pts=' '.join(f'{X(i):.2f},{Y(v):.2f}' for i,v in enumerate(vals))
        o.append(f'        <polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/>')
    o.append('      </svg>')
    for name,col,vals,endlab in series:
        for i,v in enumerate(vals):
            o.append(f'      <span class="dc-dot" style="left:{pct(X(i))};top:{pct(Y(v))};background:{col}" title="{name}, {xlabels[i]} car: {v}x the premium"></span>')
        o.append(f'      <span class="dc-end" style="left:{pct(X(n-1))};top:{pct(Y(vals[-1]))}">{endlab}</span>')
    for i,l in enumerate(xlabels):
        tf=';transform:none' if i==0 else (';transform:translateX(-100%)' if i==n-1 else '')
        o.append(f'      <span class="dc-xt" style="left:{pct(X(i))}{tf}">{l}</span>')
    o.append('    </div>')
    o.append(f'    <p class="dc-xcap">{xcap}</p>')
    return '\n'.join(o)
