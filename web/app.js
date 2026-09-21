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
      if (v.ok) validation = (await v.json()).summary;
    } catch (_) { /* validation is optional */ }
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

function evidenceRows(paths) {
  return paths.map((p) => {
    const ev = p.evidence.slice(0, 5).map((e) => `
      <div class="ev">
        <span class="lbl">${esc(EVIDENCE_LABELS[e.id] || e.id)}</span>
        <span class="bar"><i style="width:${Math.round(e.score * 100)}%"></i></span>
        <span class="val">${e.score.toFixed(2)}</span>
      </div>`).join('');
    return `
      <div class="path">
        <span class="node gene">${esc(p.gene)}</span>
        <span class="arrow">associated with →</span>
        <span class="node">disease</span>
      </div>
      <p class="pathmeta">${esc(p.geneName || '')} · combined association ${p.assoc.toFixed(2)}
        · ${p.drugsOnGene} approved drug${p.drugsOnGene === 1 ? '' : 's'} hit this gene</p>
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
  return `
    <div class="card">
      <button class="chead" aria-expanded="false" data-card="${i}">
        <span class="rank">${d.rank}</span>
        <span class="cmain">
          <span class="dname">${esc(d.name)}</span>
          <span class="dfor">${esc(approved)}</span>
        </span>
        <span class="score">
          <span class="bar"><i style="width:${Math.round(d.score * 100)}%"></i></span>
          <span class="snum">${d.score.toFixed(2)}</span>
          <svg class="caret" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
        </span>
      </button>
      <div class="cbody" id="body-${i}">
        <div class="path">
          <span class="node drug">${esc(d.name)}</span>
          <span class="arrow">targets →</span>
          <span class="node gene">${esc(d.paths[0] ? d.paths[0].gene : '?')}</span>
          <span class="arrow">associated with →</span>
          <span class="node">${esc(currentName)}</span>
        </div>
        <p class="pathmeta">This drug hits ${d.geneCount} gene${d.geneCount === 1 ? '' : 's'} overall.
          ${d.paths.length} of them ${d.paths.length === 1 ? 'is' : 'are'} linked to this disease.</p>
        ${evidenceRows(d.paths)}
        ${moa}
      </div>
    </div>`;
}

let currentName = '';

function render(r) {
  currentName = r.name;
  const thin = r.candidates.length < 5 || r.genesWithDrugs < 4;
  const v = validation
    ? `<div class="vbadge">Tested against ${validation.knownPairsEvaluated} drug&ndash;disease pairs that
       are already known to work: for <strong>${validation.diseasesWhereTopCandidateIsKnown} of
       ${validation.diseasesEvaluated}</strong> diseases the single highest-ranked candidate is a real
       treatment for that disease, and known treatments land in the top 10% of candidates
       <strong>${validation.enrichmentOverChanceTopTen}&times;</strong> as often as chance would give.
       Median position ${pct(validation.medianPercentile)}, where random would be 50%.</div>` : '';

  stage.innerHTML = `
    <div class="dhead">
      <h2>${esc(r.name)}</h2>
      <span class="tag ${r.rarity}">${r.rarity === 'rare' ? 'rare disease' : 'common disease'}</span>
    </div>
    <p class="dmeta"><b>${r.associatedGeneCount.toLocaleString()}</b> associated genes ·
      top <b>${r.genesScored}</b> scored · <b>${r.genesWithDrugs}</b> of those have an approved drug ·
      <b>${r.candidatesConsidered}</b> candidates ranked ·
      <b>${r.knownDrugCount}</b> known drugs held out</p>
    ${v}
    ${thin ? `<div class="thin">Thin result. Only ${r.genesWithDrugs} of the top
      ${r.genesScored} genes linked to this disease are hit by any approved drug, so there is
      little for the method to work with. That is the honest answer for this disease, and it is
      exactly the situation that makes these conditions hard to treat.</div>` : ''}
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
