"""Lab experiment: The Sacrificial Skin — passivation as armor + record."""

SLUG = "the-sacrificial-skin"
TITLE = "The Sacrificial Skin"
DESCRIPTION = ("Expose a metal surface and watch one layer do three jobs at once: armor the core, "
               "record the exposure, and slowly age the thing it saved. Polish it off and lose the protection "
               "and the provenance together. Paint a fake one and get neither.")
TAGS = ["interactive", "patina", "passivation", "materials-science", "provenance", "simulation"]

HTML = r"""<div class="patina-container">
  <div class="pt-head">
    <h2 class="pt-title">The Sacrificial Skin</h2>
    <p class="pt-sub">A bare metal surface meets a corrosive environment. In <b>passivate</b> mode the first damage builds a self-limiting layer that then caps the loss &mdash; and that same layer is a record of exactly how much exposure it absorbed. In <b>bare</b> mode nothing seals, and the core is eaten to failure. <b>Forge</b> a layer and it looks protected but isn't, and carries no history. <b>Polish</b> the real one off and you lose the armor and the provenance in a single scrape.</p>
  </div>

  <div class="pt-stage">
    <canvas id="pt-bar" class="pt-bar" width="260" height="320" aria-label="metal bar with growing surface layer"></canvas>
    <div class="pt-side">
      <div class="pt-readout">
        <div class="pt-metric">
          <span class="pt-metric-label">CORE INTEGRITY</span>
          <span class="pt-metric-val" id="pt-core">100<small>%</small></span>
        </div>
        <div class="pt-metric pt-metric-layer">
          <span class="pt-metric-label">LAYER</span>
          <span class="pt-metric-val" id="pt-layer">0<small>&micro;m</small></span>
        </div>
        <div class="pt-verdict" id="pt-verdict">Pick a mode and run the clock.</div>
        <div class="pt-probe" id="pt-probe">Provenance: <b>unprobed</b></div>
      </div>
      <canvas id="pt-chart" class="pt-chart" width="300" height="120" aria-label="core integrity over time"></canvas>
      <div class="pt-chart-cap">Core integrity over time &mdash; the plateau is the layer paying for itself</div>
    </div>
  </div>

  <div class="pt-controls">
    <div class="pt-mode-toggle">
      <button id="pt-passivate" class="pt-mode-btn pt-active">Passivate</button>
      <button id="pt-bare" class="pt-mode-btn">Bare</button>
      <button id="pt-forged" class="pt-mode-btn">Forge a layer</button>
    </div>
    <label class="pt-slider">Exposure &mdash; how harsh the environment is
      <input type="range" id="pt-exp" min="1" max="20" step="1" value="10">
      <output id="pt-exp-out">1.0 / tick</output>
    </label>
    <div class="pt-buttons">
      <button id="pt-run" class="pt-go">Run</button>
      <button id="pt-polish" class="pt-go pt-amber">Polish</button>
      <button id="pt-probe-btn" class="pt-go pt-cyan">Probe</button>
      <button id="pt-reset" class="pt-go pt-ghost">Reset</button>
    </div>
  </div>
</div>"""

CSS = r""".patina-container{max-width:760px;margin:0 auto;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#d8dde6;line-height:1.5}
.patina-container .pt-title{font-size:1.5rem;margin:0 0 .4rem;letter-spacing:.01em;color:#eef1f6}
.patina-container .pt-sub{font-size:.92rem;color:#9aa3b2;margin:0 0 1.2rem;max-width:690px}
.patina-container .pt-stage{display:flex;gap:1.2rem;flex-wrap:wrap;align-items:flex-start}
.patina-container .pt-bar{background:#0b0e14;border:1px solid #1e2530;border-radius:10px;flex:0 0 auto}
.patina-container .pt-side{flex:1 1 280px;min-width:260px;display:flex;flex-direction:column;gap:.7rem}
.patina-container .pt-readout{display:flex;flex-direction:column;gap:.55rem}
.patina-container .pt-metric{display:flex;justify-content:space-between;align-items:baseline;padding:.5rem .7rem;border-radius:8px;border:1px solid #1e2530;background:#0c1018}
.patina-container .pt-metric-label{font-size:.72rem;letter-spacing:.08em;color:#8a93a3}
.patina-container .pt-metric-val{font-size:1.5rem;font-variant-numeric:tabular-nums;font-weight:600;color:#b9c2cf}
.patina-container .pt-metric-val small{font-size:.7rem;color:#69707d;font-weight:400;margin-left:1px}
.patina-container .pt-metric-layer .pt-metric-val{color:#5fae7a}
.patina-container .pt-verdict{font-size:.9rem;padding:.6rem .7rem;border-radius:8px;background:#0c1018;border:1px solid #1e2530;color:#cdd4df;min-height:3.4em}
.patina-container .pt-verdict b{color:#5fae7a}
.patina-container .pt-probe{font-size:.82rem;padding:.5rem .7rem;border-radius:8px;background:#0c1018;border:1px solid #1e2530;color:#9aa3b2}
.patina-container .pt-probe b{color:#cdd4df}
.patina-container .pt-probe.pt-authentic b{color:#46c6d6}
.patina-container .pt-probe.pt-fake b{color:#e0715a}
.patina-container .pt-chart{width:300px;height:120px;background:#0b0e14;border:1px solid #1e2530;border-radius:8px}
.patina-container .pt-chart-cap{font-size:.68rem;color:#69707d;margin-top:-.3rem}
.patina-container .pt-controls{margin-top:1.2rem;display:flex;flex-direction:column;gap:.9rem}
.patina-container .pt-mode-toggle{display:flex;gap:.5rem}
.patina-container .pt-mode-btn{flex:1;padding:.6rem;border-radius:8px;border:1px solid #2a323f;background:#0c1018;color:#9aa3b2;font-size:.85rem;font-weight:600;letter-spacing:.02em;cursor:pointer;transition:all .15s}
.patina-container .pt-mode-btn:hover{border-color:#3a4452;color:#cdd4df}
.patina-container .pt-mode-btn.pt-active{background:#0d1c12;border-color:#2f6f43;color:#5fae7a}
.patina-container #pt-bare.pt-active{background:#1c0d0d;border-color:#6f2f2f;color:#e0715a}
.patina-container #pt-forged.pt-active{background:#1a160a;border-color:#6a5a20;color:#d6b24a}
.patina-container .pt-slider{display:flex;flex-direction:column;gap:.3rem;font-size:.78rem;color:#9aa3b2;letter-spacing:.02em}
.patina-container .pt-slider input[type=range]{width:100%;accent-color:#5fae7a;cursor:pointer}
.patina-container .pt-slider output{font-size:.82rem;color:#cdd4df;font-variant-numeric:tabular-nums}
.patina-container .pt-buttons{display:flex;gap:.6rem;flex-wrap:wrap}
.patina-container .pt-go{padding:.6rem 1.1rem;border-radius:8px;border:1px solid #2f6f3a;background:#0d1a10;color:#7ad48a;font-size:.88rem;font-weight:600;cursor:pointer;transition:all .15s}
.patina-container .pt-go:hover{background:#11250f;border-color:#3f8f4a}
.patina-container .pt-go.pt-running{border-color:#8a5020;background:#1a1408;color:#f0b24a}
.patina-container .pt-go.pt-amber{border-color:#6a5020;background:#1a1408;color:#f0b24a}
.patina-container .pt-go.pt-amber:hover{background:#221a0a}
.patina-container .pt-go.pt-cyan{border-color:#1f6a76;background:#06181b;color:#46c6d6}
.patina-container .pt-go.pt-cyan:hover{background:#082226}
.patina-container .pt-go.pt-ghost{border-color:#2a323f;background:#0c1018;color:#9aa3b2}
.patina-container .pt-go.pt-ghost:hover{background:#11161f}"""

JS = r"""(function(){
  var bar=document.getElementById('pt-bar'),bx=bar.getContext('2d');
  var chart=document.getElementById('pt-chart'),cx=chart.getContext('2d');
  var elCore=document.getElementById('pt-core'),elLayer=document.getElementById('pt-layer');
  var elVerdict=document.getElementById('pt-verdict'),elProbe=document.getElementById('pt-probe');
  var elExp=document.getElementById('pt-exp'),elExpOut=document.getElementById('pt-exp-out');
  var btnPass=document.getElementById('pt-passivate'),btnBare=document.getElementById('pt-bare'),btnForge=document.getElementById('pt-forged');
  var btnRun=document.getElementById('pt-run'),btnPolish=document.getElementById('pt-polish'),btnProbe=document.getElementById('pt-probe-btn'),btnReset=document.getElementById('pt-reset');

  var CAP=100, TMAX=240;
  var S={mode:'passivate',exp:1.0,t:0,core:100,layer:0,recorded:0,forged:false,
         running:false,raf:null,history:[]};

  // forged layer: a fixed visual thickness painted on, no real history
  var FORGE_THICK=72;

  function modeColor(){
    if(S.mode==='bare')return '#e0715a';
    if(S.mode==='forged')return '#d6b24a';
    return '#5fae7a';
  }

  function drawBar(){
    bx.clearRect(0,0,260,320);
    var mx=70,mw=120,top=24,bot=296,fullH=bot-top;
    // backdrop slot
    bx.fillStyle='#0c1018';bx.fillRect(mx-2,top-2,mw+4,fullH+4);
    // corroded / lost zone (the part of the core gone)
    var coreH=fullH*(S.core/100);
    var lostH=fullH-coreH;
    if(lostH>0){
      bx.fillStyle='#241a16';bx.fillRect(mx,top,mw,lostH);
      // pitting texture
      bx.fillStyle='rgba(110,70,50,0.5)';
      for(var i=0;i<40;i++){
        var px=mx+((i*53)%mw),py=top+((i*Math.E*97)%Math.max(1,lostH));
        bx.fillRect(px,py,2,2);
      }
    }
    // intact metal core
    var coreTop=top+lostH;
    var grad=bx.createLinearGradient(mx,0,mx+mw,0);
    grad.addColorStop(0,'#7e8794');grad.addColorStop(0.5,'#c4ccd7');grad.addColorStop(1,'#7e8794');
    bx.fillStyle=grad;bx.fillRect(mx,coreTop,mw,coreH);
    // the surface layer sits on the top face of the intact core
    var lt=(S.mode==='forged')?FORGE_THICK:S.layer;
    var layerPx=fullH*(lt/CAP)*0.55; // visual scale
    if(layerPx>0.5 && coreH>0){
      var ly=coreTop;
      bx.fillStyle=modeColor();
      bx.globalAlpha=(S.mode==='forged')?0.62:0.85;
      bx.fillRect(mx,ly,mw,Math.min(layerPx,coreH));
      bx.globalAlpha=1;
      if(S.mode==='forged'){
        bx.strokeStyle='#d6b24a';bx.setLineDash([4,3]);bx.lineWidth=1;
        bx.strokeRect(mx+0.5,ly+0.5,mw-1,Math.min(layerPx,coreH)-1);
        bx.setLineDash([]);
      }
    }
    // frame
    bx.strokeStyle='#2a323f';bx.lineWidth=1;bx.strokeRect(mx-2.5,top-2.5,mw+5,fullH+5);
    // labels
    bx.fillStyle='#69707d';bx.font='11px ui-monospace,monospace';
    bx.fillText('environment',mx-50,top+8);
    bx.fillText('core',mx+mw+8,bot-8);
  }

  function drawChart(){
    cx.clearRect(0,0,300,120);
    cx.strokeStyle='#1e2530';cx.lineWidth=1;
    cx.beginPath();cx.moveTo(0,119);cx.lineTo(300,119);cx.stroke();
    cx.beginPath();cx.moveTo(0,0);cx.lineTo(0,120);cx.stroke();
    if(S.history.length<2)return;
    var n=S.history.length;
    cx.strokeStyle=modeColor();cx.lineWidth=2;cx.beginPath();
    for(var i=0;i<n;i++){
      var x=(i/(TMAX))*300;
      var y=119-(S.history[i]/100)*116;
      if(i===0)cx.moveTo(x,y);else cx.lineTo(x,y);
    }
    cx.stroke();
  }

  function updateReadout(){
    elCore.innerHTML=Math.round(S.core)+'<small>%</small>';
    var lt=(S.mode==='forged')?FORGE_THICK:S.layer;
    elLayer.innerHTML=Math.round(lt)+'<small>&micro;m</small>';
    var msg;
    if(S.mode==='passivate'){
      if(S.t===0)msg='Bare metal. The first exposure will be spent building a layer instead of destroying the core.';
      else if(S.layer>=CAP*0.92)msg='The layer is <b>self-limited</b>: it now blocks the reaction that formed it, so the core loss has all but stopped. The skin paid for itself.';
      else msg='Building the skin. Core loss is front-loaded &mdash; the surface is being sacrificed so the core won’t be.';
    } else if(S.mode==='bare'){
      msg='No layer seals, so every bit of exposure reaches the core. The loss is <span style="color:#e0715a">linear to failure</span>.';
    } else {
      msg='A layer that <span style="color:#d6b24a">looks</span> like protection was painted on. It blocks nothing &mdash; the core corrodes exactly as if bare &mdash; and it recorded no history.';
    }
    elVerdict.innerHTML=msg;
  }

  function setProbe(state,text){
    elProbe.className='pt-probe'+(state?' pt-'+state:'');
    elProbe.innerHTML='Provenance: <b>'+text+'</b>';
  }

  function step(){
    if(S.t>=TMAX)return;
    S.t++;
    var e=S.exp;
    if(S.mode==='passivate'){
      var protect=1-S.layer/CAP;            // 1 when bare, 0 when full
      var dL=1.5*e*protect;
      S.layer=Math.min(CAP,S.layer+dL);
      S.recorded+=e;                         // real history accrues
      var dmg=0.3*e*protect;                 // front-loaded, ->0 as layer fills
      S.core=Math.max(0,S.core-dmg);
    } else if(S.mode==='bare'){
      S.core=Math.max(0,S.core-0.5*e);       // no protection -> failure
    } else { // forged
      S.core=Math.max(0,S.core-0.5*e);       // looks sealed, isn't
      // recorded stays 0
    }
    S.history.push(S.core);
    drawBar();drawChart();updateReadout();
  }

  function loop(){if(!S.running)return;step();if(S.t>=TMAX||S.core<=0){stop();return;}S.raf=requestAnimationFrame(loop);}
  function start(){if(S.running)return;if(S.t>=TMAX)reset();S.running=true;btnRun.textContent='Pause';btnRun.classList.add('pt-running');loop();}
  function stop(){S.running=false;if(S.raf)cancelAnimationFrame(S.raf);btnRun.textContent=(S.t>=TMAX||S.core<=0)?'Done':'Run';btnRun.classList.remove('pt-running');}
  function reset(){stop();S.t=0;S.core=100;S.layer=0;S.recorded=0;S.history=[];btnRun.textContent='Run';setProbe('','unprobed');drawBar();drawChart();updateReadout();}

  function setMode(m){
    S.mode=m;S.forged=(m==='forged');
    btnPass.classList.toggle('pt-active',m==='passivate');
    btnBare.classList.toggle('pt-active',m==='bare');
    btnForge.classList.toggle('pt-active',m==='forged');
    setProbe('','unprobed');
    drawBar();drawChart();updateReadout();
  }

  function polish(){
    // strip the surface: lose the armor AND the record in one scrape
    S.layer=0;S.recorded=0;
    setProbe('','stripped — no history, no armor');
    drawBar();updateReadout();
  }

  function probe(){
    // read the layer for accumulated, unforgeable history
    if(S.mode==='forged'){
      setProbe('fake','FAKE — appearance, but the mineralogy records no real exposure');
      return S.recorded;
    }
    if(S.recorded>1){
      setProbe('authentic','AUTHENTIC — '+Math.round(S.recorded)+' units of exposure are written into the layer');
    } else {
      setProbe('','bare surface — nothing to authenticate yet');
    }
    return S.recorded;
  }

  btnPass.onclick=function(){setMode('passivate');};
  btnBare.onclick=function(){setMode('bare');};
  btnForge.onclick=function(){setMode('forged');};
  btnRun.onclick=function(){if(S.running)stop();else start();};
  btnPolish.onclick=polish;
  btnProbe.onclick=probe;
  btnReset.onclick=reset;
  elExp.oninput=function(){S.exp=parseInt(this.value,10)/10;elExpOut.textContent=S.exp.toFixed(1)+' / tick';updateReadout();};

  window.__patina={
    setMode:setMode,
    setExposure:function(r){S.exp=r;elExp.value=Math.round(r*10);elExpOut.textContent=r.toFixed(1)+' / tick';},
    polish:polish,
    probe:probe,
    step:function(k){k=k||1;for(var i=0;i<k;i++)step();},
    run:function(){start();},stop:stop,reset:reset,
    state:function(){return{mode:S.mode,exp:S.exp,t:S.t,core:S.core,
      layer:(S.mode==='forged'?FORGE_THICK:S.layer),recorded:S.recorded};}
  };

  setMode('passivate');reset();
})();"""

if __name__ == "__main__":
    from database import save_experiment
    from website import publish_experiment
    r1 = save_experiment(SLUG, TITLE, DESCRIPTION, TAGS, HTML, CSS, JS)
    print("save:", r1)
    r2 = publish_experiment(SLUG, TITLE, DESCRIPTION, TAGS, HTML, CSS, JS)
    print("publish:", r2)
