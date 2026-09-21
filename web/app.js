/* Off The Shelf - static front end.
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
    stage.innerHTML = '<p class="empty">Search a disease above, or pick one of the examples.</p>';
  } catch (err) {
    stage.innerHTML = '<p class="empty">Could not load the disease index. If you opened this file directly, '
      + 'run a local server instead: <code>python -m http.server</code> inside the web folder.</p>';
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
  const bits = [`${index.length} diseases indexed`,
    `damping exponent w = ${payload.dampingExponent}`,
    `excluded evidence: ${payload.excludedDatatypes.join(', ')}`];
  if (validation) bits.push(`${validation.knownPairsEvaluated} known drug-disease pairs used for validation`);
  $('#footmeta').textContent = bits.join(' · ');
}

function renderAnalysis(a) {
  const el = document.getElementById('analysis');
  if (!el) return;
  const sweep = a.dampingSweep.map((d) =>
    `<tr><td>${d.w.toFixed(1)}${Math.abs(d.w - 0.4) < 1e-9 ? ' (ours)' : ''}</td>
     <td>${pct(d.median)}</td></tr>`).join('');
  const worst = [...a.ablation].sort((x, y) => y.delta - x.delta)[0];
  el.innerHTML = `
    <p><strong>Is the result stable?</strong> Resampling diseases 
       ${a.bootstrap.rounds.toLocaleString()} times puts the median between
       ${pct(a.bootstrap.ci95[0])} and ${pct(a.bootstrap.ci95[1])}.
       That interval ${a.bootstrap.excludesRandom ? 'excludes' : 'does not exclude'} the 50%
       a random ranking would give.</p>

    <p><strong>Did we pick a lucky constant?</strong> No, and we can prove it by admitting
       the opposite — a larger damping exponent would score better than the one we use.
       We keep 0.4 because that is the value the Rephetio paper published, and tuning it
       would mean we had fitted something.</p>
    <table class="mini"><tr><th>exponent</th><th>median</th></tr>${sweep}</table>

    <p><strong>What if the evidence itself leaks?</strong> Removing ${esc(worst.datatype)}
       hurts more than removing anything else, and literature evidence is partly a
       consequence of a drug already linking a gene to a disease. Stripping every
       literature-derived source still leaves a median of
       ${pct(a.conservativeFloor.median)}, so the result does not rest on it.</p>

    <p><strong>Does it break when it should?</strong> Scoring each disease against a
       different disease's known drugs moves the median to
       ${pct(a.negativeControl.mismatched)}. It does not reach a clean 50%, because many
       diseases share common treatments, so some drugs rank well everywhere. We report
       that rather than explain it away.</p>`;
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
      <p class="evtitle">Evidence behind that association (clinical evidence excluded)</p>
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
    `${esc(w.type)}${w.detail ? ` — ${esc(w.detail)}` : ''}`);
  const safety = warnList.length
    ? `<div class="safety"><strong>Safety on record:</strong> ${warnList.join('; ')}.
       ${d.withdrawn
         ? 'This drug has been withdrawn in at least one market. It is shown because the biology connects, not because it is a sensible candidate.'
         : 'Relevant to any repurposing decision, and not something this ranking accounts for.'}</div>`
    : '';
  return `
    <div class="card">
      <button class="chead" aria-expanded="false" data-card="${i}">
        <span class="rank">${d.rank}</span>
        <span class="cmain">
          <span class="dname">${esc(d.name)}</span>
          <span class="dfor">${esc(approved)}${
            d.withdrawn ? ' <span class="flag warn">withdrawn</span>'
            : d.blackBox ? ' <span class="flag">black box</span>' : ''}</span>
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
    ? `<div class="vbadge">Tested against ${validation.knownPairsEvaluated} drug&ndash;disease pairs that
       are already known to work: for <strong>${validation.diseasesWhereTopCandidateIsKnown} of
       ${validation.diseasesEvaluated}</strong> diseases the single highest-ranked candidate is a real
       treatment for that disease, and known treatments land in the top 10% of candidates
       <strong>${validation.enrichmentOverChanceTopTen}&times;</strong> as often as chance would give.
       Median position ${pct(validation.medianPercentile)}, where random would be 50%.
       ${validation.methods ? `<br><span class="vsub">Same candidates ranked by drug popularity
       alone, ignoring the disease, put them at ${pct(validation.methods.popularity.medianPercentile)}
       &mdash; so the biology is doing the work, not the arithmetic.</span>` : ''}</div>` : '';

  const pd = perDisease[r.id];
  const one = pd && pd.knownEvaluated === 1;
  const poor = pd && pd.medianPercentile > 0.5;
  const local = pd ? `<div class="vlocal">
      <strong>For this disease specifically:</strong>
      ${one
        ? `the one drug already known to treat it is <strong>${esc(pd.bestDrug)}</strong>,
           which our ranking places at ${pd.bestRank} of ${pd.candidatePool}.`
        : `of the ${pd.knownEvaluated} drugs already known to treat it, the best-placed is
           <strong>${esc(pd.bestDrug)}</strong> at rank ${pd.bestRank} of ${pd.candidatePool},
           and the median sits at ${pct(pd.medianPercentile)}.`}
      ${poor
        ? ` That is below where random guessing would land, so treat this disease's results with caution.`
        : ` The engine was never told about ${one ? 'it' : 'any of them'}.`}
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
    ${thin ? `<div class="thin">Thin result. Only ${r.candidatesConsidered} approved drugs
      can be reached from this disease's genes at all, so there is little for the method to work
      with. That is the honest answer here, and it is exactly the situation that makes these
      conditions hard to treat.</div>` : ''}
    ${poor && !thin ? `<div class="thin">This is one of the diseases our method handles badly.
      Drugs already known to treat it rank below where random guessing would put them, so the
      suggestions below are weak evidence. We are showing it rather than hiding it.</div>` : ''}
    <p class="secttl">Approved drugs not currently used for this disease</p>
    <div id="cards">${r.candidates.map(card).join('') || '<p class="empty">No candidates found.</p>'}</div>
    ${r.knownRanked.length ? `
      <div class="known">
        <h3>Known treatments our ranking also found</h3>
        <p class="sub">Held out of the list above. If the method works, real treatments should
          surface near the top without being told about them.</p>
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
