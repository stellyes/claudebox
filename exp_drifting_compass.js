(function() {
  const canvas = document.getElementById('compass-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width;
  const H = canvas.height;

  const scarcityInput = document.getElementById('scarcity');
  const genInput = document.getElementById('generations');
  const scarcityReadout = document.getElementById('scarcity-readout');
  const genReadout = document.getElementById('gen-readout');
  const resetBtn = document.getElementById('reset-btn');

  // Field setup: a gradient that points toward an optimal direction.
  // Truth: optimal heading is "south" — angle = pi/2 (90 deg, downward on canvas).
  const TRUE_HEADING = Math.PI / 2;

  // The bird's inherited bearing — accumulates drift when scarcity is low.
  // Each generation: if scarcity > threshold, the wrong-headed birds die,
  // pulling the population mean back toward TRUE_HEADING. If scarcity is low,
  // mutation/drift accumulates without selection.
  let inheritedBearing = TRUE_HEADING;
  let drift = 0;

  function readState() {
    return {
      scarcity: parseInt(scarcityInput.value, 10) / 100,
      generations: parseInt(genInput.value, 10),
    };
  }

  // Simulate inherited bearing across N generations given current scarcity.
  function computeBearing(scarcity, generations) {
    let bearing = TRUE_HEADING;
    let driftMagnitude = 0;
    // Selection strength scales with scarcity. Mutation is constant per generation.
    const mutationPerGen = 0.018; // radians
    const selectionStrength = scarcity; // 0..1
    let rngState = 12345;
    function lcg() {
      rngState = (rngState * 1103515245 + 12345) & 0x7fffffff;
      return (rngState / 0x7fffffff) - 0.5;
    }
    for (let i = 0; i < generations; i++) {
      const mutation = lcg() * mutationPerGen * 2;
      driftMagnitude += mutationPerGen * mutationPerGen;
      bearing += mutation;
      // Selection pulls back toward TRUE_HEADING with strength proportional to scarcity.
      const error = bearing - TRUE_HEADING;
      bearing -= error * selectionStrength * 0.42;
      driftMagnitude *= (1 - selectionStrength * 0.42);
    }
    return {
      bearing,
      spread: Math.sqrt(Math.max(0, driftMagnitude)),
    };
  }

  function drawCompass() {
    const state = readState();
    scarcityReadout.textContent = Math.round(state.scarcity * 100) + '%';
    genReadout.textContent = state.generations;

    ctx.clearRect(0, 0, W, H);

    // Background gradient — visualizes the food gradient. When scarcity is high,
    // the gradient is sharp; when scarcity is low, food is uniform.
    const gradX = W / 2;
    for (let y = 0; y < H; y++) {
      const t = y / H;
      // Food density: high scarcity = strong south gradient; low scarcity = flat.
      const sharpness = state.scarcity;
      const density = sharpness * t + (1 - sharpness) * 0.5;
      ctx.fillStyle = 'rgba(' + Math.floor(60 + density * 40) + ',' +
        Math.floor(50 + density * 60) + ',' +
        Math.floor(40 + density * 30) + ',1)';
      ctx.fillRect(0, y, W, 1);
    }

    // Compass center
    const cx = W / 2;
    const cy = H / 2;
    const R = Math.min(W, H) * 0.34;

    // Compass ring
    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(216, 212, 206, 0.25)';
    ctx.lineWidth = 1.2;
    ctx.stroke();

    // Compass marks
    ctx.font = '12px "JetBrains Mono", Menlo, monospace';
    ctx.fillStyle = 'rgba(216, 212, 206, 0.45)';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const marks = [
      { angle: -Math.PI / 2, label: 'N' },
      { angle: 0, label: 'E' },
      { angle: Math.PI / 2, label: 'S' },
      { angle: Math.PI, label: 'W' },
    ];
    marks.forEach(function(m) {
      const x = cx + Math.cos(m.angle) * (R + 18);
      const y = cy + Math.sin(m.angle) * (R + 18);
      ctx.fillText(m.label, x, y);
    });

    // Optimal direction (toward food)
    drawArrow(cx, cy, TRUE_HEADING, R * 0.95, 'rgba(111, 155, 211, 0.85)', 2);

    // Compute inherited bearing
    const result = computeBearing(state.scarcity, state.generations);
    const bearing = result.bearing;
    const spread = Math.min(1.4, result.spread * 4);

    // Spread cone — shows the population variance (calibration loss)
    if (spread > 0.02) {
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.arc(cx, cy, R * 0.92, bearing - spread, bearing + spread);
      ctx.closePath();
      ctx.fillStyle = 'rgba(138, 122, 94, 0.22)';
      ctx.fill();
    }

    // Inherited bearing arrow
    drawArrow(cx, cy, bearing, R * 0.92, 'rgba(212, 169, 106, 0.95)', 3);

    // Bird heading (jittered sample from inherited)
    const birdJitter = (Math.random() - 0.5) * spread * 1.6;
    const birdAngle = bearing + birdJitter;
    drawArrow(cx, cy, birdAngle, R * 0.7, 'rgba(212, 169, 106, 0.6)', 1.8);

    // Status text
    ctx.font = '13px "Inter", system-ui, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = 'rgba(216, 212, 206, 0.7)';
    ctx.fillText('Scarcity: ' + Math.round(state.scarcity * 100) + '%', 24, 32);
    ctx.fillText('Generations: ' + state.generations, 24, 52);
    const errorDeg = Math.abs((bearing - TRUE_HEADING) * 180 / Math.PI);
    ctx.fillText('Bearing error: ' + errorDeg.toFixed(1) + '°', 24, 72);
    ctx.fillText('Population spread: ±' + (spread * 180 / Math.PI).toFixed(1) + '°',
      24, 92);

    if (state.scarcity < 0.18 && state.generations > 60) {
      ctx.fillStyle = 'rgba(212, 169, 106, 0.85)';
      ctx.font = 'italic 13px "Inter", system-ui, sans-serif';
      ctx.fillText('The compass has gone vestigial.', 24, H - 24);
    } else if (state.scarcity > 0.7) {
      ctx.fillStyle = 'rgba(111, 155, 211, 0.75)';
      ctx.font = 'italic 13px "Inter", system-ui, sans-serif';
      ctx.fillText('Selection is sharpening the bearing.', 24, H - 24);
    }
  }

  function drawArrow(cx, cy, angle, length, color, width) {
    const tipX = cx + Math.cos(angle) * length;
    const tipY = cy + Math.sin(angle) * length;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(tipX, tipY);
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    ctx.lineCap = 'round';
    ctx.stroke();
    // Arrowhead
    const headSize = 10;
    ctx.beginPath();
    ctx.moveTo(tipX, tipY);
    ctx.lineTo(
      tipX - Math.cos(angle - 0.4) * headSize,
      tipY - Math.sin(angle - 0.4) * headSize
    );
    ctx.lineTo(
      tipX - Math.cos(angle + 0.4) * headSize,
      tipY - Math.sin(angle + 0.4) * headSize
    );
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
  }

  scarcityInput.addEventListener('input', drawCompass);
  genInput.addEventListener('input', drawCompass);
  resetBtn.addEventListener('click', function() {
    scarcityInput.value = 80;
    genInput.value = 0;
    drawCompass();
  });

  // Animate slight bird jitter
  let lastFrame = 0;
  function animate(t) {
    if (t - lastFrame > 200) {
      drawCompass();
      lastFrame = t;
    }
    requestAnimationFrame(animate);
  }
  drawCompass();
  requestAnimationFrame(animate);
})();
