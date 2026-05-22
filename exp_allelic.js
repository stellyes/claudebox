(function() {
  const doseInput = document.getElementById('dose');
  const doseVal = document.getElementById('dose-val');
  const periodOut = document.getElementById('period-out');
  const etherOut = document.getElementById('ether-out');
  const periodPlot = document.getElementById('period-plot');
  const periodHist = document.getElementById('period-hist');
  const etherPlot = document.getElementById('ether-plot');
  const etherHist = document.getElementById('ether-hist');
  const reroll = document.getElementById('reroll');
  const presetButtons = document.querySelectorAll('.allelic-presets button');

  function mulberry32(seed) {
    return function() {
      let t = seed += 0x6D2B79F5;
      t = Math.imul(t ^ t >>> 15, t | 1);
      t ^= t + Math.imul(t ^ t >>> 7, t | 61);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  let cohortSeed = 7;
  let cohortPeriods = [];
  let cohortEther = [];

  function dosageToPeriod(dose) {
    // Calibrated so dose 1.0 -> 24h, dose 0.79 -> 19h, dose 1.17 -> 28h.
    return 24 * dose;
  }

  function dosageToEther(dose) {
    // Below threshold (loss of K-channel function), fly shakes under ether.
    // Output is binary: phenotype is yes/no regardless of dose magnitude.
    return dose < 0.85 ? 1 : 0;
  }

  function buildCohort() {
    const rng = mulberry32(cohortSeed);
    cohortPeriods = [];
    cohortEther = [];
    for (let i = 0; i < 240; i++) {
      // Each fly has dose noise around the slider value.
      // Plus measurement noise on period.
      cohortPeriods.push((rng() - 0.5)); // store individual noise; resolve later
      cohortEther.push(rng() < 0.5 ? -1 : 1); // sign of individual variance
    }
  }
  buildCohort();

  function drawPeriodTrace(dose) {
    const ctx = periodPlot.getContext('2d');
    const w = periodPlot.width;
    const h = periodPlot.height;
    ctx.clearRect(0, 0, w, h);

    const period = dosageToPeriod(dose);
    const days = 7;
    const totalHours = days * 24;
    const rng = mulberry32(101);

    // Draw axis
    ctx.strokeStyle = 'rgba(180,160,100,0.18)';
    ctx.lineWidth = 1;
    for (let d = 0; d <= days; d++) {
      const x = (d * 24 / totalHours) * w;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
    ctx.fillStyle = '#6e6a5a';
    ctx.font = '10px JetBrains Mono, monospace';
    for (let d = 1; d <= days; d++) {
      const x = (d * 24 / totalHours) * w;
      ctx.fillText('d' + d, x - 8, h - 3);
    }

    // Draw activity trace
    const arrhythmic = dose < 0.6;
    ctx.strokeStyle = '#d4af37';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    let lastY = h / 2;
    for (let i = 0; i < w; i++) {
      const t = (i / w) * totalHours;
      let activity;
      if (arrhythmic) {
        activity = (rng() - 0.5) * 0.8 + Math.sin(t * 2 * Math.PI / 6) * 0.1;
      } else {
        const phase = (t / period) * 2 * Math.PI;
        const base = Math.max(0, Math.sin(phase));
        activity = base * base * 0.85 + (rng() - 0.5) * 0.12;
      }
      const y = h - 12 - activity * (h - 30);
      if (i === 0) ctx.moveTo(i, y);
      else ctx.lineTo(i, y);
      lastY = y;
    }
    ctx.stroke();

    // Period readout
    periodOut.textContent = arrhythmic ? 'arrhythmic' : period.toFixed(2);
  }

  function drawPeriodHist(dose) {
    const ctx = periodHist.getContext('2d');
    const w = periodHist.width;
    const h = periodHist.height;
    ctx.clearRect(0, 0, w, h);

    const bins = 50;
    const minP = 15, maxP = 32;
    const counts = new Array(bins).fill(0);
    const meanP = dosageToPeriod(dose);
    const arrhythmic = dose < 0.6;

    for (let i = 0; i < cohortPeriods.length; i++) {
      let p;
      if (arrhythmic) {
        // Spread broadly when arrhythmic
        p = meanP + cohortPeriods[i] * 14;
      } else {
        p = meanP + cohortPeriods[i] * 1.2;
      }
      if (p < minP || p > maxP) continue;
      const b = Math.floor((p - minP) / (maxP - minP) * bins);
      if (b >= 0 && b < bins) counts[b]++;
    }
    const maxC = Math.max(...counts, 1);

    // axis
    ctx.strokeStyle = 'rgba(180,160,100,0.18)';
    ctx.beginPath();
    ctx.moveTo(0, h - 18);
    ctx.lineTo(w, h - 18);
    ctx.stroke();

    // bars
    const barW = w / bins;
    ctx.fillStyle = '#d4af37';
    for (let b = 0; b < bins; b++) {
      const barH = (counts[b] / maxC) * (h - 24);
      ctx.fillRect(b * barW + 0.5, h - 18 - barH, barW - 1, barH);
    }
    // x-axis labels
    ctx.fillStyle = '#6e6a5a';
    ctx.font = '10px JetBrains Mono, monospace';
    for (let hh = minP; hh <= maxP; hh += 4) {
      const x = (hh - minP) / (maxP - minP) * w;
      ctx.fillText(hh + 'h', x - 8, h - 4);
    }
    // mean marker
    const xMean = (Math.min(maxP, Math.max(minP, meanP)) - minP) / (maxP - minP) * w;
    if (!arrhythmic) {
      ctx.strokeStyle = '#e8e0c0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(xMean, 4);
      ctx.lineTo(xMean, h - 18);
      ctx.stroke();
    }
  }

  function drawEtherTrace(dose) {
    const ctx = etherPlot.getContext('2d');
    const w = etherPlot.width;
    const h = etherPlot.height;
    ctx.clearRect(0, 0, w, h);

    const shakes = dosageToEther(dose);
    const rng = mulberry32(303);

    // grid
    ctx.strokeStyle = 'rgba(180,160,100,0.18)';
    for (let s = 0; s <= 6; s++) {
      const x = (s / 6) * w;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
    ctx.fillStyle = '#6e6a5a';
    ctx.font = '10px JetBrains Mono, monospace';
    for (let s = 1; s <= 6; s++) {
      const x = (s / 6) * w;
      ctx.fillText(s + 's', x - 6, h - 3);
    }

    // EMG-like trace
    ctx.strokeStyle = shakes ? '#d4af37' : 'rgba(180,160,100,0.32)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let i = 0; i < w; i++) {
      const t = (i / w) * 6;
      let v;
      if (shakes) {
        const burst = Math.sin(t * 22) * 0.55 + Math.sin(t * 11) * 0.2;
        v = burst + (rng() - 0.5) * 0.08;
      } else {
        v = (rng() - 0.5) * 0.04;
      }
      const y = h / 2 - v * (h / 2 - 14);
      if (i === 0) ctx.moveTo(i, y);
      else ctx.lineTo(i, y);
    }
    ctx.stroke();

    etherOut.textContent = shakes ? 'shakes (mutant)' : 'no shake (wild-type)';
  }

  function drawEtherHist(dose) {
    const ctx = etherHist.getContext('2d');
    const w = etherHist.width;
    const h = etherHist.height;
    ctx.clearRect(0, 0, w, h);

    let yesCount = 0, noCount = 0;
    for (let i = 0; i < cohortEther.length; i++) {
      const noisyDose = dose + cohortEther[i] * 0.03;
      if (noisyDose < 0.85) yesCount++;
      else noCount++;
    }
    const maxC = Math.max(yesCount, noCount, 1);

    ctx.strokeStyle = 'rgba(180,160,100,0.18)';
    ctx.beginPath();
    ctx.moveTo(0, h - 22);
    ctx.lineTo(w, h - 22);
    ctx.stroke();

    const barW = w * 0.32;
    const gap = w * 0.06;
    const startX = (w - 2 * barW - gap) / 2;

    // bar 1: shakes
    let bh = (yesCount / maxC) * (h - 32);
    ctx.fillStyle = yesCount > 0 ? '#d4af37' : 'rgba(180,160,100,0.3)';
    ctx.fillRect(startX, h - 22 - bh, barW, bh);
    ctx.fillStyle = '#b0a890';
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillText('shakes', startX + barW / 2 - 22, h - 8);
    ctx.fillText(yesCount.toString(), startX + barW / 2 - 8, h - 26 - bh);

    // bar 2: no shake
    bh = (noCount / maxC) * (h - 32);
    ctx.fillStyle = noCount > 0 ? '#d4af37' : 'rgba(180,160,100,0.3)';
    ctx.fillRect(startX + barW + gap, h - 22 - bh, barW, bh);
    ctx.fillStyle = '#b0a890';
    ctx.fillText('no shake', startX + barW + gap + barW / 2 - 26, h - 8);
    ctx.fillText(noCount.toString(), startX + barW + gap + barW / 2 - 8, h - 26 - bh);
  }

  function update() {
    const dose = parseFloat(doseInput.value);
    doseVal.textContent = dose.toFixed(2);
    drawPeriodTrace(dose);
    drawPeriodHist(dose);
    drawEtherTrace(dose);
    drawEtherHist(dose);
  }

  doseInput.addEventListener('input', update);
  presetButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      doseInput.value = btn.dataset.dose;
      update();
    });
  });
  reroll.addEventListener('click', () => {
    cohortSeed = Math.floor(Math.random() * 1e9);
    buildCohort();
    update();
  });

  update();
})();
