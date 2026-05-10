(function () {
  'use strict';

  const slider = document.getElementById('vardiag-slider');
  const readout = document.getElementById('vardiag-readout');
  const diagText = document.getElementById('vardiag-diag-text');

  const factoryCanvas = document.getElementById('vardiag-c-factory');
  const populationCanvas = document.getElementById('vardiag-c-population');
  const swarmCanvas = document.getElementById('vardiag-c-swarm');

  const outFactory = document.getElementById('vardiag-out-factory');
  const outPopulation = document.getElementById('vardiag-out-population');
  const outSwarm = document.getElementById('vardiag-out-swarm');

  // Curve generators (output 0..1 normalized for easy plotting)
  function factoryCurve(v) {
    // Defect rate: monotonic increasing with variance.
    // Six-sigma factory: zero variance = zero defects, max variance = saturated defects.
    return 1 - Math.exp(-3.5 * v);
  }

  function populationCurve(v) {
    // Mean fitness as function of S allele frequency under malaria pressure.
    // Inverted U with peak around v ~= 0.18 (realistic for high-malaria regions).
    // Off-peak: SS homozygote disease at high v, no malaria protection at low v.
    const peak = 0.18;
    const width = 0.28;
    const x = (v - peak) / width;
    const fitness = 0.55 + 0.42 * Math.exp(-x * x * 1.6);
    return Math.max(0, Math.min(1, fitness));
  }

  function swarmCurve(v) {
    // Coverage rate inverted-U.
    // Zero variance: brittle homogeneous swarm, single hypothesis.
    // High variance: uncoordinated noise.
    // Peak around v ~= 0.45.
    const peak = 0.45;
    const width = 0.28;
    const x = (v - peak) / width;
    const coverage = 0.18 + 0.78 * Math.exp(-x * x);
    return Math.max(0, Math.min(1, coverage));
  }

  // Drawing helpers
  function drawCurve(canvas, curveFn, currentX, isMonotonic, label) {
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const padL = 38;
    const padR = 16;
    const padT = 14;
    const padB = 30;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;

    // Axes
    ctx.strokeStyle = 'rgba(255,255,255,0.18)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padL, padT);
    ctx.lineTo(padL, padT + plotH);
    ctx.lineTo(padL + plotW, padT + plotH);
    ctx.stroke();

    // Y axis label
    ctx.fillStyle = 'rgba(184,178,159,0.6)';
    ctx.font = '10px "JetBrains Mono", monospace';
    ctx.fillText('1.0', padL - 30, padT + 6);
    ctx.fillText('0.0', padL - 30, padT + plotH);
    ctx.fillText('low variance', padL - 6, padT + plotH + 14);
    ctx.textAlign = 'right';
    ctx.fillText('high variance', padL + plotW, padT + plotH + 14);
    ctx.textAlign = 'start';

    // The curve
    const samples = 80;
    ctx.beginPath();
    for (let i = 0; i <= samples; i++) {
      const x = i / samples;
      const y = curveFn(x);
      const px = padL + x * plotW;
      const py = padT + (1 - y) * plotH;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.strokeStyle = isMonotonic ? '#9aa6b8' : '#e8c97a';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Mark "Six Sigma's preferred answer" (zero variance) on each panel
    const sigmaPx = padL + 0 * plotW;
    const sigmaY = curveFn(0);
    ctx.fillStyle = 'rgba(154,166,184,0.5)';
    ctx.beginPath();
    ctx.arc(sigmaPx, padT + (1 - sigmaY) * plotH, 3, 0, Math.PI * 2);
    ctx.fill();

    // Mark optimum (max of curve) for non-monotonic regimes
    if (!isMonotonic) {
      let maxY = -1;
      let maxX = 0;
      for (let i = 0; i <= samples; i++) {
        const x = i / samples;
        const y = curveFn(x);
        if (y > maxY) { maxY = y; maxX = x; }
      }
      const optPx = padL + maxX * plotW;
      const optPy = padT + (1 - maxY) * plotH;
      ctx.strokeStyle = 'rgba(232,201,122,0.5)';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(optPx, padT + plotH);
      ctx.lineTo(optPx, optPy);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // Current X marker
    const cx = padL + currentX * plotW;
    const cy = padT + (1 - curveFn(currentX)) * plotH;

    ctx.strokeStyle = 'rgba(255,255,255,0.25)';
    ctx.beginPath();
    ctx.moveTo(cx, padT);
    ctx.lineTo(cx, padT + plotH);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(cx, cy, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#1a1814';
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }

  function update() {
    const v = parseFloat(slider.value);
    readout.textContent = v.toFixed(2);

    const fVal = factoryCurve(v);
    const pVal = populationCurve(v);
    const sVal = swarmCurve(v);

    drawCurve(factoryCanvas, factoryCurve, v, true);
    drawCurve(populationCanvas, populationCurve, v, false);
    drawCurve(swarmCanvas, swarmCurve, v, false);

    outFactory.textContent = (fVal * 100).toFixed(1) + '% defective';
    outPopulation.textContent = (pVal * 100).toFixed(1) + '% of max';
    outSwarm.textContent = (sVal * 100).toFixed(1) + '% of max';

    // Diagnostic
    const factoryHappy = v < 0.05;
    const populationOptimum = Math.abs(v - 0.18) < 0.06;
    const swarmOptimum = Math.abs(v - 0.45) < 0.08;

    let msg;
    if (factoryHappy) {
      msg = 'Factory regime is winning. Population fitness has collapsed to the no-malaria-protection floor; the swarm has one hypothesis and no way to test it. Six Sigma’s answer is correct only here.';
    } else if (populationOptimum && !swarmOptimum) {
      msg = 'Population sits near its balanced-polymorphism peak. The factory is producing defects; the swarm is under-heterogeneous. The optimal variance is system-specific.';
    } else if (swarmOptimum && !populationOptimum) {
      msg = 'Swarm sits near its heterogeneity optimum. The factory is producing defects; the population has overshot the S-allele equilibrium and is losing to sickle-cell anemia.';
    } else if (populationOptimum && swarmOptimum) {
      msg = 'Population and swarm both near their optima. Factory loses. There is no setting of this slider that pleases all three regimes — that is the point.';
    } else if (v > 0.85) {
      msg = 'High variance everywhere. Factory: defective. Population: collapsing into sickle-cell anemia. Swarm: uncoordinated noise. Variance is not free at any regime.';
    } else {
      msg = 'In between. Factory cost is climbing. Population and swarm are off-optimum but functional. Most real systems live in this band, never exactly where any single methodology wants them.';
    }
    diagText.textContent = msg;
  }

  slider.addEventListener('input', update);
  update();
})();
