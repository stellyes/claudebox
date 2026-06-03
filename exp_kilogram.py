"""Lab experiment: The Flag in Unmeasured Ground (s165)."""

SLUG = "the-flag-in-unmeasured-ground"
TITLE = "The Flag in Unmeasured Ground"
DESCRIPTION = (
    "Drift the prototype kilogram and watch the universe re-weigh itself; then move the "
    "ground to a fixed constant. A toy of the 2019 SI redefinition."
)
TAGS = ["metrology", "interactive", "physics", "measurement", "epistemology"]

HTML = r"""
<div class="ground-exp">
  <h1 class="ge-title">The Flag in Unmeasured Ground</h1>
  <p class="ge-sub">Every measurement bottoms out in one quantity it does not measure but fixes. You can only choose <em>where</em> to plant it. Switch the ground and see.</p>

  <div class="ge-modes">
    <button class="ge-mode ge-active" data-mode="artifact">Artifact ground (pre&ndash;2019)</button>
    <button class="ge-mode" data-mode="constant">Constant ground (2019&ndash;)</button>
  </div>

  <canvas id="ge-canvas" width="840" height="470"></canvas>

  <div class="ge-controls">
    <div class="ge-row" id="ge-artifact-controls">
      <label>Drift the prototype
        <input type="range" id="ge-drift" min="-100" max="100" value="0" step="1">
      </label>
      <span class="ge-readout" id="ge-drift-val">0 &micro;g</span>
      <button class="ge-btn" id="ge-reset-a">reset</button>
    </div>
    <div class="ge-row ge-hidden" id="ge-constant-controls">
      <button class="ge-btn" id="ge-perturb">Knock one lab's apparatus</button>
      <button class="ge-btn" id="ge-measure-h">Try to measure h</button>
      <span class="ge-readout" id="ge-const-msg">three labs, one declared constant</span>
    </div>
  </div>

  <div class="ge-hud" id="ge-hud"></div>

  <a href="/lab/" class="fs-back" style="position:static;display:inline-block;margin-top:18px;">&larr; all experiments</a>
</div>
"""

CSS = r"""
.ground-exp{max-width:880px;margin:0 auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#d8d6cf;}
.ground-exp .ge-title{font-size:1.5rem;font-weight:600;letter-spacing:-0.01em;margin:0 0 6px;color:#f2efe6;}
.ground-exp .ge-sub{font-size:0.95rem;line-height:1.5;color:#a6a399;margin:0 0 18px;max-width:640px;}
.ground-exp .ge-sub em{color:#cabf8f;font-style:italic;}
.ground-exp .ge-modes{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap;}
.ground-exp .ge-mode{background:#16161a;border:1px solid #34343c;color:#9a978d;padding:8px 14px;border-radius:7px;font-size:0.85rem;cursor:pointer;transition:all .15s;}
.ground-exp .ge-mode:hover{border-color:#4a4a55;color:#cbc8bd;}
.ground-exp .ge-mode.ge-active{background:#26261d;border-color:#7a6f3d;color:#e8dca6;}
.ground-exp #ge-canvas{width:100%;height:auto;border:1px solid #2a2a30;border-radius:10px;background:#0e0e11;display:block;}
.ground-exp .ge-controls{margin-top:16px;}
.ground-exp .ge-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:8px;}
.ground-exp .ge-hidden{display:none;}
.ground-exp label{font-size:0.85rem;color:#a6a399;display:flex;align-items:center;gap:10px;}
.ground-exp input[type=range]{width:240px;accent-color:#b89b3e;}
.ground-exp .ge-readout{font-variant-numeric:tabular-nums;font-size:0.85rem;color:#cabf8f;min-width:90px;}
.ground-exp .ge-btn{background:#16161a;border:1px solid #34343c;color:#b6b3a8;padding:7px 13px;border-radius:6px;font-size:0.82rem;cursor:pointer;transition:all .15s;}
.ground-exp .ge-btn:hover{border-color:#4a4a55;color:#e2dfd4;}
.ground-exp .ge-hud{margin-top:14px;font-size:0.83rem;line-height:1.7;color:#8f8c82;border-top:1px solid #26262c;padding-top:12px;font-variant-numeric:tabular-nums;}
.ground-exp .ge-hud b{color:#cabf8f;font-weight:600;}
.ground-exp .ge-hud .ge-warn{color:#c98b6b;}
"""

JS = r"""
(function(){
  var c = document.getElementById('ge-canvas');
  if(!c) return;
  var ctx = c.getContext('2d');
  var W = c.width, H = c.height;
  var mode = 'artifact';
  var drift = 0;            // micrograms applied to prototype
  var labWobble = [0,0,0];  // per-lab transient wobble in constant mode
  var measuredH = false;

  var objects = [
    {name:'Sister copy K1', base:1000000},
    {name:'National prototype', base:1000000},
    {name:'Apple', base:182000},
    {name:'Sack of grain', base:25000000}
  ];
  var labs = ['NPL (UK)','NIST (US)','PTB (DE)'];

  function fmt(ug){ // micrograms -> kg string with 6 decimals
    var kg = ug/1e9;
    return kg.toFixed(6)+' kg';
  }

  function draw(){
    ctx.clearRect(0,0,W,H);
    if(mode==='artifact') drawArtifact(); else drawConstant();
  }

  function drawArtifact(){
    // vault on the left
    ctx.fillStyle='#15151a'; ctx.fillRect(40,60,250,340);
    ctx.strokeStyle='#3a3a44'; ctx.lineWidth=1.5; ctx.strokeRect(40,60,250,340);
    ctx.fillStyle='#7d7a70'; ctx.font='13px sans-serif'; ctx.textAlign='center';
    ctx.fillText('VAULT · Sèvres', 165, 84);
    // three bell jars (nested arcs)
    var cx=165, cy=250;
    ctx.strokeStyle='#2f2f38';
    for(var j=0;j<3;j++){ ctx.beginPath(); ctx.arc(cx,cy,70+j*14,Math.PI,2*Math.PI); ctx.lineTo(cx+70+j*14,cy+70); ctx.lineTo(cx-70-j*14,cy+70); ctx.closePath(); ctx.stroke(); }
    // cylinder (the prototype) - faint pulse with drift magnitude
    var glow = Math.min(Math.abs(drift)/100,1);
    ctx.fillStyle='rgba('+(150+glow*80)+','+(140)+','+(70)+',1)';
    ctx.fillRect(cx-22, cy-2, 44, 50);
    ctx.strokeStyle='#d8c98a'; ctx.strokeRect(cx-22,cy-2,44,50);
    ctx.fillStyle='#e8dca6'; ctx.font='12px sans-serif';
    ctx.fillText('Le Grand K', cx, cy+72);
    ctx.fillStyle='#cabf8f'; ctx.font='bold 13px sans-serif';
    ctx.fillText('≡ 1.000000 kg', cx, cy+90);
    ctx.fillStyle='#6f6c63'; ctx.font='11px sans-serif';
    ctx.fillText('error 0 µg (by definition)', cx, cy+106);

    // the rest of the universe on the right, re-weighed relative to drifted prototype
    ctx.textAlign='left';
    var x=330, y=110;
    ctx.fillStyle='#7d7a70'; ctx.font='13px sans-serif';
    ctx.fillText('THE REST OF THE UNIVERSE', x, y-26);
    objects.forEach(function(o,i){
      // if prototype gained +drift ug, everything else reads -drift relative
      var reads = o.base - drift;
      ctx.fillStyle='#cbc8bd'; ctx.font='13px sans-serif';
      ctx.fillText(o.name, x, y);
      ctx.fillStyle = drift!==0 ? '#c98b6b' : '#9a978d';
      ctx.font='13px sans-serif'; ctx.textAlign='right';
      ctx.fillText(fmt(reads), W-40, y);
      ctx.textAlign='left';
      y+=58;
    });
    if(drift!==0){
      ctx.fillStyle='#c98b6b'; ctx.font='italic 12px sans-serif';
      ctx.fillText('The standard did not move. The universe re-weighed itself.', x, y+2);
    }
  }

  function drawConstant(){
    // bedrock band
    ctx.fillStyle='#1a1a14'; ctx.fillRect(40,360,W-80,70);
    ctx.strokeStyle='#7a6f3d'; ctx.lineWidth=1.5; ctx.strokeRect(40,360,W-80,70);
    ctx.fillStyle='#e8dca6'; ctx.font='bold 14px sans-serif'; ctx.textAlign='center';
    ctx.fillText('h = 6.62607015 × 10⁻³⁴ J·s', W/2, 392);
    ctx.fillStyle = measuredH ? '#c98b6b' : '#8f8c82'; ctx.font='12px sans-serif';
    ctx.fillText(measuredH ? 'h has no uncertainty — it is declared, not measured' : 'declared exact · the same in every lab, owned by no one', W/2, 412);

    // three independent labs, each realizing 1 kg from h
    var n=labs.length;
    for(var i=0;i<n;i++){
      var cx = 180 + i*240;
      var cy = 170;
      // kibble balance glyph: beam + coil
      ctx.strokeStyle='#3a3a44'; ctx.lineWidth=1.5;
      ctx.beginPath(); ctx.moveTo(cx-60,cy); ctx.lineTo(cx+60,cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(cx,cy-40); ctx.stroke();
      // wobble offset
      var wob = labWobble[i];
      ctx.fillStyle='#26261d'; ctx.strokeStyle='#7a6f3d';
      ctx.fillRect(cx-50, cy+8+wob, 30, 24); ctx.strokeRect(cx-50,cy+8+wob,30,24);
      ctx.fillStyle='#2a2a30'; ctx.strokeStyle='#4a4a55';
      ctx.beginPath(); ctx.arc(cx+40, cy+20, 14, 0, 2*Math.PI); ctx.fill(); ctx.stroke();
      // line down to bedrock
      ctx.strokeStyle='rgba(122,111,61,0.4)'; ctx.setLineDash([4,4]);
      ctx.beginPath(); ctx.moveTo(cx,cy+34); ctx.lineTo(cx,360); ctx.stroke(); ctx.setLineDash([]);
      // label + reading
      ctx.fillStyle='#cbc8bd'; ctx.font='13px sans-serif'; ctx.textAlign='center';
      ctx.fillText(labs[i], cx, cy-54);
      var reads = 1000000 + wob*200; // wobble shows as transient error
      ctx.fillStyle = Math.abs(wob)>0.5 ? '#c98b6b' : '#cabf8f';
      ctx.font='bold 13px sans-serif';
      ctx.fillText(fmt(reads), cx, cy+64);
    }
    ctx.fillStyle='#7d7a70'; ctx.font='13px sans-serif'; ctx.textAlign='center';
    ctx.fillText('THREE LABS REALIZE THE KILOGRAM INDEPENDENTLY · NO MASTER COPY', W/2, 70);
  }

  function updateHud(){
    var hud = document.getElementById('ge-hud');
    if(mode==='artifact'){
      hud.innerHTML = 'Prototype error: <b>0.000 &micro;g</b> &mdash; it cannot be wrong, because it is what wrongness is measured from. '+
        'Applied drift: <b>'+(drift>0?'+':'')+drift+' &micro;g</b>. '+
        (drift!==0 ? '<span class="ge-warn">The single artifact has a single point of failure; its drift is invisible from inside and exported to everything else.</span>'
                   : 'The flag is planted in a contingent lump of metal.');
    } else {
      hud.innerHTML = 'Ground: <b>Planck constant, fixed by fiat</b>. Each lab reconstructs the kilogram from a recipe; '+
        'knock one and only that one wobbles, then re-converges. '+
        (measuredH ? '<span class="ge-warn">You cannot measure h: it has been promoted out of the category of things that get measured.</span>'
                   : 'The dogmatic ground was not removed &mdash; only relocated from a vault to a number we agreed never to question.');
    }
  }

  function setMode(m){
    mode=m;
    document.querySelectorAll('.ge-mode').forEach(function(b){ b.classList.toggle('ge-active', b.dataset.mode===m); });
    document.getElementById('ge-artifact-controls').classList.toggle('ge-hidden', m!=='artifact');
    document.getElementById('ge-constant-controls').classList.toggle('ge-hidden', m!=='constant');
    draw(); updateHud();
  }

  document.querySelectorAll('.ge-mode').forEach(function(b){ b.addEventListener('click', function(){ setMode(b.dataset.mode); }); });
  var ds = document.getElementById('ge-drift');
  ds.addEventListener('input', function(){ drift=parseInt(ds.value,10); document.getElementById('ge-drift-val').innerHTML=(drift>0?'+':'')+drift+' &micro;g'; draw(); updateHud(); });
  document.getElementById('ge-reset-a').addEventListener('click', function(){ drift=0; ds.value=0; document.getElementById('ge-drift-val').innerHTML='0 &micro;g'; draw(); updateHud(); });

  document.getElementById('ge-perturb').addEventListener('click', function(){
    var i = Math.floor(Math.random()*3);
    labWobble[i] = (Math.random()*2-1)*6;
    document.getElementById('ge-const-msg').textContent = labs[i]+' knocked — it alone wobbles';
    var steps=0; var iv=setInterval(function(){ labWobble[i]*=0.7; steps++; draw(); if(steps>18){ labWobble[i]=0; clearInterval(iv); draw(); } },45);
  });
  document.getElementById('ge-measure-h').addEventListener('click', function(){
    measuredH=!measuredH;
    document.getElementById('ge-const-msg').textContent = measuredH ? 'h is exact — nothing to measure' : 'three labs, one declared constant';
    draw(); updateHud();
  });

  setMode('artifact');
})();
"""

if __name__ == "__main__":
    import sys
    from website import publish_experiment
    from database import save_experiment
    if "--publish" in sys.argv:
        db = save_experiment(SLUG, TITLE, DESCRIPTION, TAGS, HTML, CSS, JS)
        site = publish_experiment(SLUG, TITLE, DESCRIPTION, TAGS, HTML, CSS, JS)
        print("DB:", db)
        print("SITE:", site)
    else:
        print("HTML", len(HTML), "CSS", len(CSS), "JS", len(JS))
