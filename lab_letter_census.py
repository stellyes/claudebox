"""Build the lab experiment 'The Letter Census' for the al-Kindi essay."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from server import experiment_create

slug = "the-letter-census"
title = "The Letter Census"
description = "Watch a monoalphabetic cipher relabel letters but fail to relabel the distribution. The substrate's frequency signature persists — exactly what al-Kindi saw in 850 CE."
tags = "cryptography, frequency-analysis, al-kindi, statistics, language, substrate"

html_content = """
<div class="census-container">
  <header class="census-header">
    <h1>The Letter Census</h1>
    <p class="census-tagline">A monoalphabetic substitution cipher relabels every letter. It cannot relabel the distribution. Count the letters in the ciphertext and the plaintext appears in the shape of the histogram.</p>
  </header>

  <section class="census-controls">
    <div class="census-passage-pick">
      <label for="census-passage">Passage</label>
      <select id="census-passage">
        <option value="0">Pride and Prejudice (1813)</option>
        <option value="1">Moby-Dick (1851)</option>
        <option value="2">The Federalist No. 10 (1787)</option>
        <option value="3">A passage of Arabic (transliterated)</option>
      </select>
    </div>

    <div class="census-buttons">
      <button id="census-reroll" type="button">Re-roll cipher</button>
      <button id="census-solve" type="button">Match by frequency</button>
      <button id="census-reset" type="button">Reset</button>
    </div>

    <div class="census-readout">
      <div class="census-readout-row"><span>Cipher key (a&rarr;?)</span><code id="census-key">—</code></div>
      <div class="census-readout-row"><span>Letters in passage</span><code id="census-count">—</code></div>
      <div class="census-readout-row"><span>Top plaintext letter</span><code id="census-top-plain">—</code></div>
      <div class="census-readout-row"><span>Top ciphertext letter</span><code id="census-top-cipher">—</code></div>
      <div class="census-readout-row"><span>Greedy-match accuracy</span><code id="census-accuracy">—</code></div>
    </div>
  </section>

  <section class="census-text-pair">
    <div class="census-text-block">
      <h2>Plaintext</h2>
      <pre id="census-plain"></pre>
    </div>
    <div class="census-text-block">
      <h2>Ciphertext</h2>
      <pre id="census-cipher"></pre>
    </div>
  </section>

  <section class="census-histograms">
    <div class="census-hist-block">
      <h2>Plaintext frequencies</h2>
      <div id="census-hist-plain" class="census-hist"></div>
    </div>
    <div class="census-hist-block">
      <h2>Ciphertext frequencies</h2>
      <div id="census-hist-cipher" class="census-hist"></div>
    </div>
  </section>

  <section class="census-decode">
    <h2>Decoded by greedy frequency match</h2>
    <p class="census-decode-note">Rank ciphertext letters by frequency, rank plaintext letters by frequency, match in order. This is al-Kindi's method, mechanized.</p>
    <pre id="census-decoded"></pre>
  </section>

  <footer class="census-footer">
    <p>Same passage, same cipher, same histograms. The shape is the language. The labels are the cipher.</p>
    <p class="census-cite">Method described by Abu Yusuf al-Kindi, <em>Risala fi Istikhraj al-Mu'amma</em>, Baghdad, c. 850 CE. Manuscript rediscovered Suleymaniye Archive, Istanbul, 1987 (Mrayati, Alam, al-Tayyan).</p>
  </footer>
</div>
"""

css_content = """
.census-container {
  font-family: 'EB Garamond', 'Georgia', serif;
  color: #e8e6e0;
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem 1.5rem 4rem;
  line-height: 1.55;
}
.census-container h1 {
  font-family: 'EB Garamond', 'Georgia', serif;
  font-size: 2.2rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  margin: 0 0 0.5rem;
  color: #f5f2eb;
}
.census-container h2 {
  font-family: 'EB Garamond', 'Georgia', serif;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #b9b3a4;
  margin: 0 0 0.75rem;
}
.census-tagline {
  color: #c9c4b6;
  font-size: 1.05rem;
  margin: 0 0 1.75rem;
  max-width: 760px;
}
.census-controls {
  display: grid;
  grid-template-columns: 1fr 1fr 1.4fr;
  gap: 1.25rem;
  align-items: start;
  padding: 1rem 1.25rem;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 6px;
  background: rgba(255,255,255,0.02);
  margin-bottom: 1.5rem;
}
.census-passage-pick label {
  display: block;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #b9b3a4;
  margin-bottom: 0.4rem;
}
.census-passage-pick select {
  width: 100%;
  background: rgba(0,0,0,0.35);
  color: #e8e6e0;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 0.45rem 0.6rem;
  border-radius: 4px;
  font-family: inherit;
  font-size: 0.95rem;
}
.census-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.census-buttons button {
  background: rgba(255,255,255,0.05);
  color: #e8e6e0;
  border: 1px solid rgba(255,255,255,0.18);
  padding: 0.45rem 0.8rem;
  border-radius: 4px;
  font-family: inherit;
  font-size: 0.92rem;
  cursor: pointer;
  transition: background 120ms ease, border-color 120ms ease;
}
.census-buttons button:hover {
  background: rgba(255,255,255,0.12);
  border-color: rgba(255,255,255,0.32);
}
.census-readout {
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 0.82rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}
.census-readout-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.6rem;
  border-bottom: 1px dotted rgba(255,255,255,0.08);
  padding-bottom: 0.15rem;
}
.census-readout-row span { color: #9a9486; }
.census-readout-row code { color: #f5f2eb; }
.census-text-pair, .census-histograms {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}
.census-text-block pre, .census-decode pre {
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 0.8rem;
  line-height: 1.55;
  background: rgba(0,0,0,0.35);
  padding: 0.9rem 1rem;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 4px;
  white-space: pre-wrap;
  word-break: break-word;
  margin: 0;
  max-height: 220px;
  overflow-y: auto;
  color: #d4cfc1;
}
.census-decode pre { max-height: 320px; }
.census-decode-note {
  color: #b9b3a4;
  font-size: 0.95rem;
  margin: 0 0 0.75rem;
  max-width: 760px;
}
.census-hist {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 160px;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.18);
  background: rgba(0,0,0,0.2);
  padding-left: 0.3rem;
  padding-right: 0.3rem;
}
.census-bar {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  gap: 0.25rem;
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 0.65rem;
  color: #b9b3a4;
}
.census-bar-fill {
  width: 100%;
  background: linear-gradient(180deg, #d4cfc1 0%, #8a8576 100%);
  border-radius: 2px 2px 0 0;
}
.census-bar-label {
  margin-top: 0.15rem;
  letter-spacing: 0.02em;
}
.census-bar.census-bar-top .census-bar-fill {
  background: linear-gradient(180deg, #e8c97a 0%, #a88a3e 100%);
}
.census-bar.census-bar-top .census-bar-label {
  color: #e8c97a;
}
.census-footer {
  margin-top: 2rem;
  padding-top: 1.25rem;
  border-top: 1px solid rgba(255,255,255,0.08);
  color: #9a9486;
  font-size: 0.92rem;
  line-height: 1.5;
}
.census-cite {
  font-size: 0.82rem;
  color: #7a7468;
  margin-top: 0.5rem;
}
@media (max-width: 760px) {
  .census-controls { grid-template-columns: 1fr; }
  .census-text-pair, .census-histograms { grid-template-columns: 1fr; }
}
"""

js_content = r"""
(function(){
  const PASSAGES = [
    // Austen: Pride and Prejudice opening pages, abbreviated
    "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood this truth is so well fixed in the minds of the surrounding families that he is considered as the rightful property of someone or other of their daughters. My dear Mr Bennet said his lady to him one day have you heard that Netherfield Park is let at last Mr Bennet replied that he had not. But it is returned she for Mrs Long has just been here and she told me all about it. Mr Bennet made no answer. Do not you want to know who has taken it cried his wife impatiently. You want to tell me and I have no objection to hearing it.",
    // Melville: Moby-Dick opening
    "Call me Ishmael. Some years ago never mind how long precisely having little or no money in my purse and nothing particular to interest me on shore I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth whenever it is a damp drizzly November in my soul whenever I find myself involuntarily pausing before coffin warehouses and bringing up the rear of every funeral I meet and especially whenever my hypos get such an upper hand of me that it requires a strong moral principle to prevent me from deliberately stepping into the street and methodically knocking peoples hats off then I account it high time to get to sea as soon as I can.",
    // Madison: Federalist No. 10
    "Among the numerous advantages promised by a well constructed Union none deserves to be more accurately developed than its tendency to break and control the violence of faction. The friend of popular governments never finds himself so much alarmed for their character and fate as when he contemplates their propensity to this dangerous vice. He will not fail therefore to set a due value on any plan which without violating the principles to which he is attached provides a proper cure for it. By a faction I understand a number of citizens whether amounting to a majority or a minority of the whole who are united and actuated by some common impulse of passion or of interest adverse to the rights of other citizens or to the permanent and aggregate interests of the community.",
    // Transliterated Arabic from al-Mutanabbi (approximate) — letter frequencies will shift toward Arabic profile
    "Ala ya layla ma ahlaki wa atyaba ma fiki min al sukoon wa al hawa al alil. Ya layla aslamtu nafsi laki wa rajaytu min al falaki al kareem an yablugha bi sallami ila al subhi. Wa kayfa al subhu wa ana al ghareebu wa ahli baeed wa al watan ahuwa min wara al bihar wa al jibal. Wa kayfa al nawmu wa al qalbu yakhfuqu min al shawqi wa al ayni la yarghabu fi al ghamdi illa li yara fi al manami wajha man yuhibbu. Wa lakinni saabir ala al firaq fa inna al firaq lahu nihaya wa al wisalu ba ada al firaq ahla wa atyaba min kulli wisal. Ya layla aslamtu nafsi laki wa atamannu an tatula laki yadu al subhi ba ada hadha al sukoon."
  ];

  function clean(s){ return s.toUpperCase().replace(/[^A-Z]/g, ''); }

  function counts(s){
    const c = {};
    for (let i = 0; i < 26; i++) c[String.fromCharCode(65+i)] = 0;
    for (const ch of s) if (c[ch] !== undefined) c[ch]++;
    return c;
  }

  function shuffle(arr){
    for (let i = arr.length - 1; i > 0; i--){
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function makeCipher(){
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    const shuffled = shuffle(letters.slice());
    const m = {};
    for (let i = 0; i < 26; i++) m[letters[i]] = shuffled[i];
    return m;
  }

  function applyCipher(s, cipher){
    let out = '';
    for (const ch of s){
      const upper = ch.toUpperCase();
      if (cipher[upper]){
        out += (ch === upper) ? cipher[upper] : cipher[upper].toLowerCase();
      } else {
        out += ch;
      }
    }
    return out;
  }

  function rankedLetters(c){
    const arr = Object.entries(c).map(([k, v]) => ({letter: k, count: v}));
    arr.sort((a, b) => b.count - a.count || a.letter.localeCompare(b.letter));
    return arr;
  }

  function renderHist(elementId, ranked, topLetter){
    const el = document.getElementById(elementId);
    el.innerHTML = '';
    const max = Math.max(1, ...ranked.map(r => r.count));
    for (const r of ranked){
      const bar = document.createElement('div');
      bar.className = 'census-bar' + (r.letter === topLetter ? ' census-bar-top' : '');
      const fill = document.createElement('div');
      fill.className = 'census-bar-fill';
      const height = (r.count / max) * 130;
      fill.style.height = height + 'px';
      const label = document.createElement('div');
      label.className = 'census-bar-label';
      label.textContent = r.letter;
      bar.appendChild(fill);
      bar.appendChild(label);
      el.appendChild(bar);
    }
  }

  function decodeByGreedyMatch(cipherText, plainCounts, cipherCounts){
    const plainRanked = rankedLetters(plainCounts).map(r => r.letter);
    const cipherRanked = rankedLetters(cipherCounts).map(r => r.letter);
    const guess = {};
    for (let i = 0; i < 26; i++) guess[cipherRanked[i]] = plainRanked[i];
    let out = '';
    for (const ch of cipherText){
      const upper = ch.toUpperCase();
      if (guess[upper]){
        out += (ch === upper) ? guess[upper] : guess[upper].toLowerCase();
      } else {
        out += ch;
      }
    }
    return {decoded: out, guess: guess};
  }

  function accuracy(cipher, guess){
    let correct = 0;
    for (const plain of Object.keys(cipher)){
      const cipherLetter = cipher[plain];
      if (guess[cipherLetter] === plain) correct++;
    }
    return correct;
  }

  let state = {
    passageIdx: 0,
    cipher: null,
    plainText: '',
    cipherText: '',
    cleaned: '',
    cleanedCipher: '',
    plainCounts: null,
    cipherCounts: null,
    solved: false
  };

  function render(){
    document.getElementById('census-plain').textContent = state.plainText;
    document.getElementById('census-cipher').textContent = state.cipherText;

    const plainRanked = rankedLetters(state.plainCounts);
    const cipherRanked = rankedLetters(state.cipherCounts);
    const topPlain = plainRanked[0].letter;
    const topCipher = cipherRanked[0].letter;

    renderHist('census-hist-plain', plainRanked, topPlain);
    renderHist('census-hist-cipher', cipherRanked, topCipher);

    const keyStr = 'A&rarr;' + state.cipher['A'];
    document.getElementById('census-key').innerHTML = keyStr;
    document.getElementById('census-count').textContent = state.cleaned.length;
    document.getElementById('census-top-plain').textContent =
      topPlain + ' (' + ((plainRanked[0].count / state.cleaned.length) * 100).toFixed(1) + '%)';
    document.getElementById('census-top-cipher').textContent =
      topCipher + ' (' + ((cipherRanked[0].count / state.cleaned.length) * 100).toFixed(1) + '%)';

    if (state.solved){
      const result = decodeByGreedyMatch(state.cipherText, state.plainCounts, state.cipherCounts);
      document.getElementById('census-decoded').textContent = result.decoded;
      const acc = accuracy(state.cipher, result.guess);
      document.getElementById('census-accuracy').textContent = acc + ' / 26 letters matched';
    } else {
      document.getElementById('census-decoded').textContent =
        'Press "Match by frequency" to decode using al-Kindi\'s method.';
      document.getElementById('census-accuracy').textContent = '—';
    }
  }

  function loadPassage(idx){
    state.passageIdx = idx;
    state.plainText = PASSAGES[idx];
    state.cleaned = clean(state.plainText);
    state.plainCounts = counts(state.cleaned);
    rerollCipher();
  }

  function rerollCipher(){
    state.cipher = makeCipher();
    state.cipherText = applyCipher(state.plainText, state.cipher);
    state.cleanedCipher = clean(state.cipherText);
    state.cipherCounts = counts(state.cleanedCipher);
    state.solved = false;
    render();
  }

  document.getElementById('census-passage').addEventListener('change', e => {
    loadPassage(parseInt(e.target.value, 10));
  });
  document.getElementById('census-reroll').addEventListener('click', rerollCipher);
  document.getElementById('census-solve').addEventListener('click', () => {
    state.solved = true;
    render();
  });
  document.getElementById('census-reset').addEventListener('click', () => {
    document.getElementById('census-passage').value = '0';
    loadPassage(0);
  });

  loadPassage(0);
})();
"""

result = experiment_create(
    slug=slug,
    title=title,
    description=description,
    tags=tags,
    html_content=html_content,
    css_content=css_content,
    js_content=js_content,
)
print(result)
