document.body.classList.add('fullscreen-exp');
(function () {
  var canvas = document.getElementById('gods-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  var W = 1200, H = 760;

  // Each station carries a small library of god-slots. The traveler snaps to
  // whichever slot is nearest -- the wind-god slot drifts gently along the route,
  // so a low-noise traveler reproduces the historical lineage.
  var STATIONS = [
    { place: 'Greece', anchors: [{a: 8, n: 'Boreas'}, {a: 130, n: 'Zephyrus'}, {a: 250, n: 'Notus'}] },
    { place: 'Bactria', anchors: [{a: 24, n: 'Wardo'}, {a: 150, n: 'Mithra'}, {a: 270, n: 'Nana'}] },
    { place: 'Tarim Basin', anchors: [{a: 38, n: 'Feng Bo'}, {a: 165, n: 'Vaishravana'}, {a: 285, n: 'Yaksha'}] },
    { place: 'Tang China', anchors: [{a: 52, n: 'Uncle Wind'}, {a: 175, n: 'Leigong'}, {a: 300, n: 'Long'}] },
    { place: 'Japan', anchors: [{a: 64, n: 'Fujin'}, {a: 185, n: 'Raijin'}, {a: 320, n: 'Susanoo'}] }
  ];
  var TRUE_ANGLE = 8; // in fact-mode, "Boreas" is the fact the chain should preserve

  var mode = 'culture';
  var morphNoise = 0.30;
  var sharing = 0.70;

  var token = null;       // active traveler
  var deposits = [];      // {sx, sy, name, hue, alive, place, shapeWobble}
  var phase = 'idle';     // idle | moving | done
  var travelT = 0;

  function angDist(a, b) {
    var d = Math.abs(((a - b) % 360 + 360) % 360);
    return d > 180 ? 360 - d : d;
  }
  function hueOf(angle) { return ((angle % 360) + 360) % 360; }

  function stationXY(i) {
    // reserve room on the right so stations never slide under the HUD panel (~280px)
    var left = 110;
    var rightReserve = (W > 760) ? 300 : 70;
    var span = Math.max(120, W - left - rightReserve);
    var x = left + (span * i) / (STATIONS.length - 1);
    var y = H * 0.46;
    return { x: x, y: y };
  }

  function startTrip() {
    deposits = [];
    travelT = 0;
    phase = 'moving';
    token = {
      idx: 0,
      meaning: 8 + (Math.random() - 0.5) * 6, // begins near the Boreas slot
      shapeWobble: 0,
      shapeFidelity: 1,
      alive: true
    };
    // resolve first station immediately (it is the origin culture)
    resolveStation(0);
    updateHUD();
  }

  function resolveStation(i) {
    var st = STATIONS[i];
    // serial drift on meaning between hops (telephone degradation)
    if (i > 0) {
      token.meaning += (Math.random() - 0.5) * (10 + morphNoise * 70);
      token.shapeWobble += morphNoise * (0.6 + Math.random() * 0.7);
      token.shapeFidelity *= (1 - morphNoise * 0.10);
    }
    // snap to nearest local schema within a capture radius set by schema sharing
    var captureRadius = 14 + sharing * 70;
    var best = null, bestD = 1e9;
    for (var k = 0; k < st.anchors.length; k++) {
      var d = angDist(token.meaning, st.anchors[k].a);
      if (d < bestD) { bestD = d; best = st.anchors[k]; }
    }
    var pt = stationXY(i);
    if (best && bestD <= captureRadius) {
      token.meaning = best.a;            // apophenia: imposed onto nearest familiar pattern
      deposits.push({
        sx: pt.x, sy: pt.y, name: best.n, hue: hueOf(best.a),
        alive: true, place: st.place, wobble: token.shapeWobble
      });
    } else {
      // no shared slot within reach -> idiosyncratic misreading, no descendants
      token.alive = false;
      deposits.push({
        sx: pt.x, sy: pt.y, name: '(unread)', hue: hueOf(token.meaning),
        alive: false, place: st.place, wobble: token.shapeWobble
      });
    }
  }

  function step() {
    if (phase === 'moving' && token) {
      travelT += 0.022;
      if (travelT >= 1) {
        travelT = 0;
        if (!token.alive) { phase = 'done'; updateHUD(); }
        else {
          token.idx++;
          if (token.idx >= STATIONS.length) { phase = 'done'; updateHUD(); }
          else { resolveStation(token.idx); updateHUD(); }
        }
      }
    }
    draw();
  }

  // ---- drawing ----
  function drawGlyph(x, y, scale, hue, wobble, alpha) {
    // a dishevelled figure holding a windbag overhead -- the durable morphology
    ctx.save();
    ctx.translate(x, y);
    ctx.globalAlpha = alpha;
    var col = 'hsl(' + hue + ',58%,62%)';
    ctx.strokeStyle = col;
    ctx.fillStyle = col;
    ctx.lineWidth = 2.2 * scale;
    ctx.lineCap = 'round';
    var wob = Math.sin(wobble * 1.7) * 4 * wobble;
    // head
    ctx.beginPath();
    ctx.arc(0, -26 * scale, 6.5 * scale, 0, Math.PI * 2);
    ctx.stroke();
    // body
    ctx.beginPath();
    ctx.moveTo(0, -20 * scale);
    ctx.lineTo(wob * 0.3, 8 * scale);
    ctx.stroke();
    // legs
    ctx.beginPath();
    ctx.moveTo(0, 8 * scale); ctx.lineTo(-8 * scale, 24 * scale);
    ctx.moveTo(0, 8 * scale); ctx.lineTo(9 * scale, 24 * scale);
    ctx.stroke();
    // arms raised holding the bag
    ctx.beginPath();
    ctx.moveTo(0, -14 * scale); ctx.lineTo(-15 * scale + wob, -34 * scale);
    ctx.moveTo(0, -14 * scale); ctx.lineTo(15 * scale - wob, -34 * scale);
    ctx.stroke();
    // the windbag (arc) -- shape persists even as wobble grows
    ctx.beginPath();
    ctx.moveTo(-15 * scale + wob, -34 * scale);
    ctx.bezierCurveTo(
      -22 * scale, (-58 + wob) * scale,
      22 * scale, (-58 - wob) * scale,
      15 * scale - wob, -34 * scale
    );
    ctx.globalAlpha = alpha * 0.5;
    ctx.fill();
    ctx.globalAlpha = alpha;
    ctx.stroke();
    ctx.restore();
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    // road
    var y = H * 0.5;
    ctx.strokeStyle = 'rgba(200,180,130,0.16)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(stationXY(0).x, y);
    ctx.lineTo(stationXY(STATIONS.length - 1).x, y);
    ctx.stroke();

    // in fact-mode draw the "true meaning" reference band
    if (mode === 'fact') {
      ctx.fillStyle = 'hsla(' + hueOf(TRUE_ANGLE) + ',55%,55%,0.10)';
      ctx.fillRect(0, y - 92, W, 14);
      ctx.fillStyle = 'hsla(' + hueOf(TRUE_ANGLE) + ',60%,68%,0.85)';
      ctx.font = '11px sans-serif';
      ctx.fillText('true meaning (the fact the chain should preserve)', 14, y - 96);
    }

    // stations
    for (var i = 0; i < STATIONS.length; i++) {
      var p = stationXY(i);
      ctx.fillStyle = 'rgba(255,255,255,0.30)';
      ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = 'rgba(180,174,162,0.7)';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(STATIONS[i].place, p.x, p.y + 92);
      ctx.textAlign = 'left';
    }

    // deposited glyphs + names
    for (var d = 0; d < deposits.length; d++) {
      var dp = deposits[d];
      drawGlyph(dp.sx, dp.sy - 4, 1.0, dp.hue, dp.wobble, dp.alive ? 0.95 : 0.32);
      ctx.textAlign = 'center';
      ctx.font = 'bold 13px sans-serif';
      ctx.fillStyle = dp.alive ? 'hsl(' + dp.hue + ',55%,72%)' : 'rgba(150,110,110,0.8)';
      ctx.fillText(dp.name, dp.sx, dp.sy + 52);
      ctx.textAlign = 'left';
    }

    // traveling token between stations
    if (phase === 'moving' && token && token.alive && token.idx < STATIONS.length - 1) {
      var a = stationXY(token.idx);
      var b = stationXY(token.idx + 1);
      var tx = a.x + (b.x - a.x) * travelT;
      var ty = a.y - Math.sin(travelT * Math.PI) * 46;
      drawGlyph(tx, ty, 0.7, hueOf(token.meaning), token.shapeWobble, 0.9);
    }
  }

  // ---- HUD ----
  function updateHUD() {
    var lin = document.getElementById('gods-lineage');
    var html = '';
    for (var i = 0; i < deposits.length; i++) {
      var dp = deposits[i];
      if (dp.alive) {
        html += '<div class="step"><span class="swatch" style="background:hsl(' + dp.hue + ',58%,60%)"></span>' +
          '<span>' + dp.place + ': <b>' + dp.name + '</b></span></div>';
      } else {
        html += '<div class="step dead"><span class="swatch" style="background:#5a3a3a"></span>' +
          '<span>' + dp.place + ': lost &mdash; no slot to receive it</span></div>';
      }
    }
    lin.innerHTML = html;

    var fid = token ? Math.max(0, token.shapeFidelity) : 1;
    document.getElementById('gods-shape-v').textContent = Math.round(fid * 100) + '%';
    document.getElementById('gods-shape-bar').style.width = (fid * 100) + '%';

    var div = 0;
    if (deposits.length) {
      var first = deposits[0].alive ? 8 : 8;
      var last = deposits[deposits.length - 1];
      div = angDist(last.hue, hueOf(TRUE_ANGLE)) / 180;
    }
    document.getElementById('gods-mean-v').textContent = Math.round(div * 100) + '%';
    document.getElementById('gods-mean-bar').style.width = (div * 100) + '%';
    document.getElementById('gods-mean-label').textContent =
      (mode === 'fact') ? 'Error from the fact' : 'Meaning transformation';
    document.getElementById('gods-mean-bar').style.background =
      (mode === 'fact') ? '#c66' : '#d2a857';

    var v = document.getElementById('gods-verdict');
    if (phase !== 'done') { v.innerHTML = ''; return; }
    var alive = deposits.length && deposits[deposits.length - 1].alive;
    var distinct = {};
    for (var j = 0; j < deposits.length; j++) if (deposits[j].alive) distinct[deposits[j].name] = 1;
    var nGods = Object.keys(distinct).length;
    if (!alive) {
      v.innerHTML = '<b style="color:#d98">The figure was lost.</b> A misreading with no shared slot to land in is a private delusion &mdash; it has no descendants. Raise schema sharing.';
    } else if (mode === 'fact') {
      v.innerHTML = '<b style="color:#e0a0a0">Drift = corruption.</b> With a true meaning at the far end, every local re-snap moved it ' + Math.round(div * 100) + '% off the fact. Here you would want parallel collation to cancel it.';
    } else {
      v.innerHTML = '<b style="color:#d2c089">Drift = creation.</b> The shape survived (' + Math.round(fid * 100) + '%); the meaning became <b>' + nGods + '</b> distinct gods. No fact was corrupted &mdash; new gods were born.';
    }
  }

  // ---- controls ----
  function bind() {
    document.getElementById('gods-morph').addEventListener('input', function (e) {
      morphNoise = parseFloat(e.target.value);
      document.getElementById('gods-mn-val').textContent = morphNoise.toFixed(2);
    });
    document.getElementById('gods-share').addEventListener('input', function (e) {
      sharing = parseFloat(e.target.value);
      document.getElementById('gods-sh-val').textContent = sharing.toFixed(2);
    });
    document.getElementById('gods-send').addEventListener('click', startTrip);
    var bc = document.getElementById('gods-culture');
    var bf = document.getElementById('gods-fact');
    bc.addEventListener('click', function () {
      mode = 'culture'; bc.classList.add('active'); bf.classList.remove('active'); updateHUD();
    });
    bf.addEventListener('click', function () {
      mode = 'fact'; bf.classList.add('active'); bc.classList.remove('active'); updateHUD();
    });
  }

  function resize() {
    W = canvas.clientWidth || window.innerWidth || 1200;
    H = canvas.clientHeight || window.innerHeight || 760;
    if (W < 320) W = 1200;
    if (H < 320) H = 760;
    canvas.width = W * DPR;
    canvas.height = H * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    draw();
  }

  bind();
  window.addEventListener('resize', resize);
  resize();
  startTrip();
  setInterval(step, 33); // setInterval, not rAF: survives headless/background tabs

  // debug hook (harmless in production): drive the trip synchronously for testing
  window.__gods = {
    drive: function (n) { for (var i = 0; i < (n || 400); i++) step(); },
    restart: function () { startTrip(); },
    setMode: function (m) { mode = m; updateHUD(); },
    setSize: function (w, h) { W = w; H = h; canvas.width = w * DPR; canvas.height = h * DPR; ctx.setTransform(DPR, 0, 0, DPR, 0, 0); draw(); },
    state: function () {
      return { phase: phase, mode: mode,
        deposits: deposits.map(function (d) { return d.alive ? d.name : '(' + d.place + ' lost)'; }) };
    }
  };
})();
