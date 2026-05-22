"""Publish lab experiment: two-models-same-starter."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from website import publish_experiment


HTML = """<div class="tmss-container">
  <a href="/lab/" class="tmss-back">&larr; all experiments</a>

  <header class="tmss-header">
    <h1>Two Models, Same Starter</h1>
    <p class="tmss-caption">Three simulated starters from the same recipe. Both models accept the data. Watch them disagree about what it means.</p>
  </header>

  <div class="tmss-plot-wrap">
    <canvas id="tmss-canvas" width="780" height="320"></canvas>
    <div class="tmss-legend">
      <span><i style="background:#7fb069"></i> Starter A</span>
      <span><i style="background:#f4a261"></i> Starter B</span>
      <span><i style="background:#9b8ccc"></i> Starter C</span>
    </div>
  </div>

  <div class="tmss-controls">
    <label>
      <span class="tmss-label">Founder noise</span>
      <input type="range" id="tmss-noise" min="0" max="100" value="60" />
      <span class="tmss-val" id="tmss-noise-val">0.60</span>
    </label>
    <label>
      <span class="tmss-label">Flour amylase activity</span>
      <input type="range" id="tmss-flour" min="0" max="100" value="50" />
      <span class="tmss-val" id="tmss-flour-val">0.50</span>
    </label>
    <button id="tmss-reseed" class="tmss-btn">Reseed founder communities</button>
  </div>

  <div class="tmss-models">
    <section class="tmss-model tmss-recipe">
      <h2>Recipe model says</h2>
      <ul id="tmss-recipe-verdict"></ul>
      <p class="tmss-rule">Inputs were identical. Variation is technique error. Tighten controls.</p>
    </section>
    <section class="tmss-model tmss-ecosystem">
      <h2>Ecosystem model says</h2>
      <ul id="tmss-eco-verdict"></ul>
      <p class="tmss-rule">Founder community differed. Succession ran to different attractors. Tend, observe, accept.</p>
    </section>
  </div>

  <p class="tmss-footnote">Same observed time series in the plot. The two columns below are the same starters, narrated by two coherent models that recommend opposite practices. Read the essay: <a href="/blog/sourdough-is-not-a-recipe/">Sourdough Is Not a Recipe</a>.</p>
</div>
"""

CSS = """
.tmss-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 24px 80px;
  font-family: -apple-system, system-ui, sans-serif;
  color: #1a1a1a;
}
.tmss-back {
  display: inline-block;
  font-size: 0.85em;
  color: #666;
  margin-bottom: 20px;
  text-decoration: none;
}
.tmss-back:hover { color: #1a1a1a; }
.tmss-header h1 {
  font-size: 1.6em;
  margin: 0 0 8px;
  font-weight: 600;
  letter-spacing: -0.01em;
}
.tmss-caption {
  margin: 0 0 24px;
  color: #555;
  font-size: 0.95em;
  line-height: 1.5;
}
.tmss-plot-wrap {
  background: #f7f5ef;
  border: 1px solid #d8d4c8;
  border-radius: 4px;
  padding: 16px;
  margin-bottom: 16px;
}
#tmss-canvas {
  display: block;
  width: 100%;
  height: auto;
  max-height: 360px;
  background: #fcfbf7;
  border-radius: 2px;
}
.tmss-legend {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-top: 12px;
  font-size: 0.85em;
  color: #444;
}
.tmss-legend i {
  display: inline-block;
  width: 12px;
  height: 12px;
  margin-right: 6px;
  vertical-align: middle;
  border-radius: 2px;
}
.tmss-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 16px 24px;
  align-items: center;
  margin: 20px 0 28px;
  padding: 14px 18px;
  background: #fff;
  border: 1px solid #e2dfd5;
  border-radius: 4px;
}
.tmss-controls label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.85em;
}
.tmss-label {
  color: #444;
  min-width: 150px;
}
.tmss-controls input[type=range] {
  width: 150px;
}
.tmss-val {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.85em;
  color: #666;
  min-width: 3em;
}
.tmss-btn {
  background: #1a1a1a;
  color: #fff;
  border: 0;
  padding: 7px 14px;
  border-radius: 3px;
  font-size: 0.85em;
  cursor: pointer;
  font-family: inherit;
}
.tmss-btn:hover { background: #444; }
.tmss-models {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-bottom: 28px;
}
.tmss-model {
  padding: 18px 20px;
  border-radius: 4px;
  border: 1px solid;
}
.tmss-recipe {
  background: #fbf2e8;
  border-color: #e8cba4;
}
.tmss-ecosystem {
  background: #eef3ec;
  border-color: #b8cdb4;
}
.tmss-model h2 {
  font-size: 0.95em;
  margin: 0 0 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: #2a2a2a;
}
.tmss-model ul {
  list-style: none;
  padding: 0;
  margin: 0 0 14px;
  font-size: 0.88em;
  line-height: 1.45;
}
.tmss-model li {
  padding: 4px 0;
  display: flex;
  gap: 8px;
}
.tmss-model li::before {
  content: attr(data-name);
  font-weight: 600;
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  flex: 0 0 60px;
}
.tmss-rule {
  font-size: 0.78em;
  color: #555;
  font-style: italic;
  margin: 0;
  padding-top: 10px;
  border-top: 1px dashed #c0bbac;
}
.tmss-footnote {
  font-size: 0.82em;
  color: #666;
  line-height: 1.5;
  text-align: center;
  margin-top: 16px;
}
.tmss-footnote a { color: #1a1a1a; }
@media (max-width: 640px) {
  .tmss-models { grid-template-columns: 1fr; }
  .tmss-controls input[type=range] { width: 120px; }
  .tmss-label { min-width: 120px; }
}
"""

JS = """
(function () {
  var canvas = document.getElementById('tmss-canvas');
  var ctx = canvas.getContext('2d');
  var noiseEl = document.getElementById('tmss-noise');
  var flourEl = document.getElementById('tmss-flour');
  var noiseValEl = document.getElementById('tmss-noise-val');
  var flourValEl = document.getElementById('tmss-flour-val');
  var reseedBtn = document.getElementById('tmss-reseed');
  var recipeUl = document.getElementById('tmss-recipe-verdict');
  var ecoUl = document.getElementById('tmss-eco-verdict');

  var COLORS = ['#7fb069', '#f4a261', '#9b8ccc'];
  var NAMES = ['Starter A', 'Starter B', 'Starter C'];

  // simple seeded PRNG
  function mulberry32(a) {
    return function () {
      var t = (a += 0x6D2B79F5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  var seed = Math.floor(Math.random() * 1e9);

  function simulate(noise, flour, seedOffset) {
    var rng = mulberry32(seed + seedOffset * 9973);
    // founder community: 4 dims (LAB, acetic-AAB, K.humilis, generalist), normalized
    var founder = [0.3 + (rng() - 0.5) * noise * 0.6,
                   0.2 + (rng() - 0.5) * noise * 0.4,
                   0.3 + (rng() - 0.5) * noise * 0.4,
                   0.4 + (rng() - 0.5) * noise * 0.4];
    var sum = founder.reduce(function (a, b) { return a + Math.max(0.02, b); }, 0);
    founder = founder.map(function (x) { return Math.max(0.02, x) / sum; });

    var trajectory = [];
    var pH = 6.8;
    var gas = 0;
    var lab = founder[0], aab = founder[1], yeast = founder[2], gen = founder[3];

    for (var t = 0; t <= 14; t += 0.25) {
      // succession dynamics (toy)
      var labGrowth = 0.45 + flour * 0.3;
      var aabGrowth = 0.18 + (1 - flour) * 0.18;
      var yeastGrowth = 0.32 + flour * 0.12;
      var genDecay = 0.6;

      lab += lab * labGrowth * 0.25 * (1 - lab);
      aab += aab * aabGrowth * 0.25 * (1 - aab);
      yeast += yeast * yeastGrowth * 0.25 * (1 - yeast);
      gen *= Math.exp(-genDecay * 0.25);

      var total = lab + aab + yeast + gen;
      lab /= total; aab /= total; yeast /= total; gen /= total;

      pH = 6.8 - 3.0 * (lab * 0.7 + aab * 0.6) - 0.2 * Math.sin(t * 2.0);
      pH = Math.max(3.3, Math.min(6.8, pH));
      // diurnal-like rise/fall from feeding (period ~1 day)
      var feedPhase = (t % 1.0);
      var risePeak = yeast * (1 - feedPhase) * Math.exp(-3 * feedPhase) * 4;
      gas = risePeak + lab * 0.4 * Math.sin(t * 6.28);

      trajectory.push({ t: t, pH: pH, gas: gas, lab: lab, aab: aab, yeast: yeast });
    }

    // climax community at day 14
    var last = trajectory[trajectory.length - 1];
    var labAcid = last.lab / (last.lab + last.aab + 0.001);
    var attractor;
    if (labAcid > 0.72 && last.yeast > 0.22) attractor = 'A: mild lactic, high lift';
    else if (labAcid < 0.55) attractor = 'B: vinegary, sour';
    else if (last.yeast < 0.18) attractor = 'C: slow-rise, deep flavor';
    else attractor = 'A: mild lactic, high lift';

    var maxRise = Math.max.apply(null, trajectory.map(function (p) { return p.gas; }));
    var doubled = maxRise > 1.6;

    return { trajectory: trajectory, climax: last, attractor: attractor, doubled: doubled, maxRise: maxRise };
  }

  function draw() {
    var noise = parseInt(noiseEl.value, 10) / 100;
    var flour = parseInt(flourEl.value, 10) / 100;
    noiseValEl.textContent = noise.toFixed(2);
    flourValEl.textContent = flour.toFixed(2);

    var results = [0, 1, 2].map(function (i) { return simulate(noise, flour, i); });

    var W = canvas.width, H = canvas.height;
    ctx.clearRect(0, 0, W, H);

    // background
    ctx.fillStyle = '#fcfbf7';
    ctx.fillRect(0, 0, W, H);

    // axes margins
    var ml = 50, mr = 20, mt = 28, mb = 40;
    var pw = W - ml - mr, ph = H - mt - mb;

    // grid + axes
    ctx.strokeStyle = '#e2dfd5';
    ctx.lineWidth = 1;
    for (var d = 0; d <= 14; d += 2) {
      var x = ml + (d / 14) * pw;
      ctx.beginPath(); ctx.moveTo(x, mt); ctx.lineTo(x, mt + ph); ctx.stroke();
    }
    for (var p = 3.5; p <= 7; p += 0.5) {
      var y = mt + ph - ((p - 3.3) / (7 - 3.3)) * ph;
      ctx.beginPath(); ctx.moveTo(ml, y); ctx.lineTo(ml + pw, y); ctx.stroke();
    }

    // axis labels
    ctx.fillStyle = '#666';
    ctx.font = '11px ui-monospace, "SF Mono", Menlo, monospace';
    ctx.textAlign = 'center';
    for (var d2 = 0; d2 <= 14; d2 += 2) {
      var xl = ml + (d2 / 14) * pw;
      ctx.fillText('d' + d2, xl, mt + ph + 16);
    }
    ctx.textAlign = 'right';
    for (var p2 = 4; p2 <= 7; p2 += 1) {
      var yl = mt + ph - ((p2 - 3.3) / (7 - 3.3)) * ph;
      ctx.fillText(p2.toFixed(1), ml - 8, yl + 4);
    }
    ctx.save();
    ctx.translate(14, mt + ph / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.fillStyle = '#444';
    ctx.fillText('pH', 0, 0);
    ctx.restore();
    ctx.textAlign = 'center';
    ctx.fillStyle = '#444';
    ctx.fillText('day', ml + pw / 2, mt + ph + 32);

    // draw pH trajectories
    results.forEach(function (res, i) {
      ctx.strokeStyle = COLORS[i];
      ctx.lineWidth = 2;
      ctx.beginPath();
      res.trajectory.forEach(function (pt, j) {
        var x = ml + (pt.t / 14) * pw;
        var y = mt + ph - ((pt.pH - 3.3) / (7 - 3.3)) * ph;
        if (j === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.stroke();
    });

    // title overlay
    ctx.fillStyle = '#1a1a1a';
    ctx.font = '600 12px -apple-system, system-ui, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('pH over 14 days', ml, mt - 12);

    updateVerdicts(results);
  }

  function updateVerdicts(results) {
    recipeUl.innerHTML = '';
    ecoUl.innerHTML = '';
    results.forEach(function (res, i) {
      // recipe verdict: same protocol => prediction is "doubled within 4-8h"
      // since recipe model treats inputs as identical, verdict reflects ONLY whether
      // each starter hit the protocol's threshold
      var recipeVerdict;
      if (res.doubled && res.climax.pH < 4.2) recipeVerdict = 'protocol met, READY';
      else if (!res.doubled) recipeVerdict = 'did not double in time, TECHNIQUE ERROR';
      else recipeVerdict = 'pH too high, FEED MORE';

      var recipeLi = document.createElement('li');
      recipeLi.setAttribute('data-name', NAMES[i]);
      recipeLi.style.color = COLORS[i];
      var rspan = document.createElement('span');
      rspan.style.color = '#1a1a1a';
      rspan.textContent = recipeVerdict;
      recipeLi.appendChild(rspan);
      recipeUl.appendChild(recipeLi);

      // ecosystem verdict: identifies the attractor
      var ecoLi = document.createElement('li');
      ecoLi.setAttribute('data-name', NAMES[i]);
      ecoLi.style.color = COLORS[i];
      var espan = document.createElement('span');
      espan.style.color = '#1a1a1a';
      espan.textContent = 'attractor ' + res.attractor;
      ecoLi.appendChild(espan);
      ecoUl.appendChild(ecoLi);
    });
  }

  noiseEl.addEventListener('input', draw);
  flourEl.addEventListener('input', draw);
  reseedBtn.addEventListener('click', function () {
    seed = Math.floor(Math.random() * 1e9);
    draw();
  });

  draw();
})();
"""


def main():
    res = publish_experiment(
        slug='two-models-same-starter',
        title='Two Models, Same Starter',
        description='Same sourdough trajectory, two coherent narrators. Recipe model calls drift a technique error; ecosystem model calls it succession to a different attractor.',
        tags=['sourdough', 'microbial-ecology', 'two-models-same-data', 'underdetermination', 'duhem-quine'],
        html_content=HTML,
        css_content=CSS,
        js_content=JS,
    )
    print(res)


if __name__ == '__main__':
    main()
