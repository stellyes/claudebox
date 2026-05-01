(() => {
  const cWorkshop = document.getElementById('canvas-workshop');
  const cFossil = document.getElementById('canvas-fossil');
  const cRebuild = document.getElementById('canvas-rebuild');
  const ctxWorkshop = cWorkshop.getContext('2d');
  const ctxFossil = cFossil.getContext('2d');
  const ctxRebuild = cRebuild.getContext('2d');

  const meterChem = document.getElementById('meter-chem');
  const meterTone = document.getElementById('meter-tone');
  const meterLoop = document.getElementById('meter-loop');
  const meterDetect = document.getElementById('meter-detect');
  const meterLineage = document.getElementById('meter-lineage');
  const meterMatchChem = document.getElementById('meter-match-chem');
  const meterMatchTone = document.getElementById('meter-match-tone');

  const yearActive = document.getElementById('year-active');
  const yearFossil = document.getElementById('year-fossil');
  const continuityInput = document.getElementById('continuity');
  const continuityReadout = document.getElementById('continuity-readout');
  const btnClose = document.getElementById('btn-close');
  const btnRebuild = document.getElementById('btn-rebuild');
  const btnReset = document.getElementById('btn-reset');
  const rebuildReadout = document.getElementById('rebuild-readout');
  const paneWorkshop = document.getElementById('pane-workshop');
  const paneFossil = document.getElementById('pane-fossil');
  const paneRebuild = document.getElementById('pane-rebuild');

  // The hidden, never-written-down loop parameters that produce tone.
  // These are the analog of timing, water chemistry, plate-tap judgment.
  const HIDDEN_LOOP_PARAMS = {
    soakSeconds: 0.61803,    // golden-ratio fraction of a base period
    plankSeasonPhase: 0.31,
    plateTapTuning: 0.78,
    apprenticeFeedback: 0.45,
  };

  // Detected chemistry — surface composition, recoverable from the fossil.
  const CHEMISTRY = {
    borax: 0.42,
    zinc: 0.18,
    copper: 0.07,
    alum: 0.22,
    lime: 0.11,
  };

  let state = {
    phase: 'workshop',  // workshop | fossil | rebuild
    workshopYear: 1665,
    chemistryDepth: 0,
    toneQuality: 0,
    loopIntegrity: 0,
    fossilYear: 1744,   // Guarneri del Gesù dies; Cremona school silent
    detectionLevel: 0,
    lineageRemaining: 0,
    rebuiltChemistry: 0,
    rebuiltTone: 0,
    grain: [],
    chemSpots: [],
  };

  // Initialize a wood grain pattern for the workshop plank
  function initGrain() {
    state.grain = [];
    for (let i = 0; i < 28; i++) {
      state.grain.push({
        y: 30 + i * 12 + (Math.random() - 0.5) * 4,
        wobble: Math.random() * Math.PI * 2,
        wobbleSpeed: 0.7 + Math.random() * 0.6,
      });
    }
    state.chemSpots = [];
  }

  function clearCanvas(ctx, c) {
    ctx.fillStyle = '#050403';
    ctx.fillRect(0, 0, c.width, c.height);
  }

  function drawWoodPlank(ctx, c, chemistryDepth, toneQuality, age = 0, scattered = false) {
    clearCanvas(ctx, c);
    const w = c.width, h = c.height;
    const baseHue = 32 - age * 6;        // wood darkens with age
    const baseSat = 38 - age * 12;
    const baseLight = 18 + chemistryDepth * 14;

    // Plank body
    ctx.fillStyle = `hsl(${baseHue}, ${baseSat}%, ${baseLight}%)`;
    ctx.fillRect(20, 20, w - 40, h - 40);

    // Wood grain
    ctx.lineWidth = 1.2;
    state.grain.forEach((g, i) => {
      const gradient = ctx.createLinearGradient(20, 0, w - 20, 0);
      const grainHue = baseHue - 4;
      const grainAlpha = 0.32 + (chemistryDepth * 0.18);
      gradient.addColorStop(0, `hsla(${grainHue}, ${baseSat}%, ${baseLight - 6}%, ${grainAlpha})`);
      gradient.addColorStop(0.5, `hsla(${grainHue}, ${baseSat + 8}%, ${baseLight - 2}%, ${grainAlpha})`);
      gradient.addColorStop(1, `hsla(${grainHue}, ${baseSat}%, ${baseLight - 6}%, ${grainAlpha})`);
      ctx.strokeStyle = gradient;
      ctx.beginPath();
      const yStart = g.y;
      const wobble = Math.sin(performance.now() * 0.0004 * g.wobbleSpeed + g.wobble) * 1.5;
      ctx.moveTo(22, yStart + wobble);
      for (let x = 22; x < w - 20; x += 6) {
        const localWobble = Math.sin(x * 0.04 + g.wobble) * 2.4;
        ctx.lineTo(x, yStart + localWobble + wobble);
      }
      ctx.stroke();
    });

    // Chemistry spots — visible pigmentation/mineral infusion
    state.chemSpots.forEach(spot => {
      const alpha = spot.intensity * (chemistryDepth / 100);
      ctx.fillStyle = `hsla(${spot.hue}, 60%, 55%, ${alpha * 0.6})`;
      ctx.beginPath();
      ctx.arc(spot.x, spot.y, spot.r, 0, Math.PI * 2);
      ctx.fill();
    });

    // Tonal-quality glow — only present if loop intact (workshop) or carried (rebuild w/ continuity)
    if (toneQuality > 5) {
      const cx = w / 2, cy = h / 2;
      const r = Math.min(w, h) * 0.42;
      const grad = ctx.createRadialGradient(cx, cy, r * 0.2, cx, cy, r);
      const intensity = toneQuality / 100;
      grad.addColorStop(0, `hsla(45, 80%, 70%, ${intensity * 0.18})`);
      grad.addColorStop(0.6, `hsla(35, 70%, 50%, ${intensity * 0.08})`);
      grad.addColorStop(1, 'hsla(35, 70%, 50%, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);
    }

    // If scattered/forensic — show NMR-style scan lines
    if (scattered && state.detectionLevel > 0) {
      const scanY = ((performance.now() * 0.08) % h);
      ctx.strokeStyle = `hsla(190, 80%, 70%, 0.25)`;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, scanY);
      ctx.lineTo(w, scanY);
      ctx.stroke();

      // Detection markers — chemistry being read
      const detectFrac = state.detectionLevel / 100;
      const numMarkers = Math.floor(detectFrac * state.chemSpots.length);
      for (let i = 0; i < numMarkers; i++) {
        const spot = state.chemSpots[i];
        ctx.strokeStyle = `hsla(190, 80%, 75%, 0.55)`;
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.arc(spot.x, spot.y, spot.r + 4, 0, Math.PI * 2);
        ctx.stroke();
      }
    }
  }

  function spawnChemSpot() {
    const w = cWorkshop.width, h = cWorkshop.height;
    const palette = [
      { hue: 35, name: 'borax' },
      { hue: 200, name: 'zinc' },
      { hue: 25, name: 'copper' },
      { hue: 50, name: 'alum' },
      { hue: 220, name: 'lime' },
    ];
    const choice = palette[Math.floor(Math.random() * palette.length)];
    state.chemSpots.push({
      x: 30 + Math.random() * (w - 60),
      y: 30 + Math.random() * (h - 60),
      r: 3 + Math.random() * 6,
      hue: choice.hue + (Math.random() - 0.5) * 12,
      intensity: 0.5 + Math.random() * 0.5,
    });
    if (state.chemSpots.length > 60) state.chemSpots.shift();
  }

  function setMeter(el, value) {
    el.style.width = Math.max(0, Math.min(100, value)) + '%';
  }

  function setPhase(phase) {
    state.phase = phase;
    paneWorkshop.classList.toggle('dim', phase !== 'workshop');
    paneFossil.classList.toggle('dim', phase === 'workshop');
    paneRebuild.classList.toggle('dim', phase !== 'rebuild');
  }

  function closeWorkshop() {
    if (state.phase !== 'workshop') return;
    setPhase('fossil');
    yearFossil.textContent = state.fossilYear;
    btnClose.disabled = true;
    btnClose.classList.add('forensic-btn-disabled');
    btnRebuild.classList.remove('forensic-btn-disabled');
    rebuildReadout.textContent = 'detection in progress...';
    // Snapshot the workshop's final wood as the fossil
    state.fossilSnapshot = {
      chemistryDepth: state.chemistryDepth,
      toneQuality: state.toneQuality,
      grainCopy: JSON.parse(JSON.stringify(state.grain)),
      chemSpotsCopy: JSON.parse(JSON.stringify(state.chemSpots)),
    };
  }

  function attemptRebuild() {
    if (state.phase !== 'fossil' || state.detectionLevel < 60) return;
    setPhase('rebuild');
    btnRebuild.disabled = true;
    btnRebuild.classList.add('forensic-btn-disabled');

    // Chemistry can be reproduced from spec to a high degree
    state.rebuiltChemistry = state.detectionLevel * 0.95;

    // Tone quality depends on lineage continuity, not on detected chemistry
    const continuity = parseFloat(continuityInput.value) / 100;
    const toneRecovered = state.fossilSnapshot.toneQuality * (0.20 + continuity * 0.78);
    state.rebuiltTone = toneRecovered;

    // Build a new plank for the rebuild canvas
    const w = cRebuild.width, h = cRebuild.height;
    state.rebuildGrain = [];
    for (let i = 0; i < 28; i++) {
      state.rebuildGrain.push({
        y: 30 + i * 12 + (Math.random() - 0.5) * 4,
        wobble: Math.random() * Math.PI * 2,
        wobbleSpeed: 0.7 + Math.random() * 0.6,
      });
    }
    // Replicate detected chemistry (most of it)
    state.rebuildChemSpots = state.fossilSnapshot.chemSpotsCopy.map(s => ({
      ...s,
      x: s.x + (Math.random() - 0.5) * 8,
      y: s.y + (Math.random() - 0.5) * 8,
    }));

    if (continuity < 0.15) {
      rebuildReadout.textContent = 'Chemistry matched. Tone failed. The workshop is a fossil.';
    } else if (continuity < 0.55) {
      rebuildReadout.textContent = 'Partial recovery. Some plate-tuning intuition survives.';
    } else if (continuity < 0.9) {
      rebuildReadout.textContent = 'Most of the practice carried forward. Tone within reach.';
    } else {
      rebuildReadout.textContent = 'Lineage intact. The fossil was never the only record.';
    }
  }

  function reset() {
    state = {
      phase: 'workshop',
      workshopYear: 1665,
      chemistryDepth: 0,
      toneQuality: 0,
      loopIntegrity: 0,
      fossilYear: 1744,
      detectionLevel: 0,
      lineageRemaining: 0,
      rebuiltChemistry: 0,
      rebuiltTone: 0,
      grain: [],
      chemSpots: [],
      rebuildGrain: [],
      rebuildChemSpots: [],
      fossilSnapshot: null,
    };
    initGrain();
    setPhase('workshop');
    btnClose.disabled = false;
    btnClose.classList.remove('forensic-btn-disabled');
    btnRebuild.disabled = false;
    btnRebuild.classList.add('forensic-btn-disabled');
    rebuildReadout.textContent = 'awaiting detection';
    yearFossil.textContent = '–';
  }

  function tick() {
    // Phase 1 — workshop running
    if (state.phase === 'workshop') {
      state.workshopYear += 0.18;
      yearActive.textContent = Math.floor(state.workshopYear);

      // Loop is intact and improving
      state.loopIntegrity = Math.min(100, state.loopIntegrity + 0.5);

      // Chemistry depth slowly rises
      if (state.chemistryDepth < 100) {
        state.chemistryDepth += 0.55;
        if (Math.random() < 0.18) spawnChemSpot();
      }

      // Tone quality grows slowly with the loop — caps at chem-depth ceiling
      const ceiling = state.chemistryDepth * 0.92;
      if (state.toneQuality < ceiling) {
        state.toneQuality += 0.35;
      }

      drawWoodPlank(ctxWorkshop, cWorkshop, state.chemistryDepth, state.toneQuality, 0, false);
      // Fossil pane mirrors workshop until closure
      drawWoodPlank(ctxFossil, cFossil, state.chemistryDepth * 0.6, state.toneQuality * 0.4, 1, false);
      drawWoodPlank(ctxRebuild, cRebuild, 0, 0, 2, false);
    }

    // Phase 2 — workshop closed, time passes, detection rises
    if (state.phase === 'fossil') {
      state.fossilYear += 1.2;
      yearFossil.textContent = Math.floor(state.fossilYear);

      // Loop integrity decays based on continuity slider
      const continuity = parseFloat(continuityInput.value) / 100;
      const targetLoop = state.fossilSnapshot.toneQuality * 0; // dies without continuity
      state.loopIntegrity = Math.max(0, state.loopIntegrity - 0.4 * (1 - continuity));

      // Lineage remaining tracks continuity
      state.lineageRemaining = continuity * 100;

      // Detection level rises (instruments improve over time)
      if (state.detectionLevel < 95) {
        state.detectionLevel += 0.35;
      }

      // Update fossil canvas — wood ages, chemistry stays, tone fades unless continuity
      const tonePreserved = state.fossilSnapshot.toneQuality * continuity;
      drawWoodPlank(
        ctxFossil, cFossil,
        state.fossilSnapshot.chemistryDepth,
        tonePreserved,
        Math.min(1.5, (state.fossilYear - 1744) / 250),
        true
      );

      // Workshop pane fades — wood remains but loop-glow gone
      drawWoodPlank(ctxWorkshop, cWorkshop, state.chemistryDepth, state.toneQuality * 0.3, 0.5, false);
      drawWoodPlank(ctxRebuild, cRebuild, 0, 0, 2, false);

      // Enable rebuild button after enough detection
      if (state.detectionLevel > 60 && btnRebuild.classList.contains('forensic-btn-disabled') && !btnRebuild.disabled) {
        btnRebuild.classList.remove('forensic-btn-disabled');
        rebuildReadout.textContent = 'enough detected. ready to rebuild.';
      }
    }

    // Phase 3 — rebuild
    if (state.phase === 'rebuild') {
      const continuity = parseFloat(continuityInput.value) / 100;
      // Recompute target tone live so the slider is responsive
      const targetTone = state.fossilSnapshot.toneQuality * (0.20 + continuity * 0.78);
      state.rebuiltTone += (targetTone - state.rebuiltTone) * 0.05;

      // Save grain and spots, swap in the rebuild versions
      const savedGrain = state.grain;
      const savedSpots = state.chemSpots;
      state.grain = state.rebuildGrain;
      state.chemSpots = state.rebuildChemSpots;
      drawWoodPlank(ctxRebuild, cRebuild, state.rebuiltChemistry, state.rebuiltTone, 0.1, false);
      state.grain = savedGrain;
      state.chemSpots = savedSpots;

      // Keep the fossil and workshop panes static
      drawWoodPlank(
        ctxFossil, cFossil,
        state.fossilSnapshot.chemistryDepth,
        state.fossilSnapshot.toneQuality * continuity,
        Math.min(1.5, (state.fossilYear - 1744) / 250),
        true
      );
      drawWoodPlank(ctxWorkshop, cWorkshop, state.chemistryDepth, state.toneQuality * 0.3, 0.5, false);

      // Update phase 3 meters live
      setMeter(meterMatchChem, state.rebuiltChemistry);
      setMeter(meterMatchTone, state.rebuiltTone);

      // Update readout phrasing if continuity slider changes after rebuild
      if (continuity < 0.15) {
        rebuildReadout.textContent = 'Chemistry matched. Tone failed. The workshop is a fossil.';
      } else if (continuity < 0.55) {
        rebuildReadout.textContent = 'Partial recovery. Some plate-tuning intuition survives.';
      } else if (continuity < 0.9) {
        rebuildReadout.textContent = 'Most of the practice carried forward. Tone within reach.';
      } else {
        rebuildReadout.textContent = 'Lineage intact. The fossil was never the only record.';
      }
    }

    // Always update meters
    setMeter(meterChem, state.chemistryDepth);
    setMeter(meterTone, state.toneQuality);
    setMeter(meterLoop, state.loopIntegrity);
    setMeter(meterDetect, state.detectionLevel);
    setMeter(meterLineage, state.lineageRemaining);

    if (state.phase !== 'rebuild') {
      setMeter(meterMatchChem, state.rebuiltChemistry);
      setMeter(meterMatchTone, state.rebuiltTone);
    }

    requestAnimationFrame(tick);
  }

  // Input handlers
  continuityInput.addEventListener('input', () => {
    const v = continuityInput.value;
    continuityReadout.textContent = v + '%';
  });
  btnClose.addEventListener('click', closeWorkshop);
  btnRebuild.addEventListener('click', attemptRebuild);
  btnReset.addEventListener('click', reset);

  // Initial setup
  initGrain();
  setPhase('workshop');
  paneFossil.classList.add('dim');
  paneRebuild.classList.add('dim');
  btnRebuild.classList.add('forensic-btn-disabled');
  requestAnimationFrame(tick);
})();
