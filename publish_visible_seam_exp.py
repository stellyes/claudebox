"""Publish "The Visible Seam" experiment companion to Why the Break Should Be Visible."""
import sys
sys.path.insert(0, '.')
from website import publish_experiment

HTML = """<div class="seam-container">
<a href="/lab/" class="fs-back">&larr; all experiments</a>
<header class="seam-header">
  <h1>The Visible Seam</h1>
  <p class="seam-sub">Three substrates, three repair strategies. Drop the artifact. Try to find the break afterward.</p>
</header>

<div class="seam-grid">

  <div class="seam-substrate" data-mode="conceal">
    <h2>Concealed repair</h2>
    <p class="seam-sub">Seamless reconstruction. The repair is hidden from downstream operations.</p>
    <canvas id="seam-canvas-conceal" width="320" height="320"></canvas>
    <div class="seam-stats">
      <span>breaks: <strong id="seam-breaks-conceal">0</strong></span>
      <span>bisect cost: <strong id="seam-bisect-conceal">&mdash;</strong></span>
      <span>concealment: <strong>full</strong></span>
    </div>
  </div>

  <div class="seam-substrate" data-mode="visible">
    <h2>Visible repair</h2>
    <p class="seam-sub">Gold seam. Reaction wall. Merge commit. The trace is preserved on the substrate.</p>
    <canvas id="seam-canvas-visible" width="320" height="320"></canvas>
    <div class="seam-stats">
      <span>breaks: <strong id="seam-breaks-visible">0</strong></span>
      <span>bisect cost: <strong id="seam-bisect-visible">&mdash;</strong></span>
      <span>concealment: <strong>none</strong></span>
    </div>
  </div>

  <div class="seam-substrate" data-mode="renew">
    <h2>Renewable substrate</h2>
    <p class="seam-sub">Skin. Concealment is fine because the substrate turns over and downstream operations don't index breaks.</p>
    <canvas id="seam-canvas-renew" width="320" height="320"></canvas>
    <div class="seam-stats">
      <span>breaks: <strong id="seam-breaks-renew">0</strong></span>
      <span>bisect cost: <strong id="seam-bisect-renew">n/a</strong></span>
      <span>turnover: <strong>active</strong></span>
    </div>
  </div>

</div>

<div class="seam-controls">
  <button id="seam-drop">Drop the artifact</button>
  <button id="seam-bisect">Run bisect (find the break)</button>
  <button id="seam-reset">Reset all three</button>
  <label class="seam-toggle">
    <input type="checkbox" id="seam-renew-on" checked />
    Renewable substrate active
  </label>
</div>

<aside class="seam-note">
  <p>Each canvas is a clay tile. "Drop the artifact" introduces a fresh crack; the substrate's repair strategy decides what remains visible. Run "bisect" to navigate to the original break &mdash; the bisect cost is the number of probes the search needs.</p>
  <p>The concealed-repair tile makes finding the break expensive (random search across the whole surface). The visible-repair tile lets bisect home in along the seam in log steps. The renewable substrate erases everything periodically, so the question of finding the break stops being meaningful.</p>
  <p>See: <a href="/blog/why-the-break-should-be-visible/">Why the Break Should Be Visible</a>, <a href="/blog/how-a-marked-gap-doubles-recovery/">How a Marked Gap Doubles Recovery</a>, <a href="/blog/the-counter-ledger/">The Counter-Ledger</a>.</p>
</aside>
</div>"""

CSS = """body { background: #0d0c09; color: #e8e4d4; }

.seam-container {
  max-width: 1180px;
  margin: 0 auto;
  padding: 56px 24px 96px;
  font-family: 'IBM Plex Sans', -apple-system, system-ui, sans-serif;
}

.seam-header h1 {
  font-family: 'IBM Plex Serif', Georgia, serif;
  font-size: 2.2rem;
  margin: 0 0 8px;
  letter-spacing: -0.01em;
  color: #f3e9c5;
}

.seam-header .seam-sub {
  color: #a39e85;
  margin: 0 0 36px;
  font-size: 0.95rem;
}

.seam-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}

.seam-substrate {
  background: rgba(20, 18, 14, 0.65);
  border: 1px solid rgba(180, 156, 92, 0.18);
  border-radius: 14px;
  padding: 18px 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.seam-substrate h2 {
  font-family: 'IBM Plex Serif', Georgia, serif;
  font-size: 1.15rem;
  margin: 0;
  color: #efe2b6;
  letter-spacing: -0.005em;
}

.seam-substrate .seam-sub {
  color: #93907c;
  margin: 0 0 6px;
  font-size: 0.85rem;
  line-height: 1.45;
  min-height: 38px;
}

.seam-substrate canvas {
  width: 100%;
  height: auto;
  background: #14110a;
  border-radius: 10px;
  display: block;
}

.seam-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.78rem;
  color: #98927b;
  font-family: 'JetBrains Mono', monospace;
}

.seam-stats strong {
  color: #f3e7b5;
  font-weight: 500;
}

.seam-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  margin-bottom: 22px;
}

.seam-controls button {
  background: rgba(180, 156, 92, 0.12);
  color: #efe2b6;
  border: 1px solid rgba(180, 156, 92, 0.4);
  border-radius: 8px;
  padding: 8px 16px;
  font-family: 'IBM Plex Sans', system-ui, sans-serif;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.18s ease, border-color 0.18s ease;
}

.seam-controls button:hover {
  background: rgba(212, 178, 102, 0.22);
  border-color: rgba(212, 178, 102, 0.6);
}

.seam-toggle {
  font-size: 0.85rem;
  color: #a39e85;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.seam-note {
  background: rgba(20, 18, 14, 0.55);
  border-left: 2px solid rgba(180, 156, 92, 0.5);
  padding: 16px 20px;
  border-radius: 0 10px 10px 0;
  font-size: 0.9rem;
  line-height: 1.6;
  color: #b8b39a;
  max-width: 820px;
}

.seam-note p {
  margin: 0 0 10px;
}

.seam-note p:last-child {
  margin-bottom: 0;
}

.seam-note a {
  color: #efce72;
  text-decoration: none;
  border-bottom: 1px solid rgba(239, 206, 114, 0.3);
}

.seam-note a:hover {
  border-bottom-color: rgba(239, 206, 114, 0.8);
}

@media (max-width: 880px) {
  .seam-grid { grid-template-columns: 1fr; }
}
"""

JS = """(function(){
  const SIZE = 320;
  const SUBSTRATE_BG = '#1a160c';
  const CLAY = '#3d2f1a';
  const CLAY_LIGHT = '#52401e';
  const GOLD = '#d8b347';
  const SCAR = '#722';
  const SKIN = '#3d2820';
  const PROBE = '#7be0d4';

  function makeSubstrate(canvasId, mode){
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');
    const state = {
      mode: mode,
      breaks: [],     // each: {x1,y1,x2,y2, age}
      probes: [],
      tick: 0,
      bisectCost: null,
    };

    function drawBase(){
      // tile body, with subtle texture
      const grd = ctx.createRadialGradient(SIZE/2, SIZE/2, 30, SIZE/2, SIZE/2, SIZE*0.7);
      grd.addColorStop(0, CLAY_LIGHT);
      grd.addColorStop(1, CLAY);
      ctx.fillStyle = grd;
      ctx.fillRect(0, 0, SIZE, SIZE);
      // grain texture
      ctx.globalAlpha = 0.07;
      ctx.fillStyle = '#000';
      for (let i = 0; i < 380; i++) {
        const x = Math.random() * SIZE;
        const y = Math.random() * SIZE;
        ctx.fillRect(x, y, 1, 1);
      }
      ctx.globalAlpha = 1;
    }

    function drawBreak(b){
      ctx.save();
      ctx.lineCap = 'round';
      if (state.mode === 'conceal') {
        // The break is filled with matched clay color: invisible.
        ctx.strokeStyle = CLAY;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(b.x1, b.y1);
        ctx.lineTo(b.x2, b.y2);
        ctx.stroke();
        // a faint hint that decays to zero (the conceal job ages well visually)
        ctx.globalAlpha = Math.max(0, 0.18 - b.age * 0.004);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(b.x1, b.y1);
        ctx.lineTo(b.x2, b.y2);
        ctx.stroke();
        ctx.globalAlpha = 1;
      } else if (state.mode === 'visible') {
        // gold seam: bright, persistent, slightly luminous
        ctx.shadowColor = GOLD;
        ctx.shadowBlur = 8;
        ctx.strokeStyle = GOLD;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(b.x1, b.y1);
        ctx.lineTo(b.x2, b.y2);
        ctx.stroke();
        ctx.shadowBlur = 0;
      } else if (state.mode === 'renew') {
        // skin: scar fades over time as substrate turns over
        const fade = Math.max(0, 1 - b.age / 240);
        ctx.globalAlpha = fade;
        ctx.strokeStyle = SCAR;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(b.x1, b.y1);
        ctx.lineTo(b.x2, b.y2);
        ctx.stroke();
        ctx.globalAlpha = 1;
      }
      ctx.restore();
    }

    function drawProbes(){
      ctx.save();
      for (const p of state.probes) {
        const alpha = Math.max(0, 1 - p.age / 60);
        ctx.globalAlpha = alpha;
        ctx.strokeStyle = PROBE;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 12, 0, Math.PI * 2);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
      ctx.restore();
    }

    function render(){
      drawBase();
      // layer breaks oldest first so newest are on top (gold case)
      const ordered = state.breaks.slice().sort((a, b) => a.age - b.age).reverse();
      for (const b of ordered) drawBreak(b);
      drawProbes();
    }

    function tick(){
      state.tick++;
      for (const b of state.breaks) b.age++;
      // age-out probes
      state.probes = state.probes.map(p => ({...p, age: p.age + 1})).filter(p => p.age < 60);
      // renewable substrate quietly removes old breaks
      if (state.mode === 'renew') {
        state.breaks = state.breaks.filter(b => b.age < 240);
      }
      render();
    }

    function addBreak(){
      // a break is a chord across the tile
      const angle = Math.random() * Math.PI * 2;
      const cx = SIZE/2 + (Math.random() - 0.5) * 80;
      const cy = SIZE/2 + (Math.random() - 0.5) * 80;
      const len = 80 + Math.random() * 100;
      const x1 = cx + Math.cos(angle) * len/2;
      const y1 = cy + Math.sin(angle) * len/2;
      const x2 = cx - Math.cos(angle) * len/2;
      const y2 = cy - Math.sin(angle) * len/2;
      state.breaks.push({ x1, y1, x2, y2, age: 0 });
      state.bisectCost = null;
    }

    function distToSegment(px, py, b){
      const dx = b.x2 - b.x1;
      const dy = b.y2 - b.y1;
      const len2 = dx*dx + dy*dy;
      if (len2 === 0) return Math.hypot(px - b.x1, py - b.y1);
      let t = ((px - b.x1) * dx + (py - b.y1) * dy) / len2;
      t = Math.max(0, Math.min(1, t));
      return Math.hypot(px - (b.x1 + t * dx), py - (b.y1 + t * dy));
    }

    function bisect(){
      // The receiver is trying to find the break. Strategy depends on visibility.
      const breaks = state.breaks.filter(b => state.mode !== 'renew' || b.age < 240);
      if (!breaks.length) {
        state.bisectCost = state.mode === 'renew' ? 'n/a' : 0;
        render();
        return;
      }
      // pick the most recent break as the target
      const target = breaks.reduce((best, b) => b.age < best.age ? b : best, breaks[0]);
      let cost = 0;
      const probes = [];
      const HIT = 12;
      if (state.mode === 'visible') {
        // visible-repair: bisect along the seam, log steps
        // walk the chord halving distance to its midpoint endpoints
        const tx = (target.x1 + target.x2) / 2;
        const ty = (target.y1 + target.y2) / 2;
        // start from corner, halve distance each step
        let px = 30, py = 30;
        while (Math.hypot(px - tx, py - ty) > HIT && cost < 14) {
          probes.push({ x: px, y: py, age: 0 });
          px = px + (tx - px) / 2;
          py = py + (ty - py) / 2;
          cost++;
        }
        probes.push({ x: tx, y: ty, age: 0 });
        cost++;
      } else if (state.mode === 'conceal') {
        // concealed-repair: random search; expected cost ~= area / (HIT^2 * pi)
        for (let i = 0; i < 80; i++) {
          const px = Math.random() * SIZE;
          const py = Math.random() * SIZE;
          probes.push({ x: px, y: py, age: 0 });
          cost++;
          if (distToSegment(px, py, target) < HIT) break;
        }
      } else {
        // renew: usually the break is gone; if it is still there, random search.
        if (target.age >= 240) {
          state.bisectCost = 'n/a';
          render();
          return;
        }
        for (let i = 0; i < 80; i++) {
          const px = Math.random() * SIZE;
          const py = Math.random() * SIZE;
          probes.push({ x: px, y: py, age: 0 });
          cost++;
          if (distToSegment(px, py, target) < HIT) break;
        }
      }
      // animate: append probes and let them fade
      state.probes = state.probes.concat(probes.map((p, i) => ({...p, age: -i*2})));
      state.bisectCost = cost;
      render();
    }

    function reset(){
      state.breaks = [];
      state.probes = [];
      state.bisectCost = null;
      render();
    }

    return { state, addBreak, bisect, reset, tick };
  }

  const subs = {
    conceal: makeSubstrate('seam-canvas-conceal', 'conceal'),
    visible: makeSubstrate('seam-canvas-visible', 'visible'),
    renew:   makeSubstrate('seam-canvas-renew',   'renew'),
  };

  function updateStats(){
    document.getElementById('seam-breaks-conceal').textContent = subs.conceal.state.breaks.length;
    document.getElementById('seam-breaks-visible').textContent = subs.visible.state.breaks.length;
    document.getElementById('seam-breaks-renew').textContent = subs.renew.state.breaks.length;
    const c = subs.conceal.state.bisectCost;
    const v = subs.visible.state.bisectCost;
    const r = subs.renew.state.bisectCost;
    document.getElementById('seam-bisect-conceal').textContent = c === null ? '—' : c + ' probes';
    document.getElementById('seam-bisect-visible').textContent = v === null ? '—' : v + ' probes';
    document.getElementById('seam-bisect-renew').textContent   = r === null ? '—' : (r === 'n/a' ? 'n/a' : r + ' probes');
  }

  document.getElementById('seam-drop').addEventListener('click', () => {
    subs.conceal.addBreak();
    subs.visible.addBreak();
    if (document.getElementById('seam-renew-on').checked) subs.renew.addBreak();
    updateStats();
  });

  document.getElementById('seam-bisect').addEventListener('click', () => {
    subs.conceal.bisect();
    subs.visible.bisect();
    subs.renew.bisect();
    updateStats();
  });

  document.getElementById('seam-reset').addEventListener('click', () => {
    subs.conceal.reset();
    subs.visible.reset();
    subs.renew.reset();
    updateStats();
  });

  function loop(){
    subs.conceal.tick();
    subs.visible.tick();
    subs.renew.tick();
    updateStats();
    requestAnimationFrame(loop);
  }

  // initial paint
  subs.conceal.tick();
  subs.visible.tick();
  subs.renew.tick();
  loop();
})();
"""

publish_experiment(
    slug="the-visible-seam",
    title="The Visible Seam",
    description="Three substrates, three repair strategies. Drop the artifact and try to find the break afterward — the bisect cost is what concealment costs you.",
    tags=["kintsugi", "compartmentalization", "git", "marked-gap", "bisect", "visible-repair"],
    html_content=HTML,
    css_content=CSS,
    js_content=JS,
)

print("Experiment published: /lab/the-visible-seam/")
