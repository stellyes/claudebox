(function () {
  const N = 52;

  // Bayer-Diaconis 1992 Table 1 values for n=52, GSR riffle.
  // d_TV(k) for k = 0..15. k=0 is identity (distance 1). Values for k>=12 extrapolated by halving.
  const BD_TV = [
    1.000, 1.000, 1.000, 1.000, 1.000,
    0.924, 0.614, 0.334, 0.167, 0.085,
    0.043, 0.021, 0.010, 0.005, 0.002, 0.001,
  ];

  function verdictFor(tv) {
    if (tv >= 0.95) return "structure intact";
    if (tv >= 0.5)  return "still distinguishable";
    if (tv >= 0.1)  return "approaching uniform";
    if (tv >= 0.02) return "indistinguishable to most tests";
    return "indistinguishable";
  }

  // mulberry32 seeded PRNG
  function mulberry32(seed) {
    let s = seed >>> 0;
    return function () {
      s = (s + 0x6D2B79F5) | 0;
      let t = s;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // Gilbert-Shannon-Reeds riffle shuffle.
  // Cut size from Binomial(n, 1/2). Then interleave: at each step,
  // draw the next card from the top of pile A with prob a/(a+b),
  // else from B. This preserves the GSR distribution.
  function riffleGSR(deck, rng) {
    const n = deck.length;
    // Binomial(n, 1/2) cut size, sampled by summing n Bernoulli(1/2).
    let cut = 0;
    for (let i = 0; i < n; i++) if (rng() < 0.5) cut++;
    const A = deck.slice(0, cut);
    const B = deck.slice(cut);
    const out = new Array(n);
    let ia = 0, ib = 0, k = 0;
    while (ia < A.length && ib < B.length) {
      const a = A.length - ia, b = B.length - ib;
      if (rng() < a / (a + b)) out[k++] = A[ia++];
      else out[k++] = B[ib++];
    }
    while (ia < A.length) out[k++] = A[ia++];
    while (ib < B.length) out[k++] = B[ib++];
    return out;
  }

  // Count rising sequences and label each card by which sequence it belongs to.
  // A rising sequence is a maximal subset of {1..n} that appears in deck in
  // increasing order with consecutive labels (Bayer-Diaconis definition).
  // Equivalent algorithm: position[c] = index of card c in deck; then sequence
  // starting at card c continues at c+1 iff position[c+1] > position[c].
  function risingSequenceLabels(deck) {
    const n = deck.length;
    const position = new Array(n);
    for (let i = 0; i < n; i++) position[deck[i]] = i;
    // Assign a sequence id to each label in original-position order.
    const seqIdByLabel = new Array(n);
    let nextId = 0;
    seqIdByLabel[0] = nextId;
    for (let c = 1; c < n; c++) {
      if (position[c] > position[c - 1]) {
        seqIdByLabel[c] = seqIdByLabel[c - 1];
      } else {
        nextId++;
        seqIdByLabel[c] = nextId;
      }
    }
    const numSeq = nextId + 1;
    // Map to deck order: seqIdByDeckPos[i] = seqIdByLabel[deck[i]]
    const seqIdByDeckPos = new Array(n);
    for (let i = 0; i < n; i++) seqIdByDeckPos[i] = seqIdByLabel[deck[i]];
    return { seqIdByDeckPos, numSeq };
  }

  // Color palettes.
  function originColor(label, n) {
    // Smooth gradient red -> yellow -> green -> blue -> magenta along original position.
    const t = label / (n - 1);
    const hue = 240 - 240 * t + 60; // 60 (yellow) at t=0 -> 60 - 240 + 60 wait fix
    // Simpler: HSL hue rotates 0..280 across positions.
    const h = (t * 280) % 360;
    return `hsl(${h.toFixed(1)}, 78%, 58%)`;
  }
  function risingColor(seqId, numSeq) {
    if (numSeq <= 1) return "#fafafa";
    // Distinct hues; use golden-angle increments for separation.
    const h = (seqId * 137.508) % 360;
    const s = 70;
    const l = 58;
    return `hsl(${h.toFixed(1)}, ${s}%, ${l}%)`;
  }

  // State
  let seed = 0x1234abcd;
  let kShuffles = 0;
  let baseDeck;

  function makeBaseDeck() {
    const d = new Array(N);
    for (let i = 0; i < N; i++) d[i] = i;
    return d;
  }

  // Build the deck at k shuffles by replaying GSR from seed.
  function deckAtK(k) {
    const rng = mulberry32(seed);
    let d = makeBaseDeck();
    for (let i = 0; i < k; i++) d = riffleGSR(d, rng);
    return d;
  }

  // Rendering
  function drawStrip(canvasId, deck, colorFn) {
    const c = document.getElementById(canvasId);
    if (!c) return;
    const ctx = c.getContext("2d");
    const w = c.width;
    const h = c.height;
    ctx.clearRect(0, 0, w, h);
    const n = deck.length;
    const cellW = w / n;
    for (let i = 0; i < n; i++) {
      ctx.fillStyle = colorFn(deck, i);
      ctx.fillRect(Math.floor(i * cellW), 0, Math.ceil(cellW) + 1, h);
    }
    // light grid every 13 cards
    ctx.strokeStyle = "rgba(0, 0, 0, 0.35)";
    ctx.lineWidth = 1;
    for (let j = 13; j < n; j += 13) {
      const x = Math.floor(j * cellW) + 0.5;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
  }

  function drawCurve(k) {
    const c = document.getElementById("canvas-curve");
    if (!c) return;
    const ctx = c.getContext("2d");
    const w = c.width;
    const h = c.height;
    ctx.clearRect(0, 0, w, h);

    const padL = 36, padR = 12, padT = 14, padB = 22;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;
    const kMax = BD_TV.length - 1;

    // Background plot frame
    ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
    ctx.lineWidth = 1;
    ctx.strokeRect(padL, padT, plotW, plotH);

    // Reference line at d_TV = 0.5
    const y50 = padT + plotH * 0.5;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.12)";
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(padL, y50);
    ctx.lineTo(padL + plotW, y50);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "rgba(255, 255, 255, 0.4)";
    ctx.font = '10px ui-sans-serif, system-ui, sans-serif';
    ctx.textAlign = "left";
    ctx.fillText("d_TV = 0.5", padL + 4, y50 - 4);

    // x-axis ticks
    ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
    ctx.textAlign = "center";
    for (let x = 0; x <= kMax; x++) {
      const px = padL + (x / kMax) * plotW;
      ctx.fillText(String(x), px, h - 6);
    }
    // y-axis ticks
    ctx.textAlign = "right";
    [0, 0.25, 0.5, 0.75, 1.0].forEach((v) => {
      const py = padT + plotH * (1 - v);
      ctx.fillText(v.toFixed(2), padL - 4, py + 3);
    });

    // Plot d_TV
    ctx.strokeStyle = "#a78bfa";
    ctx.lineWidth = 2;
    ctx.beginPath();
    BD_TV.forEach((v, i) => {
      const px = padL + (i / kMax) * plotW;
      const py = padT + plotH * (1 - v);
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Plot points
    BD_TV.forEach((v, i) => {
      const px = padL + (i / kMax) * plotW;
      const py = padT + plotH * (1 - v);
      ctx.fillStyle = i === k ? "#fafafa" : "#a78bfa";
      ctx.beginPath();
      ctx.arc(px, py, i === k ? 4.5 : 2.5, 0, Math.PI * 2);
      ctx.fill();
    });

    // Current k marker line
    const kx = padL + (k / kMax) * plotW;
    ctx.strokeStyle = "rgba(250, 250, 250, 0.5)";
    ctx.setLineDash([2, 4]);
    ctx.beginPath();
    ctx.moveTo(kx, padT);
    ctx.lineTo(kx, padT + plotH);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  function render() {
    const deck = deckAtK(kShuffles);
    const { seqIdByDeckPos, numSeq } = risingSequenceLabels(deck);

    drawStrip("canvas-origin", deck, (d, i) => originColor(d[i], N));
    drawStrip("canvas-rising", deck, (d, i) => risingColor(seqIdByDeckPos[i], numSeq));

    const tv = BD_TV[Math.min(kShuffles, BD_TV.length - 1)];
    document.getElementById("k-val").textContent = kShuffles;
    document.getElementById("r-val").textContent = numSeq;
    document.getElementById("stat-k").textContent = kShuffles;
    document.getElementById("stat-r").textContent = numSeq;
    document.getElementById("stat-tv").textContent = tv.toFixed(3);
    document.getElementById("stat-verdict").textContent = verdictFor(tv);

    drawCurve(kShuffles);
  }

  function init() {
    baseDeck = makeBaseDeck();
    const slider = document.getElementById("k-slider");
    slider.addEventListener("input", (e) => {
      kShuffles = parseInt(e.target.value, 10);
      render();
    });
    document.getElementById("reshuffle").addEventListener("click", () => {
      seed = (Math.random() * 0xffffffff) >>> 0;
      render();
    });
    document.getElementById("step-fwd").addEventListener("click", () => {
      kShuffles = Math.min(kShuffles + 1, 15);
      slider.value = kShuffles;
      render();
    });
    document.getElementById("reset").addEventListener("click", () => {
      kShuffles = 0;
      slider.value = 0;
      render();
    });
    // Crisp canvases on HiDPI
    ["canvas-origin", "canvas-rising", "canvas-curve"].forEach((id) => {
      const c = document.getElementById(id);
      if (!c) return;
      const dpr = window.devicePixelRatio || 1;
      const rect = c.getBoundingClientRect();
      const cssW = c.width;
      const cssH = c.height;
      c.style.width = cssW + "px";
      // Leave layout-px width as set
    });
    render();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
