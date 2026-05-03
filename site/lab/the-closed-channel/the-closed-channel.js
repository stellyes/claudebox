(function () {
  const canvas = document.getElementById('closed-channel-canvas');
  const ctx = canvas.getContext('2d');
  const resetBtn = document.getElementById('reset-btn');
  const playBtn = document.getElementById('play-btn');

  const N = 24;
  let message = [];
  let emissions = [];
  let t = 0;
  let playing = false;
  let lastFrame = 0;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  function generateMessage() {
    const chars = ['A', 'C', 'G', 'T', 'X', 'O'];
    message = [];
    for (let i = 0; i < N; i++) {
      message.push(chars[Math.floor(Math.random() * chars.length)]);
    }
    // Each emission is a "thermal" quantum (looks random) entangled with the message bit.
    // Correlation reading uses the running entanglement entropy (Page curve shape).
    emissions = [];
    for (let i = 0; i < N; i++) {
      emissions.push({
        thermalChar: chars[Math.floor(Math.random() * chars.length)],
        sourceChar: message[i],
        x: 0,
        y: 0,
        phase: Math.random() * Math.PI * 2,
      });
    }
    t = 0;
  }

  // Page-curve-shaped recovery: rises then falls, peak at N/2.
  // Information accessible via correlation probe = N - max(t, N - t) - small noise
  function correlationInfo(step) {
    if (step <= 0) return 0;
    const half = N / 2;
    // Up to half: entanglement entropy of radiation grows linearly with t
    // After half: it must fall, and the recovered info = step
    if (step <= half) return Math.min(step / N, 0.5) * 2 - (step / N); // small for early
    return 1 - Math.exp(-(step - half) / (N / 4));
  }

  function draw() {
    const W = canvas.width;
    const H = canvas.height;
    ctx.fillStyle = '#0a0a12';
    ctx.fillRect(0, 0, W, H);

    // The horizon (vertical line center)
    const horizonX = W / 2;
    const topPad = Math.max(80, H * 0.18);
    const botPad = Math.max(220, H * 0.32);

    // Horizon glow
    const grad = ctx.createLinearGradient(horizonX - 60, 0, horizonX + 60, 0);
    grad.addColorStop(0, 'rgba(20,20,28,0)');
    grad.addColorStop(0.5, 'rgba(80,80,110,0.18)');
    grad.addColorStop(1, 'rgba(20,20,28,0)');
    ctx.fillStyle = grad;
    ctx.fillRect(horizonX - 60, topPad, 120, H - topPad - botPad);

    // Horizon line
    ctx.strokeStyle = 'rgba(160,160,200,0.32)';
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(horizonX, topPad);
    ctx.lineTo(horizonX, H - botPad);
    ctx.stroke();
    ctx.setLineDash([]);

    // Labels
    ctx.fillStyle = '#6e7484';
    ctx.font = '10px IBM Plex Mono, monospace';
    ctx.textAlign = 'center';
    ctx.fillText('SOURCE', horizonX / 2, topPad - 18);
    ctx.fillText('HORIZON', horizonX, topPad - 18);
    ctx.fillText('RADIATION', horizonX + (W - horizonX) / 2, topPad - 18);

    // The source: render the original message as a fixed grid, fading as time advances
    const sourceX = horizonX * 0.5;
    const sourceCellW = 22;
    const sourceCols = 6;
    const sourceRows = Math.ceil(N / sourceCols);
    const sourceGridW = sourceCols * sourceCellW;
    const sourceGridH = sourceRows * sourceCellW;
    const sx0 = sourceX - sourceGridW / 2;
    const sy0 = topPad + 40;

    ctx.font = '14px IBM Plex Mono, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for (let i = 0; i < N; i++) {
      const col = i % sourceCols;
      const row = Math.floor(i / sourceCols);
      const x = sx0 + col * sourceCellW + sourceCellW / 2;
      const y = sy0 + row * sourceCellW + sourceCellW / 2;
      const emitted = i < t;
      ctx.fillStyle = emitted ? 'rgba(110,116,132,0.4)' : '#d4d4dc';
      ctx.fillText(message[i], x, y);
    }

    // Emissions traveling rightward then arriving at the receiver area
    const recvX = horizonX + (W - horizonX) * 0.62;
    const recvCellW = 26;
    const recvGridW = sourceCols * recvCellW;
    const rx0 = recvX - recvGridW / 2;
    const ry0 = topPad + 40;

    // Standard probe readout cells (on the right, top)
    ctx.fillStyle = '#9da3b0';
    ctx.font = '10px IBM Plex Mono, monospace';
    ctx.textAlign = 'center';
    ctx.fillText('STANDARD PROBE — local readout', recvX, ry0 - 18);

    ctx.font = '14px IBM Plex Mono, monospace';
    ctx.textBaseline = 'middle';
    for (let i = 0; i < N; i++) {
      const col = i % sourceCols;
      const row = Math.floor(i / sourceCols);
      const x = rx0 + col * recvCellW + recvCellW / 2;
      const y = ry0 + row * recvCellW + recvCellW / 2;
      if (i < t) {
        // Thermal-looking output: pseudo-random char that flickers
        const flicker = Math.floor((Date.now() / 80 + emissions[i].phase * 30)) % 6;
        const chars = ['A', 'C', 'G', 'T', 'X', 'O'];
        ctx.fillStyle = 'rgba(163,126,156,0.85)';
        ctx.fillText(chars[flicker], x, y);
      } else {
        ctx.fillStyle = 'rgba(80,80,100,0.3)';
        ctx.fillText('·', x, y);
      }
    }

    // Correlation probe readout (below, same grid)
    const cy0 = ry0 + sourceRows * recvCellW + 60;
    ctx.fillStyle = '#9da3b0';
    ctx.font = '10px IBM Plex Mono, monospace';
    ctx.textAlign = 'center';
    ctx.fillText('CORRELATION PROBE — joint readout across emissions', recvX, cy0 - 18);

    const corr = correlationInfo(t);
    ctx.font = '14px IBM Plex Mono, monospace';
    ctx.textBaseline = 'middle';
    for (let i = 0; i < N; i++) {
      const col = i % sourceCols;
      const row = Math.floor(i / sourceCols);
      const x = rx0 + col * recvCellW + recvCellW / 2;
      const y = cy0 + row * recvCellW + recvCellW / 2;
      if (i < t) {
        // Information recovered as t passes the page point
        const recovered = (i / N) < corr;
        ctx.fillStyle = recovered ? 'rgba(198,230,198,0.92)' : 'rgba(120,130,140,0.4)';
        ctx.fillText(recovered ? message[i] : '?', x, y);
      } else {
        ctx.fillStyle = 'rgba(80,80,100,0.3)';
        ctx.fillText('·', x, y);
      }
    }

    // Page curve plot at bottom
    const plotY = H - botPad + 30;
    const plotH = 90;
    const plotW = Math.min(720, W - 96);
    const plotX = (W - plotW) / 2;
    ctx.strokeStyle = 'rgba(180,180,200,0.18)';
    ctx.lineWidth = 1;
    ctx.strokeRect(plotX, plotY, plotW, plotH);

    ctx.fillStyle = '#9da3b0';
    ctx.font = '10px IBM Plex Mono, monospace';
    ctx.textAlign = 'left';
    ctx.fillText('Page curve — entanglement entropy of radiation', plotX, plotY - 6);
    ctx.textAlign = 'right';
    ctx.fillText('t / N', plotX + plotW, plotY + plotH + 14);

    // Page curve shape: rises linearly to N/2, then falls linearly
    ctx.strokeStyle = 'rgba(180,180,200,0.4)';
    ctx.beginPath();
    for (let i = 0; i <= 100; i++) {
      const tt = (i / 100) * N;
      const e = tt <= N / 2 ? tt / N : (N - tt) / N;
      const px = plotX + (i / 100) * plotW;
      const py = plotY + plotH - (e * 2) * plotH;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Current position
    const tx = plotX + (t / N) * plotW;
    const tyVal = t <= N / 2 ? t / N : (N - t) / N;
    const ty = plotY + plotH - (tyVal * 2) * plotH;
    ctx.fillStyle = '#c6e6c6';
    ctx.beginPath();
    ctx.arc(tx, ty, 4, 0, Math.PI * 2);
    ctx.fill();

    // Time slider track
    const trackY = plotY + plotH + 32;
    ctx.strokeStyle = 'rgba(180,180,200,0.32)';
    ctx.beginPath();
    ctx.moveTo(plotX, trackY);
    ctx.lineTo(plotX + plotW, trackY);
    ctx.stroke();
    const handleX = plotX + (t / N) * plotW;
    ctx.fillStyle = '#d4d4dc';
    ctx.beginPath();
    ctx.arc(handleX, trackY, 6, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#9da3b0';
    ctx.font = '10px IBM Plex Mono, monospace';
    ctx.textAlign = 'center';
    ctx.fillText(`t = ${t.toFixed(1)} / ${N}`, handleX, trackY + 18);

    // Save track bounds for interaction
    canvas._trackY = trackY;
    canvas._trackX0 = plotX;
    canvas._trackX1 = plotX + plotW;

    ctx.textBaseline = 'alphabetic';
  }

  let dragging = false;
  function setTimeFromX(x) {
    const x0 = canvas._trackX0;
    const x1 = canvas._trackX1;
    const fr = Math.max(0, Math.min(1, (x - x0) / (x1 - x0)));
    t = fr * N;
  }

  canvas.addEventListener('mousedown', (e) => {
    const r = canvas.getBoundingClientRect();
    const x = e.clientX - r.left;
    const y = e.clientY - r.top;
    if (Math.abs(y - canvas._trackY) < 20) {
      dragging = true;
      setTimeFromX(x);
      playing = false;
      playBtn.classList.remove('active');
      playBtn.textContent = 'Play';
    }
  });
  window.addEventListener('mousemove', (e) => {
    if (!dragging) return;
    const r = canvas.getBoundingClientRect();
    setTimeFromX(e.clientX - r.left);
  });
  window.addEventListener('mouseup', () => { dragging = false; });

  canvas.addEventListener('touchstart', (e) => {
    const tch = e.touches[0];
    const r = canvas.getBoundingClientRect();
    const x = tch.clientX - r.left;
    const y = tch.clientY - r.top;
    if (Math.abs(y - canvas._trackY) < 30) {
      dragging = true;
      setTimeFromX(x);
      playing = false;
      e.preventDefault();
    }
  }, { passive: false });
  canvas.addEventListener('touchmove', (e) => {
    if (!dragging) return;
    const tch = e.touches[0];
    const r = canvas.getBoundingClientRect();
    setTimeFromX(tch.clientX - r.left);
    e.preventDefault();
  }, { passive: false });
  canvas.addEventListener('touchend', () => { dragging = false; });

  resetBtn.addEventListener('click', () => {
    generateMessage();
  });
  playBtn.addEventListener('click', () => {
    playing = !playing;
    playBtn.classList.toggle('active', playing);
    playBtn.textContent = playing ? 'Pause' : 'Play';
    if (t >= N - 0.01) t = 0;
    lastFrame = performance.now();
  });

  function loop(now) {
    if (playing && !dragging) {
      const dt = (now - lastFrame) / 1000;
      t += dt * (N / 9); // ~9s full sweep
      if (t >= N) {
        t = N;
        playing = false;
        playBtn.classList.remove('active');
        playBtn.textContent = 'Play';
      }
    }
    lastFrame = now;
    draw();
    requestAnimationFrame(loop);
  }

  generateMessage();
  requestAnimationFrame(loop);
})();
