HTML = r"""
<div class="dtn-container">
  <p class="dtn-intro">Two ways to cross the same gap. <b>Stream</b> pushes bits through a live link &mdash; fast, but it dies whenever the link partitions and loses any half-sent chunk. <b>Carry</b> hands the payload to a mover that ferries it across &mdash; slow, but immune to partitions, and its bandwidth <i>is</i> the mover's speed. Watch which one delivers more.</p>

  <canvas id="dtn-canvas" width="700" height="320"></canvas>

  <div class="dtn-verdict" id="dtn-verdict">CARRY vs STREAM</div>

  <div class="dtn-controls">
    <label>Mobility (carrier speed)
      <input type="range" id="dtn-mob" min="0.2" max="3" step="0.1" value="1">
      <span id="dtn-mob-v">1.0&times;</span>
    </label>
    <label>Payload size (per delivery)
      <input type="range" id="dtn-pay" min="1" max="12" step="1" value="3">
      <span id="dtn-pay-v">3</span>
    </label>
    <label>Partition rate (link downtime)
      <input type="range" id="dtn-part" min="0" max="0.85" step="0.05" value="0.2">
      <span id="dtn-part-v">20%</span>
    </label>
    <div class="dtn-buttons">
      <button id="dtn-run">Pause</button>
      <button id="dtn-reset">Reset counts</button>
    </div>
  </div>

  <p class="dtn-note">Low payload + reliable link &rarr; <b>Stream wins</b>. Raise the payload, the partition rate, or the mobility and watch the crossover: past a point, the moving body beats the wire. This is Tanenbaum's station wagon, Amazon's Snowmobile truck, and the journeyman's <i>Walz</i> &mdash; the same physics.</p>
</div>
"""

CSS = r"""
.dtn-container { max-width: 720px; margin: 0 auto; font-family: 'Inter', system-ui, sans-serif; color: #d8d4cc; }
.dtn-container .dtn-intro, .dtn-container .dtn-note { font-size: 0.95rem; line-height: 1.6; color: #b8b3a8; }
.dtn-container .dtn-note { font-size: 0.85rem; color: #8f8a80; margin-top: 0.5rem; }
.dtn-container canvas { width: 100%; height: auto; display: block; background: #14130f; border: 1px solid #2c2a24; border-radius: 6px; margin: 1rem 0 0.5rem; }
.dtn-container .dtn-verdict { font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; text-align: center; letter-spacing: 0.02em; padding: 0.4rem; color: #e8e3d8; min-height: 1.4em; }
.dtn-container .dtn-controls { display: flex; flex-wrap: wrap; gap: 0.9rem 1.4rem; align-items: center; margin: 0.6rem 0; }
.dtn-container .dtn-controls label { display: flex; flex-direction: column; font-size: 0.78rem; color: #9a958a; letter-spacing: 0.03em; flex: 1 1 180px; }
.dtn-container .dtn-controls input[type=range] { width: 100%; margin-top: 0.35rem; accent-color: #c98a3a; }
.dtn-container .dtn-controls label span { font-family: 'JetBrains Mono', monospace; color: #d8d4cc; margin-top: 0.15rem; }
.dtn-container .dtn-buttons { display: flex; gap: 0.5rem; flex: 1 1 100%; margin-top: 0.2rem; }
.dtn-container .dtn-buttons button { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; background: #1d1b15; color: #d8d4cc; border: 1px solid #3a372f; border-radius: 4px; padding: 0.4rem 0.9rem; cursor: pointer; }
.dtn-container .dtn-buttons button:hover { background: #2a271f; border-color: #c98a3a; }
@media (max-width: 640px) { .dtn-container .dtn-controls label { flex: 1 1 100%; } }
"""

JS = r"""
(function () {
  var canvas = document.getElementById('dtn-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W = canvas.width, H = canvas.height;

  // geometry
  var sx = 90, rx = 610;          // sender / receiver x
  var streamY = 120, carryY = 230;
  var gapL = sx + 30, gapR = rx - 30;

  var S = {
    mobility: 1.0, payload: 3, partition: 0.20,
    running: true,
    // stream state
    inflight: 0, streamDelivered: 0, linkUp: true, cyclePos: 0,
    // carry state
    carrierX: gapL, carryDelivered: 0,
    // viz
    pulses: [],
  };

  var CYCLE = 120;          // ticks per up/down cycle
  var STREAM_RATE = 0.5;    // units per tick while link up
  var BASE_SPEED = 6.0;     // carrier px/tick at mobility 1
  var CARRY_BATCH = 5;      // buffer capacity: each trip hauls a big batch

  function reset() {
    S.inflight = 0; S.streamDelivered = 0; S.carryDelivered = 0;
    S.cyclePos = 0; S.linkUp = true; S.carrierX = gapL; S.pulses = [];
  }

  function step() {
    // --- link partition schedule (deterministic duty cycle) ---
    var downLen = S.partition * CYCLE;
    S.cyclePos = (S.cyclePos + 1) % CYCLE;
    var wasUp = S.linkUp;
    S.linkUp = S.cyclePos >= downLen;            // down for first part of cycle
    if (wasUp && !S.linkUp) { S.inflight = 0; }  // partition mid-transfer -> lose the half-sent chunk

    // --- STREAM ---
    if (S.linkUp) {
      S.inflight += STREAM_RATE;
      if (Math.random() < 0.5) S.pulses.push({ x: gapL, t: 1 });
      if (S.inflight >= S.payload) {
        S.inflight -= S.payload;
        S.streamDelivered += S.payload;
      }
    }
    // advance stream pulses
    for (var i = S.pulses.length - 1; i >= 0; i--) {
      S.pulses[i].x += (gapR - gapL) / 18;
      if (S.pulses[i].x >= gapR) S.pulses.splice(i, 1);
    }

    // --- CARRY (unaffected by partitions; one-way ferry, respawns at sender) ---
    var v = BASE_SPEED * S.mobility;
    S.carrierX += v;
    if (S.carrierX >= gapR) {
      S.carrierX = gapL;                                 // respawn at sender
      S.carryDelivered += CARRY_BATCH * S.payload;       // drop the whole batch
    }
  }

  function node(x, y, label, sub) {
    ctx.fillStyle = '#241f17'; ctx.strokeStyle = '#4a4536'; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(x - 26, y - 26, 52, 52, 8); ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#cfc8b8'; ctx.font = '600 11px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(label, x, y - 32);
    if (sub) { ctx.fillStyle = '#7d7768'; ctx.font = '9px JetBrains Mono, monospace'; ctx.fillText(sub, x, y + 42); }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // ---- STREAM track ----
    ctx.lineWidth = 2;
    if (S.linkUp) { ctx.strokeStyle = '#3f7d52'; ctx.setLineDash([]); }
    else { ctx.strokeStyle = '#9c4034'; ctx.setLineDash([6, 7]); }
    ctx.beginPath(); ctx.moveTo(gapL, streamY); ctx.lineTo(gapR, streamY); ctx.stroke();
    ctx.setLineDash([]);
    // stream pulses
    if (S.linkUp) {
      ctx.fillStyle = '#6fce8e';
      for (var i = 0; i < S.pulses.length; i++) {
        ctx.beginPath(); ctx.arc(S.pulses[i].x, streamY, 3, 0, 7); ctx.fill();
      }
    }
    // in-flight chunk bar
    if (S.payload > 0) {
      var frac = Math.max(0, Math.min(1, S.inflight / S.payload));
      ctx.fillStyle = '#2a3a2e'; ctx.fillRect(gapL, streamY + 12, gapR - gapL, 6);
      ctx.fillStyle = S.linkUp ? '#5fae7e' : '#9c4034';
      ctx.fillRect(gapL, streamY + 12, (gapR - gapL) * frac, 6);
    }
    ctx.fillStyle = '#8f8a80'; ctx.font = '9px JetBrains Mono, monospace'; ctx.textAlign = 'left';
    ctx.fillText(S.linkUp ? 'LINK UP' : 'PARTITIONED', gapL, streamY - 12);

    // ---- CARRY track ----
    ctx.strokeStyle = '#2c2a24'; ctx.lineWidth = 1; ctx.setLineDash([2, 6]);
    ctx.beginPath(); ctx.moveTo(gapL, carryY); ctx.lineTo(gapR, carryY); ctx.stroke();
    ctx.setLineDash([]);
    // carrier (always loaded with a batch)
    ctx.fillStyle = '#c98a3a';
    ctx.fillRect(S.carrierX - 11, carryY - 9, 22, 18);
    ctx.strokeStyle = '#e0a85a'; ctx.lineWidth = 1.2; ctx.strokeRect(S.carrierX - 11, carryY - 9, 22, 18);
    ctx.fillStyle = '#1a1610'; ctx.font = '700 9px JetBrains Mono'; ctx.textAlign = 'center';
    ctx.fillText(CARRY_BATCH * S.payload, S.carrierX, carryY + 3);

    // nodes
    node(sx, (streamY + carryY) / 2, 'SENDER', '');
    node(rx, (streamY + carryY) / 2, 'RECEIVER', '');
    // connect nodes to tracks
    ctx.strokeStyle = '#3a372f'; ctx.lineWidth = 1; ctx.setLineDash([]);
    ctx.beginPath();
    ctx.moveTo(sx + 26, streamY); ctx.lineTo(gapL, streamY);
    ctx.moveTo(gapR, streamY); ctx.lineTo(rx - 26, streamY);
    ctx.moveTo(sx + 26, carryY); ctx.lineTo(gapL, carryY);
    ctx.moveTo(gapR, carryY); ctx.lineTo(rx - 26, carryY);
    ctx.stroke();

    // labels + counters
    ctx.textAlign = 'left'; ctx.font = '600 12px Inter, sans-serif';
    ctx.fillStyle = '#9bbfa6'; ctx.fillText('STREAM', 20, streamY - 30);
    ctx.fillStyle = '#d9a55e'; ctx.fillText('CARRY', 20, carryY - 30);
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillStyle = '#cfc8b8';
    ctx.fillText('delivered: ' + Math.round(S.streamDelivered), 20, streamY + 50);
    ctx.fillText('delivered: ' + Math.round(S.carryDelivered), 20, carryY + 46);
  }

  function updateVerdict() {
    var el = document.getElementById('dtn-verdict');
    if (!el) return;
    var s = Math.round(S.streamDelivered), c = Math.round(S.carryDelivered);
    var txt, col;
    if (s === 0 && c === 0) { txt = 'warming up…'; col = '#8f8a80'; }
    else if (c > s) { txt = 'CARRY WINS — ' + c + ' vs ' + s; col = '#d9a55e'; }
    else if (s > c) { txt = 'STREAM WINS — ' + s + ' vs ' + c; col = '#9bbfa6'; }
    else { txt = 'TIED — ' + s + ' vs ' + c; col = '#cfc8b8'; }
    el.textContent = txt; el.style.color = col;
  }

  var acc = 0;
  function loop() {
    if (S.running) { for (var k = 0; k < 2; k++) step(); }
    draw(); updateVerdict();
    requestAnimationFrame(loop);
  }

  // ---- controls ----
  function bind(id, fn) { var e = document.getElementById(id); if (e) e.addEventListener('input', fn); }
  bind('dtn-mob', function (e) { S.mobility = parseFloat(e.target.value); document.getElementById('dtn-mob-v').textContent = S.mobility.toFixed(1) + '×'; });
  bind('dtn-pay', function (e) { S.payload = parseInt(e.target.value); document.getElementById('dtn-pay-v').textContent = S.payload; });
  bind('dtn-part', function (e) { S.partition = parseFloat(e.target.value); document.getElementById('dtn-part-v').textContent = Math.round(S.partition * 100) + '%'; });
  var runBtn = document.getElementById('dtn-run');
  if (runBtn) runBtn.addEventListener('click', function () { S.running = !S.running; runBtn.textContent = S.running ? 'Pause' : 'Run'; });
  var resetBtn = document.getElementById('dtn-reset');
  if (resetBtn) resetBtn.addEventListener('click', reset);

  // ---- test hooks ----
  window.__dtn = {
    setMobility: function (v) { S.mobility = v; },
    setPayload: function (v) { S.payload = v; },
    setPartition: function (v) { S.partition = v; },
    reset: reset,
    run: function (b) { S.running = b; },
    step: function (n) { for (var i = 0; i < (n || 1); i++) step(); },
    state: function () { return { mobility: S.mobility, payload: S.payload, partition: S.partition, streamDelivered: Math.round(S.streamDelivered), carryDelivered: Math.round(S.carryDelivered), linkUp: S.linkUp, verdict: S.carryDelivered > S.streamDelivered ? 'carry' : (S.streamDelivered > S.carryDelivered ? 'stream' : 'tie') }; },
  };

  loop();
})();
"""
