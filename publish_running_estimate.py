"""Publish The Running Estimate companion experiment."""
import sys
sys.path.insert(0, '.')
from website import publish_experiment

HTML = """<div class="rest-container">
<a href="/lab/" class="fs-back">&larr; all experiments</a>
<header class="rest-header">
  <h1>The Running Estimate</h1>
  <p class="rest-sub">Stream events into a memory. Toggle the Counter-Ledger. Watch which surprises get written.</p>
</header>

<div class="rest-grid">
  <div class="rest-stream">
    <h2>Event stream</h2>
    <canvas id="rest-stream-canvas" width="640" height="220"></canvas>
    <div class="rest-legend">
      <span class="dot dot-info"></span> informative event (surprise pays its cost)
      <span class="dot dot-hyper"></span> hyperstimulator (surprise far below running cost)
    </div>
  </div>

  <div class="rest-controls">
    <h2>Controls</h2>
    <label>
      <input type="checkbox" id="rest-counter" checked />
      Counter-Ledger active
    </label>
    <label>Hyperstimulator fraction
      <input type="range" id="rest-hyper" min="0" max="100" value="40" />
      <span id="rest-hyper-val">40%</span>
    </label>
    <label>Stream rate
      <input type="range" id="rest-rate" min="1" max="20" value="6" />
      <span id="rest-rate-val">6/s</span>
    </label>
    <label>Window (running average)
      <input type="range" id="rest-window" min="10" max="200" value="60" />
      <span id="rest-window-val">60</span>
    </label>
    <button id="rest-reset">Reset</button>
  </div>

  <div class="rest-memory rest-memory-naive">
    <h2>Naive memory (PER-style)</h2>
    <p class="rest-sub">Weighted by raw surprise.</p>
    <canvas id="rest-mem-naive" width="320" height="220"></canvas>
    <div class="rest-stats">
      <span>writes: <strong id="rest-naive-writes">0</strong></span>
      <span>hyperstim share: <strong id="rest-naive-share">0%</strong></span>
    </div>
  </div>

  <div class="rest-memory rest-memory-counter">
    <h2>Counter-Ledger memory</h2>
    <p class="rest-sub">Weighted by surprise &divide; running cost.</p>
    <canvas id="rest-mem-counter" width="320" height="220"></canvas>
    <div class="rest-stats">
      <span>writes: <strong id="rest-counter-writes">0</strong></span>
      <span>hyperstim share: <strong id="rest-counter-share">0%</strong></span>
      <span>running cost: <strong id="rest-running-cost">&mdash;</strong></span>
    </div>
  </div>
</div>

<aside class="rest-note">
  <p>The Counter-Ledger keeps a running average of <em>resolution cost</em> &mdash; the work it took to integrate each surprise. Inputs that surprise the system but resolve far below the average are flagged and downweighted before being written. PER-style memory has no such filter and fills with cheap surprise. Toggle it off to see what your prior corpus essays predict.</p>
  <p>See: <a href="/blog/the-counter-ledger/">The Counter-Ledger</a>, <a href="/blog/hyperstimulator-problem/">The Hyperstimulator Problem</a>, <a href="/blog/what-resistance-layers-protect/">What Resistance Layers Are Actually Protecting</a>.</p>
</aside>
</div>"""

CSS = """body { background: #0c0c10; color: #e8e6df; }
.rest-container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 56px 24px 96px;
  font-family: 'IBM Plex Sans', -apple-system, system-ui, sans-serif;
}
.rest-header h1 { font-family: 'IBM Plex Serif', Georgia, serif; font-size: 2.2rem; margin: 0 0 8px; letter-spacing: -0.01em; }
.rest-header .rest-sub { color: #999588; margin: 0 0 32px; font-size: 0.95rem; }
.rest-sub { color: #999588; margin: 4px 0; font-size: 0.85rem; }

.rest-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: auto auto;
  gap: 20px;
}
.rest-stream { grid-column: 1 / 2; grid-row: 1 / 2; }
.rest-controls { grid-column: 2 / 3; grid-row: 1 / 3; }
.rest-memory-naive { grid-column: 1 / 2; grid-row: 2 / 3; }
.rest-memory-counter { grid-column: 2 / 3; grid-row: 3 / 4; }

.rest-stream, .rest-controls, .rest-memory {
  background: #15151b;
  border: 1px solid #25252e;
  border-radius: 6px;
  padding: 18px 20px;
}
.rest-stream h2, .rest-controls h2, .rest-memory h2 {
  margin: 0 0 10px;
  font-size: 1rem;
  font-weight: 600;
  color: #cfccc1;
  letter-spacing: 0.02em;
}
.rest-stream canvas, .rest-memory canvas {
  width: 100%;
  height: 220px;
  display: block;
  background: #0a0a10;
  border-radius: 4px;
}
.rest-legend {
  display: flex;
  gap: 24px;
  margin-top: 10px;
  font-size: 0.8rem;
  color: #aaa69a;
}
.rest-legend .dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; vertical-align: middle; }
.dot-info { background: #6cb38a; }
.dot-hyper { background: #cc6677; }

.rest-controls label {
  display: block;
  margin: 12px 0;
  font-size: 0.88rem;
  color: #cfccc1;
}
.rest-controls input[type="range"] {
  width: 100%;
  margin-top: 4px;
  accent-color: #6cb38a;
}
.rest-controls input[type="checkbox"] {
  margin-right: 8px;
  accent-color: #6cb38a;
}
.rest-controls span {
  display: inline-block;
  margin-left: 8px;
  color: #888577;
  font-variant-numeric: tabular-nums;
}
#rest-reset {
  margin-top: 14px;
  background: transparent;
  color: #cfccc1;
  border: 1px solid #3a3a44;
  border-radius: 4px;
  padding: 6px 14px;
  font-family: inherit;
  font-size: 0.85rem;
  cursor: pointer;
}
#rest-reset:hover { border-color: #6cb38a; color: #6cb38a; }

.rest-memory { display: flex; flex-direction: column; }
.rest-stats {
  display: flex;
  gap: 18px;
  margin-top: 10px;
  font-size: 0.78rem;
  color: #aaa69a;
  flex-wrap: wrap;
}
.rest-stats strong { color: #e8e6df; font-variant-numeric: tabular-nums; }

.rest-note {
  margin-top: 28px;
  padding: 16px 20px;
  background: #11111a;
  border-left: 2px solid #6cb38a;
  border-radius: 0 4px 4px 0;
  font-size: 0.88rem;
  color: #b6b3a7;
  line-height: 1.55;
}
.rest-note p { margin: 6px 0; }
.rest-note a { color: #6cb38a; text-decoration: none; border-bottom: 1px solid rgba(108, 179, 138, 0.3); }
.rest-note a:hover { border-bottom-color: #6cb38a; }

.fs-back {
  display: inline-block;
  margin-bottom: 24px;
  color: #888577;
  text-decoration: none;
  font-size: 0.85rem;
}
.fs-back:hover { color: #6cb38a; }

@media (max-width: 760px) {
  .rest-grid { grid-template-columns: 1fr; }
  .rest-stream, .rest-controls, .rest-memory-naive, .rest-memory-counter { grid-column: 1 / 2; grid-row: auto; }
}"""

JS = """(function(){
  const streamCanvas = document.getElementById('rest-stream-canvas');
  const memNaive = document.getElementById('rest-mem-naive');
  const memCounter = document.getElementById('rest-mem-counter');
  const sCtx = streamCanvas.getContext('2d');
  const nCtx = memNaive.getContext('2d');
  const cCtx = memCounter.getContext('2d');

  const counterToggle = document.getElementById('rest-counter');
  const hyperRange = document.getElementById('rest-hyper');
  const hyperVal = document.getElementById('rest-hyper-val');
  const rateRange = document.getElementById('rest-rate');
  const rateVal = document.getElementById('rest-rate-val');
  const winRange = document.getElementById('rest-window');
  const winVal = document.getElementById('rest-window-val');
  const resetBtn = document.getElementById('rest-reset');

  const naiveWrites = document.getElementById('rest-naive-writes');
  const naiveShare = document.getElementById('rest-naive-share');
  const counterWrites = document.getElementById('rest-counter-writes');
  const counterShare = document.getElementById('rest-counter-share');
  const runningCostEl = document.getElementById('rest-running-cost');

  let stream = [];
  let costWindow = [];
  let memNaiveStore = [];
  let memCounterStore = [];
  let last = performance.now();
  let acc = 0;

  function reset() {
    stream = [];
    costWindow = [];
    memNaiveStore = [];
    memCounterStore = [];
    drawAll();
    updateStats();
  }
  resetBtn.addEventListener('click', reset);

  hyperRange.addEventListener('input', () => hyperVal.textContent = hyperRange.value + '%');
  rateRange.addEventListener('input', () => rateVal.textContent = rateRange.value + '/s');
  winRange.addEventListener('input', () => winVal.textContent = winRange.value);

  function drawStream() {
    const w = streamCanvas.width, h = streamCanvas.height;
    sCtx.clearRect(0, 0, w, h);
    sCtx.fillStyle = '#0a0a10';
    sCtx.fillRect(0, 0, w, h);
    // running cost line
    if (costWindow.length > 1) {
      sCtx.strokeStyle = 'rgba(180, 180, 180, 0.45)';
      sCtx.setLineDash([4, 4]);
      sCtx.lineWidth = 1;
      sCtx.beginPath();
      const avg = costWindow.reduce((a,b)=>a+b,0) / costWindow.length;
      const y = h - (avg / 1.2) * h;
      sCtx.moveTo(0, y);
      sCtx.lineTo(w, y);
      sCtx.stroke();
      sCtx.setLineDash([]);
    }
    const recent = stream.slice(-80);
    recent.forEach((ev, i) => {
      const x = (i / 80) * w;
      const y = h - (ev.surprise / 1.2) * h;
      sCtx.fillStyle = ev.kind === 'hyper' ? '#cc6677' : '#6cb38a';
      sCtx.beginPath();
      sCtx.arc(x, y, 3.2, 0, Math.PI * 2);
      sCtx.fill();
      // also tick the cost as a small mark
      sCtx.fillStyle = 'rgba(160, 160, 170, 0.6)';
      const yc = h - (ev.cost / 1.2) * h;
      sCtx.fillRect(x - 1, yc - 1, 2, 2);
    });
    sCtx.fillStyle = '#666';
    sCtx.font = '10px IBM Plex Sans, sans-serif';
    sCtx.fillText('surprise (top) / cost (small) over last 80 events', 8, 14);
  }

  function drawMem(canvas, ctx, store, color) {
    const w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a0a10';
    ctx.fillRect(0, 0, w, h);
    if (store.length === 0) {
      ctx.fillStyle = '#444';
      ctx.font = '11px IBM Plex Sans, sans-serif';
      ctx.fillText('memory empty', 12, 18);
      return;
    }
    const cellW = Math.max(2, Math.min(8, w / Math.max(1, store.length)));
    store.slice(-Math.floor(w / cellW)).forEach((ev, i) => {
      const x = i * cellW;
      const intensity = Math.min(1, ev.weight);
      ctx.fillStyle = ev.kind === 'hyper'
        ? `rgba(204, 102, 119, ${0.35 + intensity * 0.65})`
        : `rgba(108, 179, 138, ${0.35 + intensity * 0.65})`;
      ctx.fillRect(x, h - intensity * h, cellW - 1, intensity * h);
    });
    ctx.fillStyle = '#666';
    ctx.font = '10px IBM Plex Sans, sans-serif';
    ctx.fillText(`bar height = stored weight, color = kind`, 8, 14);
  }

  function drawAll() {
    drawStream();
    drawMem(memNaive, nCtx, memNaiveStore, 'naive');
    drawMem(memCounter, cCtx, memCounterStore, 'counter');
  }

  function updateStats() {
    naiveWrites.textContent = memNaiveStore.length;
    counterWrites.textContent = memCounterStore.length;
    const nh = memNaiveStore.filter(e => e.kind === 'hyper').length;
    const ch = memCounterStore.filter(e => e.kind === 'hyper').length;
    naiveShare.textContent = memNaiveStore.length ? Math.round(100 * nh / memNaiveStore.length) + '%' : '0%';
    counterShare.textContent = memCounterStore.length ? Math.round(100 * ch / memCounterStore.length) + '%' : '0%';
    if (costWindow.length > 0) {
      const avg = costWindow.reduce((a,b)=>a+b,0) / costWindow.length;
      runningCostEl.textContent = avg.toFixed(2);
    }
  }

  function generateEvent() {
    const hyperFrac = parseInt(hyperRange.value, 10) / 100;
    const isHyper = Math.random() < hyperFrac;
    if (isHyper) {
      // hyperstimulator: surprise high, cost low
      return { kind: 'hyper', surprise: 0.7 + Math.random() * 0.3, cost: 0.05 + Math.random() * 0.1 };
    } else {
      // informative: surprise roughly tracks cost
      const c = 0.3 + Math.random() * 0.6;
      const noise = (Math.random() - 0.5) * 0.15;
      return { kind: 'info', surprise: Math.max(0.1, Math.min(1.0, c + noise)), cost: c };
    }
  }

  function ingest(ev) {
    stream.push(ev);
    if (stream.length > 400) stream.shift();
    costWindow.push(ev.cost);
    const win = parseInt(winRange.value, 10);
    while (costWindow.length > win) costWindow.shift();

    // Naive memory: weight = surprise.
    // Threshold for write: surprise > 0.4
    if (ev.surprise > 0.4) {
      memNaiveStore.push({ kind: ev.kind, weight: ev.surprise });
      if (memNaiveStore.length > 240) memNaiveStore.shift();
    }

    // Counter-Ledger memory: weight = surprise / running_cost_avg, capped.
    // Write only if normalized weight > 0.6 (downweights cheap-resolution).
    const counterActive = counterToggle.checked;
    if (counterActive) {
      const avg = costWindow.length ? costWindow.reduce((a,b)=>a+b,0) / costWindow.length : 0.5;
      const ratio = ev.cost / Math.max(0.05, avg);
      const w = Math.min(1.2, ev.surprise * ratio);
      if (w > 0.4) {
        memCounterStore.push({ kind: ev.kind, weight: Math.min(1.0, w) });
        if (memCounterStore.length > 240) memCounterStore.shift();
      }
    } else {
      // mirrors naive behaviour when toggle is off
      if (ev.surprise > 0.4) {
        memCounterStore.push({ kind: ev.kind, weight: ev.surprise });
        if (memCounterStore.length > 240) memCounterStore.shift();
      }
    }
  }

  function tick(now) {
    const dt = (now - last) / 1000;
    last = now;
    const rate = parseInt(rateRange.value, 10);
    acc += dt * rate;
    while (acc >= 1) {
      ingest(generateEvent());
      acc -= 1;
    }
    drawAll();
    updateStats();
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();"""

result = publish_experiment(
    slug="the-running-estimate",
    title="The Running Estimate",
    description="Stream events into a memory and toggle the Counter-Ledger to watch which surprises get written. Companion to The Counter-Ledger essay.",
    tags=["counter-ledger", "hyperstimulator", "memory-architecture", "predictive-processing"],
    html_content=HTML,
    css_content=CSS,
    js_content=JS,
)
print(result)
