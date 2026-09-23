/* Drug Match - static front end.
   Reads only precomputed JSON, so the whole app works with no network. */

const EVIDENCE_LABELS = {
  genetic_association: 'Genetic association',
  genetic_literature: 'Genetic literature',
  somatic_mutation: 'Somatic mutation',
  known_drug: 'Known drug',
  affected_pathway: 'Affected pathway',
  literature: 'Text mining',
  animal_model: 'Animal model',
  rna_expression: 'RNA expression',
};

const EXAMPLES = [
  'MONDO_0010679', 'MONDO_0010726', 'MONDO_0007739',
  'MONDO_0004976', 'MONDO_0008753',
];

const $ = (s) => document.querySelector(s);
const stage = $('#stage');
let index = [];
let validation = null;
const perDisease = {};
let cursor = -1;

const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g,
  (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const pct = (x) => Math.round(x * 100) + '%';

async function boot() {
  try {
    const res = await fetch('data/index.json');
    if (!res.ok) throw new Error('index.json ' + res.status);
    const payload = await res.json();
    index = payload.diseases;
    try {
      const v = await fetch('data/validation.json');
      if (v.ok) {
        const payload = await v.json();
        validation = payload.summary;
        (payload.perDisease || []).forEach((d) => { perDisease[d.id] = d; });
      }
    } catch (_) { /* validation is optional */ }
    try {
      const a = await fetch('data/analysis.json');
      if (a.ok) renderAnalysis(await a.json());
    } catch (_) { /* analysis is optional */ }
    renderChips();
    renderFootMeta(payload);
    renderHeroStats(payload);
    stage.innerHTML = '<p class="empty">Search a disease above, or try one of the examples below.</p>';
  } catch (err) {
    stage.innerHTML = '<p class="empty">We could not load the disease index. If you opened this file directly, '
      + 'run a local server instead. Try <code>python -m http.server</code> inside the web folder.</p>';
    console.error(err);
  }
}

function renderChips() {
  const chips = EXAMPLES.map((id) => index.find((d) => d.id === id)).filter(Boolean);
  $('#chips').innerHTML = chips.map((d) =>
    `<button class="chip" data-id="${d.id}">${esc(d.name)}</button>`).join('');
  $('#chips').addEventListener('click', (e) => {
    const b = e.target.closest('.chip');
    if (b) select(b.dataset.id);
  });
}

function renderFootMeta(payload) {
  // The browsable set and the measured set differ, and saying so matters:
  // quoting a validation figure from thousands of diseases beside a search box
  // covering hundreds would be quietly misleading.
  const bits = [`${index.length} diseases browsable here`];
  if (payload.diseasesInCache && payload.diseasesInCache > index.length) {
    bits.push(`${payload.diseasesInCache} scored and measured`);
  }
  bits.push(...
  [`damping exponent w = ${payload.dampingExponent}`,
    `excluded evidence: ${payload.excludedDatatypes.join(', ')}`]);
  if (validation) bits.push(`${validation.knownPairsEvaluated} known drug-disease pairs used for validation`);
  $('#footmeta').textContent = bits.join(' · ');
}

function renderHeroStats(payload) {
  // Real numbers standing in for the marketing stats a hero section usually
  // carries, pulled from the same data the rest of the page reads. They
  // can never drift out of sync with what the site actually measures.
  const total = payload.diseasesInCache || index.length;
  const hc = document.getElementById('heroCount');
  if (hc) hc.textContent = `${total.toLocaleString()} diseases scored`;
  const set = (id, text) => { const el = document.getElementById(id); if (el && text != null) el.textContent = text; };
  set('statDiseases', total.toLocaleString());
  if (validation) {
    set('statPairs', validation.knownPairsEvaluated.toLocaleString());
    if (validation.rareOnly) set('statRare', pct(validation.rareOnly.medianPercentile));
  }
}

function renderAnalysis(a) {
  const el = document.getElementById('analysis');
  if (!el) return;
  const sweep = a.dampingSweep.map((d) =>
    `<tr><td>${d.w.toFixed(1)}${Math.abs(d.w - 0.4) < 1e-9 ? ' (ours)' : ''}</td>
     <td>${pct(d.median)}</td></tr>`).join('');
  const worst = [...a.ablation].sort((x, y) => y.delta - x.delta)[0];
  el.innerHTML = `
    <p><strong>Stability.</strong> We resampled diseases ${a.bootstrap.rounds.toLocaleString()} times.
       The median landed between ${pct(a.bootstrap.ci95[0])} and ${pct(a.bootstrap.ci95[1])} every time.
       That range ${a.bootstrap.excludesRandom ? 'excludes' : 'does not exclude'} the 50% a random
       ranking would produce.</p>

    <p><strong>The damping constant.</strong> A larger exponent scores better than the 0.4 we use.
       We kept 0.4 anyway, because it is the value Rephetio published. Tuning it upward would mean
       we fitted the model to our own test, and we did not want that.</p>
    <table class="mini"><tr><th>exponent</th><th>median</th></tr>${sweep}</table>

    <p><strong>Leaking evidence.</strong> Removing ${esc(worst.datatype)} hurts the score more than
       removing any other evidence type. Literature evidence partly reflects a drug already linked
       to a gene and a disease, so that is a real concern. We stripped every literature-derived source
       anyway. The median still landed at ${pct(a.conservativeFloor.median)}, well clear of chance.</p>

    <p><strong>The negative control.</strong> We scored each disease against a different disease's
       known drugs. The median moved to ${pct(a.negativeControl.mismatched)}, not a clean 50%, because
       many diseases share common treatments and some drugs rank well everywhere. We report that number
       as it stands, not explained away.</p>`;
}

/* ---------- search ---------- */

const q = $('#q');
const suggest = $('#suggest');

function matches(term) {
  const t = term.trim().toLowerCase();
  if (!t) return [];
  return index.filter((d) => d.name.toLowerCase().includes(t)).slice(0, 8);
}

function drawSuggestions(list) {
  if (!list.length) { suggest.hidden = true; return; }
  suggest.innerHTML = list.map((d, i) =>
    `<li role="option" data-id="${d.id}" aria-selected="${i === cursor}">`
    + `<span>${esc(d.name)}</span><span class="n">${d.candidates} candidates</span></li>`).join('');
  suggest.hidden = false;
}

q.addEventListener('input', () => { cursor = -1; drawSuggestions(matches(q.value)); });
q.addEventListener('keydown', (e) => {
  const items = [...suggest.querySelectorAll('li')];
  if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
    e.preventDefault();
    if (!items.length) return;
    cursor = e.key === 'ArrowDown'
      ? (cursor + 1) % items.length
      : (cursor - 1 + items.length) % items.length;
    drawSuggestions(matches(q.value));
  } else if (e.key === 'Enter') {
    const pick = items[cursor] || items[0];
    if (pick) select(pick.dataset.id);
  } else if (e.key === 'Escape') {
    suggest.hidden = true;
  }
});
suggest.addEventListener('click', (e) => {
  const li = e.target.closest('li');
  if (li) select(li.dataset.id);
});
document.addEventListener('click', (e) => {
  if (!e.target.closest('.searchrow')) suggest.hidden = true;
});

/* ---------- render a disease ---------- */

async function select(id) {
  suggest.hidden = true;
  const entry = index.find((d) => d.id === id);
  if (entry) q.value = entry.name;
  stage.innerHTML = '<p class="loading">Scoring…</p>';
  try {
    const res = await fetch(`data/results/${id}.json`);
    if (!res.ok) throw new Error('missing result file');
    render(await res.json());
    stage.scrollIntoView({ behavior: 'smooth', block: 'start' });
  } catch (err) {
    stage.innerHTML = '<p class="empty">No results file for that disease.</p>';
    console.error(err);
  }
}

function chain(drugName, p, diseaseName) {
  const arrow = (t) => `<span class="arrow">${t} →</span>`;
  const bits = [`<span class="node drug">${esc(drugName)}</span>`, arrow('targets')];
  if (p && p.hops === 3) {
    bits.push(`<span class="node gene">${esc(p.via)}</span>`,
      arrow(`interacts ${p.viaScore}`));
  }
  bits.push(`<span class="node gene">${esc(p ? p.gene : '?')}</span>`,
    arrow('associated with'), `<span class="node">${esc(diseaseName)}</span>`);
  return `<div class="path">${bits.join('')}</div>`;
}

function evidenceRows(paths, drugName) {
  return paths.map((p) => {
    const ev = p.evidence.slice(0, 5).map((e) => `
      <div class="ev">
        <span class="lbl">${esc(EVIDENCE_LABELS[e.id] || e.id)}</span>
        <span class="bar"><i style="width:${Math.round(e.score * 100)}%"></i></span>
        <span class="val">${e.score.toFixed(2)}</span>
      </div>`).join('');
    const via = p.hops === 3
      ? ` · reached through ${esc(p.via)}, which interacts with it at ${p.viaScore}`
      : '';
    return `
      ${chain(drugName, p, currentName)}
      <p class="pathmeta">${esc(p.geneName || '')} · combined association ${p.assoc.toFixed(2)}
        · ${p.drugsOnGene} approved drug${p.drugsOnGene === 1 ? '' : 's'} hit the targeted gene${via}</p>
      <p class="evtitle">Evidence behind that link. Clinical evidence excluded.</p>
      ${ev}`;
  }).join('<hr style="border:0;border-top:1px solid var(--line);margin:16px 0">');
}

function card(d, i) {
  const approved = d.approvedFor.length
    ? 'Approved for ' + d.approvedFor.slice(0, 2).join(', ')
      + (d.indicationCount > 2 ? ` and ${d.indicationCount - 2} more` : '')
    : 'Approved drug';
  const moa = d.mechanisms.length
    ? `<p class="moa"><strong>Mechanism:</strong> ${esc(d.mechanisms.join('; '))}</p>` : '';
  const warnList = (d.warnings || []).map((w) =>
    `${esc(w.type)}${w.detail ? `: ${esc(w.detail)}` : ''}`);
  const safety = warnList.length
    ? `<div class="safety"><strong>Safety on record:</strong> ${warnList.join('; ')}.
       ${d.withdrawn
         ? 'A regulator withdrew this drug in at least one market. We show it because the biology connects. That does not make it a sensible candidate.'
         : 'Weigh this before you consider repurposing it. Our ranking does not account for it.'}</div>`
    : '';
  const noveltyFlag = d.possiblyAlreadyApproved
    ? `<div class="safety"><strong>This may already be approved for this disease.</strong>
       Its own record lists "${esc(d.possiblyAlreadyApproved)}" as an approved indication, which
       overlaps this disease's name. Our known-drug list missed the connection. See
       <a href="https://github.com/aryanyaksh-art/drug-match#is-novel-always-actually-novel-one-confirmed-case-says-no" target="_blank" rel="noopener">why, and one confirmed example</a>.
       Treat the novel label here with caution.</div>`
    : '';
  return `
    <div class="card">
      <button class="chead" aria-expanded="false" data-card="${i}">
        <span class="rank">${d.rank}</span>
        <span class="cmain">
          <span class="dname">${esc(d.name)}</span>
          <span class="dfor">${esc(approved)}${
            d.withdrawn ? ' <span class="flag warn">withdrawn</span>'
            : d.blackBox ? ' <span class="flag">black box</span>' : ''}${
            d.possiblyAlreadyApproved ? ' <span class="flag warn">check: maybe not novel</span>' : ''
          }</span>
        </span>
        <span class="score">
          <span class="bar"><i style="width:${Math.round(d.score * 100)}%"></i></span>
          <span class="snum">${d.score.toFixed(2)}</span>
          <svg class="caret" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
        </span>
      </button>
      <div class="cbody" id="body-${i}">
        <p class="pathmeta">This drug hits ${d.geneCount} gene${d.geneCount === 1 ? '' : 's'} overall.
          Showing its ${d.paths.length} strongest route${d.paths.length === 1 ? '' : 's'} into this disease.</p>
        ${evidenceRows(d.paths, d.name)}
        ${moa}
        ${safety}
        ${noveltyFlag}
      </div>
    </div>`;
}

let currentName = '';

function render(r) {
  currentName = r.name;
  // Two separate honesty signals, which used to be conflated. "Thin" is about
  // how much the method had to work with; "poor" is about whether it actually
  // performed. A disease can have a small pool and still rank its real
  // treatment first, which is exactly what alkaptonuria does.
  const thin = r.candidatesConsidered < 25;
  const v = validation
    ? `<div class="vbadge">We tested this against ${validation.knownPairsEvaluated} drug-disease pairs
       already known to work. For <strong>${validation.diseasesWhereTopCandidateIsKnown} of
       ${validation.diseasesEvaluated}</strong> diseases, our top candidate is already a real treatment.
       Known treatments land in the top 10% of candidates
       <strong>${validation.enrichmentOverChanceTopTen}&times;</strong> as often as chance predicts.
       Median position ${pct(validation.medianPercentile)}, where random guessing lands at 50%.
       ${validation.methods ? `<br><span class="vsub">We also ranked the same candidates by drug
       popularity alone, ignoring the disease entirely. That method put them at
       ${pct(validation.methods.popularity.medianPercentile)}. The biology drives our ranking.
       Popularity alone would not.</span>` : ''}</div>` : '';

  const pd = perDisease[r.id];
  const one = pd && pd.knownEvaluated === 1;
  const poor = pd && pd.medianPercentile > 0.5;
  const local = pd ? `<div class="vlocal">
      <strong>For this disease:</strong>
      ${one
        ? `the one known treatment is <strong>${esc(pd.bestDrug)}</strong>. Our ranking places it
           ${pd.bestRank} of ${pd.candidatePool}.`
        : `${pd.knownEvaluated} drugs already treat this disease. The best-placed,
           <strong>${esc(pd.bestDrug)}</strong>, ranks ${pd.bestRank} of ${pd.candidatePool}, with a
           median of ${pct(pd.medianPercentile)}.`}
      ${poor
        ? ` That sits below random guessing. Treat these results with caution.`
        : ` We never told the engine about ${one ? 'it' : 'them'}.`}
    </div>` : '';

  stage.innerHTML = `
    <div class="dhead">
      <h2>${esc(r.name)}</h2>
      <span class="tag ${r.rarity}">${
        r.rarity === 'rare' ? 'rare disease'
        : r.rarity === 'common' ? 'common disease'
        : 'auto-selected'}</span>
    </div>
    <p class="dmeta"><b>${r.associatedGeneCount.toLocaleString()}</b> associated genes ·
      top <b>${r.genesScored}</b> scored · <b>${r.genesWithDrugs}</b> of those have an approved drug ·
      <b>${r.candidatesConsidered}</b> candidates ranked ·
      <b>${r.knownDrugCount}</b> known drug${r.knownDrugCount === 1 ? '' : 's'} held out</p>
    ${local}
    ${v}
    ${thin ? `<div class="thin">Thin result. Only ${r.candidatesConsidered} approved drugs connect
      to this disease's genes at all. The method has little to work with here. That is also why
      these conditions are hard to treat in the first place.</div>` : ''}
    ${poor && !thin ? `<div class="thin">Our method handles this disease badly. Known treatments
      rank below where random guessing would put them. Treat the suggestions below as weak evidence.
      We are showing you the failure, not hiding it.</div>` : ''}
    <p class="secttl">Approved drugs not used for this disease yet</p>
    <div id="cards">${r.candidates.map(card).join('') || '<p class="empty">No candidates found.</p>'}</div>
    ${r.knownRanked.length ? `
      <div class="known">
        <h3>Known treatments we found anyway</h3>
        <p class="sub">We held these out of the list above. If the method works, it should surface
          real treatments near the top without ever being told about them.</p>
        ${r.knownRanked.map((k) => `<div class="krow"><span>${esc(k.name)}</span>
          <span>rank ${k.rank} of ${r.candidatesConsidered}</span></div>`).join('')}
      </div>` : ''}`;

  $('#cards').addEventListener('click', (e) => {
    const btn = e.target.closest('.chead');
    if (!btn) return;
    const body = document.getElementById('body-' + btn.dataset.card);
    const open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    body.classList.toggle('open', !open);
  });
}

boot();
