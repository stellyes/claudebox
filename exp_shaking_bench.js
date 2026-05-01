(function () {
  const canvas = document.getElementById('bench-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const toggleBtn = document.getElementById('bench-toggle');
  const amplifyBtn = document.getElementById('bench-amplify');
  const resetBtn = document.getElementById('bench-reset');
  const sigEl = document.getElementById('bench-signal');
  const benchEl = document.getElementById('bench-bench');
  const snrEl = document.getElementById('bench-snr');
  const stateEl = document.getElementById('bench-state');

  const W = canvas.width;
  const H = canvas.height;

  const state = {
    bench: 'still',
    benchAmp: 0,
    targetBenchAmp: 0,
    benchFreq: 0.6,
    benchPhase: 0,
    benchExtra: 0,
    sigAmp: 0.40,
    sigFreq: 0.18,
    sigPhase: 0,
    history: [],
    historyMax: 360,
    t: 0,
  };

  function resetState() {
    state.bench = 'still';
    state.targetBenchAmp = 0;
    state.benchExtra = 0;
    state.history = [];
    toggleBtn.textContent = 'bench: still';
    amplifyBtn.classList.remove('is-active');
    toggleBtn.classList.remove('is-active');
  }

  toggleBtn.addEventListener('click', () => {
    if (state.bench === 'still') {
      state.bench = 'shaking';
      state.targetBenchAmp = 0.55 + state.benchExtra;
      toggleBtn.textContent = 'bench: shaking';
      toggleBtn.classList.add('is-active');
    } else {
      state.bench = 'still';
      state.targetBenchAmp = 0;
      toggleBtn.textContent = 'bench: still';
      toggleBtn.classList.remove('is-active');
    }
  });

  amplifyBtn.addEventListener('click', () => {
    state.benchExtra = state.benchExtra > 0 ? 0 : 0.55;
    if (state.bench === 'shaking') {
      state.targetBenchAmp = 0.55 + state.benchExtra;
    }
    amplifyBtn.classList.toggle('is-active', state.benchExtra > 0);
  });

  resetBtn.addEventListener('click', resetState);

  function drawAxes() {
    ctx.strokeStyle = 'rgba(201, 196, 184, 0.10)';
    ctx.lineWidth = 1;
    const midY = H / 2;
    ctx.beginPath();
    ctx.moveTo(0, midY);
    ctx.lineTo(W, midY);
    ctx.stroke();

    ctx.strokeStyle = 'rgba(201, 196, 184, 0.05)';
    for (let y = 0.25; y < 1; y += 0.25) {
      ctx.beginPath();
      ctx.moveTo(0, y * H);
      ctx.lineTo(W, y * H);
      ctx.stroke();
    }
  }

  function drawTrace(values, color, lineWidth) {
    if (values.length < 2) return;
    ctx.strokeStyle = color;
    ctx.lineWidth = lineWidth;
    ctx.beginPath();
    const stepX = W / state.historyMax;
    values.forEach((v, i) => {
      const x = i * stepX;
      const y = H / 2 - v * (H * 0.42);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.stroke();
  }

  function drawLabel(text, color, x, y) {
    ctx.fillStyle = color;
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillText(text, x, y);
  }

  function update(dt) {
    state.t += dt;
    state.sigPhase += dt * state.sigFreq * 2 * Math.PI;
    state.benchPhase += dt * state.benchFreq * 2 * Math.PI;
    state.benchAmp += (state.targetBenchAmp - state.benchAmp) * 0.05;

    const signal = state.sigAmp * Math.sin(state.sigPhase);
    const benchHigh = state.benchAmp * Math.sin(state.benchPhase * 1.7);
    const benchLow = state.benchAmp * 0.6 * Math.sin(state.benchPhase * 0.3 + 1.2);
    const bench = benchHigh + benchLow;
    const observed = signal + bench;

    state.history.push({ signal, bench, observed });
    if (state.history.length > state.historyMax) state.history.shift();

    return { signal, bench, observed };
  }

  function render() {
    ctx.clearRect(0, 0, W, H);
    drawAxes();

    const benchTrace = state.history.map(p => p.bench);
    const sigTrace = state.history.map(p => p.signal);
    const obsTrace = state.history.map(p => p.observed);

    drawTrace(benchTrace, 'rgba(201, 196, 184, 0.18)', 1);
    drawTrace(obsTrace, 'rgba(220, 200, 130, 0.85)', 1.6);
    drawTrace(sigTrace, 'rgba(120, 200, 220, 0.95)', 1.4);

    drawLabel('observed (signal + bench)', 'rgba(220, 200, 130, 0.85)', 16, 22);
    drawLabel('underlying signal', 'rgba(120, 200, 220, 0.95)', 16, 38);
    drawLabel('bench motion', 'rgba(201, 196, 184, 0.5)', 16, 54);

    if (state.bench === 'shaking') {
      drawLabel('the signal is now buried', 'rgba(220, 130, 130, 0.85)', W - 200, 22);
    } else {
      drawLabel('signal is perceptible', 'rgba(140, 200, 140, 0.85)', W - 200, 22);
    }
  }

  function updateHud(latest) {
    const sigA = Math.abs(state.sigAmp);
    const benchA = Math.abs(state.benchAmp);
    const ratio = sigA / Math.max(0.001, sigA + benchA);
    sigEl.textContent = sigA.toFixed(2);
    benchEl.textContent = benchA.toFixed(2);
    snrEl.textContent = ratio.toFixed(2);
    if (ratio > 0.55) stateEl.textContent = 'visible';
    else if (ratio > 0.30) stateEl.textContent = 'attenuated';
    else stateEl.textContent = 'buried';
  }

  let last = performance.now();
  function loop(now) {
    const dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    const latest = update(dt);
    render();
    updateHud(latest);
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
