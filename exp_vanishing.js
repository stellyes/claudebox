(function(){
  var canvas = document.getElementById('vp-canvas');
  var ctx = canvas.getContext('2d');
  var W=0, H=0, DPR=Math.min(window.devicePixelRatio||1, 2);

  // stakeholders along the ground: fx in [-1,1]
  var FIG = [
    {fx:-0.82, name:'30-yr tenant', col:'#6fa8dc'},
    {fx:-0.38, name:'children / lot', col:'#93c47d'},
    {fx: 0.06, name:'watershed',     col:'#76d7c4'},
    {fx: 0.48, name:'neighbor',      col:'#c39bd3'},
    {fx: 0.86, name:'speculator',    col:'#e0b060'}
  ];

  var state = { mode:'price', station:0.85 }; // station in [-1,1]

  function resize(){
    W = canvas.clientWidth; H = canvas.clientHeight;
    canvas.width = W*DPR; canvas.height = H*DPR;
    ctx.setTransform(DPR,0,0,DPR,0,0);
    draw();
  }

  // distortion: distance of each figure from the eye's sightline.
  // PRICE: d_i = |fx_i - station|  (the nearest figure is the marginal exchanger, crisp ~0)
  // SPLIT: land removed from projection -> ground distortion 0 for all.
  function distortions(){
    return FIG.map(function(f){
      if(state.mode==='split') return 0;
      return Math.abs(f.fx - state.station);
    });
  }

  function draw(){
    ctx.clearRect(0,0,W,H);
    var horizonY = H*0.42;
    var groundTop = horizonY;
    var cx = W*0.5;
    // vanishing point x follows the station point
    var vpx = cx + state.station * (W*0.34);

    // sky / ground fill
    var g = ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,'#0a0a12'); g.addColorStop(0.42,'#0d0e18');
    g.addColorStop(0.44,'#14130f'); g.addColorStop(1,'#08070a');
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);

    if(state.mode==='price'){
      drawPerspectiveGround(horizonY, vpx);
      // vanishing point marker
      ctx.fillStyle='rgba(240,216,154,0.9)';
      ctx.beginPath(); ctx.arc(vpx,horizonY,4,0,7); ctx.fill();
      ctx.strokeStyle='rgba(240,216,154,0.35)';
      ctx.beginPath(); ctx.moveTo(vpx,horizonY); ctx.lineTo(vpx,horizonY-22); ctx.stroke();
      ctx.fillStyle='rgba(240,216,154,0.75)'; ctx.font='10px sans-serif'; ctx.textAlign='center';
      ctx.fillText('vanishing point = the eye', vpx, horizonY-28);
    } else {
      drawFlatGround(horizonY);
      ctx.fillStyle='rgba(127,214,166,0.8)'; ctx.font='11px sans-serif'; ctx.textAlign='center';
      ctx.fillText('land held flat, in common — off the projection', cx, horizonY-14);
    }

    var ds = distortions();
    // draw figures back-to-front (by |fx| irrelevant; just left to right)
    FIG.forEach(function(f,i){ drawFigure(f, ds[i], horizonY, vpx); });

    updateHUD(ds);
  }

  function drawPerspectiveGround(hy, vpx){
    ctx.strokeStyle='rgba(255,255,255,0.10)'; ctx.lineWidth=1;
    // converging longitudinal lines from foreground to VP
    var n=11;
    for(var i=0;i<=n;i++){
      var t=i/n;
      var fxBottom = (t*2-1); // -1..1 along bottom edge
      var bx = W*0.5 + fxBottom*(W*0.42);
      ctx.beginPath(); ctx.moveTo(bx,H); ctx.lineTo(vpx,hy); ctx.stroke();
    }
    // transverse lines (depth bands) — spaced by perspective foreshortening
    ctx.strokeStyle='rgba(255,255,255,0.07)';
    for(var k=1;k<=7;k++){
      var d=k/8; // 0..1 depth
      var y = hy + (H-hy)*(1-d)*(1-d); // foreshortened
      ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(W,y); ctx.stroke();
    }
  }

  function drawFlatGround(hy){
    // orthographic top-ish grid: even, non-converging
    ctx.strokeStyle='rgba(127,214,166,0.13)'; ctx.lineWidth=1;
    var n=13;
    for(var i=0;i<=n;i++){
      var x=(i/n)*W;
      ctx.beginPath(); ctx.moveTo(x,hy+10); ctx.lineTo(x,H); ctx.stroke();
    }
    for(var k=0;k<=8;k++){
      var y=hy+10+((H-hy-10)*k/8);
      ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(W,y); ctx.stroke();
    }
  }

  function screenX(fx){ return W*0.5 + fx*(W*0.42); }

  function drawFigure(f, d, hy, vpx){
    var baseY = H*0.84;
    var x = screenX(f.fx);
    var crisp = d < 0.12;
    var skull = d > 0.9;
    // anamorphic stretch: width grows + horizontal skew toward the off-axis direction
    var stretch = state.mode==='split' ? 0 : Math.min(d,1.6);
    var baseW = 26, baseHh = 90;
    var w = baseW*(1+stretch*1.7);
    var hh = baseHh*(1 - stretch*0.18);
    var skew = state.mode==='split' ? 0 : (f.fx - state.station)*48;
    var alpha = crisp?1: (state.mode==='split'?1: Math.max(0.35,1-stretch*0.42));

    ctx.save();
    ctx.globalAlpha = alpha;
    ctx.translate(x, baseY);
    // shadow
    ctx.fillStyle='rgba(0,0,0,0.35)';
    ctx.beginPath(); ctx.ellipse(0,6,w*0.6,7,0,0,7); ctx.fill();
    // body as a rounded bar, skewed when anamorphic
    ctx.transform(1,0, skew/100,1, 0,0);
    var col = f.col;
    ctx.fillStyle = col;
    if(crisp){ ctx.shadowColor=col; ctx.shadowBlur=14; }
    roundRect(ctx, -w/2, -hh, w, hh, Math.min(8,w/3));
    ctx.fill();
    ctx.shadowBlur=0;
    // head
    ctx.beginPath(); ctx.arc(0,-hh-9, Math.min(11, baseW*0.42*(1+stretch*0.3)),0,7); ctx.fill();
    ctx.restore();

    // label + state tag
    ctx.globalAlpha=1;
    ctx.textAlign='center';
    ctx.font='10px sans-serif';
    ctx.fillStyle = crisp?'#7fd6a6':(skull?'#e08a7f':'rgba(232,230,223,0.7)');
    var tag = state.mode==='split' ? '' : (crisp?'  ◀ crisp':(skull?'  ▶ the skull':''));
    ctx.fillText(f.name+tag, x, baseY+22);
  }

  function roundRect(c,x,y,w,h,r){
    c.beginPath();
    c.moveTo(x+r,y); c.arcTo(x+w,y,x+w,y+h,r); c.arcTo(x+w,y+h,x,y+h,r);
    c.arcTo(x,y+h,x,y,r); c.arcTo(x,y,x+w,y,r); c.closePath();
  }

  function updateHUD(ds){
    var total = ds.reduce(function(a,b){return a+b;},0);
    var minIdx = 0; for(var i=1;i<ds.length;i++){ if(ds[i]<ds[minIdx]) minIdx=i; }
    var maxIdx = 0; for(var j=1;j<ds.length;j++){ if(ds[j]>ds[maxIdx]) maxIdx=j; }
    var ro = document.getElementById('vp-readout');
    var html='';
    FIG.forEach(function(f,i){
      var cls=''; if(state.mode!=='split'){ if(i===minIdx&&ds[i]<0.12) cls='crisp'; else if(i===maxIdx&&ds[i]>0.9) cls='skull'; }
      html+='<div class="vp-fig '+cls+'"><span class="nm">'+f.name+'</span><span class="dv">'+ds[i].toFixed(2)+'</span></div>';
    });
    html+='<div class="vp-fig" style="margin-top:6px;border-top:1px solid rgba(255,255,255,0.08);padding-top:5px"><span class="nm"><b>total distortion</b></span><span class="dv"><b>'+total.toFixed(2)+'</b></span></div>';
    ro.innerHTML=html;

    var v=document.getElementById('vp-verdict');
    if(state.mode==='split'){
      v.textContent='SPLIT: total distortion = 0. The land left the surface the price is painted on; no stakeholder is the skull.';
    } else {
      v.textContent='PRICE: '+FIG[minIdx].name+' is the marginal exchanger (crisp). Total = '+total.toFixed(2)+' — move the eye and it relocates, but never reaches zero.';
    }
  }

  // ---- controls ----
  document.querySelectorAll('.vp-mode').forEach(function(b){
    b.addEventListener('click',function(){
      document.querySelectorAll('.vp-mode').forEach(function(x){x.classList.remove('active');});
      b.classList.add('active');
      state.mode=b.getAttribute('data-mode');
      draw();
    });
  });
  var slider=document.getElementById('vp-station');
  slider.addEventListener('input',function(){
    state.station=parseInt(slider.value,10)/100;
    if(state.mode!=='price'){ // moving the eye implies the price projection
      document.querySelectorAll('.vp-mode').forEach(function(x){x.classList.remove('active');});
      document.querySelector('.vp-mode[data-mode=price]').classList.add('active');
      state.mode='price';
    }
    draw();
  });

  window.addEventListener('resize', resize);

  // ---- hooks for verification ----
  window.__vp = {
    setMode:function(m){ if(m==='price'||m==='split'){ state.mode=m;
      document.querySelectorAll('.vp-mode').forEach(function(x){x.classList.toggle('active',x.getAttribute('data-mode')===m);});
      draw(); } return state.mode; },
    setStation:function(x){ state.station=Math.max(-1,Math.min(1,x)); slider.value=Math.round(state.station*100); if(state.mode==='price') draw(); else { state.mode='price'; document.querySelectorAll('.vp-mode').forEach(function(z){z.classList.toggle('active',z.getAttribute('data-mode')==='price');}); draw(); } return state.station; },
    state:function(){ var ds=distortions(); var total=ds.reduce(function(a,b){return a+b;},0);
      var minIdx=0; for(var i=1;i<ds.length;i++){ if(ds[i]<ds[minIdx]) minIdx=i; }
      return { mode:state.mode, station:+state.station.toFixed(3),
        distortions:ds.map(function(d){return +d.toFixed(3);}),
        total:+total.toFixed(3),
        marginal: state.mode==='split'?null:FIG[minIdx].name }; }
  };

  resize();
})();
