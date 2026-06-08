(function(){
  const cv = document.getElementById('sp-canvas');
  if(!cv) return;
  const ctx = cv.getContext('2d');
  const W = cv.width, H = cv.height;
  const M = {l:58, r:212, t:24, b:42};   // right margin clears the HUD
  const plotW = W - M.l - M.r, plotH = H - M.t - M.b;

  const TMAX = 160, YMAX = 4, TAU = 0.8;
  const KRATE = 0.035, ADAPT = 0.30, GATE_W = 0.02;

  const PRESETS = {
    ssri:{ varLbl:"serotonin reaching downstream", rawLbl:"reuptake blocked (immediate)",
           thrLbl:"clinical response", sensor:"5-HT1A autoreceptor", unit:"days" },
    diet:{ varLbl:"fat loss the body permits", rawLbl:"caloric deficit (immediate)",
           thrLbl:"durable loss", sensor:"lipostat", unit:"weeks" },
    rate:{ varLbl:"real output / hiring", rawLbl:"rate cut (immediate)",
           thrLbl:"real effect", sensor:"expectations", unit:"quarters" },
    dose:{ varLbl:"net hedonic effect", rawLbl:"drug in system (immediate)",
           thrLbl:"the high", sensor:"opponent process", unit:"uses" }
  };

  let I=1.0, G=2.0, D=0.6, preset="ssri";
  let t, v, conf, hist, latency, running;

  function cThresh(g){ return 0.60 - 0.085*g; }   // stronger defense -> sensor must fall further

  function reset(){
    t=0; v=0; conf=1.0; hist=[]; latency=null; running=true;
  }

  function step(){
    if(t>=TMAX){ running=false; return; }
    // sensor desensitizes at a roughly saturated rate while the intervention is present
    conf -= D * KRATE;
    if(conf<0) conf=0;
    // regulator authority: gate ~0 while confident (effect cancelled), ~1 once it gives up
    const gate = 1/(1+Math.exp((conf - cThresh(G))/GATE_W));
    const permitted = I * gate;
    v += (permitted - v) * ADAPT;
    if(v<0) v=0;
    hist.push({t:t, v:v, conf:conf, raw:I});
    if(latency===null && v>=TAU) latency=t;
    t++;
  }

  function x(tt){ return M.l + (tt/TMAX)*plotW; }
  function y(vv){ return M.t + plotH - (vv/YMAX)*plotH; }

  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#11151c"; ctx.fillRect(0,0,W,H);
    const P = PRESETS[preset];

    // confidence area (faint), drawn first as backdrop
    if(hist.length>1){
      ctx.beginPath();
      ctx.moveTo(x(hist[0].t), y(0));
      for(const h of hist) ctx.lineTo(x(h.t), y(h.conf*YMAX));
      ctx.lineTo(x(hist[hist.length-1].t), y(0));
      ctx.closePath();
      ctx.fillStyle="rgba(180,142,173,.07)";
      ctx.fill();
    }

    // gridlines + axes
    ctx.strokeStyle="rgba(255,255,255,.06)"; ctx.lineWidth=1;
    for(let g=1; g<=4; g++){ const yy=y(g); ctx.beginPath(); ctx.moveTo(M.l,yy); ctx.lineTo(M.l+plotW,yy); ctx.stroke(); }
    ctx.strokeStyle="rgba(255,255,255,.18)";
    ctx.beginPath(); ctx.moveTo(M.l,M.t); ctx.lineTo(M.l,M.t+plotH); ctx.lineTo(M.l+plotW,M.t+plotH); ctx.stroke();

    // threshold line
    ctx.strokeStyle="rgba(208,135,112,.7)"; ctx.setLineDash([5,4]); ctx.lineWidth=1.4;
    ctx.beginPath(); ctx.moveTo(M.l,y(TAU)); ctx.lineTo(M.l+plotW,y(TAU)); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle="#d08770"; ctx.font="11px -apple-system,sans-serif"; ctx.textAlign="left";
    ctx.fillText(P.thrLbl, M.l+6, y(TAU)-5);

    // raw mechanism line (immediate, constant = I)
    ctx.strokeStyle="rgba(143,188,187,.45)"; ctx.setLineDash([4,4]); ctx.lineWidth=1.6;
    ctx.beginPath(); ctx.moveTo(x(0),y(I)); ctx.lineTo(x(Math.max(1,t-1)),y(I)); ctx.stroke();
    ctx.setLineDash([]);

    // downstream effect curve
    if(hist.length>1){
      ctx.strokeStyle="#88c0d0"; ctx.lineWidth=2.4; ctx.beginPath();
      ctx.moveTo(x(hist[0].t), y(hist[0].v));
      for(const h of hist) ctx.lineTo(x(h.t), y(h.v));
      ctx.stroke();
      // now-head dot
      const last=hist[hist.length-1];
      ctx.fillStyle="#eceff4"; ctx.beginPath(); ctx.arc(x(last.t),y(last.v),3.2,0,7); ctx.fill();
    }

    // latency marker
    if(latency!==null){
      ctx.strokeStyle="rgba(163,190,140,.6)"; ctx.setLineDash([2,3]); ctx.lineWidth=1.2;
      ctx.beginPath(); ctx.moveTo(x(latency),M.t); ctx.lineTo(x(latency),M.t+plotH); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle="#a3be8c"; ctx.textAlign="center";
      ctx.fillText("latency", x(latency), M.t+plotH+14);
    }

    // axis labels
    ctx.fillStyle="#7d8696"; ctx.font="11px -apple-system,sans-serif";
    ctx.textAlign="center"; ctx.fillText("time ("+P.unit+")", M.l+plotW/2, H-8);
    ctx.save(); ctx.translate(15, M.t+plotH/2); ctx.rotate(-Math.PI/2);
    ctx.fillText(P.varLbl, 0,0); ctx.restore();

    // legend (bottom-left inside plot)
    let lx=M.l+10, ly=M.t+14;
    ctx.textAlign="left"; ctx.font="11px -apple-system,sans-serif";
    ctx.strokeStyle="rgba(143,188,187,.45)"; ctx.setLineDash([4,4]); ctx.lineWidth=1.6;
    ctx.beginPath(); ctx.moveTo(lx,ly); ctx.lineTo(lx+20,ly); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle="#8a93a3"; ctx.fillText(P.rawLbl, lx+26, ly+4);
    ly+=17;
    ctx.strokeStyle="#88c0d0"; ctx.lineWidth=2.4;
    ctx.beginPath(); ctx.moveTo(lx,ly); ctx.lineTo(lx+20,ly); ctx.stroke();
    ctx.fillStyle="#aab2c0"; ctx.fillText("downstream effect", lx+26, ly+4);
    ly+=17;
    ctx.fillStyle="rgba(180,142,173,.5)"; ctx.fillRect(lx,ly-6,20,9);
    ctx.fillStyle="#8a93a3"; ctx.fillText(P.sensor+" confidence", lx+26, ly+4);

    updateHud();
  }

  function updateHud(){
    const P=PRESETS[preset];
    document.getElementById('sp-effect').textContent = v.toFixed(2);
    document.getElementById('sp-conf').textContent = Math.round(conf*100)+"%";
    const lat=document.getElementById('sp-lat');
    const ver=document.getElementById('sp-verdict');
    if(latency!==null){
      lat.textContent = latency+" "+P.unit;
      ver.textContent = "effect emerged at "+latency+" "+P.unit+" — sensor gave up";
      ver.classList.add('go');
    } else {
      lat.textContent = (I<TAU && conf<0.05) ? "never (subtherapeutic)" : "—";
      if(I<TAU && conf<0.05){
        ver.textContent = "sensor defeated, but the push was too weak to matter";
        ver.classList.remove('go');
      } else {
        ver.textContent = "loop intact — intervention being canceled";
        ver.classList.remove('go');
      }
    }
  }

  function loop(){
    if(running){ step(); step(); }   // 2 sub-steps/frame for a brisk run
    draw();
    requestAnimationFrame(loop);
  }

  // ---- controls ----
  function bind(id, valId, set, fmt){
    const el=document.getElementById(id);
    el.addEventListener('input', ()=>{ set(parseFloat(el.value)); document.getElementById(valId).textContent=fmt(parseFloat(el.value)); reset(); });
  }
  bind('sp-I','sp-Ival', x=>I=x, x=>x.toFixed(1));
  bind('sp-G','sp-Gval', x=>G=x, x=>x.toFixed(1));
  bind('sp-D','sp-Dval', x=>D=x, x=>x.toFixed(2));

  document.getElementById('sp-disable').addEventListener('click', ()=>{ conf=0; });
  document.getElementById('sp-reset').addEventListener('click', reset);

  document.querySelectorAll('.sp-preset').forEach(b=>{
    b.addEventListener('click', ()=>{
      document.querySelectorAll('.sp-preset').forEach(x=>x.classList.remove('active'));
      b.classList.add('active'); preset=b.dataset.preset; reset();
    });
  });

  reset();
  requestAnimationFrame(loop);
})();
