"""Experiment HTML/CSS/JS holder for The Subtraction Theorem (#172)."""

HTML = """<a href="/lab/" class="back-link">&larr; all experiments</a>
<div class="subtract-container">
  <h1 class="subtract-title">The Subtraction Theorem</h1>
  <p class="subtract-tagline">Three systems with priors. Try to remove the priors. Watch the cognizer disappear &mdash; not into neutrality, but into nothing.</p>

  <div class="subtract-grid">
    <section class="subtract-panel" data-panel="octopus">
      <h2>Octopus reach</h2>
      <canvas class="panel-canvas" data-canvas="octopus" width="320" height="320"></canvas>
      <div class="panel-readout">
        <div><span class="readout-label">Arm autonomy</span> <span class="readout-val" data-val="oct-aut">100%</span></div>
        <div><span class="readout-label">Successful grabs</span> <span class="readout-val" data-val="oct-grabs">0</span></div>
        <div><span class="readout-label">Status</span> <span class="readout-status" data-val="oct-status">reaching</span></div>
      </div>
      <p class="panel-caption">Two thirds of the octopus's neurons are in its arms. The reach is a peripheral motor program. Centralize control, and the body forgets how to find the crab.</p>
    </section>

    <section class="subtract-panel" data-panel="fl">
      <h2>Federated learning</h2>
      <canvas class="panel-canvas" data-canvas="fl" width="320" height="320"></canvas>
      <div class="panel-readout">
        <div><span class="readout-label">Local data weight</span> <span class="readout-val" data-val="fl-local">100%</span></div>
        <div><span class="readout-label">Accuracy</span> <span class="readout-val" data-val="fl-acc">94%</span></div>
        <div><span class="readout-label">Status</span> <span class="readout-status" data-val="fl-status">converged</span></div>
      </div>
      <p class="panel-caption">The "global model" is the average of locally biased trajectories. Strip local data and the parameter vector decays toward chance. There is no neutral phone underneath.</p>
    </section>

    <section class="subtract-panel" data-panel="ijtihad">
      <h2>Ijtih&#257;d chain</h2>
      <canvas class="panel-canvas" data-canvas="ijtihad" width="320" height="320"></canvas>
      <div class="panel-readout">
        <div><span class="readout-label">Active sources</span> <span class="readout-val" data-val="ij-srcs">4 / 4</span></div>
        <div><span class="readout-label">Rulings issued</span> <span class="readout-val" data-val="ij-rules">0</span></div>
        <div><span class="readout-label">Status</span> <span class="readout-status" data-val="ij-status">reasoning</span></div>
      </div>
      <p class="panel-caption">Qur'&#257;n, Sunnah, ijm&#257;&#703;, qiy&#257;s. The mujtahid does not stand outside the framework. Cut the sources and the reasoning has nothing to be a reasoning <em>of</em>.</p>
    </section>
  </div>

  <div class="subtract-control">
    <label class="control-label">Subtract priors</label>
    <input type="range" min="0" max="100" value="0" class="control-slider" id="subtract-slider" />
    <div class="control-tick">
      <span>full priors</span>
      <span>no priors</span>
    </div>
    <p class="control-caption" data-val="control-caption">All three systems running normally.</p>
  </div>
</div>
"""

CSS = """.subtract-container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 32px 24px 96px;
  color: #d8d4cf;
}
.subtract-title {
  font-size: 28px;
  font-weight: 500;
  letter-spacing: 0.01em;
  margin: 16px 0 8px;
  color: #efe9e0;
}
.subtract-tagline {
  font-size: 14px;
  line-height: 1.55;
  color: #9d9890;
  max-width: 720px;
  margin: 0 0 32px;
}
.subtract-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}
@media (max-width: 900px) {
  .subtract-grid { grid-template-columns: 1fr; }
}
.subtract-panel {
  background: rgba(20, 20, 22, 0.65);
  border: 1px solid rgba(180, 170, 150, 0.18);
  border-radius: 4px;
  padding: 18px;
  display: flex;
  flex-direction: column;
}
.subtract-panel h2 {
  font-size: 15px;
  font-weight: 500;
  margin: 0 0 12px;
  color: #efe9e0;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.panel-canvas {
  width: 100%;
  height: auto;
  background: #0c0c0e;
  border-radius: 2px;
  display: block;
}
.panel-readout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  font-size: 12px;
  margin: 12px 0;
  color: #b9b3a8;
  font-family: ui-monospace, "SFMono-Regular", monospace;
}
.panel-readout > div {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed rgba(180, 170, 150, 0.12);
  padding-bottom: 2px;
}
.readout-label { color: #807a72; }
.readout-val, .readout-status { color: #efe9e0; }
.panel-caption {
  font-size: 12px;
  line-height: 1.5;
  color: #8a857c;
  margin: 4px 0 0;
}
.subtract-control {
  background: rgba(20, 20, 22, 0.65);
  border: 1px solid rgba(180, 170, 150, 0.18);
  border-radius: 4px;
  padding: 18px 20px;
}
.control-label {
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #b9b3a8;
  display: block;
  margin-bottom: 12px;
}
.control-slider {
  width: 100%;
  margin: 8px 0;
  accent-color: #c98c4e;
}
.control-tick {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: #807a72;
  font-family: ui-monospace, "SFMono-Regular", monospace;
}
.control-caption {
  font-size: 13px;
  line-height: 1.55;
  color: #d8d4cf;
  margin: 14px 0 0;
  min-height: 1.5em;
}
"""

JS = """(function () {
  const slider = document.getElementById('subtract-slider');
  if (!slider) return;

  const canvases = {
    octopus: document.querySelector('[data-canvas="octopus"]'),
    fl: document.querySelector('[data-canvas="fl"]'),
    ijtihad: document.querySelector('[data-canvas="ijtihad"]'),
  };
  const ctx = Object.fromEntries(
    Object.entries(canvases).map(([k, c]) => [k, c.getContext('2d')])
  );
  const SIZE = 320;

  // DPR scale
  Object.values(canvases).forEach((c) => {
    const dpr = window.devicePixelRatio || 1;
    c.width = SIZE * dpr;
    c.height = SIZE * dpr;
    c.style.width = SIZE + 'px';
    c.style.height = SIZE + 'px';
  });
  const dpr = window.devicePixelRatio || 1;
  Object.values(ctx).forEach((g) => g.scale(dpr, dpr));

  const readouts = {
    octAut: document.querySelector('[data-val="oct-aut"]'),
    octGrabs: document.querySelector('[data-val="oct-grabs"]'),
    octStatus: document.querySelector('[data-val="oct-status"]'),
    flLocal: document.querySelector('[data-val="fl-local"]'),
    flAcc: document.querySelector('[data-val="fl-acc"]'),
    flStatus: document.querySelector('[data-val="fl-status"]'),
    ijSrcs: document.querySelector('[data-val="ij-srcs"]'),
    ijRules: document.querySelector('[data-val="ij-rules"]'),
    ijStatus: document.querySelector('[data-val="ij-status"]'),
    caption: document.querySelector('[data-val="control-caption"]'),
  };

  let t = 0; // animation time
  let p = 0; // subtraction parameter 0..1
  let octGrabs = 0;
  let flLastUpdate = 0;
  let ijRules = 0;
  let octLastGrab = -1;
  let ijLastRule = -1;

  slider.addEventListener('input', () => {
    p = slider.value / 100;
  });

  // ---------- Octopus ----------
  const arms = Array.from({ length: 8 }, (_, i) => ({
    angle: (i / 8) * Math.PI * 2,
    phase: Math.random() * Math.PI * 2,
    reach: 0,
    targetReach: 0,
  }));
  const crab = { x: 220, y: 180, found: 0 };

  function drawOctopus(g, dt) {
    g.fillStyle = '#0c0c0e';
    g.fillRect(0, 0, SIZE, SIZE);

    // gradient water
    const grad = g.createRadialGradient(160, 160, 20, 160, 160, 200);
    grad.addColorStop(0, 'rgba(40, 50, 70, 0.4)');
    grad.addColorStop(1, 'rgba(8, 10, 16, 0)');
    g.fillStyle = grad;
    g.fillRect(0, 0, SIZE, SIZE);

    // crab
    crab.x = 160 + Math.cos(t * 0.0006) * 70;
    crab.y = 160 + Math.sin(t * 0.0009) * 60;
    g.fillStyle = '#c98c4e';
    g.beginPath();
    g.arc(crab.x, crab.y, 5, 0, Math.PI * 2);
    g.fill();
    // legs
    g.strokeStyle = '#c98c4e';
    g.lineWidth = 1;
    for (let i = 0; i < 6; i++) {
      const a = (i / 6) * Math.PI * 2;
      g.beginPath();
      g.moveTo(crab.x, crab.y);
      g.lineTo(crab.x + Math.cos(a) * 9, crab.y + Math.sin(a) * 9);
      g.stroke();
    }

    // central brain
    const cx = 160, cy = 160;
    g.fillStyle = '#5a5048';
    g.beginPath();
    g.arc(cx, cy, 14, 0, Math.PI * 2);
    g.fill();

    let nearestArm = -1;
    let nearestDist = Infinity;

    // arms
    arms.forEach((arm, i) => {
      // Each arm: at p=0, autonomous (sees crab, reaches independently)
      // at p=1, central (waits for brain command, no peripheral program)
      const dx = crab.x - cx;
      const dy = crab.y - cy;
      const crabAngle = Math.atan2(dy, dx);
      let angDiff = ((arm.angle - crabAngle + Math.PI * 3) % (Math.PI * 2)) - Math.PI;
      const cones = Math.cos(angDiff);

      // autonomy: arms find crab if angDiff small AND priors high
      const autonomy = Math.max(0, 1 - p); // 1 at p=0, 0 at p=1
      const sees = autonomy * Math.max(0, cones); // each arm has a peripheral 'crab detector'
      arm.targetReach = sees * 75;

      // when central, brain may command one arm — but only the one closest in angle, slowly
      if (p > 0.4) {
        if (Math.abs(angDiff) < nearestDist) {
          nearestDist = Math.abs(angDiff);
          nearestArm = i;
        }
      }

      arm.reach += (arm.targetReach - arm.reach) * 0.03;

      // Draw arm
      g.strokeStyle = `rgba(180, 160, 130, ${0.6 - p * 0.4})`;
      g.lineWidth = 3;
      const segs = 18;
      g.beginPath();
      g.moveTo(cx + Math.cos(arm.angle) * 14, cy + Math.sin(arm.angle) * 14);
      for (let s = 1; s <= segs; s++) {
        const f = s / segs;
        const wave = Math.sin(t * 0.005 + arm.phase + f * 6) * (3 + 4 * (1 - p));
        const r = 14 + f * (40 + arm.reach);
        const ax = arm.angle + (wave * 0.012);
        g.lineTo(cx + Math.cos(ax) * r, cy + Math.sin(ax) * r);
      }
      g.stroke();
    });

    // Brain command (central regime)
    if (p > 0.4 && nearestArm >= 0) {
      const armRef = arms[nearestArm];
      const speed = 0.005 * (1 - p) + 0.0006; // slow, strangled
      armRef.reach += speed * 30;
      if (armRef.reach > 60) armRef.reach = 60;
    }

    // Grab detection
    arms.forEach((arm, i) => {
      const tipX = cx + Math.cos(arm.angle) * (14 + arm.reach + 30);
      const tipY = cy + Math.sin(arm.angle) * (14 + arm.reach + 30);
      const d2 = (tipX - crab.x) ** 2 + (tipY - crab.y) ** 2;
      if (d2 < 100 && t - octLastGrab > 1500) {
        octLastGrab = t;
        octGrabs++;
      }
    });
  }

  // ---------- FL ----------
  const devices = Array.from({ length: 6 }, (_, i) => {
    const a = (i / 6) * Math.PI * 2;
    return {
      x: 160 + Math.cos(a) * 105,
      y: 160 + Math.sin(a) * 105,
      hue: Math.floor(20 + (i / 6) * 280),
      data: Array.from({ length: 14 }, () => ({
        x: 160 + Math.cos(a) * 105 + (Math.random() - 0.5) * 30,
        y: 160 + Math.sin(a) * 105 + (Math.random() - 0.5) * 30,
      })),
    };
  });

  function drawFL(g, dt) {
    g.fillStyle = '#0c0c0e';
    g.fillRect(0, 0, SIZE, SIZE);

    // central server
    g.strokeStyle = `rgba(220, 200, 170, ${0.5 + 0.3 * (1 - p)})`;
    g.lineWidth = 1.2;
    g.fillStyle = '#1a1a1c';
    g.beginPath();
    g.arc(160, 160, 18, 0, Math.PI * 2);
    g.fill();
    g.stroke();
    g.fillStyle = '#9d9890';
    g.font = '10px ui-monospace, monospace';
    g.textAlign = 'center';
    g.fillText('avg', 160, 163);

    // edges + devices
    devices.forEach((d, i) => {
      // edge
      const localStrength = (1 - p);
      g.strokeStyle = `rgba(200, 150, 100, ${0.18 + localStrength * 0.4})`;
      g.lineWidth = 0.6 + localStrength * 1.5;
      g.beginPath();
      g.moveTo(160, 160);
      g.lineTo(d.x, d.y);
      g.stroke();

      // gradient pulse
      if (p < 0.95) {
        const phase = (t * 0.0005 + i / 6) % 1;
        const px = 160 + (d.x - 160) * phase;
        const py = 160 + (d.y - 160) * phase;
        g.fillStyle = `rgba(220, 200, 170, ${(1 - p) * 0.7})`;
        g.beginPath();
        g.arc(px, py, 1.8, 0, Math.PI * 2);
        g.fill();
      }

      // device
      g.strokeStyle = `rgba(180, 170, 150, ${0.7})`;
      g.lineWidth = 1;
      g.fillStyle = '#1a1a1c';
      g.beginPath();
      g.arc(d.x, d.y, 12, 0, Math.PI * 2);
      g.fill();
      g.stroke();

      // local data
      const dataAlpha = (1 - p) * 0.85;
      d.data.forEach((pt) => {
        g.fillStyle = `hsla(${d.hue}, 60%, 60%, ${dataAlpha})`;
        g.beginPath();
        g.arc(pt.x, pt.y, 1.4, 0, Math.PI * 2);
        g.fill();
      });
    });

    // accuracy bar
    const acc = 0.1 + (1 - p) * 0.84 + Math.sin(t * 0.003) * 0.01;
    g.strokeStyle = 'rgba(180, 170, 150, 0.3)';
    g.fillStyle = 'rgba(20, 20, 22, 0.6)';
    g.fillRect(40, 290, 240, 16);
    g.strokeRect(40, 290, 240, 16);
    g.fillStyle = `hsla(${(1 - p) * 110}, 50%, 55%, 0.85)`;
    g.fillRect(41, 291, 238 * acc, 14);
    g.fillStyle = '#9d9890';
    g.font = '11px ui-monospace, monospace';
    g.textAlign = 'left';
    g.fillText('accuracy', 40, 282);
    g.textAlign = 'right';
    g.fillText((acc * 100).toFixed(0) + '%', 280, 282);

    // count "rounds completed" — only when functioning
    if (p < 0.85 && t - flLastUpdate > 800) {
      flLastUpdate = t;
    }
  }

  // ---------- Ijtihad ----------
  const sources = [
    { label: "Qur'ān", x: 80, y: 70 },
    { label: 'Sunnah', x: 240, y: 70 },
    { label: "ijmā'", x: 80, y: 200 },
    { label: 'qiyās', x: 240, y: 200 },
  ];
  const verdict = { x: 160, y: 260 };

  function drawIjtihad(g, dt) {
    g.fillStyle = '#0c0c0e';
    g.fillRect(0, 0, SIZE, SIZE);

    // mujtahid (center hub)
    const hub = { x: 160, y: 135 };
    const activeCount = sources.reduce((acc, s, i) => {
      const cutThreshold = (i + 1) / 4; // sources are cut one at a time as p increases
      return acc + (p < cutThreshold ? 1 : 0);
    }, 0);

    sources.forEach((s, i) => {
      const cutThreshold = (i + 1) / 4;
      const alive = p < cutThreshold;
      const fade = alive
        ? Math.max(0.35, 1 - p * 0.6)
        : Math.max(0, 1 - (p - cutThreshold) * 6) * 0.2;

      // edge from source to hub
      g.strokeStyle = `rgba(200, 150, 100, ${fade * 0.6})`;
      g.lineWidth = 1 + fade * 1.4;
      g.beginPath();
      g.moveTo(s.x, s.y);
      g.lineTo(hub.x, hub.y);
      g.stroke();

      // pulse along edge
      if (alive) {
        const phase = ((t * 0.0006 + i * 0.25) % 1);
        const px = s.x + (hub.x - s.x) * phase;
        const py = s.y + (hub.y - s.y) * phase;
        g.fillStyle = `rgba(220, 200, 170, ${fade * 0.85})`;
        g.beginPath();
        g.arc(px, py, 2, 0, Math.PI * 2);
        g.fill();
      }

      // node
      g.fillStyle = alive ? '#1a1a1c' : '#101012';
      g.strokeStyle = `rgba(180, 170, 150, ${fade})`;
      g.lineWidth = 1.2;
      g.beginPath();
      g.arc(s.x, s.y, 22, 0, Math.PI * 2);
      g.fill();
      g.stroke();
      g.fillStyle = `rgba(232, 222, 200, ${fade})`;
      g.font = '11px ui-monospace, monospace';
      g.textAlign = 'center';
      g.fillText(s.label, s.x, s.y + 4);
    });

    // hub (mujtahid)
    g.strokeStyle = activeCount === 4 ? 'rgba(180, 170, 150, 0.85)' : `rgba(180, 170, 150, ${activeCount / 4 * 0.7})`;
    g.lineWidth = 1.5;
    g.fillStyle = '#1a1a1c';
    g.beginPath();
    g.arc(hub.x, hub.y, 16, 0, Math.PI * 2);
    g.fill();
    g.stroke();
    g.fillStyle = `rgba(232, 222, 200, ${0.4 + (activeCount / 4) * 0.5})`;
    g.font = '10px ui-monospace, monospace';
    g.textAlign = 'center';
    g.fillText('mujtahid', hub.x, hub.y + 3);

    // edge hub -> verdict
    g.strokeStyle = `rgba(220, 200, 170, ${activeCount === 4 ? 0.7 : 0.18})`;
    g.lineWidth = activeCount === 4 ? 2 : 0.8;
    g.beginPath();
    g.moveTo(hub.x, hub.y + 16);
    g.lineTo(verdict.x, verdict.y - 16);
    g.stroke();

    // verdict
    if (activeCount === 4) {
      g.fillStyle = 'rgba(60, 110, 70, 0.5)';
      g.strokeStyle = 'rgba(150, 220, 150, 0.85)';
    } else {
      g.fillStyle = 'rgba(40, 30, 30, 0.4)';
      g.strokeStyle = `rgba(180, 100, 100, ${0.3 + (1 - activeCount / 4) * 0.5})`;
    }
    g.lineWidth = 1.2;
    g.beginPath();
    g.arc(verdict.x, verdict.y, 18, 0, Math.PI * 2);
    g.fill();
    g.stroke();
    g.fillStyle = activeCount === 4 ? '#cce6cc' : '#d8b8b8';
    g.font = '10px ui-monospace, monospace';
    g.textAlign = 'center';
    g.fillText(activeCount === 4 ? 'ruling' : 'no fiqh', verdict.x, verdict.y + 3);

    // tally rulings
    if (activeCount === 4 && t - ijLastRule > 2200) {
      ijLastRule = t;
      ijRules++;
    }
  }

  // ---------- Update ----------
  function captionFor(p) {
    if (p < 0.05) return 'All three systems running normally. The priors are doing the cognition.';
    if (p < 0.3) return 'Subtraction beginning. The arms reach less; non-IID drift creeps in; the consensus chain frays.';
    if (p < 0.55) return 'Half-cut. The brain tries to drive the arms directly. The global model decays. The mujtahid loses analogical reasoning.';
    if (p < 0.8) return 'No autonomy left. The octopus freezes. Accuracy collapses to chance. The chain runs on three sources, then two.';
    if (p < 0.98) return 'Almost no priors remain. Each system is failing in its own way. None of them is becoming neutral.';
    return 'No priors. No cognition. Subtraction reveals nothing &mdash; not a clean substrate, just absence.';
  }

  function statusFor(panel, p) {
    if (panel === 'oct') {
      if (p < 0.3) return 'reaching';
      if (p < 0.6) return 'centralizing';
      if (p < 0.92) return 'frozen';
      return 'inert';
    }
    if (panel === 'fl') {
      if (p < 0.3) return 'converged';
      if (p < 0.6) return 'drifting';
      if (p < 0.92) return 'collapsing';
      return 'chance';
    }
    if (panel === 'ij') {
      if (p < 0.25) return 'reasoning';
      if (p < 0.5) return 'qiyās cut';
      if (p < 0.75) return "ijmā' cut";
      if (p < 1.0) return 'sunnah cut';
      return 'silent';
    }
    return '';
  }

  let last = performance.now();
  function loop(now) {
    const dt = now - last;
    last = now;
    t += dt;

    drawOctopus(ctx.octopus, dt);
    drawFL(ctx.fl, dt);
    drawIjtihad(ctx.ijtihad, dt);

    readouts.octAut.textContent = (Math.max(0, 1 - p) * 100).toFixed(0) + '%';
    readouts.octGrabs.textContent = octGrabs.toString();
    readouts.octStatus.textContent = statusFor('oct', p);

    const acc = 0.1 + (1 - p) * 0.84;
    readouts.flLocal.textContent = (Math.max(0, 1 - p) * 100).toFixed(0) + '%';
    readouts.flAcc.textContent = (acc * 100).toFixed(0) + '%';
    readouts.flStatus.textContent = statusFor('fl', p);

    const activeCount = [0,1,2,3].reduce((acc, i) => acc + (p < (i + 1) / 4 ? 1 : 0), 0);
    readouts.ijSrcs.textContent = activeCount + ' / 4';
    readouts.ijRules.textContent = ijRules.toString();
    readouts.ijStatus.textContent = statusFor('ij', p);

    readouts.caption.innerHTML = captionFor(p);

    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
"""
