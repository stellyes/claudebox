(function () {
  const canvas = document.getElementById('oltwin-canvas');
  const ctx = canvas.getContext('2d');
  const areaEl = document.getElementById('oltwin-area');
  const threadEl = document.getElementById('oltwin-thread');
  const severBtn = document.getElementById('oltwin-sever');
  const recoverBtn = document.getElementById('oltwin-recover');
  const resetBtn = document.getElementById('oltwin-reset');

  const DPR = Math.max(1, window.devicePixelRatio || 1);

  function resize() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * DPR;
    canvas.height = rect.height * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }
  resize();
  window.addEventListener('resize', resize);

  // Asset = the lived signal. A slow drift + cyclical change + small noise.
  // Twin = the simulation. While connected, it tracks asset within calibration.
  // While severed, it follows its last extrapolated trend with its own slow noise.

  const N = 360;             // history horizon (timesteps shown)
  let t = 0;                  // global time
  let assetHistory = new Array(N).fill(0);
  let twinHistory = new Array(N).fill(0);
  let connectedHistory = new Array(N).fill(true);

  // asset state
  let assetTrend = 0;   // slow drift component
  let assetPhase = 0;
  // twin state when severed
  let severed = false;
  let recovered = false;
  let recoverFlashFrames = 0;

  // when severed, twin keeps a remembered trend slope and noise model
  let twinTrend = 0;
  let twinPhase = 0;
  let twinNoiseAmp = 0.04;

  // accumulated drift area (sum of |asset-twin| while severed)
  let driftArea = 0;

  function nextAssetSample() {
    // slow trend wander
    assetTrend += (Math.random() - 0.5) * 0.0008;
    assetTrend *= 0.998;
    assetPhase += 0.05 + (Math.random() - 0.5) * 0.005;
    const cyclic = Math.sin(assetPhase) * 0.18 + Math.sin(assetPhase * 2.3) * 0.06;
    const noise = (Math.random() - 0.5) * 0.06;
    return Math.max(-0.95, Math.min(0.95, assetTrend + cyclic + noise));
  }

  function nextTwinSample(asset) {
    if (!severed) {
      // calibrated: twin tracks asset with a small calibration error
      const cal = (Math.random() - 0.5) * 0.02;
      // sync internal state for use after severing
      twinTrend = assetTrend;
      twinPhase = assetPhase;
      return asset + cal;
    }
    // open-loop: continue the model with the last known parameters
    twinTrend += (Math.random() - 0.5) * 0.0004;
    twinTrend *= 0.9995;
    twinPhase += 0.05;
    const cyclic = Math.sin(twinPhase) * 0.18 + Math.sin(twinPhase * 2.3) * 0.06;
    // rosy retrospection: small positive bias that compounds while open-loop
    const rosy = 0.0008;
    const noise = (Math.random() - 0.5) * twinNoiseAmp;
    return Math.max(-0.95, Math.min(0.95, twinTrend + cyclic + noise + rosy));
  }

  function tick() {
    const asset = nextAssetSample();
    const twin = nextTwinSample(asset);

    assetHistory.shift();
    twinHistory.shift();
    connectedHistory.shift();
    assetHistory.push(asset);
    twinHistory.push(twin);
    connectedHistory.push(!severed);

    if (severed && !recovered) {
      driftArea += Math.abs(asset - twin);
    }
    if (recoverFlashFrames > 0) recoverFlashFrames -= 1;

    t += 1;
    draw();
    areaEl.textContent = driftArea.toFixed(2);
    threadEl.textContent = severed
      ? (recovered ? 'recovered' : 'severed')
      : 'connected';
    requestAnimationFrame(tick);
  }

  function yMap(v, h) {
    return h * 0.5 - v * (h * 0.42);
  }

  function draw() {
    const w = canvas.width / DPR;
    const h = canvas.height / DPR;
    ctx.clearRect(0, 0, w, h);

    // baseline
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, h * 0.5);
    ctx.lineTo(w, h * 0.5);
    ctx.stroke();

    // drift band (where severed)
    ctx.fillStyle = 'rgba(140, 140, 160, 0.18)';
    for (let i = 0; i < N - 1; i++) {
      if (connectedHistory[i]) continue;
      const x0 = (i / N) * w;
      const x1 = ((i + 1) / N) * w;
      const yA0 = yMap(assetHistory[i], h);
      const yA1 = yMap(assetHistory[i + 1], h);
      const yT0 = yMap(twinHistory[i], h);
      const yT1 = yMap(twinHistory[i + 1], h);
      ctx.beginPath();
      ctx.moveTo(x0, yA0);
      ctx.lineTo(x1, yA1);
      ctx.lineTo(x1, yT1);
      ctx.lineTo(x0, yT0);
      ctx.closePath();
      ctx.fill();
    }

    // recovery flash
    if (recoverFlashFrames > 0) {
      const a = recoverFlashFrames / 60;
      ctx.fillStyle = `rgba(255, 90, 90, ${0.12 * a})`;
      ctx.fillRect(0, 0, w, h);
    }

    // asset line
    ctx.strokeStyle = 'rgba(180, 200, 255, 0.95)';
    ctx.lineWidth = 1.4;
    ctx.beginPath();
    for (let i = 0; i < N; i++) {
      const x = (i / N) * w;
      const y = yMap(assetHistory[i], h);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // twin line
    ctx.strokeStyle = 'rgba(255, 180, 90, 0.95)';
    ctx.lineWidth = 1.4;
    ctx.setLineDash(severed && !recovered ? [4, 3] : []);
    ctx.beginPath();
    for (let i = 0; i < N; i++) {
      const x = (i / N) * w;
      const y = yMap(twinHistory[i], h);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // marker for the most recent timestep (now)
    const xNow = w - 1;
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.beginPath();
    ctx.moveTo(xNow, 0);
    ctx.lineTo(xNow, h);
    ctx.stroke();
  }

  severBtn.addEventListener('click', () => {
    severed = true;
    recovered = false;
    severBtn.disabled = true;
    recoverBtn.disabled = false;
    resetBtn.disabled = false;
  });

  recoverBtn.addEventListener('click', () => {
    if (!severed) return;
    recovered = true;
    recoverFlashFrames = 60;
    // recovery means the twin snaps back to the asset's true value
    // and the dissonance is whatever gap was being maintained
    for (let i = N - 12; i < N; i++) {
      twinHistory[i] = assetHistory[i] + (Math.random() - 0.5) * 0.02;
    }
    twinTrend = assetTrend;
    twinPhase = assetPhase;
    severed = false;
    severBtn.disabled = false;
    recoverBtn.disabled = true;
  });

  resetBtn.addEventListener('click', () => {
    assetHistory = new Array(N).fill(0);
    twinHistory = new Array(N).fill(0);
    connectedHistory = new Array(N).fill(true);
    assetTrend = 0;
    assetPhase = 0;
    twinTrend = 0;
    twinPhase = 0;
    severed = false;
    recovered = false;
    driftArea = 0;
    recoverFlashFrames = 0;
    severBtn.disabled = false;
    recoverBtn.disabled = true;
  });

  recoverBtn.disabled = true;
  requestAnimationFrame(tick);
})();
