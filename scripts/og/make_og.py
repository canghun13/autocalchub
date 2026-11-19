"""Make og:image cards + social meta for pages.
Usage (from repo root):  python3 scripts/og/make_og.py blog/new-post.html tools/new-tool.html
                         python3 scripts/og/make_og.py --all
Needs node + playwright. Writes assets/img/og/<slug>.jpg, inserts og/twitter meta after the
canonical link, and adds "image" to the page's Article/WebPage JSON-LD (skips if already there)."""
import re,json,html,sys,subprocess,os,tempfile
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
EMO=re.compile('[\U0001F000-\U0001FAFF☀-➿️‍⬀-⯿]')
def slug(p): s=re.sub(r'\.html$','',p).replace('/','-'); s=re.sub(r'-index$','',s); return s or 'home'
def info(p):
    t=open(p).read()
    title=html.unescape(re.search(r'<title>(.*?)</title>',t,re.S).group(1)).strip()
    h=re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S)
    h1=re.sub(r'\s+',' ',EMO.sub('',html.unescape(re.sub(r'<[^>]+>','',h.group(1))))).strip() if h else ''
    kind=('Guides' if p=='blog/index.html' else 'Calculators' if p=='tools/index.html' else 'Guide' if p.startswith('blog/')
          else 'Calculator' if p.startswith('tools/') else 'Glossary' if p.startswith('glossary/')
          else 'Calculators & Guides' if p=='index.html' else 'About')
    return dict(path=p,title=title,h1=h1,kind=kind)
args=sys.argv[1:]
if args==['--all']:
    sm=open('sitemap.xml').read()
    args=[u if u and not u.endswith('/') else u+'index.html' for u in re.findall(r'<loc>https://autocalchub\.com/([^<]*)</loc>',sm)]
L=[info(p) for p in args]
with tempfile.NamedTemporaryFile('w',suffix='.json',delete=False) as f: json.dump(L,f)
subprocess.run(['node',os.path.join(ROOT,'scripts/og/render.js'),f.name,os.path.join(ROOT,'assets/img/og')],check=True)
A=lambda s:html.escape(s,quote=False).replace('"','&quot;')
for i in L:
    p=i['path']; t=open(p).read(); img=f'https://autocalchub.com/assets/img/og/{slug(p)}.jpg'
    t=re.sub(r'\n[ \t]*<meta (property="og:[^"]*"|name="twitter:[^"]*")[^>]*>','',t)
    c=re.search(r'<link rel="canonical" href="([^"]+)">',t)
    desc=html.unescape(re.search(r'<meta name="description" content="([^"]*)"',t).group(1))
    title=re.sub(r'\s*\|\s*AutoCalcHub$','',i['title'])
    typ='article' if p.startswith('blog/') and p!='blog/index.html' else 'website'
    block=(f'\n  <meta property="og:type" content="{typ}">\n  <meta property="og:site_name" content="AutoCalcHub">'
           f'\n  <meta property="og:title" content="{A(title)}">\n  <meta property="og:description" content="{A(desc)}">'
           f'\n  <meta property="og:url" content="{c.group(1)}">\n  <meta property="og:image" content="{img}">'
           f'\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">'
           f'\n  <meta property="og:image:alt" content="{A(i["h1"] or title)}">\n  <meta name="twitter:card" content="summary_large_image">')
    t=t[:c.end()]+block+t[c.end():]
    def ld(m):
        s=m.group(2); d=json.loads(s)
        if isinstance(d,dict) and d.get('@type') in('Article','WebPage') and 'image' not in d:
            s=re.sub(r'("@type"\s*:\s*"(?:Article|WebPage)",)(\s*)',lambda x:x.group(1)+x.group(2)+f'"image": "{img}",'+x.group(2),s,count=1)
            json.loads(s)
        return m.group(1)+s+m.group(3)
    t=re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',ld,t,flags=re.S)
    open(p,'w').write(t); print('og:',p)
