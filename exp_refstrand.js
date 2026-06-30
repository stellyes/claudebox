(function(){
  var N = 12;
  var mode = 'legible';
  var damage = 6;
  var repaired = false;

  var strip = document.getElementById('rs-strip');
  var elHealth = document.getElementById('rs-health');
  var elScars = document.getElementById('rs-scars');
  var elVerdict = document.getElementById('rs-verdict');
  var elDamage = document.getElementById('rs-damage');
  var elDamageVal = document.getElementById('rs-damage-val');
  var elCaption = document.getElementById('rs-caption');

  var CAPTIONS = {
    legible: "<strong>Legible.</strong> The reference is readable, so every fault is located and rewritten. Health returns to 100% no matter how much you broke &mdash; like homologous repair against a sister chromatid, or a phone with its schematic.",
    notemplate: "<strong>No template.</strong> You can detect the breaks but have no reference to read them against, so repair is a guess. It leaves permanent scars &mdash; like non-homologous end joining, lossy by necessity.",
    paired: "<strong>Paired.</strong> The genuine part exists, but the device refuses to read it as legitimate, so the repair is rejected outright. It stays bricked &mdash; like parts pairing, or an obfuscated binary."
  };

  // Deterministic repair model — mirrors /tmp reference truth table
  function computeStates(){
    var state = [];
    var i;
    for(i=0;i<N;i++) state.push(i < damage ? 'broken' : 'good');
    if(!repaired) return state;
    for(i=0;i<damage;i++){
      if(mode==='legible'){ state[i]='good'; }
      else if(mode==='paired'){ /* rejected: stays broken */ }
      else if(mode==='notemplate'){ state[i] = (i%2===0) ? 'good' : 'scar'; }
    }
    return state;
  }
  function health(state){
    var g=0; for(var i=0;i<N;i++) if(state[i]==='good') g++;
    return Math.round(100*g/N);
  }
  function scars(state){
    var s=0; for(var i=0;i<N;i++) if(state[i]==='scar') s++;
    return s;
  }
  function verdict(){
    if(!repaired) return '—';
    if(mode==='legible') return 'REPAIRED';
    if(mode==='paired') return 'BRICKED';
    return 'SCARRED';
  }

  function render(){
    var state = computeStates();
    strip.innerHTML='';
    for(var i=0;i<N;i++){
      var c=document.createElement('div');
      c.className='rs-cell rs-'+state[i];
      c.textContent = state[i]==='good' ? 'OK' : (state[i]==='scar' ? 'SCAR' : '✕');
      strip.appendChild(c);
    }
    elHealth.textContent = health(state)+'%';
    elScars.textContent = scars(state);
    elVerdict.textContent = verdict();
    elDamageVal.textContent = damage;
    elCaption.innerHTML = repaired ? CAPTIONS[mode] : 'Break some components, then attempt a repair.';
  }

  // controls
  elDamage.addEventListener('input', function(){
    damage = parseInt(this.value,10); repaired=false; render();
  });
  var modeBtns = document.querySelectorAll('.rs-mode');
  modeBtns.forEach(function(b){
    b.addEventListener('click', function(){
      modeBtns.forEach(function(x){x.classList.remove('rs-active');});
      b.classList.add('rs-active');
      mode = b.getAttribute('data-mode'); repaired=false; render();
    });
  });
  document.getElementById('rs-repair').addEventListener('click', function(){
    repaired=true; render();
  });
  document.getElementById('rs-reset').addEventListener('click', function(){
    repaired=false; render();
  });

  // verification hooks
  window.__repair = {
    setMode:function(m){mode=m;repaired=false;modeBtns.forEach(function(x){x.classList.toggle('rs-active', x.getAttribute('data-mode')===m);});render();},
    setDamage:function(d){damage=d;repaired=false;elDamage.value=d;render();},
    repair:function(){repaired=true;render();},
    reset:function(){repaired=false;render();},
    health:function(){return health(computeStates());},
    scars:function(){return scars(computeStates());},
    verdict:verdict,
    state:function(){return {mode:mode,damage:damage,repaired:repaired,health:health(computeStates()),scars:scars(computeStates()),verdict:verdict()};}
  };

  render();
})();
