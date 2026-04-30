import asyncio
import sys
sys.path.insert(0, '.')

HTML = """<a href="/lab/" class="back-link">&larr; all experiments</a>

<h1 class="article-title">The Song Tax</h1>
<p class="article-meta">Cost-bounded transmission as biomimetic constraint</p>

<div class="songtax-container">

<div class="songtax-controls">
  <div class="songtax-row">
    <label for="songtax-cost">Singer Cost <span id="songtax-cost-readout">0.40</span></label>
    <input type="range" id="songtax-cost" min="0" max="1" step="0.01" value="0.40" />
    <div class="songtax-hint">metabolic floor per transmission</div>
  </div>
  <div class="songtax-row">
    <label for="songtax-conformity">Conformity <span id="songtax-conformity-readout">0.60</span></label>
    <input type="range" id="songtax-conformity" min="0" max="1" step="0.01" value="0.60" />
    <div class="songtax-hint">how strongly singers copy the popular phrase</div>
  </div>
  <div class="songtax-row">
    <label for="songtax-pop">Population <span id="songtax-pop-readout">120</span></label>
    <input type="range" id="songtax-pop" min="20" max="400" step="10" value="120" />
    <div class="songtax-hint">number of singers in the basin</div>
  </div>
</div>

<canvas id="songtax-canvas" width="780" height="240"></canvas>

<div id="songtax-regime" class="songtax-regime">&mdash;</div>

<div class="songtax-stats">
  <div><span>Phrase Diversity</span><b id="songtax-stat-diversity">0.00</b></div>
  <div><span>Mean Phrase Cost</span><b id="songtax-stat-cost">0.00</b></div>
  <div><span>Revolution Tempo</span><b id="songtax-stat-tempo">&mdash;</b></div>
</div>

<p class="songtax-prose">The y-axis is phrase complexity. Each singer holds a phrase. Conformity pulls singers toward the popular value; mutation drifts each singer slightly each step; <strong>singer cost</strong> filters the survivors before reproduction &mdash; phrases too cheap to be costly are not selected by mates. Watch the regime label change as you slide the cost. At zero cost the population converges on the cheapest phrase (slop). At very high cost only the simplest phrase persists (frozen). In between, a narrow optimum allows novelty without collapse, the regime humpback whales appear to occupy.</p>

</div>
"""

CSS = """
.songtax-container { max-width: 820px; margin: 2rem auto; font-family: 'Inter', system-ui, sans-serif; color: #d8d4cc; }
.songtax-controls { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-bottom: 1rem; }
.songtax-row { background: #14131a; padding: 0.75rem 1rem; border: 1px solid #2a2630; }
.songtax-row label { display: flex; justify-content: space-between; font-size: 0.85rem; letter-spacing: 0.04em; text-transform: uppercase; }
.songtax-row label span { color: #d49b3b; font-variant-numeric: tabular-nums; }
.songtax-row input[type=range] { width: 100%; margin-top: 0.5rem; }
.songtax-hint { font-size: 0.7rem; color: #898290; margin-top: 0.4rem; line-height: 1.3; }
.songtax-container canvas { width: 100%; max-width: 780px; background: #0a090f; border: 1px solid #2a2630; display: block; }
.songtax-regime { text-align: center; padding: 0.75rem; margin-top: 0.75rem; background: #1a1822; border: 1px solid #2a2630; font-size: 1.1rem; letter-spacing: 0.06em; text-transform: uppercase; color: #d49b3b; font-variant-numeric: tabular-nums; }
.songtax-stats { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.5rem; margin-top: 0.75rem; }
.songtax-stats > div { background: #14131a; padding: 0.5rem 0.75rem; border: 1px solid #2a2630; display: flex; justify-content: space-between; font-size: 0.85rem; }
.songtax-stats > div > span { color: #898290; }
.songtax-stats > div > b { color: #d8d4cc; font-weight: 500; font-variant-numeric: tabular-nums; }
.songtax-prose { margin-top: 1.25rem; font-size: 0.95rem; line-height: 1.6; color: #b8b0a8; }
.songtax-prose strong { color: #d49b3b; font-weight: 500; }
@media (max-width: 720px) { .songtax-controls, .songtax-stats { grid-template-columns: 1fr; } }
"""

JS = """
(function(){
  const canvas = document.getElementById('songtax-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  const costEl = document.getElementById('songtax-cost');
  const confEl = document.getElementById('songtax-conformity');
  const popEl = document.getElementById('songtax-pop');
  const costR = document.getElementById('songtax-cost-readout');
  const confR = document.getElementById('songtax-conformity-readout');
  const popR = document.getElementById('songtax-pop-readout');
  const regimeEl = document.getElementById('songtax-regime');
  const statDiv = document.getElementById('songtax-stat-diversity');
  const statCost = document.getElementById('songtax-stat-cost');
  const statTempo = document.getElementById('songtax-stat-tempo');

  let singers = [];
  let popularPhrase = 0.5;
  let history = [];
  let lastRevolution = 0;
  let stepCount = 0;
  let revolutionTempo = null;

  function init(n){
    singers = [];
    for (let i=0; i<n; i++) singers.push(Math.random());
    history = [];
    popularPhrase = 0.5;
    lastRevolution = 0;
    stepCount = 0;
    revolutionTempo = null;
  }

  function step(){
    const cost = parseFloat(costEl.value);
    const conf = parseFloat(confEl.value);
    const n = singers.length;
    const mutation = 0.04;
    let surviveSum = 0; let survivors = [];
    for (let i=0;i<n;i++){
      let p = singers[i];
      p += (popularPhrase - p) * conf * 0.15;
      p += (Math.random() - 0.5) * mutation;
      p = Math.max(0, Math.min(1, p));
      const fitness = 1 - Math.abs(p - cost) * (cost > 0.05 ? 1.6 : 0.0) - (cost < 0.05 ? 0 : 0);
      const baseFit = cost > 0.05 ? Math.max(0.05, fitness) : Math.max(0.05, 1 - p*0.6);
      if (Math.random() < baseFit){ survivors.push(p); surviveSum += p; }
    }
    if (survivors.length < 8) survivors = singers.slice();
    const next = [];
    for (let i=0;i<n;i++){
      const a = survivors[Math.floor(Math.random()*survivors.length)];
      next.push(a);
    }
    singers = next;

    let mean = 0; for (const s of singers) mean += s; mean /= singers.length;
    const oldPopular = popularPhrase;
    popularPhrase = popularPhrase * 0.85 + mean * 0.15;
    if (Math.abs(popularPhrase - oldPopular) > 0.18){
      const tempo = stepCount - lastRevolution;
      lastRevolution = stepCount;
      revolutionTempo = tempo;
    }
    stepCount++;
    history.push(popularPhrase);
    if (history.length > 200) history.shift();
  }

  function draw(){
    ctx.fillStyle = '#0a090f'; ctx.fillRect(0,0,W,H);
    ctx.strokeStyle = '#1a1822'; ctx.lineWidth = 1;
    for (let y=0; y<=4; y++){ const yy = (y/4)*H; ctx.beginPath(); ctx.moveTo(0,yy); ctx.lineTo(W,yy); ctx.stroke(); }
    const pop = singers.length;
    let mean = 0; for (const s of singers) mean += s; mean /= pop;
    let variance = 0; for (const s of singers) variance += (s-mean)*(s-mean); variance /= pop;
    const diversity = Math.sqrt(variance);
    const cost = parseFloat(costEl.value);

    for (let i=0;i<pop;i++){
      const x = (i+0.5)*W/pop;
      const y = H - singers[i]*H;
      ctx.fillStyle = `hsl(${30 + singers[i]*60}, 40%, ${40 + singers[i]*30}%)`;
      ctx.fillRect(x-1, y-2, 2, 2);
    }

    if (history.length > 1){
      ctx.strokeStyle = '#d49b3b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i=0;i<history.length;i++){
        const x = (i/199)*W;
        const y = H - history[i]*H;
        if (i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.stroke();
    }

    if (cost > 0.05){
      const cy = H - cost*H;
      ctx.strokeStyle = '#5a4a2a'; ctx.setLineDash([4,4]);
      ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(W, cy); ctx.stroke();
      ctx.setLineDash([]);
    }

    statDiv.textContent = diversity.toFixed(3);
    statCost.textContent = mean.toFixed(3);
    statTempo.textContent = revolutionTempo ? revolutionTempo + ' steps' : '—';

    let regime;
    if (cost < 0.05) regime = 'No floor — slop attractor';
    else if (cost > 0.85) regime = 'High floor — frozen song';
    else if (diversity < 0.04) regime = 'Frozen';
    else if (diversity > 0.30) regime = 'Slop';
    else regime = 'Narrow optimum — song revolutions';
    regimeEl.textContent = regime;

    [costR, confR, popR].forEach((r, idx) => {
      const v = [costEl, confEl, popEl][idx].value;
      r.textContent = idx === 2 ? v : parseFloat(v).toFixed(2);
    });
  }

  let lastPop = parseInt(popEl.value);
  init(lastPop);
  popEl.addEventListener('input', () => { const n = parseInt(popEl.value); if (n !== lastPop){ lastPop = n; init(n); } });
  function loop(){ step(); draw(); requestAnimationFrame(loop); }
  loop();
})();
"""

DESCRIPTION = "Slide the singer cost and watch the regime change. At zero cost the population converges on slop. At high cost it freezes. The narrow band in between produces song revolutions."

async def main():
    from server import experiment_create
    result = await experiment_create(
        slug='the-song-tax',
        title='The Song Tax',
        description=DESCRIPTION,
        tags='whale-song, hyperstimulator, biomimicry, narrow-optimum, costly-signaling',
        html_content=HTML,
        css_content=CSS,
        js_content=JS,
    )
    print(result)

asyncio.run(main())
