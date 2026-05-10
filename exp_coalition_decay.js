(function () {
  const slider = document.getElementById('coalition-stress');
  const stressVal = document.getElementById('coalition-stress-val');

  const c1 = document.getElementById('coalition-canvas-1').getContext('2d');
  const c2 = document.getElementById('coalition-canvas-2').getContext('2d');
  const c3 = document.getElementById('coalition-canvas-3').getContext('2d');

  const vocab1 = document.getElementById('coalition-vocab-1');
  const vocab2 = document.getElementById('coalition-vocab-2');
  const vocab3 = document.getElementById('coalition-vocab-3');
  const read1 = document.getElementById('coalition-readout-1');
  const read2 = document.getElementById('coalition-readout-2');
  const read3 = document.getElementById('coalition-readout-3');

  const W = 280, H = 280;

  // ----- Panel 1: WABI-SABI WILTING FLOWER -----
  function drawFlower(ctx, t) {
    ctx.clearRect(0, 0, W, H);
    const cx = W / 2, cy = H / 2 + 18;
    const stemLen = 90 - t * 18;
    const stemX = cx;

    // stem
    ctx.strokeStyle = `rgba(120, 110, 70, ${1 - t * 0.5})`;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(stemX, cy + 95);
    ctx.quadraticCurveTo(
      stemX + Math.sin(t * 1.2) * 22,
      cy + 50 - t * 10,
      stemX + t * 36,
      cy - stemLen + 60
    );
    ctx.stroke();

    // leaf
    const leafTilt = t * 0.9;
    ctx.fillStyle = `rgba(80, 95, 55, ${(1 - t * 0.7).toFixed(3)})`;
    ctx.beginPath();
    ctx.ellipse(cx - 30 + t * 6, cy + 30 + t * 18, 18 - t * 6, 6, -0.5 + leafTilt, 0, Math.PI * 2);
    ctx.fill();

    // petals
    const petals = 6;
    const headX = stemX + t * 36;
    const headY = cy - stemLen + 60;

    for (let i = 0; i < petals; i++) {
      const angle = (i / petals) * Math.PI * 2 + t * 0.3;
      const dropOff = Math.max(0, 1 - t * 1.4 + Math.sin(i * 1.7) * 0.18);
      const r = 24 * dropOff;
      if (r < 2) continue;
      const fade = Math.max(0, 1 - t * 1.1);
      const r1 = 240 - t * 60;
      const g1 = 140 + Math.sin(i) * 18 - t * 60;
      const b1 = 170 - t * 80;
      ctx.fillStyle = `rgba(${r1|0}, ${g1|0}, ${b1|0}, ${fade.toFixed(3)})`;
      ctx.beginPath();
      ctx.ellipse(
        headX + Math.cos(angle) * (12 + t * 10),
        headY + Math.sin(angle) * (12 + t * 10) + t * 16,
        r, r * 0.6, angle, 0, Math.PI * 2
      );
      ctx.fill();
    }

    // dropped petals
    if (t > 0.45) {
      const dropped = Math.floor((t - 0.45) * 14);
      for (let i = 0; i < dropped; i++) {
        const seed = i * 13.7;
        const px = headX + Math.sin(seed) * (40 + i * 6);
        const py = cy + 70 + (i * 5) % 30;
        const fade = Math.max(0.05, 1 - t * 0.6 - i * 0.05);
        ctx.fillStyle = `rgba(${(220 - t * 80)|0}, ${(120 - t * 60)|0}, ${(150 - t * 100)|0}, ${fade.toFixed(3)})`;
        ctx.beginPath();
        ctx.ellipse(px, py, 8, 4, seed, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // center / stamen
    ctx.fillStyle = `rgba(${(180 - t * 100)|0}, ${(140 - t * 80)|0}, ${(60 - t * 30)|0}, ${(1 - t * 0.5).toFixed(3)})`;
    ctx.beginPath();
    ctx.arc(headX, headY + t * 16, 6 - t * 2, 0, Math.PI * 2);
    ctx.fill();
  }

  // ----- Panel 2: VANITAS ROTTING FRUIT -----
  function drawFruit(ctx, t) {
    ctx.clearRect(0, 0, W, H);
    const cx = W / 2, cy = H / 2 + 6;

    // shadow
    ctx.fillStyle = 'rgba(0,0,0,0.45)';
    ctx.beginPath();
    ctx.ellipse(cx, cy + 80, 70, 8, 0, 0, Math.PI * 2);
    ctx.fill();

    // fruit body
    const baseR = 80 - t * 8;
    const r = 220 - t * 110;
    const g = 90 - t * 30;
    const b = 70 - t * 30;
    ctx.fillStyle = `rgb(${r|0}, ${g|0}, ${b|0})`;
    ctx.beginPath();
    ctx.ellipse(cx, cy, baseR, baseR * 0.95, 0, 0, Math.PI * 2);
    ctx.fill();

    // highlight
    ctx.fillStyle = `rgba(255, 230, 200, ${(0.35 - t * 0.3).toFixed(3)})`;
    ctx.beginPath();
    ctx.ellipse(cx - 22, cy - 26, 14, 22, -0.4, 0, Math.PI * 2);
    ctx.fill();

    // decay patches (deterministic seeded)
    const patches = Math.floor(t * 14);
    for (let i = 0; i < patches; i++) {
      const seed = i * 17.3 + 5;
      const px = cx + Math.cos(seed) * (baseR * 0.55);
      const py = cy + Math.sin(seed * 1.7) * (baseR * 0.55);
      const pr = 5 + (i % 5) * 4 + t * 6;
      const dark = Math.max(0, 0.7 - i * 0.04);
      ctx.fillStyle = `rgba(${(50 - i * 2)|0}, ${(40 - i)|0}, ${(20)|0}, ${dark.toFixed(3)})`;
      ctx.beginPath();
      ctx.arc(px, py, pr, 0, Math.PI * 2);
      ctx.fill();
    }

    // mold halo at high stress
    if (t > 0.65) {
      const h = (t - 0.65) * 3;
      ctx.strokeStyle = `rgba(120, 130, 90, ${Math.min(0.5, h * 0.5).toFixed(3)})`;
      ctx.lineWidth = 1;
      for (let i = 0; i < 12; i++) {
        const a = (i / 12) * Math.PI * 2;
        ctx.beginPath();
        ctx.moveTo(cx + Math.cos(a) * baseR, cy + Math.sin(a) * baseR);
        ctx.lineTo(cx + Math.cos(a) * (baseR + 6 + h * 3), cy + Math.sin(a) * (baseR + 6 + h * 3));
        ctx.stroke();
      }
    }

    // stem
    ctx.strokeStyle = `rgba(80, 60, 30, ${(1 - t * 0.5).toFixed(3)})`;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(cx, cy - baseR + 4);
    ctx.lineTo(cx + 4, cy - baseR - 14);
    ctx.stroke();
  }

  // ----- Panel 3: COALITION DECAY (POLYP + ZOOXANTHELLAE) -----
  function drawCoalition(ctx, t) {
    ctx.clearRect(0, 0, W, H);
    const cx = W / 2, cy = H / 2;

    // polyp position (slow drift left as treaty breaks)
    const sep = t * 70;
    const ax = cx - sep * 0.5;
    const bx = cx + sep * 0.5;
    const ay = cy - 6 + Math.sin(t * 0.7) * 4;
    const by = cy + 8 + Math.sin(t * 1.3 + 1) * 4;

    // interface band (the partnership)
    if (t < 0.95) {
      const bandAlpha = Math.max(0, 0.95 - t * 1.05);
      const bandWobble = t * 6;
      ctx.strokeStyle = `rgba(255, 220, 140, ${bandAlpha.toFixed(3)})`;
      ctx.lineWidth = 18 - t * 14;
      ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(ax + 30, ay);
      ctx.bezierCurveTo(
        ax + 50, ay - 10 + bandWobble * Math.sin(t * 12),
        bx - 50, by + 10 + bandWobble * Math.cos(t * 13),
        bx - 30, by
      );
      ctx.stroke();

      // exchange particles (sugars / nitrogen)
      const particles = Math.max(0, 8 - Math.floor(t * 9));
      for (let i = 0; i < particles; i++) {
        const phase = (Date.now() / 1000 + i * 0.4) % 1;
        const px = ax + 30 + (bx - 30 - (ax + 30)) * phase;
        const py = ay + (by - ay) * phase;
        ctx.fillStyle = `rgba(255, 220, 140, ${(bandAlpha * 0.7).toFixed(3)})`;
        ctx.beginPath();
        ctx.arc(px, py, 1.6, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // failing-interface frays (visible from t > 0.4)
    if (t > 0.4 && t < 0.95) {
      const frays = Math.floor((t - 0.4) * 18);
      for (let i = 0; i < frays; i++) {
        const seed = i * 7.3;
        const fx = cx + Math.sin(seed * 2.3) * 40;
        const fy = cy + Math.cos(seed) * 14;
        const len = 8 + (i % 5) * 3;
        const a = seed * 1.2;
        ctx.strokeStyle = `rgba(255, 200, 120, ${(0.4 - (t - 0.4) * 0.6).toFixed(3)})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(fx, fy);
        ctx.lineTo(fx + Math.cos(a) * len, fy + Math.sin(a) * len);
        ctx.stroke();
      }
    }

    // POLYP (a) — coral animal, tentacled circle
    const polypR = 28;
    ctx.fillStyle = '#d49a7c';
    ctx.beginPath();
    ctx.arc(ax, ay, polypR, 0, Math.PI * 2);
    ctx.fill();

    // tentacles
    const tentacles = 10;
    ctx.strokeStyle = '#d49a7c';
    ctx.lineWidth = 2;
    ctx.lineCap = 'round';
    for (let i = 0; i < tentacles; i++) {
      const a = (i / tentacles) * Math.PI * 2 + t * 0.5;
      const wob = Math.sin(Date.now() / 600 + i) * 4;
      ctx.beginPath();
      ctx.moveTo(ax + Math.cos(a) * polypR, ay + Math.sin(a) * polypR);
      ctx.lineTo(
        ax + Math.cos(a) * (polypR + 16 + wob),
        ay + Math.sin(a) * (polypR + 16 + wob)
      );
      ctx.stroke();
    }

    // mouth ring
    ctx.fillStyle = '#7a3a26';
    ctx.beginPath();
    ctx.arc(ax, ay, 7, 0, Math.PI * 2);
    ctx.fill();

    // ZOOXANTHELLAE (b) — single-celled cluster
    const zoox = [
      [bx, by], [bx - 12, by + 10], [bx + 12, by - 8],
      [bx - 6, by - 12], [bx + 8, by + 14], [bx + 14, by + 4],
      [bx - 14, by - 4], [bx - 4, by + 16],
    ];
    for (const [zx, zy] of zoox) {
      ctx.fillStyle = '#86b96e';
      ctx.beginPath();
      ctx.arc(zx, zy, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = 'rgba(180, 220, 140, 0.6)';
      ctx.beginPath();
      ctx.arc(zx - 1.5, zy - 1.5, 2, 0, Math.PI * 2);
      ctx.fill();
    }

    // bleaching tint over polyp at high stress (the visible Counter-Ledger entry)
    if (t > 0.55) {
      const bleach = Math.min(1, (t - 0.55) * 2.4);
      ctx.fillStyle = `rgba(245, 240, 232, ${(bleach * 0.78).toFixed(3)})`;
      ctx.beginPath();
      ctx.arc(ax, ay, polypR + 2, 0, Math.PI * 2);
      ctx.fill();
    }

    // labels (substrate-level)
    ctx.fillStyle = 'rgba(180, 160, 110, 0.7)';
    ctx.font = '10px JetBrains Mono, monospace';
    ctx.textAlign = 'center';
    ctx.fillText('polyp', ax, ay + polypR + 36);
    ctx.fillText('zooxanthellae', bx, by + 32);
  }

  // ----- VOCAB / READOUT -----
  function vocabOne(t) {
    if (t < 0.2) return 'wabi-sabi: intact';
    if (t < 0.45) return 'wabi-sabi: wilting';
    if (t < 0.75) return 'wabi-sabi: petals falling';
    if (t < 0.95) return 'wabi-sabi: dust';
    return 'after wabi-sabi: dead';
  }

  function vocabTwo(t) {
    if (t < 0.2) return 'vanitas: intact';
    if (t < 0.45) return 'vanitas: blemished';
    if (t < 0.75) return 'vanitas: rotting';
    if (t < 0.95) return 'vanitas: fully decayed';
    return 'after vanitas: corpse';
  }

  function vocabThree(t) {
    // No vocabulary exists for the middle. Show the gap.
    if (t < 0.2) return 'symbiosis: intact';
    if (t < 0.45) return '[ ? ] interface stressed';
    if (t < 0.75) return '[ no aesthetic register ]';
    if (t < 0.95) return '[ no aesthetic register ]';
    return '[ no aesthetic register ] separated';
  }

  function readoutOne(t) {
    if (t < 0.95) return 'subject: alive';
    return 'subject: dead';
  }

  function readoutTwo(t) {
    if (t < 0.95) return 'subject: alive';
    return 'subject: dead';
  }

  function readoutThree(t) {
    if (t < 0.45) {
      return 'part A: alive · part B: alive · union: present';
    }
    if (t < 0.95) {
      return 'part A: alive · part B: alive · union: dissolving';
    }
    return 'part A: alive · part B: alive · union: absent';
  }

  function render() {
    const v = parseFloat(slider.value) / 100;
    stressVal.textContent = slider.value;

    drawFlower(c1, v);
    drawFruit(c2, v);
    drawCoalition(c3, v);

    vocab1.textContent = vocabOne(v);
    vocab2.textContent = vocabTwo(v);
    vocab3.textContent = vocabThree(v);
    vocab3.classList.toggle('coalition-vocab-empty', v >= 0.45);

    read1.textContent = readoutOne(v);
    read2.textContent = readoutTwo(v);
    read3.textContent = readoutThree(v);
  }

  slider.addEventListener('input', render);

  // animate (for tentacle wobble, particles)
  function tick() {
    render();
    requestAnimationFrame(tick);
  }
  tick();
})();
