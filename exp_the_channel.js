(function () {
  const canvas = document.getElementById('channel-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const slider = document.getElementById('channel-insulation');
  const insVal = document.getElementById('channel-ins-val');
  const stateEl = document.getElementById('channel-state');

  const barEls = {
    medicine: document.getElementById('bar-medicine'),
    quantum: document.getElementById('bar-quantum'),
    ai: document.getElementById('bar-ai'),
  };
  const readEls = {
    medicine: document.getElementById('read-medicine'),
    quantum: document.getElementById('read-quantum'),
    ai: document.getElementById('read-ai'),
  };

  const W = canvas.width;
  const H = canvas.height;

  // Particles representing signals. They drift from "verified" to "verifier";
  // when insulation is high, the barrier blocks them.
  const particles = [];
  for (let i = 0; i < 60; i++) {
    particles.push({
      x: 60 + Math.random() * 280,
      y: 30 + Math.random() * (H - 60),
      vx: 0.3 + Math.random() * 0.7,
      vy: (Math.random() - 0.5) * 0.3,
      r: 1.2 + Math.random() * 1.4,
      crossed: false,
    });
  }

  let insulation = 1.0;

  function setInsulation(percent) {
    insulation = percent / 100;
    insVal.textContent = String(Math.round(percent));

    // State text
    if (insulation >= 0.85) stateEl.textContent = 'Insulated';
    else if (insulation >= 0.5) stateEl.textContent = 'Leaky';
    else if (insulation >= 0.2) stateEl.textContent = 'Coupled';
    else stateEl.textContent = 'Collapsed';

    updateMetrics();
  }

  function updateMetrics() {
    // Medicine: fidelity drops smoothly with insulation, autopsy data only useful if insulated
    const med = Math.max(0, insulation);
    const medPct = Math.round(med * 100);
    barEls.medicine.style.width = medPct + '%';
    barEls.medicine.classList.toggle('broken', med < 0.5);
    if (med >= 0.85) {
      readEls.medicine.textContent = `${medPct}% of fatal misdiagnoses recoverable`;
    } else if (med >= 0.5) {
      readEls.medicine.textContent = `Pathologist sees the chart. Blinding compromised.`;
    } else if (med >= 0.2) {
      readEls.medicine.textContent = `Autopsy rate has fallen to ~${Math.round(med * 20)}%.`;
    } else {
      readEls.medicine.textContent = `No external check. Confidence stops being measurable.`;
    }

    // Quantum: CHSH parameter S. Tsirelson bound = 2.828. Classical = 2.0.
    // At full insulation, S = 2.828 (genuinely quantum). At zero, S can be faked up to 4.
    const S = 2 + insulation * 0.828 + (1 - insulation) * 1.172;
    const verified = insulation >= 0.5;
    const sPct = Math.max(0, Math.min(100, ((S - 2) / 0.828) * 100));
    barEls.quantum.style.width = (verified ? sPct : 0) + '%';
    barEls.quantum.classList.toggle('broken', !verified);
    if (insulation >= 0.85) {
      readEls.quantum.textContent = `S = ${S.toFixed(3)} (genuine entanglement, Tsirelson bound)`;
    } else if (insulation >= 0.5) {
      readEls.quantum.textContent = `S = ${S.toFixed(3)} — signaling channel narrows the proof`;
    } else if (insulation >= 0.2) {
      readEls.quantum.textContent = `S = ${S.toFixed(3)} — fakeable by classical correlation`;
    } else {
      readEls.quantum.textContent = `S = ${S.toFixed(3)} — verifier cannot distinguish quantum from cheating`;
    }

    // AI: independent-error coverage. Errors detected = independence between grader and graded.
    const ai = Math.max(0, insulation);
    const aiPct = Math.round(ai * 100);
    barEls.ai.style.width = aiPct + '%';
    barEls.ai.classList.toggle('broken', ai < 0.5);
    if (ai >= 0.85) {
      readEls.ai.textContent = `${aiPct}% of grader errors uncorrelated with model`;
    } else if (ai >= 0.5) {
      readEls.ai.textContent = `Shared base model. Errors begin to correlate.`;
    } else if (ai >= 0.2) {
      readEls.ai.textContent = `Same labelers, same training data. Blind spots align.`;
    } else {
      readEls.ai.textContent = `Self-grading. Verifier and verified are the same network.`;
    }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Background
    ctx.fillStyle = 'rgba(255,255,255,0.015)';
    ctx.fillRect(0, 0, W, H);

    // Two zones: VERIFIED (left) and VERIFIER (right). Barrier in the middle.
    const barrierX = W / 2;
    const barrierWidth = 6;

    // Zone labels
    ctx.font = '11px Inter, system-ui, sans-serif';
    ctx.fillStyle = 'rgba(255,255,255,0.35)';
    ctx.textAlign = 'left';
    ctx.fillText('VERIFIED  (the device, the doctor, the model)', 14, 18);
    ctx.textAlign = 'right';
    ctx.fillText('VERIFIER  (autopsy, Bell test, grader)', W - 14, 18);
    ctx.textAlign = 'center';
    ctx.fillText('no-signaling', barrierX, H - 8);

    // Zone tints
    ctx.fillStyle = 'rgba(180, 100, 100, 0.04)';
    ctx.fillRect(0, 24, barrierX - barrierWidth / 2, H - 36);
    ctx.fillStyle = 'rgba(100, 160, 200, 0.04)';
    ctx.fillRect(barrierX + barrierWidth / 2, 24, W - barrierX - barrierWidth / 2, H - 36);

    // Barrier — opacity proportional to insulation
    const barrierAlpha = 0.15 + insulation * 0.7;
    ctx.fillStyle = `rgba(211, 169, 88, ${barrierAlpha})`;
    ctx.fillRect(barrierX - barrierWidth / 2, 24, barrierWidth, H - 36);

    // Particle motion
    particles.forEach((p) => {
      p.x += p.vx;
      p.y += p.vy;
      // Bounce vertically
      if (p.y < 28 || p.y > H - 16) p.vy = -p.vy;

      // Hit barrier — block proportional to insulation
      if (!p.crossed && p.x >= barrierX - barrierWidth / 2 && p.x <= barrierX + barrierWidth / 2) {
        if (Math.random() < insulation) {
          // blocked — bounce back
          p.vx = -Math.abs(p.vx);
          p.x = barrierX - barrierWidth / 2 - 1;
        } else {
          p.crossed = true;
        }
      }

      // Off-screen reset
      if (p.x > W + 10 || p.x < -10) {
        p.x = 60 + Math.random() * 60;
        p.vx = 0.3 + Math.random() * 0.7;
        p.vy = (Math.random() - 0.5) * 0.3;
        p.crossed = false;
      }

      // Render
      ctx.beginPath();
      ctx.fillStyle = p.crossed
        ? 'rgba(220, 120, 120, 0.85)'
        : 'rgba(180, 180, 200, 0.55)';
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    });

    // Verifier outcome circle on the right — flickers if too many particles crossed
    const crossedCount = particles.filter((p) => p.crossed).length;
    const fidelity = 1 - crossedCount / particles.length;
    const cx = W - 54;
    const cy = H / 2;
    ctx.beginPath();
    ctx.fillStyle = fidelity > 0.7
      ? 'rgba(150, 200, 150, 0.18)'
      : fidelity > 0.4
      ? 'rgba(220, 180, 100, 0.18)'
      : 'rgba(220, 100, 100, 0.18)';
    ctx.arc(cx, cy, 28, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = fidelity > 0.7
      ? 'rgba(150, 200, 150, 0.7)'
      : fidelity > 0.4
      ? 'rgba(220, 180, 100, 0.7)'
      : 'rgba(220, 100, 100, 0.7)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    requestAnimationFrame(draw);
  }

  slider.addEventListener('input', (e) => setInsulation(parseInt(e.target.value, 10)));
  setInsulation(parseInt(slider.value, 10));
  draw();
})();
