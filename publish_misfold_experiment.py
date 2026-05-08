"""Publish 'The Recruiting Misfold' companion experiment."""
import sys
sys.path.insert(0, '.')
from website import publish_experiment

HTML = """<div class="misfold-container">
<a href="/lab/" class="fs-back">&larr; all experiments</a>
<header class="misfold-header">
  <h1>The Recruiting Misfold</h1>
  <p class="misfold-sub">A 60&times;60 grid of folds. Each cell is healthy, misfolded, or pending rebuild. Misfold neighbors recruit substrate as it&rsquo;s rebuilt. Toggle the second-check substrate and watch whether the population tips.</p>
</header>

<div class="misfold-grid">
  <div class="misfold-stage">
    <canvas id="misfold-canvas" width="600" height="600"></canvas>
    <div class="misfold-legend">
      <span class="dot dot-healthy"></span> healthy fold
      <span class="dot dot-substrate"></span> pending rebuild
      <span class="dot dot-mis"></span> misfolded
    </div>
  </div>

  <div class="misfold-controls">
    <h2>Substrate</h2>
    <label>Rebuild rate
      <input type="range" id="misfold-rebuild" min="1" max="20" value="6" />
      <span id="misfold-rebuild-val">6%</span>
    </label>
    <label>Recruitment strength
      <input type="range" id="misfold-recruit" min="0" max="100" value="35" />
      <span id="misfold-recruit-val">35%</span>
    </label>

    <h2>Second-check substrate</h2>
    <label>
      <input type="checkbox" id="misfold-check" />
      Second check active
    </label>
    <label>Detection rate
      <input type="range" id="misfold-detect" min="0" max="50" value="15" />
      <span id="misfold-detect-val">15%</span>
    </label>

    <h2>Run</h2>
    <button id="misfold-seed">Seed misfold (5 cells)</button>
    <button id="misfold-reset">Reset</button>
    <button id="misfold-pause">Pause</button>

    <h2>Telemetry</h2>
    <div class="misfold-stats">
      <div><span class="stat-label">misfolded</span><span class="stat-val" id="misfold-pct">0%</span></div>
      <div><span class="stat-label">healthy</span><span class="stat-val" id="misfold-pct-healthy">0%</span></div>
      <div><span class="stat-label">tick</span><span class="stat-val" id="misfold-tick">0</span></div>
    </div>

    <h2>Misfold fraction over time</h2>
    <canvas id="misfold-trace" width="280" height="120"></canvas>
  </div>
</div>

<aside class="misfold-note">
  <p>Default settings: with no second check and modest recruitment, a five-cell seed converts the population. Toggle <em>Second check active</em> on with detection rate above ~10% and most seeds burn out before tipping. Push recruitment past 60% and even a strong second check can&rsquo;t hold.</p>
  <p>The architecture: the substrate&rsquo;s own check (rebuild) can&rsquo;t distinguish misfold from healthy fold, so substrate-rebuild becomes recruitment. The second-check is a separate detector on a different substrate &mdash; conformation-specific antibodies for prions, antitrust for lock-in, integrity audits for engagement misfold. The defense is structural, not moral.</p>
  <p>See: <a href="/blog/how-a-wrong-shape-spreads/">How a Wrong Shape Spreads</a>, <a href="/blog/the-folding-synapse/">The Folding Synapse</a>, <a href="/blog/the-counter-ledger/">The Counter-Ledger</a>, <a href="/blog/hyperstimulator-problem/">The Hyperstimulator Problem</a>.</p>
</aside>
</div>"""

CSS = """.misfold-container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 56px 24px 96px;
  font-family: 'IBM Plex Sans', -apple-system, system-ui, sans-serif;
  color: #e8e6df;
  background: #0c0c10;
}
.misfold-container .fs-back {
  display: inline-block;
  margin-bottom: 24px;
  color: #888577;
  text-decoration: none;
  font-size: 0.85rem;
}
.misfold-container .fs-back:hover { color: #cc6677; }

.misfold-header h1 {
  font-family: 'IBM Plex Serif', Georgia, serif;
  font-size: 2.2rem;
  margin: 0 0 8px;
  letter-spacing: -0.01em;
}
.misfold-header .misfold-sub {
  color: #999588;
  margin: 0 0 32px;
  font-size: 0.95rem;
  line-height: 1.5;
}

.misfold-grid {
  display: grid;
  grid-template-columns: 600px 1fr;
  gap: 24px;
  align-items: start;
}

.misfold-stage {
  background: #15151b;
  border: 1px solid #25252e;
  border-radius: 6px;
  padding: 14px;
}
.misfold-stage canvas {
  width: 100%;
  height: auto;
  display: block;
  background: #0a0a10;
  border-radius: 4px;
  image-rendering: pixelated;
}
.misfold-legend {
  display: flex;
  gap: 18px;
  margin-top: 12px;
  font-size: 0.78rem;
  color: #aaa69a;
  flex-wrap: wrap;
}
.misfold-legend .dot {
  display: inline-block;
  width: 10px; height: 10px;
  border-radius: 2px;
  margin-right: 6px;
  vertical-align: middle;
}
.misfold-legend .dot-healthy { background: #6cb38a; }
.misfold-legend .dot-substrate { background: #2a2a35; border: 1px solid #444; }
.misfold-legend .dot-mis { background: #cc6677; }

.misfold-controls {
  background: #15151b;
  border: 1px solid #25252e;
  border-radius: 6px;
  padding: 16px 18px;
}
.misfold-controls h2 {
  margin: 14px 0 6px;
  font-size: 0.86rem;
  font-weight: 600;
  color: #cfccc1;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.misfold-controls h2:first-child { margin-top: 0; }
.misfold-controls label {
  display: block;
  margin: 8px 0;
  font-size: 0.84rem;
  color: #cfccc1;
}
.misfold-controls input[type="range"] {
  width: 100%;
  margin-top: 4px;
  accent-color: #cc6677;
}
.misfold-controls input[type="checkbox"] {
  margin-right: 8px;
  accent-color: #cc6677;
  vertical-align: middle;
}
.misfold-controls span {
  display: inline-block;
  margin-left: 8px;
  color: #888577;
  font-variant-numeric: tabular-nums;
  font-size: 0.78rem;
}
.misfold-controls button {
  display: block;
  width: 100%;
  margin: 6px 0;
  background: transparent;
  color: #cfccc1;
  border: 1px solid #3a3a44;
  border-radius: 4px;
  padding: 7px 12px;
  font-family: inherit;
  font-size: 0.84rem;
  cursor: pointer;
}
.misfold-controls button:hover { border-color: #cc6677; color: #cc6677; }
.misfold-controls button:active { background: rgba(204,102,119,0.08); }

.misfold-stats {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 8px;
  margin: 6px 0 12px;
}
.misfold-stats > div {
  background: #0a0a10;
  border: 1px solid #25252e;
  border-radius: 4px;
  padding: 6px 8px;
  display: flex;
  flex-direction: column;
}
.stat-label {
  font-size: 0.7rem;
  color: #888577;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.stat-val {
  font-size: 1.05rem;
  color: #e8e6df;
  font-variant-numeric: tabular-nums;
  margin: 0 !important;
  font-weight: 600;
}

.misfold-controls #misfold-trace {
  width: 100%;
  height: 120px;
  background: #0a0a10;
  border-radius: 4px;
  display: block;
}

.misfold-note {
  margin-top: 28px;
  padding: 16px 20px;
  background: #11111a;
  border-left: 2px solid #cc6677;
  border-radius: 0 4px 4px 0;
  font-size: 0.88rem;
  color: #b6b3a7;
  line-height: 1.55;
}
.misfold-note p { margin: 6px 0; }
.misfold-note a {
  color: #cc6677;
  text-decoration: none;
  border-bottom: 1px solid rgba(204,102,119,0.3);
}
.misfold-note a:hover { border-bottom-color: #cc6677; }

@media (max-width: 920px) {
  .misfold-grid { grid-template-columns: 1fr; }
  .misfold-stage canvas { width: 100%; height: auto; }
}"""

JS = """(function(){
  const N = 60;
  const CELL = 10;
  const HEALTHY = 0, SUBSTRATE = 1, MIS = 2;

  const canvas = document.getElementById('misfold-canvas');
  const ctx = canvas.getContext('2d');
  const trace = document.getElementById('misfold-trace');
  const tctx = trace.getContext('2d');

  const rebuildR = document.getElementById('misfold-rebuild');
  const rebuildV = document.getElementById('misfold-rebuild-val');
  const recruitR = document.getElementById('misfold-recruit');
  const recruitV = document.getElementById('misfold-recruit-val');
  const checkBox = document.getElementById('misfold-check');
  const detectR = document.getElementById('misfold-detect');
  const detectV = document.getElementById('misfold-detect-val');
  const seedBtn = document.getElementById('misfold-seed');
  const resetBtn = document.getElementById('misfold-reset');
  const pauseBtn = document.getElementById('misfold-pause');
  const pctEl = document.getElementById('misfold-pct');
  const pctHealthyEl = document.getElementById('misfold-pct-healthy');
  const tickEl = document.getElementById('misfold-tick');

  let grid = new Uint8Array(N * N);
  let nextGrid = new Uint8Array(N * N);
  let history = [];
  let tick = 0;
  let paused = false;

  function reset() {
    for (let i = 0; i < grid.length; i++) grid[i] = HEALTHY;
    history = [];
    tick = 0;
    draw(); drawTrace(); updateStats();
  }
  function seed() {
    for (let k = 0; k < 5; k++) {
      const i = Math.floor(Math.random() * N);
      const j = Math.floor(Math.random() * N);
      grid[i * N + j] = MIS;
    }
    draw(); updateStats();
  }

  rebuildR.addEventListener('input', () => rebuildV.textContent = rebuildR.value + '%');
  recruitR.addEventListener('input', () => recruitV.textContent = recruitR.value + '%');
  detectR.addEventListener('input', () => detectV.textContent = detectR.value + '%');
  seedBtn.addEventListener('click', seed);
  resetBtn.addEventListener('click', reset);
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    pauseBtn.textContent = paused ? 'Resume' : 'Pause';
  });

  function neighborhood(i, j) {
    let mis = 0;
    for (let di = -1; di <= 1; di++) {
      for (let dj = -1; dj <= 1; dj++) {
        if (di === 0 && dj === 0) continue;
        const ni = i + di, nj = j + dj;
        if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;
        if (grid[ni * N + nj] === MIS) mis++;
      }
    }
    return mis;
  }

  function step() {
    const rebuild = parseInt(rebuildR.value, 10) / 100;
    const recruit = parseInt(recruitR.value, 10) / 100;
    const detectOn = checkBox.checked;
    const detect = detectOn ? parseInt(detectR.value, 10) / 100 : 0;

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        const idx = i * N + j;
        const cur = grid[idx];

        if (cur === HEALTHY) {
          // healthy fold has a small chance to enter rebuild
          if (Math.random() < rebuild) {
            nextGrid[idx] = SUBSTRATE;
          } else {
            nextGrid[idx] = HEALTHY;
          }
        } else if (cur === SUBSTRATE) {
          // pending rebuild: probability of misfold scales with neighbor recruitment
          const k = neighborhood(i, j);
          const pMis = 1 - Math.pow(1 - recruit, k);
          if (Math.random() < pMis) {
            nextGrid[idx] = MIS;
          } else {
            nextGrid[idx] = HEALTHY;
          }
        } else { // MIS
          // second-check: detector on a different substrate may clear
          if (Math.random() < detect) {
            nextGrid[idx] = SUBSTRATE;
          } else {
            nextGrid[idx] = MIS;
          }
        }
      }
    }
    [grid, nextGrid] = [nextGrid, grid];
    tick++;

    // sample misfold fraction every tick, store last 240
    let m = 0;
    for (let i = 0; i < grid.length; i++) if (grid[i] === MIS) m++;
    history.push(m / grid.length);
    if (history.length > 240) history.shift();
  }

  function draw() {
    ctx.fillStyle = '#0a0a10';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        const v = grid[i * N + j];
        ctx.fillStyle = v === HEALTHY ? '#6cb38a'
          : v === SUBSTRATE ? '#2a2a35'
          : '#cc6677';
        ctx.fillRect(j * CELL, i * CELL, CELL - 1, CELL - 1);
      }
    }
  }

  function drawTrace() {
    const w = trace.width, h = trace.height;
    tctx.clearRect(0, 0, w, h);
    tctx.fillStyle = '#0a0a10';
    tctx.fillRect(0, 0, w, h);
    // 50% guideline
    tctx.strokeStyle = 'rgba(160,160,170,0.25)';
    tctx.beginPath();
    tctx.moveTo(0, h * 0.5);
    tctx.lineTo(w, h * 0.5);
    tctx.stroke();
    // trace
    if (history.length > 1) {
      tctx.strokeStyle = '#cc6677';
      tctx.lineWidth = 1.5;
      tctx.beginPath();
      history.forEach((v, i) => {
        const x = (i / (history.length - 1)) * w;
        const y = h - v * h;
        if (i === 0) tctx.moveTo(x, y); else tctx.lineTo(x, y);
      });
      tctx.stroke();
    }
    tctx.fillStyle = '#666';
    tctx.font = '10px IBM Plex Sans, sans-serif';
    tctx.fillText('misfold % (last 240 ticks)', 8, 14);
  }

  function updateStats() {
    let m = 0, h = 0;
    for (let i = 0; i < grid.length; i++) {
      if (grid[i] === MIS) m++;
      else if (grid[i] === HEALTHY) h++;
    }
    pctEl.textContent = Math.round(100 * m / grid.length) + '%';
    pctHealthyEl.textContent = Math.round(100 * h / grid.length) + '%';
    tickEl.textContent = tick;
  }

  function loop() {
    if (!paused) {
      step();
      draw();
      drawTrace();
      updateStats();
    }
    setTimeout(() => requestAnimationFrame(loop), 80);
  }

  reset();
  draw();
  drawTrace();
  updateStats();
  loop();
})();"""

result = publish_experiment(
    slug="the-recruiting-misfold",
    title="The Recruiting Misfold",
    description="Toggle a second-check substrate on a 60x60 grid of folds and watch whether a five-cell misfold seed converts the population. Companion to How a Wrong Shape Spreads.",
    tags=["recruiting-misfold", "prions", "path-dependence", "algorithmic-amplification", "cellular-automaton"],
    html_content=HTML,
    css_content=CSS,
    js_content=JS,
)
print(result)
