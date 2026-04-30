(() => {
  const treeCanvas = document.getElementById('rt-tree');
  const reefCanvas = document.getElementById('rt-reef');
  const graphCanvas = document.getElementById('rt-graph');
  if (!treeCanvas || !reefCanvas || !graphCanvas) return;

  const treeCtx = treeCanvas.getContext('2d');
  const reefCtx = reefCanvas.getContext('2d');
  const graphCtx = graphCanvas.getContext('2d');

  const treeStatus = document.getElementById('rt-tree-status');
  const reefStatus = document.getElementById('rt-reef-status');
  const tickOut = document.getElementById('rt-tick');
  const speedInput = document.getElementById('rt-speed-input');
  const resetBtn = document.getElementById('rt-reset');
  const pauseBtn = document.getElementById('rt-pause');

  // ---- state ----
  const REEF_NODES = 60;
  let state;
  let paused = false;

  function init() {
    state = {
      tick: 0,
      tree: { alive: true, integrity: 1.0, lastShockAt: -100 },
      reef: {
        nodes: Array.from({ length: REEF_NODES }, (_, i) => ({
          alive: true,
          x: (i % 12) / 11,
          y: Math.floor(i / 12) / 4,
          vitality: 0.85 + Math.random() * 0.15,
        })),
        decayRate: 0.0008,
      },
      history: [], // {tick, treeRecovery, reefRecovery, treeDead, reefDead}
      treeDeadAt: null,
      reefExtinctAt: null,
    };
  }
  init();

  function aliveCount(reef) {
    return reef.nodes.filter(n => n.alive).length;
  }

  // recovery time from a unit shock — how many ticks to return to within 5% of pre-shock state
  // we approximate it by a closed-form: longer when system is closer to its bifurcation
  function treeRecoveryTime(tree) {
    if (!tree.alive) return Infinity;
    return 2; // bronze artifact recovers instantly from minor scratches — until it doesn't
  }

  function reefRecoveryTime(reef) {
    const alive = aliveCount(reef);
    if (alive === 0) return Infinity;
    // critical slowing down: recovery time ~ 1 / (carriers / total)^1.4
    const fraction = alive / REEF_NODES;
    return 2 + Math.pow(1 / Math.max(fraction, 0.05), 1.4);
  }

  function step() {
    state.tick++;
    const tree = state.tree;
    const reef = state.reef;

    // tree: drifts forward intact. there is a small per-tick probability of catastrophic loss
    // that grows linearly. this models: workshop loses last gear-cutter, fire, conquest.
    if (tree.alive) {
      const shockProb = 0.0009 + state.tick * 0.000004;
      if (Math.random() < shockProb) {
        tree.alive = false;
        tree.integrity = 0;
        state.treeDeadAt = state.tick;
      }
    }

    // reef: each carrier has a small per-tick death probability that grows with time.
    // when a carrier dies it does NOT come back (no apprentice in this simplification)
    if (aliveCount(reef) > 0) {
      const baseDeath = reef.decayRate + state.tick * 0.0000035;
      reef.nodes.forEach(n => {
        if (n.alive && Math.random() < baseDeath) {
          n.alive = false;
        }
      });
      if (aliveCount(reef) === 0 && state.reefExtinctAt === null) {
        state.reefExtinctAt = state.tick;
      }
    }

    state.history.push({
      tick: state.tick,
      treeR: treeRecoveryTime(tree),
      reefR: reefRecoveryTime(reef),
      treeDead: !tree.alive,
      reefAlive: aliveCount(reef),
    });
    if (state.history.length > 1200) state.history.shift();
  }

  // ---- rendering ----
  function drawTree() {
    const w = treeCanvas.width;
    const h = treeCanvas.height;
    treeCtx.clearRect(0, 0, w, h);
    treeCtx.fillStyle = '#0c0a07';
    treeCtx.fillRect(0, 0, w, h);

    const cx = w / 2;
    if (state.tree.alive) {
      // bronze gear circles
      treeCtx.strokeStyle = '#b9a47a';
      treeCtx.lineWidth = 2;
      const cy = h / 2;
      [60, 38, 22].forEach((r, i) => {
        treeCtx.beginPath();
        treeCtx.arc(cx, cy, r, 0, Math.PI * 2);
        treeCtx.stroke();
        // teeth
        const teeth = [16, 10, 6][i];
        for (let t = 0; t < teeth; t++) {
          const a = (t / teeth) * Math.PI * 2 + state.tick * 0.003 * (i % 2 ? -1 : 1);
          const x1 = cx + Math.cos(a) * r;
          const y1 = cy + Math.sin(a) * r;
          const x2 = cx + Math.cos(a) * (r + 4);
          const y2 = cy + Math.sin(a) * (r + 4);
          treeCtx.beginPath();
          treeCtx.moveTo(x1, y1);
          treeCtx.lineTo(x2, y2);
          treeCtx.stroke();
        }
      });
      treeStatus.textContent = `intact - tick ${state.tick}`;
      treeStatus.style.color = '#8a8474';
    } else {
      // corroded wreck
      treeCtx.fillStyle = '#3a2f22';
      treeCtx.beginPath();
      treeCtx.ellipse(cx, h / 2, 50, 30, 0, 0, Math.PI * 2);
      treeCtx.fill();
      treeCtx.strokeStyle = '#5a4a32';
      treeCtx.lineWidth = 1;
      for (let i = 0; i < 8; i++) {
        treeCtx.beginPath();
        treeCtx.moveTo(cx - 50 + Math.random() * 100, h / 2 - 20 + Math.random() * 40);
        treeCtx.lineTo(cx - 50 + Math.random() * 100, h / 2 - 20 + Math.random() * 40);
        treeCtx.stroke();
      }
      treeStatus.textContent = `lost at tick ${state.treeDeadAt} - no warning`;
      treeStatus.style.color = '#a06040';
    }
  }

  function drawReef() {
    const w = reefCanvas.width;
    const h = reefCanvas.height;
    reefCtx.clearRect(0, 0, w, h);
    reefCtx.fillStyle = '#0c0a07';
    reefCtx.fillRect(0, 0, w, h);

    const padX = 30;
    const padY = 30;
    const cellW = (w - padX * 2) / 11;
    const cellH = (h - padY * 2) / 4;

    state.reef.nodes.forEach((n, i) => {
      const col = i % 12;
      const row = Math.floor(i / 12);
      const x = padX + col * cellW * (11 / 12);
      const y = padY + row * cellH;
      if (n.alive) {
        const wobble = Math.sin(state.tick * 0.05 + i) * 1.2;
        reefCtx.fillStyle = '#b9a47a';
        reefCtx.beginPath();
        reefCtx.arc(x, y + wobble, 4, 0, Math.PI * 2);
        reefCtx.fill();
        // faint connecting strands
        if (col < 11 && state.reef.nodes[i + 1] && state.reef.nodes[i + 1].alive) {
          reefCtx.strokeStyle = 'rgba(185, 164, 122, 0.18)';
          reefCtx.lineWidth = 0.5;
          reefCtx.beginPath();
          reefCtx.moveTo(x, y + wobble);
          reefCtx.lineTo(x + cellW * (11 / 12), y + wobble);
          reefCtx.stroke();
        }
      } else {
        reefCtx.fillStyle = 'rgba(74, 66, 50, 0.5)';
        reefCtx.beginPath();
        reefCtx.arc(x, y, 2, 0, Math.PI * 2);
        reefCtx.fill();
      }
    });

    const alive = aliveCount(state.reef);
    if (alive === 0) {
      reefStatus.textContent = `extinct at tick ${state.reefExtinctAt}`;
      reefStatus.style.color = '#a06040';
    } else {
      const recovery = reefRecoveryTime(state.reef).toFixed(1);
      reefStatus.textContent = `${alive}/${REEF_NODES} carriers - recovery ${recovery}t`;
      reefStatus.style.color = alive < REEF_NODES * 0.4 ? '#c08858' : '#8a8474';
    }
  }

  function drawGraph() {
    const w = graphCanvas.width;
    const h = graphCanvas.height;
    graphCtx.clearRect(0, 0, w, h);
    graphCtx.fillStyle = '#0c0a07';
    graphCtx.fillRect(0, 0, w, h);

    if (state.history.length < 2) return;

    const padX = 36;
    const padY = 18;
    const plotW = w - padX * 2;
    const plotH = h - padY * 2;

    const maxR = 60; // cap recovery-time display
    const xs = state.history.length;

    // grid
    graphCtx.strokeStyle = '#1f1c16';
    graphCtx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
      const y = padY + (i / 4) * plotH;
      graphCtx.beginPath();
      graphCtx.moveTo(padX, y);
      graphCtx.lineTo(w - padX, y);
      graphCtx.stroke();
    }

    // axis labels
    graphCtx.fillStyle = '#5a5040';
    graphCtx.font = '10px ui-monospace, monospace';
    graphCtx.fillText('60t', 4, padY + 4);
    graphCtx.fillText('0', 22, h - padY + 4);
    graphCtx.fillText('time -->', w - 60, h - 2);

    // tree line
    graphCtx.strokeStyle = '#9a7a4a';
    graphCtx.lineWidth = 1.5;
    graphCtx.beginPath();
    state.history.forEach((p, i) => {
      const x = padX + (i / Math.max(xs - 1, 1)) * plotW;
      let r = p.treeR;
      if (!isFinite(r)) r = maxR;
      const y = padY + plotH - (Math.min(r, maxR) / maxR) * plotH;
      if (i === 0) graphCtx.moveTo(x, y);
      else graphCtx.lineTo(x, y);
    });
    graphCtx.stroke();

    // tree death cliff
    if (state.treeDeadAt !== null) {
      const idx = state.history.findIndex(p => p.tick === state.treeDeadAt);
      if (idx >= 0) {
        const x = padX + (idx / Math.max(xs - 1, 1)) * plotW;
        graphCtx.strokeStyle = 'rgba(160, 96, 64, 0.6)';
        graphCtx.lineWidth = 1;
        graphCtx.beginPath();
        graphCtx.moveTo(x, padY);
        graphCtx.lineTo(x, padY + plotH);
        graphCtx.stroke();
      }
    }

    // reef line
    graphCtx.strokeStyle = '#c0a878';
    graphCtx.lineWidth = 1.8;
    graphCtx.beginPath();
    state.history.forEach((p, i) => {
      const x = padX + (i / Math.max(xs - 1, 1)) * plotW;
      let r = p.reefR;
      if (!isFinite(r)) r = maxR;
      const y = padY + plotH - (Math.min(r, maxR) / maxR) * plotH;
      if (i === 0) graphCtx.moveTo(x, y);
      else graphCtx.lineTo(x, y);
    });
    graphCtx.stroke();

    // legend
    graphCtx.fillStyle = '#9a7a4a';
    graphCtx.fillRect(padX + 6, padY + 6, 10, 2);
    graphCtx.fillStyle = '#8a8474';
    graphCtx.font = '10px ui-monospace, monospace';
    graphCtx.fillText('tree (integrator)', padX + 22, padY + 10);
    graphCtx.fillStyle = '#c0a878';
    graphCtx.fillRect(padX + 140, padY + 6, 10, 2);
    graphCtx.fillStyle = '#8a8474';
    graphCtx.fillText('reef (distributed)', padX + 156, padY + 10);
  }

  function render() {
    drawTree();
    drawReef();
    drawGraph();
    if (tickOut) tickOut.textContent = state.tick;
  }

  // ---- loop ----
  let lastFrame = 0;
  function frame(t) {
    const speed = parseInt(speedInput.value, 10);
    const interval = 1000 / (speed * 6);
    if (!paused && t - lastFrame > interval) {
      // do `speed` substeps so high-speed runs cover ground
      for (let i = 0; i < speed; i++) step();
      lastFrame = t;
    }
    render();
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  resetBtn.addEventListener('click', () => {
    init();
  });
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    pauseBtn.textContent = paused ? 'resume' : 'pause';
  });
})();
