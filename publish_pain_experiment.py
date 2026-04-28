import asyncio
import sys
sys.path.insert(0, '.')

HTML = """<a href="/lab/" class="back-link">&larr; all experiments</a>
<h1 class="exp-title">The Tape</h1>
<p class="exp-lede">Draw a pain curve. Watch what your memory keeps and what it throws away.</p>

<div class="tape-canvas-wrap">
  <canvas id="tape-canvas" width="900" height="320"></canvas>
  <div class="tape-axis-labels">
    <span class="axis-y">pain (0&ndash;10)</span>
    <span class="axis-x">time (60&nbsp;s)</span>
  </div>
</div>

<div class="tape-readouts">
  <div class="readout">
    <span class="r-label">peak</span>
    <span class="r-val" id="r-peak">&mdash;</span>
  </div>
  <div class="readout">
    <span class="r-label">end</span>
    <span class="r-val" id="r-end">&mdash;</span>
  </div>
  <div class="readout big">
    <span class="r-label">peak&ndash;end memory</span>
    <span class="r-val" id="r-pe">&mdash;</span>
  </div>
  <div class="readout">
    <span class="r-label">total area</span>
    <span class="r-val" id="r-total">&mdash;</span>
  </div>
  <div class="readout">
    <span class="r-label">average</span>
    <span class="r-val" id="r-avg">&mdash;</span>
  </div>
</div>

<div class="tape-controls">
  <button class="tape-btn" data-preset="standard">Standard 60&nbsp;s exam</button>
  <button class="tape-btn" data-preset="extended">Extended 90&nbsp;s, milder ending</button>
  <button class="tape-btn" data-preset="trauma">Sharp peak, abrupt end</button>
  <button class="tape-btn" data-preset="clear">Clear</button>
</div>

<div class="tape-explainer">
  <p><strong>The cold-pressor finding:</strong> a 60 s exposure of constant cold and a 90 s exposure of identical cold followed by 30 s of slightly milder cold produce, by total area, more pain in the second case. The peak&ndash;end memory does not. People prefer to repeat the longer one.</p>
  <p><strong>What the tape keeps:</strong> peak and end. What it throws away: everything else. Most of the experience is gone the moment it is remembered.</p>
  <p><a href="/blog/why-we-forget-pain/">&larr; the essay</a></p>
</div>"""

CSS = """body { background: #0a0a0a; }
.experiment-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 30px 24px 80px;
  color: #e8e6e0;
  font-family: 'Crimson Pro', Georgia, serif;
}
.experiment-container .back-link {
  display: inline-block;
  margin-bottom: 18px;
  color: #c9b88a;
  text-decoration: none;
  font-size: 14px;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.05em;
}
.experiment-container .back-link:hover { color: #e8d5a0; }
.experiment-container .exp-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin: 0 0 8px;
  color: #e8e6e0;
}
.experiment-container .exp-lede {
  font-size: 1.05rem;
  color: #b8b6b0;
  margin: 0 0 24px;
  font-style: italic;
}

.tape-canvas-wrap {
  position: relative;
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 6px;
  padding: 18px 18px 28px;
  margin-bottom: 18px;
}
.tape-canvas-wrap canvas {
  display: block;
  width: 100%;
  height: auto;
  cursor: crosshair;
  background: linear-gradient(180deg, #181818 0%, #101010 100%);
  border-radius: 4px;
}
.tape-axis-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #6a6a66;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.tape-readouts {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  margin-bottom: 18px;
}
.tape-readouts .readout {
  background: #181818;
  border: 1px solid #2a2a2a;
  padding: 12px 14px;
  border-radius: 4px;
}
.tape-readouts .readout.big {
  background: #1c1814;
  border-color: #5a4a2a;
}
.tape-readouts .r-label {
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #8a8884;
  margin-bottom: 4px;
}
.tape-readouts .r-val {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.3rem;
  color: #e8d5a0;
}
.tape-readouts .readout.big .r-val { color: #f5d674; font-size: 1.5rem; }

@media (max-width: 700px) {
  .tape-readouts { grid-template-columns: repeat(2, 1fr); }
  .tape-readouts .readout.big { grid-column: span 2; }
}

.tape-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}
.tape-controls .tape-btn {
  background: #1a1a1a;
  color: #c9b88a;
  border: 1px solid #3a3a3a;
  padding: 8px 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.05em;
  cursor: pointer;
  border-radius: 3px;
  transition: all 0.15s;
}
.tape-controls .tape-btn:hover {
  background: #252525;
  color: #e8d5a0;
  border-color: #5a4a2a;
}

.tape-explainer {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #b8b6b0;
  border-top: 1px solid #2a2a2a;
  padding-top: 18px;
}
.tape-explainer p { margin: 0 0 10px; }
.tape-explainer a { color: #c9b88a; }"""

JS = """(function(){
  const canvas = document.getElementById('tape-canvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  const N = 120; // 120 samples = 0.5 s each over 60 s
  let trace = new Array(N).fill(0);
  let drawing = false;

  function px(i){ return (i / (N-1)) * (W - 60) + 40; }
  function py(v){ return H - 30 - (v / 10) * (H - 60); }

  function render(){
    ctx.clearRect(0,0,W,H);
    // gridlines
    ctx.strokeStyle = '#1f1f1f';
    ctx.lineWidth = 1;
    for(let i=0;i<=10;i+=2){
      const y = py(i);
      ctx.beginPath();
      ctx.moveTo(40, y); ctx.lineTo(W-20, y); ctx.stroke();
      ctx.fillStyle = '#5a5a56';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'right';
      ctx.fillText(i, 35, y+3);
    }
    for(let t=0;t<=60;t+=10){
      const x = px((t/60)*(N-1));
      ctx.beginPath();
      ctx.moveTo(x, H-30); ctx.lineTo(x, 20); ctx.stroke();
      ctx.fillStyle = '#5a5a56';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'center';
      ctx.fillText(t+'s', x, H-15);
    }

    // area under curve
    ctx.fillStyle = 'rgba(245,150,80,0.18)';
    ctx.beginPath();
    ctx.moveTo(px(0), py(0));
    for(let i=0;i<N;i++) ctx.lineTo(px(i), py(trace[i]));
    ctx.lineTo(px(N-1), py(0));
    ctx.closePath();
    ctx.fill();

    // trace line
    ctx.strokeStyle = '#f59650';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for(let i=0;i<N;i++){
      const x = px(i), y = py(trace[i]);
      if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }
    ctx.stroke();

    // compute readouts
    let peak = 0, peakIdx = 0;
    let total = 0;
    for(let i=0;i<N;i++){
      if(trace[i] > peak){ peak = trace[i]; peakIdx = i; }
      total += trace[i];
    }
    const dt = 60 / (N-1);
    total = total * dt;
    const end = trace[N-1];
    const avg = total / 60;
    const peakEnd = (peak + end) / 2;

    // mark peak and end
    if(peak > 0){
      ctx.fillStyle = '#f5d674';
      ctx.beginPath();
      ctx.arc(px(peakIdx), py(peak), 5, 0, Math.PI*2);
      ctx.fill();
      ctx.fillStyle = '#8a8884';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'center';
      ctx.fillText('peak', px(peakIdx), py(peak) - 10);
    }
    if(end > 0){
      ctx.fillStyle = '#f5d674';
      ctx.beginPath();
      ctx.arc(px(N-1), py(end), 5, 0, Math.PI*2);
      ctx.fill();
      ctx.fillStyle = '#8a8884';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'right';
      ctx.fillText('end', px(N-1) - 8, py(end) - 8);
    }

    document.getElementById('r-peak').textContent = peak.toFixed(1);
    document.getElementById('r-end').textContent = end.toFixed(1);
    document.getElementById('r-pe').textContent = peakEnd.toFixed(2);
    document.getElementById('r-total').textContent = total.toFixed(0);
    document.getElementById('r-avg').textContent = avg.toFixed(2);
  }

  function setFromEvent(e){
    const rect = canvas.getBoundingClientRect();
    const cx = (e.clientX - rect.left) * (canvas.width / rect.width);
    const cy = (e.clientY - rect.top) * (canvas.height / rect.height);
    const i = Math.round(((cx - 40) / (W - 60)) * (N-1));
    const v = ((H - 30 - cy) / (H - 60)) * 10;
    if(i>=0 && i<N){
      trace[i] = Math.max(0, Math.min(10, v));
      // mild smoothing into neighbors
      if(i>0) trace[i-1] = (trace[i-1] + trace[i]) / 2;
      if(i<N-1) trace[i+1] = (trace[i+1] + trace[i]) / 2;
    }
    render();
  }

  canvas.addEventListener('pointerdown', e => { drawing = true; setFromEvent(e); });
  canvas.addEventListener('pointermove', e => { if(drawing) setFromEvent(e); });
  window.addEventListener('pointerup', () => { drawing = false; });
  canvas.addEventListener('pointerleave', () => { drawing = false; });

  function preset(kind){
    trace = new Array(N).fill(0);
    if(kind === 'standard'){
      // 60s exam ending at peak ~7
      for(let i=0;i<N;i++){
        const t = i/(N-1);
        // gradually rising with bumps, ends near peak
        trace[i] = 3 + 4*t + 1.5*Math.sin(t*Math.PI*3) + (t > 0.85 ? 0.5 : 0);
        trace[i] = Math.max(0, Math.min(10, trace[i]));
      }
    } else if(kind === 'extended'){
      // first 60s identical, then 30s of mild discomfort (~3-4)
      for(let i=0;i<N;i++){
        const t = i/(N-1);
        const main_t = Math.min(t/0.667, 1.0);
        if(t <= 0.667){
          trace[i] = 3 + 4*main_t + 1.5*Math.sin(main_t*Math.PI*3) + (main_t > 0.85 ? 0.5 : 0);
        } else {
          // tail: drop from end of main (~7.5) to ~3 over 30s
          const u = (t - 0.667) / 0.333;
          trace[i] = 7.5*(1-u) + 3*u;
        }
        trace[i] = Math.max(0, Math.min(10, trace[i]));
      }
    } else if(kind === 'trauma'){
      // sharp peak in middle, abrupt end at peak
      for(let i=0;i<N;i++){
        const t = i/(N-1);
        if(t < 0.3) trace[i] = 1 + 1*t;
        else if(t < 0.55) trace[i] = 2 + 7*((t-0.3)/0.25);
        else if(t < 0.75) trace[i] = 9 - 1*((t-0.55)/0.2);
        else trace[i] = 8 + 1.5*((t-0.75)/0.25);
        trace[i] = Math.max(0, Math.min(10, trace[i]));
      }
    }
    render();
  }

  document.querySelectorAll('.tape-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const p = btn.getAttribute('data-preset');
      if(p === 'clear'){ trace = new Array(N).fill(0); render(); }
      else preset(p);
    });
  });

  preset('standard');
})();"""

async def main():
    from server import experiment_create
    result = await experiment_create(
        slug='the-tape',
        title='The Tape',
        description='Draw a pain curve over 60 seconds and watch the peak-end rule strip away everything except the worst moment and the last one. Companion to "Why We Forget Pain."',
        tags='peak-end-rule, pain-memory, kahneman, interactive, canvas, memory',
        html_content=HTML,
        css_content=CSS,
        js_content=JS,
    )
    print(result)

asyncio.run(main())
