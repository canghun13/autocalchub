const {chromium}=require('playwright');const fs=require('fs');
const list=JSON.parse(fs.readFileSync(process.argv[2]));const out=process.argv[3];const only=process.argv[4];
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const slug=p=>p.replace(/\.html$/,'').replace(/\//g,'-').replace(/-index$/,'')||'home';
function card(i){
  const OV={'tools/index.html':'Free Car Cost Calculators With the Math Shown','blog/index.html':'Car Money Guides: Worked Numbers, Linked Sources'};
  const t=OV[i.path]||i.h1||i.title.replace(/\s*\|\s*AutoCalcHub$/,'');
  const n=t.length, fs_=n<=30?78:n<=45?68:n<=60?58:n<=72?52:48;
  const sub={Calculator:'Free calculator · every assumption shown',Guide:'Worked numbers · every source linked',Glossary:'Plain-English definitions with the math',Calculators:'Free car cost calculators · math shown',Guides:'Car money guides · sources linked','Calculators & Guides':'Free car cost calculators · math shown',About:'Free car cost calculators · math shown'}[i.kind];
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:630px;overflow:hidden;font-family:'Inter';background:#0f1b2d}
  .c{position:relative;width:1200px;height:630px;padding:64px 72px;background:radial-gradient(900px 520px at 100% 100%,#243b55 0%,rgba(36,59,85,0) 70%),linear-gradient(135deg,#0f1b2d 0%,#14243a 100%);color:#fff;display:flex;flex-direction:column}
  .grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:48px 48px}
  .bar{position:absolute;left:0;top:0;bottom:0;width:12px;background:#f47c20}
  .top{position:relative;display:flex;align-items:center;gap:20px}
  .logo{font-family:'Inter Display';font-weight:700;font-size:34px;letter-spacing:-.5px}.logo span{color:#f47c20}
  .tag{font-weight:600;font-size:20px;letter-spacing:2px;text-transform:uppercase;color:#ffa64d;border:2px solid rgba(244,124,32,.55);border-radius:100px;padding:6px 18px}
  h1{position:relative;margin-top:auto;margin-bottom:auto;max-width:750px;font-family:'Inter Display';font-weight:700;font-size:${fs_}px;line-height:1.12;letter-spacing:-1.5px}
  .bot{position:relative;display:flex;justify-content:space-between;align-items:flex-end;font-size:24px;color:#9aa3ad}
  .bot b{color:#fff;font-weight:600}
  .chart{position:absolute;right:72px;top:150px;display:flex;align-items:flex-end;gap:16px;height:300px}
  .chart i{display:block;width:40px;border-radius:8px 8px 0 0;background:linear-gradient(180deg,#ffa64d,#f47c20)}
  .chart i:nth-child(odd){background:rgba(255,255,255,.16)}
  .base{position:absolute;right:72px;top:450px;width:264px;height:3px;background:rgba(255,255,255,.25)}
  </style></head><body><div class="c"><div class="grid"></div><div class="bar"></div>
  <div class="chart"><i style="height:90px"></i><i style="height:140px"></i><i style="height:120px"></i><i style="height:210px"></i><i style="height:270px"></i></div><div class="base"></div>
  <div class="top"><div class="logo">Auto<span>Calc</span>Hub</div><div class="tag">${esc(i.kind)}</div></div>
  <h1>${esc(t)}</h1>
  <div class="bot"><div>${esc(sub)}</div><b>autocalchub.com</b></div></div></body></html>`;}
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630},deviceScaleFactor:1});
 const map={};
 for(const i of list){ if(only&&!i.path.includes(only))continue;
   await p.setContent(card(i));await p.evaluate(()=>document.fonts.ready);
   const h=await p.evaluate(()=>{const r=q=>document.querySelector(q).getBoundingClientRect();const a=r('h1'),t=r('.top'),b=r('.bot');return a.top<t.bottom+24||a.bottom>b.top-24||a.right>830});
   if(h)console.log('OVERFLOW',i.path);
   const f=slug(i.path)+'.jpg';await p.screenshot({path:out+'/'+f,type:'jpeg',quality:82});map[i.path]=f;}
 await b.close();})();
