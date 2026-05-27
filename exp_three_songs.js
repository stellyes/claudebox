(function(){
  const sonoCanvas = document.getElementById('ts-sonogram');
  const sonoCtx = sonoCanvas.getContext('2d');
  const sonoTitle = document.getElementById('ts-sono-title');
  const sonoCaption = document.getElementById('ts-sono-caption');
  const siteButtons = document.querySelectorAll('.ts-sono-controls .ts-btn');
  const mapSites = {
    berkeley: document.getElementById('site-berkeley'),
    inverness: document.getElementById('site-inverness'),
    sunset: document.getElementById('site-sunset')
  };

  const dialects = {
    berkeley: {
      name: 'Berkeley',
      caption: 'Opening whistle ~4.0 kHz, descending buzzy trill, thin terminal note.',
      color: '#5fb37a',
      // [type, freqStart, freqEnd, duration_ms, density]
      // type: 0 whistle, 1 trill, 2 buzz, 3 note
      segments: [
        { type: 0, fStart: 4.0, fEnd: 4.0, dur: 380, density: 1 },
        { type: 0, fStart: 4.0, fEnd: 3.4, dur: 220, density: 1 },
        { type: 2, fStart: 3.6, fEnd: 2.8, dur: 520, density: 16 },
        { type: 3, fStart: 5.2, fEnd: 5.0, dur: 140, density: 1 }
      ]
    },
    inverness: {
      name: 'Inverness',
      caption: 'Longer opening whistle, faster trill at higher frequency, no terminal note.',
      color: '#d4a44c',
      segments: [
        { type: 0, fStart: 4.2, fEnd: 4.2, dur: 620, density: 1 },
        { type: 0, fStart: 4.2, fEnd: 3.8, dur: 180, density: 1 },
        { type: 1, fStart: 4.4, fEnd: 3.6, dur: 460, density: 22 }
      ]
    },
    sunset: {
      name: 'Sunset Beach',
      caption: 'Whistle replaced by discrete stepped notes; no trill.',
      color: '#7da3d4',
      segments: [
        { type: 0, fStart: 3.8, fEnd: 3.8, dur: 280, density: 1 },
        { type: 3, fStart: 4.6, fEnd: 4.6, dur: 90, density: 1 },
        { type: 3, fStart: 4.2, fEnd: 4.2, dur: 90, density: 1 },
        { type: 3, fStart: 3.6, fEnd: 3.6, dur: 90, density: 1 },
        { type: 3, fStart: 5.0, fEnd: 5.0, dur: 90, density: 1 },
        { type: 3, fStart: 4.4, fEnd: 4.4, dur: 90, density: 1 }
      ]
    }
  };

  function drawSonogram(siteKey) {
    const w = sonoCanvas.width;
    const h = sonoCanvas.height;
    sonoCtx.fillStyle = '#0c1014';
    sonoCtx.fillRect(0, 0, w, h);
    // axes
    const padL = 40, padR = 12, padT = 12, padB = 30;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;
    // Y-axis ticks (kHz, 2-7)
    sonoCtx.strokeStyle = '#2a3640';
    sonoCtx.lineWidth = 1;
    sonoCtx.fillStyle = '#5f6b58';
    sonoCtx.font = '10px Inter, sans-serif';
    sonoCtx.textAlign = 'right';
    const fMin = 2.0, fMax = 7.0;
    for (let f = 2; f <= 7; f++) {
      const y = padT + plotH * (1 - (f - fMin) / (fMax - fMin));
      sonoCtx.beginPath();
      sonoCtx.moveTo(padL, y);
      sonoCtx.lineTo(w - padR, y);
      sonoCtx.strokeStyle = f === 2 || f === 7 ? '#2a3640' : '#1b2530';
      sonoCtx.stroke();
      sonoCtx.fillText(f + ' kHz', padL - 4, y + 3);
    }
    // X-axis tick (time)
    sonoCtx.textAlign = 'center';
    const totalDur = dialects[siteKey].segments.reduce((s, seg) => s + seg.dur, 0);
    sonoCtx.fillText('0', padL, h - padB + 14);
    sonoCtx.fillText((totalDur/1000).toFixed(2) + ' s', w - padR, h - padB + 14);
    sonoCtx.fillText('time', padL + plotW/2, h - padB + 14);

    // Plot segments
    const dialect = dialects[siteKey];
    let xCursor = padL;
    const xScale = plotW / totalDur;

    dialect.segments.forEach(seg => {
      const segW = seg.dur * xScale;
      const y1 = padT + plotH * (1 - (seg.fStart - fMin) / (fMax - fMin));
      const y2 = padT + plotH * (1 - (seg.fEnd - fMin) / (fMax - fMin));

      if (seg.type === 0) {
        // smooth whistle line
        sonoCtx.strokeStyle = dialect.color;
        sonoCtx.lineWidth = 3.5;
        sonoCtx.beginPath();
        sonoCtx.moveTo(xCursor, y1);
        sonoCtx.lineTo(xCursor + segW, y2);
        sonoCtx.stroke();
      } else if (seg.type === 1) {
        // trill: alternating short notes
        sonoCtx.strokeStyle = dialect.color;
        sonoCtx.lineWidth = 2.2;
        const n = seg.density;
        for (let i = 0; i < n; i++) {
          const xs = xCursor + (segW * i) / n;
          const xe = xs + (segW * 0.65) / n;
          const t = i / Math.max(1, n - 1);
          const fy = y1 + (y2 - y1) * t;
          const osc = ((i % 2) === 0 ? -1 : 1) * 8;
          sonoCtx.beginPath();
          sonoCtx.moveTo(xs, fy - osc);
          sonoCtx.lineTo(xe, fy + osc);
          sonoCtx.stroke();
        }
      } else if (seg.type === 2) {
        // buzz: dense vertical hash with downward slope
        sonoCtx.strokeStyle = dialect.color;
        sonoCtx.lineWidth = 1;
        const n = seg.density;
        for (let i = 0; i < n; i++) {
          const xs = xCursor + (segW * i) / n;
          const t = i / Math.max(1, n - 1);
          const fy = y1 + (y2 - y1) * t;
          sonoCtx.beginPath();
          sonoCtx.moveTo(xs, fy - 14);
          sonoCtx.lineTo(xs, fy + 14);
          sonoCtx.stroke();
        }
      } else if (seg.type === 3) {
        // discrete note: solid short rectangle at frequency
        sonoCtx.fillStyle = dialect.color;
        sonoCtx.fillRect(xCursor + segW * 0.1, y1 - 3, segW * 0.8, 6);
      }
      xCursor += segW;
    });

    sonoTitle.textContent = dialect.name;
    sonoCaption.textContent = dialect.caption;
  }

  function setActiveSite(siteKey) {
    siteButtons.forEach(b => {
      b.classList.toggle('ts-btn-active', b.dataset.site === siteKey);
    });
    Object.keys(mapSites).forEach(k => {
      mapSites[k].classList.toggle('active', k === siteKey);
    });
    drawSonogram(siteKey);
  }

  siteButtons.forEach(b => {
    b.addEventListener('click', () => setActiveSite(b.dataset.site));
  });
  Object.keys(mapSites).forEach(k => {
    mapSites[k].addEventListener('click', () => setActiveSite(k));
  });

  // --- Simulator ---
  const simCanvas = document.getElementById('ts-sim');
  const simCtx = simCanvas.getContext('2d');
  const dispInput = document.getElementById('ts-disp');
  const mutInput = document.getElementById('ts-mut');
  const tmplInput = document.getElementById('ts-tmpl');
  const dispVal = document.getElementById('ts-disp-val');
  const mutVal = document.getElementById('ts-mut-val');
  const tmplVal = document.getElementById('ts-tmpl-val');
  const runBtn = document.getElementById('ts-run');
  const resetBtn = document.getElementById('ts-reset');

  const NCELLS = 24;
  const NGEN = 80;

  // Each "song" is a scalar in [0,1] representing trill rate or frequency.
  // Three founder attractors: 0.18 (Inverness-like), 0.50 (Berkeley-like), 0.82 (Sunset-like)
  const ATTRACTORS = [0.18, 0.50, 0.82];

  function colorForValue(v) {
    // smooth interpolation: closer to which attractor wins the color, but mix
    const r = 0xd4 * weight(v, 0.18) + 0x5f * weight(v, 0.50) + 0x7d * weight(v, 0.82);
    const g = 0xa4 * weight(v, 0.18) + 0xb3 * weight(v, 0.50) + 0xa3 * weight(v, 0.82);
    const b = 0x4c * weight(v, 0.18) + 0x7a * weight(v, 0.50) + 0xd4 * weight(v, 0.82);
    return 'rgb(' + Math.round(r) + ',' + Math.round(g) + ',' + Math.round(b) + ')';
  }
  function weight(v, a) {
    const d = Math.abs(v - a);
    const w = Math.exp(-d * 18);
    return w;
  }
  function normalizeWeights(v) {
    const ws = ATTRACTORS.map(a => weight(v, a));
    const s = ws.reduce((x,y)=>x+y,0);
    return ws.map(w => w/s);
  }

  function initPopulation() {
    // Three regions, three founder dialects
    const pop = new Array(NCELLS);
    for (let i = 0; i < NCELLS; i++) {
      if (i < 8) pop[i] = ATTRACTORS[0] + (Math.random() - 0.5) * 0.02;
      else if (i < 16) pop[i] = ATTRACTORS[1] + (Math.random() - 0.5) * 0.02;
      else pop[i] = ATTRACTORS[2] + (Math.random() - 0.5) * 0.02;
    }
    return pop;
  }

  function stepGeneration(pop, dispersal, mutation, tmplWidth) {
    const next = new Array(NCELLS);
    for (let i = 0; i < NCELLS; i++) {
      // pick a random tutor within dispersal radius
      const lo = Math.max(0, i - dispersal);
      const hi = Math.min(NCELLS - 1, i + dispersal);
      const tutorIdx = lo + Math.floor(Math.random() * (hi - lo + 1));
      let val = pop[tutorIdx] + (Math.random() - 0.5) * mutation * 2;
      // species template prunes: clamp toward nearest attractor if outside tmplWidth
      const nearest = ATTRACTORS.reduce((best, a) => Math.abs(val - a) < Math.abs(val - best) ? a : best, ATTRACTORS[0]);
      if (Math.abs(val - nearest) > tmplWidth) {
        // pull strongly toward template
        val = nearest + (val - nearest) * (tmplWidth / Math.abs(val - nearest)) * 0.4;
      }
      val = Math.max(0, Math.min(1, val));
      next[i] = val;
    }
    return next;
  }

  function drawSimRow(pop, gen) {
    const w = simCanvas.width;
    const h = simCanvas.height;
    const cellW = w / NCELLS;
    const rowH = h / NGEN;
    const y = gen * rowH;
    for (let i = 0; i < NCELLS; i++) {
      simCtx.fillStyle = colorForValue(pop[i]);
      simCtx.fillRect(i * cellW, y, cellW, rowH + 0.5);
    }
  }

  function runSim() {
    simCtx.fillStyle = '#0c1014';
    simCtx.fillRect(0, 0, simCanvas.width, simCanvas.height);
    let pop = initPopulation();
    const dispersal = parseInt(dispInput.value, 10);
    const mutation = parseInt(mutInput.value, 10) / 100;
    const tmplWidth = parseInt(tmplInput.value, 10) / 100;
    drawSimRow(pop, 0);
    let gen = 0;
    function tick() {
      gen++;
      if (gen >= NGEN) return;
      pop = stepGeneration(pop, dispersal, mutation, tmplWidth);
      drawSimRow(pop, gen);
      if (gen < NGEN - 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  function updateLabels() {
    dispVal.textContent = dispInput.value;
    mutVal.textContent = (parseInt(mutInput.value, 10) / 100).toFixed(2);
    tmplVal.textContent = (parseInt(tmplInput.value, 10) / 100).toFixed(2);
  }

  dispInput.addEventListener('input', updateLabels);
  mutInput.addEventListener('input', updateLabels);
  tmplInput.addEventListener('input', updateLabels);
  runBtn.addEventListener('click', runSim);
  resetBtn.addEventListener('click', () => {
    simCtx.fillStyle = '#0c1014';
    simCtx.fillRect(0, 0, simCanvas.width, simCanvas.height);
    drawSimRow(initPopulation(), 0);
  });

  // initial paint
  setActiveSite('berkeley');
  updateLabels();
  drawSimRow(initPopulation(), 0);
})();
