(function () {
  const canvas = document.getElementById('sig-canvas');
  const ctx = canvas.getContext('2d');

  const POP_COUNT = 18;
  const NUM_VARIANTS = 8;
  const TARGET_VARIANT = 3;

  const variantColors = [
    '#c89c5a', '#7faab8', '#b87a8a', '#9bb87a',
    '#b8a07a', '#7ab8a8', '#a87ab8', '#b8b07a'
  ];

  let mode = 'drift';
  let truthStrength = 0.6;
  let contactRate = 0.4;
  let perturbRate = 0;
  let pops = [];
  let connections = [];
  let lastReversionInjection = null;
  let blindActualMode = null;
  let blindGuessed = false;

  function makePops() {
    pops = [];
    const rect = canvas.getBoundingClientRect();
    const cx = canvas.width / 2;
    const cy = canvas.height / 2 - 10;
    for (let i = 0; i < POP_COUNT; i++) {
      const angle = (i / POP_COUNT) * Math.PI * 2;
      const ringRadius = 180 + (i % 3) * 40;
      const x = cx + Math.cos(angle) * ringRadius;
      const y = cy + Math.sin(angle) * ringRadius * 0.55;
      pops.push({
        id: i,
        x, y,
        variant: Math.floor(Math.random() * NUM_VARIANTS),
        nextVariant: null,
        size: 14 + Math.random() * 8
      });
    }
    connections = [];
    for (let i = 0; i < POP_COUNT; i++) {
      const a = pops[(i) % POP_COUNT];
      const b = pops[(i + 1) % POP_COUNT];
      connections.push([a.id, b.id]);
      if (i % 3 === 0) {
        const c = pops[(i + Math.floor(POP_COUNT / 2)) % POP_COUNT];
        connections.push([a.id, c.id]);
      }
    }
  }

  function step() {
    for (const p of pops) p.nextVariant = p.variant;
    const effectiveMode = mode === 'blind' ? blindActualMode : mode;

    for (const [aId, bId] of connections) {
      if (Math.random() < contactRate * 0.06) {
        const a = pops[aId], b = pops[bId];
        const direction = a.size > b.size ? 1 : (a.size < b.size ? -1 : (Math.random() < 0.5 ? 1 : -1));
        if (direction > 0) b.nextVariant = a.variant;
        else a.nextVariant = b.variant;
      }
    }

    if (effectiveMode === 'truth') {
      for (const p of pops) {
        if (Math.random() < truthStrength * 0.04) {
          p.nextVariant = TARGET_VARIANT;
        }
      }
    }

    if (perturbRate > 0) {
      for (const p of pops) {
        if (Math.random() < perturbRate * 0.005) {
          p.nextVariant = Math.floor(Math.random() * NUM_VARIANTS);
        }
      }
    }

    if (lastReversionInjection !== null) {
      const inj = lastReversionInjection;
      inj.ticksSince++;
      if (inj.ticksSince > 80) {
        let surviving = 0;
        for (const id of inj.injected) {
          if (pops[id].variant === inj.variant) surviving++;
        }
        const survivalRate = surviving / inj.injected.length;
        document.getElementById('sig-rev').textContent = survivalRate.toFixed(2);
        lastReversionInjection = null;
      }
    }

    for (const p of pops) p.variant = p.nextVariant;
  }

  function computeStats() {
    const counts = new Array(NUM_VARIANTS).fill(0);
    for (const p of pops) counts[p.variant]++;
    let dominantCount = Math.max(...counts);
    const convergence = dominantCount / POP_COUNT;

    let entropy = 0;
    for (const c of counts) {
      if (c === 0) continue;
      const pr = c / POP_COUNT;
      entropy -= pr * Math.log2(pr);
    }

    document.getElementById('sig-conv').textContent = convergence.toFixed(2);
    document.getElementById('sig-ent').textContent = entropy.toFixed(2);
  }

  function draw() {
    ctx.fillStyle = '#14110d';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = 'rgba(140, 125, 100, 0.16)';
    ctx.lineWidth = 1;
    for (const [aId, bId] of connections) {
      const a = pops[aId], b = pops[bId];
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    for (const p of pops) {
      ctx.fillStyle = variantColors[p.variant];
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = 'rgba(20, 17, 13, 0.5)';
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    ctx.fillStyle = '#9c9588';
    ctx.font = '12px JetBrains Mono, monospace';
    const effectiveMode = mode === 'blind' ? '???' : mode.toUpperCase();
    ctx.fillText('mode: ' + effectiveMode, 14, 22);
    if (mode === 'blind' && blindGuessed) {
      ctx.fillStyle = '#c89c5a';
      ctx.fillText('actual: ' + (blindActualMode || '').toUpperCase(), 14, 40);
    }

    if (lastReversionInjection !== null) {
      ctx.fillStyle = '#c89c5a';
      ctx.fillText('reversion test in progress', 14, 540 - 14);
    }
  }

  function tick() {
    step();
    computeStats();
    draw();
    requestAnimationFrame(tick);
  }

  function injectReversion() {
    const counts = new Array(NUM_VARIANTS).fill(0);
    for (const p of pops) counts[p.variant]++;
    let dominantVariant = 0;
    let dominantCount = counts[0];
    for (let i = 1; i < NUM_VARIANTS; i++) {
      if (counts[i] > dominantCount) {
        dominantCount = counts[i];
        dominantVariant = i;
      }
    }
    let altVariant = (dominantVariant + 1) % NUM_VARIANTS;
    const injected = [];
    let toInject = 4;
    const order = pops.slice().sort(() => Math.random() - 0.5);
    for (const p of order) {
      if (toInject === 0) break;
      if (p.variant === dominantVariant) {
        p.variant = altVariant;
        injected.push(p.id);
        toInject--;
      }
    }
    if (injected.length > 0) {
      lastReversionInjection = {
        variant: altVariant,
        injected,
        ticksSince: 0
      };
      document.getElementById('sig-rev').textContent = '...';
    }
  }

  function setMode(newMode) {
    mode = newMode;
    document.querySelectorAll('.sig-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.mode === newMode);
    });
    if (newMode === 'blind') {
      blindActualMode = Math.random() < 0.5 ? 'drift' : 'truth';
      blindGuessed = false;
      const result = document.getElementById('sig-blind-result');
      result.classList.remove('show', 'correct', 'wrong');
      result.innerHTML = 'Watch the dynamics. When you have a guess, click Drift mode or Truth mode above to commit.';
      result.classList.add('show');
    } else if (blindActualMode !== null && !blindGuessed) {
      blindGuessed = true;
      const correct = newMode === blindActualMode;
      const result = document.getElementById('sig-blind-result');
      result.classList.remove('correct', 'wrong');
      result.classList.add(correct ? 'correct' : 'wrong');
      result.innerHTML = correct
        ? 'Correct. The hidden mode was <strong>' + blindActualMode.toUpperCase() + '</strong>. Reset and try again.'
        : 'Wrong. The hidden mode was <strong>' + blindActualMode.toUpperCase() + '</strong>. Reset and try again.';
      result.classList.add('show');
      blindActualMode = null;
    }
  }

  document.querySelectorAll('.sig-btn').forEach(b => {
    b.addEventListener('click', () => setMode(b.dataset.mode));
  });

  document.getElementById('sig-truth').addEventListener('input', e => {
    truthStrength = e.target.value / 100;
    document.getElementById('sig-truth-val').textContent = truthStrength.toFixed(2);
  });
  document.getElementById('sig-contact').addEventListener('input', e => {
    contactRate = e.target.value / 100;
    document.getElementById('sig-contact-val').textContent = contactRate.toFixed(2);
  });
  document.getElementById('sig-perturb').addEventListener('input', e => {
    perturbRate = e.target.value / 100;
    document.getElementById('sig-perturb-val').textContent = perturbRate.toFixed(2);
  });

  document.getElementById('sig-reset').addEventListener('click', () => {
    makePops();
    document.getElementById('sig-rev').textContent = '--';
    if (mode === 'blind') {
      blindActualMode = Math.random() < 0.5 ? 'drift' : 'truth';
      blindGuessed = false;
      const result = document.getElementById('sig-blind-result');
      result.classList.remove('correct', 'wrong');
      result.classList.add('show');
      result.innerHTML = 'New hidden mode. Watch the dynamics. When you have a guess, click Drift mode or Truth mode above to commit.';
    }
  });

  document.getElementById('sig-perturb-btn').addEventListener('click', injectReversion);

  makePops();
  requestAnimationFrame(tick);
})();
