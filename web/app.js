/* Drug Match - static front end.
   Reads only precomputed JSON, so the whole app works with no network.
   Routes: "#/" is the home page, "#/d/<disease id>" is a disease's results. */

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

const RARITY_LABELS = { rare: 'Rare disease', common: 'Common disease', other: 'Auto-selected' };

const EXAMPLES = [
  'MONDO_0008753', 'MONDO_0010726', 'MONDO_0010679',
  'MONDO_0007739', 'MONDO_0004976',
];

const NOVELTY_URL = 'https://github.com/aryanyaksh-art/drug-match#is-novel-always-actually-novel-one-confirmed-case-says-no';

const $ = (s, root = document) => root.querySelector(s);
const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g,
  (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const cap = (s) => (s ? s[0].toUpperCase() + s.slice(1) : s);
const pct = (x) => Math.round(x * 100) + '%';
const plural = (n, word, many = word + 's') => `${n.toLocaleString()} ${n === 1 ? word : many}`;

const ICONS = {
  warn: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
  info: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
  back: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
  caret: '<svg class="caret" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
  search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
};

const state = {
  index: [],
  byId: {},
  meta: null,
  validation: null,
  perDisease: {},
  trials: {},
  results: {},
  homeScroll: 0,
  current: null,
  open: new Set(),
  filter: '',
  showKnown: true,
  hideFlagged: false,
};

/* ---------- boot ---------- */

async function getJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} ${res.status}`);
  return res.json();
}

async function boot() {
  try {
    const payload = await getJSON('data/index.json');
    state.meta = payload;
    state.index = payload.diseases;
    state.index.forEach((d) => { state.byId[d.id] = d; });
  } catch (err) {
    console.error(err);
    $('#browseGrid').innerHTML = '<p class="empty">We could not load the disease index. If you opened this file directly, '
      + 'run a local server instead: <code>python -m http.server</code> inside the web folder.</p>';
    return;
  }

  // Optional datasets. The page still works if any of these are missing.
  const [validation, analysis, trials, novelty] = await Promise.all([
    getJSON('data/validation.json').catch(() => null),
    getJSON('data/analysis.json').catch(() => null),
    getJSON('data/trial_check.json').catch(() => null),
    getJSON('data/novelty_audit.json').catch(() => null),
  ]);
  if (validation) {
    state.validation = validation.summary;
    (validation.perDisease || []).forEach((d) => { state.perDisease[d.id] = d; });
  }
  if (trials) {
    (trials.results || []).forEach((t) => {
      if (t.trialsFound) state.trials[`${t.diseaseId}|${t.drug}`] = t;
    });
  }

  renderChips();
  renderHeroStats();
  renderBrowse();
  renderAccuracy();
  renderAnalysis(analysis, trials, novelty);
  renderFootMeta();
  route();
}

/* ---------- router ---------- */

function route() {
  const m = location.hash.match(/^#\/d\/([\w:.-]+)/);
  if (m) {
    openDisease(m[1]);
    return;
  }
  const wasDisease = !$('#disease').hidden;
  showView('home');
  document.title = 'Drug Match: drug repurposing candidates';
  const anchor = location.hash.length > 1 && !location.hash.startsWith('#/')
    ? document.getElementById(location.hash.slice(1)) : null;
  if (anchor) {
    if (wasDisease) jump(anchor.getBoundingClientRect().top + window.scrollY - 84);
    else anchor.scrollIntoView();
  } else if (wasDisease) jump(state.homeScroll);
}

function jump(y) {
  window.scrollTo({ top: y, behavior: 'instant' });
}

function showView(which) {
  const home = which === 'home';
  if (!home && !$('#home').hidden) state.homeScroll = window.scrollY;
  $('#home').hidden = !home;
  $('#disease').hidden = home;
  updateNavSearch();
}

window.addEventListener('hashchange', route);

function go(id) {
  location.hash = `#/d/${id}`;
}

/* ---------- nav ---------- */

const heroSearchEl = $('#heroSearch');
const navSearchEl = $('#navSearch');
let heroVisible = true;

new IntersectionObserver(([e]) => {
  heroVisible = e.isIntersecting;
  updateNavSearch();
}, { rootMargin: '-64px 0px 0px 0px' }).observe(heroSearchEl);

function updateNavSearch() {
  const onHome = !$('#home').hidden;
  navSearchEl.hidden = onHome && heroVisible;
}

window.addEventListener('scroll', () => {
  $('.nav').classList.toggle('scrolled', window.scrollY > 8);
}, { passive: true });

document.addEventListener('keydown', (e) => {
  if (e.key !== '/' || e.metaKey || e.ctrlKey) return;
  const t = e.target;
  if (t.matches('input, textarea, [contenteditable]')) return;
  e.preventDefault();
  const box = navSearchEl.hidden ? heroSearchEl : navSearchEl;
  $('input', box).focus();
});

/* ---------- search ---------- */

function rankMatches(term) {
  const t = term.trim().toLowerCase();
  if (!t) return [];
  const scored = [];
  for (const d of state.index) {
    const n = d.name.toLowerCase();
    const at = n.indexOf(t);
    if (at < 0) continue;
    const tier = at === 0 ? 0 : /[\s(,-]/.test(n[at - 1]) ? 1 : 2;
    scored.push([tier, d.rarity === 'other' ? 1 : 0, n.length, d]);
  }
  scored.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
  return scored.slice(0, 8).map((s) => s[3]);
}

function highlight(raw, term) {
  const name = cap(raw);
  const t = term.trim();
  const at = name.toLowerCase().indexOf(t.toLowerCase());
  if (!t || at < 0) return esc(name);
  return esc(name.slice(0, at)) + '<mark>' + esc(name.slice(at, at + t.length)) + '</mark>'
    + esc(name.slice(at + t.length));
}

function attachSearch(box) {
  const input = $('input', box);
  const list = $('.suggest', box);
  const listId = `sugg-${box.id}`;
  list.id = listId;
  input.setAttribute('role', 'combobox');
  input.setAttribute('aria-controls', listId);
  input.setAttribute('aria-expanded', 'false');
  input.setAttribute('aria-autocomplete', 'list');
  let items = [];
  let cursor = -1;

  const close = () => {
    list.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    input.removeAttribute('aria-activedescendant');
  };

  const draw = () => {
    const term = input.value;
    if (!term.trim()) { close(); return; }
    if (!items.length) {
      list.innerHTML = `<li class="snone">No disease matches “${esc(term.trim())}”.
        <a href="#browse">Browse the full list</a></li>`;
    } else {
      list.innerHTML = items.map((d, i) => `
        <li role="option" id="${listId}-${i}" data-id="${d.id}" aria-selected="${i === cursor}">
          <span class="sname">${highlight(d.name, term)}</span>
          <span class="tag ${d.rarity}">${esc(RARITY_LABELS[d.rarity] || d.rarity)}</span>
          <span class="scount">${plural(d.candidates, 'drug')}</span>
        </li>`).join('');
    }
    list.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    if (cursor >= 0) input.setAttribute('aria-activedescendant', `${listId}-${cursor}`);
    else input.removeAttribute('aria-activedescendant');
    const sel = list.querySelector('[aria-selected="true"]');
    if (sel) sel.scrollIntoView({ block: 'nearest' });
  };

  const pick = (id) => {
    close();
    input.value = '';
    input.blur();
    go(id);
  };

  input.addEventListener('input', () => {
    items = rankMatches(input.value);
    cursor = items.length ? 0 : -1;
    draw();
  });
  input.addEventListener('focus', () => { if (input.value.trim()) draw(); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (!items.length) return;
      cursor = e.key === 'ArrowDown'
        ? (cursor + 1) % items.length
        : (cursor - 1 + items.length) % items.length;
      draw();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      const d = items[cursor] || items[0];
      if (d) pick(d.id);
    } else if (e.key === 'Escape') {
      if (list.hidden) input.blur();
      close();
    }
  });
  list.addEventListener('mousedown', (e) => e.preventDefault());
  list.addEventListener('click', (e) => {
    const li = e.target.closest('li[data-id]');
    if (li) pick(li.dataset.id);
    else if (e.target.closest('a')) close();
  });
  input.addEventListener('blur', () => setTimeout(close, 100));
}

attachSearch(heroSearchEl);
attachSearch(navSearchEl);

/* ---------- home ---------- */

function renderChips() {
  const chips = EXAMPLES.map((id) => state.byId[id]).filter(Boolean);
  $('#chips').innerHTML = chips.map((d) =>
    `<a class="chip" href="#/d/${d.id}">${esc(cap(d.name))}</a>`).join('');
}

function renderHeroStats() {
  // Real numbers standing in for the marketing stats a hero section usually
  // carries, pulled from the same data the rest of the page reads. They
  // can never drift out of sync with what the site actually measures.
  const set = (id, v) => { if (v != null) $(id).textContent = v; };
  set('#statDiseases', (state.meta.diseasesInCache || state.index.length).toLocaleString());
  const v = state.validation;
  if (v) {
    set('#statPairs', v.knownPairsEvaluated.toLocaleString());
    set('#statTop', v.diseasesWhereTopCandidateIsKnown.toLocaleString());
  }
}

const browse = { tab: 'rare', filter: '', limit: 36 };

function renderBrowse() {
  const counts = { all: state.index.length, rare: 0, common: 0, other: 0 };
  state.index.forEach((d) => { counts[d.rarity] = (counts[d.rarity] || 0) + 1; });
  const tabs = [['rare', 'Rare'], ['common', 'Common'], ['other', 'Auto-selected'], ['all', 'All']];
  $('#browseTabs').innerHTML = tabs.map(([k, label]) =>
    `<button class="tab" role="tab" data-tab="${k}" aria-selected="${k === browse.tab}">${label}<span class="tc">${counts[k] || 0}</span></button>`).join('');

  $('#browseTabs').addEventListener('click', (e) => {
    const b = e.target.closest('.tab');
    if (!b) return;
    browse.tab = b.dataset.tab;
    browse.limit = 36;
    $('#browseTabs').querySelectorAll('.tab').forEach((t) =>
      t.setAttribute('aria-selected', String(t === b)));
    drawBrowse();
  });
  $('#browseFilter').addEventListener('input', (e) => {
    browse.filter = e.target.value.trim().toLowerCase();
    browse.limit = 36;
    drawBrowse();
  });
  $('#browseMore').addEventListener('click', () => {
    browse.limit += 96;
    drawBrowse();
  });
  drawBrowse();
}

function drawBrowse() {
  const list = state.index
    .filter((d) => browse.tab === 'all' || d.rarity === browse.tab)
    .filter((d) => !browse.filter || d.name.toLowerCase().includes(browse.filter))
    .sort((a, b) => a.name.localeCompare(b.name));
  const shown = list.slice(0, browse.limit);
  $('#browseGrid').innerHTML = shown.length
    ? shown.map((d) => `
      <a class="ditem" href="#/d/${d.id}">
        <span class="dn">${esc(cap(d.name))}</span>
        <span class="dm"><span class="tag ${d.rarity}">${esc(RARITY_LABELS[d.rarity] || d.rarity)}</span>
          <span>${plural(d.candidates, 'candidate')}</span></span>
      </a>`).join('')
    : '<p class="empty" style="grid-column:1/-1">No diseases match that filter.</p>';
  const left = list.length - shown.length;
  $('#browseMore').hidden = left <= 0;
  $('#browseMore').textContent = `Show more (${left.toLocaleString()} left)`;
}

function renderAccuracy() {
  const v = state.validation;
  if (!v) {
    $('#accuracy').hidden = true;
    return;
  }
  $('#accLede').textContent = `We hid ${v.knownPairsEvaluated.toLocaleString()} known drug–disease pairs from the engine, `
    + `across ${v.diseasesEvaluated.toLocaleString()} diseases, then checked where it ranked them anyway.`;

  const kpis = [
    [v.diseasesWhereTopCandidateIsKnown.toLocaleString(),
      `diseases where our #1 pick is already a real treatment, out of ${v.diseasesEvaluated.toLocaleString()}`],
    [`${v.enrichmentOverChanceTopTen}×`, 'as many known treatments in our top 10% as chance would put there'],
    [pct(v.medianPercentile), 'median position of known treatments. Random guessing lands at 50%'],
  ];
  if (v.rareOnly) kpis.push([pct(v.rareOnly.medianPercentile), 'the same median for rare diseases only, where it matters most']);
  $('#kpis').innerHTML = kpis.map(([b, s]) => `<div class="kpi"><b>${b}</b><span>${s}</span></div>`).join('');

  const rows = [];
  if (v.methods) {
    rows.push(['ours', 'Drug Match', 'our full method', v.methods.ours.medianPercentile]);
    if (v.rareOnly) rows.push(['ours', 'Drug Match, rare only', `${v.rareOnly.pairs.toLocaleString()} rare-disease pairs`, v.rareOnly.medianPercentile]);
    rows.push(['', 'Without damping', 'every path counted equally', v.methods.nodamp.medianPercentile]);
    rows.push(['', 'Popularity only', 'ignores the disease entirely', v.methods.popularity.medianPercentile]);
  } else {
    rows.push(['ours', 'Drug Match', 'our full method', v.medianPercentile]);
  }
  rows.push(['rand', 'Random guess', 'the baseline to beat', v.randomBaselineMedian || 0.5]);
  const max = 0.7;
  $('#methodChart').innerHTML = rows.map(([cls, label, sub, val], i) => `
    <div class="hbar ${cls}">
      <span class="hl">${esc(label)}<small>${esc(sub)}</small></span>
      <span class="ht"><span class="hf" style="width:${Math.min(val / max, 1) * 100}%; animation-delay:${i * 80}ms"></span></span>
      <span class="hv">${pct(val)}</span>
    </div>`).join('');
}

function renderAnalysis(a, trials, novelty) {
  const el = $('#analysis');
  if (!a) {
    $('.deep').hidden = true;
    return;
  }
  const lo = Math.min(...a.dampingSweep.map((d) => d.median));
  const hi = Math.max(...a.dampingSweep.map((d) => d.median));
  const sweep = a.dampingSweep.map((d) => {
    const ours = Math.abs(d.w - 0.4) < 1e-9;
    const h = 30 + ((d.median - lo) / (hi - lo || 1)) * 60;
    return `<div class="${ours ? 'on' : ''}"><span>${pct(d.median)}</span><i style="height:${h}%"></i>
      <span>w=${d.w.toFixed(1)}${ours ? ' ★' : ''}</span></div>`;
  }).join('');
  const worst = [...a.ablation].sort((x, y) => y.delta - x.delta)[0];
  const hop = a.interactionHop;

  el.innerHTML = `
    <p><strong>Stability.</strong> We resampled diseases ${a.bootstrap.rounds.toLocaleString()} times.
       The median landed between ${pct(a.bootstrap.ci95[0])} and ${pct(a.bootstrap.ci95[1])} every time.
       That range ${a.bootstrap.excludesRandom ? 'excludes' : 'does not exclude'} the 50% a random
       ranking would produce.</p>

    <p><strong>The damping constant.</strong> A larger exponent scores better than the 0.4 we use.
       We kept 0.4 anyway, because it is the value Rephetio published. Tuning it upward would mean
       we fitted the model to our own test, and we did not want that.</p>
    <div class="sweep" role="img" aria-label="Median rank of known treatments for each damping exponent">${sweep}</div>
    <p class="fine">Median position of known treatments per exponent. Shorter bars are better.</p>

    ${hop ? `<p><strong>The extra interaction step.</strong> Allowing drug → gene → gene → disease paths improved
       ${hop.diseasesImproved.toLocaleString()} diseases and worsened ${hop.diseasesWorsened.toLocaleString()}.
       Rare diseases gain the most: ${pct(hop.byRarity.rare.directOnly)} → ${pct(hop.byRarity.rare.withHop)}.</p>` : ''}

    <p><strong>Leaking evidence.</strong> Removing ${esc(EVIDENCE_LABELS[worst.datatype] || worst.datatype).toLowerCase()}
       hurts the score more than removing any other evidence type. Literature evidence partly reflects a drug already linked
       to a gene and a disease, so that is a real concern. We stripped every literature-derived source
       anyway. The median still landed at ${pct(a.conservativeFloor.median)}, well clear of chance.</p>

    <p><strong>The negative control.</strong> We scored each disease against a different disease's
       known drugs. The median moved to ${pct(a.negativeControl.mismatched)}, not a clean 50%, because
       many diseases share common treatments and some drugs rank well everywhere. We report that number
       as it stands, not explained away.</p>

    ${trials ? `<p><strong>Has anyone tried these?</strong> For the top new candidate on ${trials.diseasesChecked} curated
       diseases, we searched ClinicalTrials.gov. ${trials.withExistingTrial} already have a registered trial.
       That doesn't prove the drug works, only that the idea occurred to someone else too.</p>` : ''}

    ${novelty ? `<p><strong>Is “new” always new?</strong> A sweep of ${novelty.checked.toLocaleString()} candidates flagged
       ${novelty.flaggedCount} whose own record lists a similar approved use. Those are marked
       “may not be new” on their cards. <a href="${NOVELTY_URL}" target="_blank" rel="noopener">Why this happens</a>.</p>` : ''}`;
}

function renderFootMeta() {
  // The browsable set and the measured set differ, and saying so matters:
  // quoting a validation figure from thousands of diseases beside a search box
  // covering hundreds would be quietly misleading.
  const p = state.meta;
  const bits = [`${state.index.length} diseases browsable here`];
  if (p.diseasesInCache && p.diseasesInCache > state.index.length) {
    bits.push(`${p.diseasesInCache.toLocaleString()} scored and measured`);
  }
  bits.push(`damping exponent w = ${p.dampingExponent}`,
    `excluded evidence: ${p.excludedDatatypes.join(', ')}`);
  if (state.validation) bits.push(`${state.validation.knownPairsEvaluated.toLocaleString()} known pairs used for validation`);
  $('#footmeta').textContent = bits.join(' · ');
}

/* ---------- disease page ---------- */

const stage = $('#stage');

async function openDisease(id) {
  showView('disease');
  jump(0);
  const entry = state.byId[id];
  document.title = `${entry ? cap(entry.name) : 'Disease'} · Drug Match`;

  if (!state.results[id]) {
    stage.innerHTML = `${backLink()}
      <div class="dtitle"><h1>${esc(entry ? cap(entry.name) : 'Loading…')}</h1></div>
      <div class="dstats">${'<div class="skel"></div>'.repeat(4)}</div>
      <div class="skel tall"></div>${'<div class="skel"></div>'.repeat(5)}`;
    try {
      state.results[id] = await getJSON(`data/results/${id}.json`);
    } catch (err) {
      console.error(err);
      stage.innerHTML = `${backLink()}<p class="empty" style="margin-top:24px">We don't have results for that disease.
        <a href="#browse">Browse the diseases we do have</a>.</p>`;
      return;
    }
    // A slow load may have been overtaken by another navigation.
    if (!location.hash.endsWith(id)) return;
  }

  if (state.current !== id) {
    state.open = new Set();
    state.filter = '';
  }
  state.current = id;
  renderDisease(state.results[id]);
}

function backLink() {
  return `<a class="back" href="#/">${ICONS.back}All diseases</a>`;
}

function renderDisease(r) {
  document.title = `${cap(r.name)} · Drug Match`;
  const pd = state.perDisease[r.id];
  // Two separate honesty signals, which used to be conflated. "Thin" is about
  // how much the method had to work with; "poor" is about whether it actually
  // performed. A disease can have a small pool and still rank its real
  // treatment first, which is exactly what alkaptonuria does.
  const thin = r.candidatesConsidered < 25;
  const poor = pd && pd.medianPercentile > 0.5;
  const longDesc = r.description && r.description.length > 260;

  stage.innerHTML = `
    ${backLink()}
    <header class="dtitle">
      <div class="tags">
        <span class="tag ${r.rarity}">${esc(RARITY_LABELS[r.rarity] || r.rarity)}</span>
        <span class="tag plain">${esc(r.id.replace('_', ':'))}</span>
      </div>
      <h1>${esc(cap(r.name))}</h1>
      ${r.description ? `<p class="ddesc ${longDesc ? 'clamp' : ''}" id="ddesc">${esc(r.description)}</p>
        ${longDesc ? '<button class="linkbtn" id="descMore">Read more</button>' : ''}` : ''}
    </header>

    <div class="dstats">
      <div class="dstat"><b>${r.associatedGeneCount.toLocaleString()}</b><span>genes linked to this disease</span></div>
      <div class="dstat"><b>${r.genesWithDrugs}<small style="font-size:.55em;color:var(--ink3)"> / ${r.genesScored}</small></b>
        <span>of its strongest genes are hit by an approved drug</span></div>
      <div class="dstat"><b>${r.candidatesConsidered.toLocaleString()}</b><span>approved drugs ranked</span></div>
      <div class="dstat"><b>${r.knownDrugCount.toLocaleString()}</b><span>known treatment${r.knownDrugCount === 1 ? '' : 's'} hidden from the engine</span></div>
    </div>

    ${checkCard(r, pd)}

    ${thin ? notice('warn', `<strong>Thin result.</strong> Only ${plural(r.candidatesConsidered, 'approved drug')} connect
      to this disease's genes at all, so the method has little to work with. That is also part of why
      conditions like this are hard to treat.`) : ''}
    ${poor && !thin ? notice('bad', `<strong>Our method handles this disease badly.</strong> Known treatments
      rank below where random guessing would put them. Treat the suggestions below as weak evidence.
      We are showing you the failure, not hiding it.`) : ''}

    <div class="listhead">
      <div>
        <h2>Repurposing candidates</h2>
        <p>Approved drugs not yet used for ${esc(r.name)}, ranked by how strongly the genes they act on
          connect to it. Tap any drug to see why it's here.</p>
      </div>
    </div>

    <div class="toolbar">
      <label class="filterin">${ICONS.search}
        <input id="candFilter" type="search" placeholder="Filter by drug, gene or mechanism" value="${esc(state.filter)}" aria-label="Filter candidates">
      </label>
      ${r.knownRanked.length ? `<label class="toggle"><input type="checkbox" id="tKnown" ${state.showKnown ? 'checked' : ''}>
        Show known treatments</label>` : ''}
      <label class="toggle"><input type="checkbox" id="tFlag" ${state.hideFlagged ? 'checked' : ''}>
        Hide drugs with safety warnings</label>
      <span class="count" id="candCount"></span>
    </div>
    <div class="legend" aria-hidden="true">
      <span><i style="background:var(--accent)"></i>Drug</span>
      <span><i style="background:var(--gene)"></i>Gene</span>
      <span><i style="background:var(--dis)"></i>Disease</span>
      <span>Match = score relative to the top candidate (1.00)</span>
    </div>
    <div id="cards"></div>

    <div class="endnote">
      <h3>What these results mean</h3>
      <p>A high match means the biology connects, not that the drug works. Every candidate here would need laboratory work and
        clinical trials before anyone could use it for ${esc(r.name)}.</p>
      <p><a href="#how">How the ranking works</a> · <a href="#accuracy">How accurate it is</a></p>
    </div>`;

  if (longDesc) {
    $('#descMore').addEventListener('click', (e) => {
      const d = $('#ddesc');
      const clamped = d.classList.toggle('clamp');
      e.target.textContent = clamped ? 'Read more' : 'Show less';
    });
  }
  $('#candFilter').addEventListener('input', (e) => { state.filter = e.target.value; drawCards(r); });
  const tKnown = $('#tKnown');
  if (tKnown) tKnown.addEventListener('change', (e) => { state.showKnown = e.target.checked; drawCards(r); });
  $('#tFlag').addEventListener('change', (e) => { state.hideFlagged = e.target.checked; drawCards(r); });
  $('#cards').addEventListener('click', (e) => {
    const head = e.target.closest('.chead');
    if (!head) return;
    const cardEl = head.parentElement;
    const key = cardEl.dataset.key;
    const open = !cardEl.classList.contains('open');
    cardEl.classList.toggle('open', open);
    head.setAttribute('aria-expanded', String(open));
    if (open) state.open.add(key); else state.open.delete(key);
  });

  drawCards(r);
}

function notice(kind, html) {
  return `<div class="notice ${kind}">${kind === 'info' ? ICONS.info : ICONS.warn}<div>${html}</div></div>`;
}

function checkCard(r, pd) {
  if (!pd) {
    return notice('info', `We couldn't check the ranking on this disease: none of its known treatments reached the candidate pool.
      The results below are untested here.`);
  }
  const one = pd.knownEvaluated === 1;
  const m = pd.medianPercentile;
  const verdict = m <= 0.25 ? ['good', 'Strong result'] : m <= 0.5 ? ['warn', 'Mixed result'] : ['bad', 'Weak result'];
  // Tied scores can be ordered differently in validation.json and the result
  // file, so name the best drug from the list the reader is looking at.
  const shown = r.knownRanked[0];
  const best = shown ? { name: shown.name, rank: shown.rank, pool: r.candidatesConsidered }
    : { name: pd.bestDrug, rank: pd.bestRank, pool: pd.candidatePool };
  const headline = one
    ? `We hid <b>${esc(best.name)}</b>, ${r.knownDrugCount === 1 ? 'the one' : 'a'} known treatment, from the engine.
       It still ranked it <b>#${best.rank} of ${best.pool}</b>.`
    : `${pd.knownEvaluated} of its known treatments reached the ranking. The engine never saw them, yet put
       <b>${esc(best.name)}</b> at <b>#${best.rank} of ${best.pool}</b>.`;

  const pool = r.candidatesConsidered;
  const spot = (rank) => (pool > 1 ? (rank - 1) / (pool - 1) : 0);
  const pins = r.knownRanked.length
    ? r.knownRanked.map((k) => ({ x: spot(k.rank), tip: `${k.name}: #${k.rank}` }))
    : [{ x: m, tip: `Median: ${pct(m)}` }];
  const pinHtml = pins.map((p) => {
    const cls = p.x <= 0.25 ? '' : p.x <= 0.5 ? 'mid' : 'low';
    return `<span class="pin ${cls}" style="left:calc(9px + ${p.x.toFixed(3)} * (100% - 18px))" data-tip="${esc(p.tip)}" title="${esc(p.tip)}"></span>`;
  }).join('');

  return `
    <section class="check" aria-label="How well the ranking did on this disease">
      <div>
        <span class="tag ${verdict[0]}">${verdict[1]}</span>
        <h3>${headline}</h3>
        <p>${one ? '' : `The median known treatment sits ${pct(m)} of the way down the list. `}Random guessing would land
          around 50%.</p>
      </div>
      <div>
        <div class="track" role="img" aria-label="Positions of known treatments in the ranking, from best on the left to worst on the right">
          <div class="ends"><span>#1 best</span><span>#${pool} worst</span></div>
          <div class="rail"></div>
          <div class="half"></div>
          <span class="halfl">random guess</span>
          ${pinHtml}
        </div>
      </div>
    </section>`;
}

function drawCards(r) {
  const term = state.filter.trim().toLowerCase();
  let list = r.candidates.map((d) => ({ d, known: false }));
  if (state.showKnown) list = list.concat(r.knownRanked.map((d) => ({ d, known: true })));
  list.sort((a, b) => a.d.rank - b.d.rank);

  if (state.hideFlagged) list = list.filter(({ d }) => !d.withdrawn && !d.blackBox);
  if (term) {
    list = list.filter(({ d }) => [d.name, ...d.mechanisms, ...d.approvedFor,
      ...d.paths.flatMap((p) => [p.gene, p.geneName, p.via])]
      .some((s) => s && s.toLowerCase().includes(term)));
  }

  const total = r.candidates.length + (state.showKnown ? r.knownRanked.length : 0);
  $('#candCount').textContent = list.length === total
    ? `${plural(list.length, 'drug')}`
    : `${list.length} of ${total} drugs`;

  $('#cards').innerHTML = list.length
    ? list.map(({ d, known }) => card(d, known, r)).join('')
    : `<p class="empty">${r.candidates.length ? 'No drugs match those filters.' : 'No candidates found for this disease.'}</p>`;
}

function approvedText(d) {
  if (!d.approvedFor.length) return 'Approved drug';
  const extra = d.indicationCount - 2;
  return 'Approved for ' + d.approvedFor.slice(0, 2).join(', ') + (extra > 0 ? ` +${extra} more` : '');
}

function card(d, known, r) {
  const key = `${known ? 'k' : 'c'}-${d.id}`;
  const open = state.open.has(key);
  const paths = [...d.paths].sort((a, b) => b.contribution - a.contribution);
  const lead = paths[0];
  const trial = !known && state.trials[`${r.id}|${d.name}`];

  const tags = [];
  if (known) tags.push('<span class="tag good">Known treatment</span>');
  if (d.withdrawn) tags.push('<span class="tag bad">Withdrawn</span>');
  else if (d.blackBox) tags.push('<span class="tag warn">Black box warning</span>');
  if (!known && d.possiblyAlreadyApproved) tags.push('<span class="tag warn">May not be new</span>');
  if (trial) tags.push('<span class="tag common">In a trial</span>');

  const via = lead
    ? ` · via <span class="via">${esc(lead.hops === 3 ? `${lead.via} → ${lead.gene}` : lead.gene)}</span>` : '';

  return `
    <article class="cand ${known ? 'known' : ''} ${d.rank <= 3 && !known ? 'top' : ''} ${open ? 'open' : ''}" data-key="${key}">
      <button class="chead" aria-expanded="${open}">
        <span class="rankb" aria-label="Rank ${d.rank}">${d.rank}</span>
        <span class="cmain">
          <span class="cline1"><span class="cname">${esc(d.name)}</span>${tags.join('')}</span>
          <span class="cline2">${esc(approvedText(d))}${via}</span>
        </span>
        <span class="meter" title="Score relative to the top candidate">
          <span class="mv">Match <b>${d.score.toFixed(2)}</b></span>
          <span class="mt"><i style="width:${Math.max(2, Math.round(d.score * 100))}%"></i></span>
        </span>
        ${ICONS.caret}
      </button>
      <div class="cbody">${cardBody(d, known, r, paths, trial)}</div>
    </article>`;
}

function whySentence(d, p, disease, routeCount) {
  if (!p) return '';
  const top = [...p.evidence].sort((a, b) => b.score - a.score)[0];
  const gene = `<b>${esc(p.gene)}</b>${p.geneName ? ` (${esc(p.geneName)})` : ''}`;
  const reach = p.hops === 3
    ? `acts on <b>${esc(p.via)}</b>, a protein that works closely with ${gene}`
    : `acts on ${gene}`;
  const ev = top ? `, mainly through ${esc((EVIDENCE_LABELS[top.id] || top.id).toLowerCase())} evidence` : '';
  const more = routeCount > 1 ? ` That's the strongest of ${routeCount} routes shown below.` : '';
  return `<b>${esc(d.name)}</b> ${reach}. That gene is linked to ${esc(disease)}${ev}.${more}`;
}

function arrow() {
  return '<svg viewBox="0 0 60 10" preserveAspectRatio="none" aria-hidden="true"><line x1="0" y1="5" x2="56" y2="5"/><path d="M52 1l5 4-5 4"/></svg>';
}

function flow(d, p, disease) {
  const node = (cls, b, small) => `<span class="fnode ${cls}"><b>${esc(b)}</b>${small ? `<small>${esc(small)}</small>` : ''}</span>`;
  const edge = (label) => `<span class="fedge">${esc(label)}${arrow()}</span>`;
  const parts = [node('drug', d.name, 'drug'), edge('targets')];
  if (p.hops === 3) parts.push(node('gene', p.via, 'target protein'), edge(`interacts (${p.viaScore})`));
  parts.push(node('gene', p.gene, p.geneName), edge(`linked (${p.assoc.toFixed(2)})`), node('dis', disease, 'disease'));
  return `<div class="flow">${parts.join('')}</div>`;
}

function routeBlock(d, p, i, disease) {
  const share = d.rawScore ? Math.round((p.contribution / d.rawScore) * 100) : null;
  const ev = [...p.evidence].sort((a, b) => b.score - a.score).map((e) => `
    <div class="ev">
      <span>${esc(EVIDENCE_LABELS[e.id] || e.id)}</span>
      <span class="eb"><i style="width:${Math.round(e.score * 100)}%"></i></span>
      <span class="evv">${e.score.toFixed(2)}</span>
    </div>`).join('');
  return `
    <div class="route">
      <div class="routetop">
        <span class="rl">Route ${i + 1} · ${p.hops === 3 ? 'through a protein interaction' : 'direct'}</span>
        ${share != null ? `<span class="tag plain">${share}% of this drug's score</span>` : ''}
      </div>
      ${flow(d, p, disease)}
      <div class="facts">
        <span>Gene–disease link <b>${p.assoc.toFixed(2)}</b> of 1</span>
        <span><b>${p.drugsOnGene}</b> approved drug${p.drugsOnGene === 1 ? '' : 's'} hit this target</span>
        ${p.hops === 3 ? `<span>Interaction confidence <b>${p.viaScore}</b></span>` : ''}
      </div>
      <p class="evh">Evidence for the gene–disease link (clinical evidence excluded)</p>
      <div class="evgrid">${ev}</div>
    </div>`;
}

function cardBody(d, known, r, paths, trial) {
  const warnList = (d.warnings || []).map((w) => `${esc(w.type)}${w.detail ? `: ${esc(w.detail)}` : ''}`);
  const safety = warnList.length
    ? notice(d.withdrawn ? 'bad' : 'warn', `<strong>Safety on record:</strong> ${warnList.join('; ')}.
       ${d.withdrawn
        ? 'A regulator withdrew this drug in at least one market. We show it because the biology connects. That does not make it a sensible candidate.'
        : 'Weigh this before you consider repurposing it. Our ranking does not account for it.'}`)
    : '';
  const novelty = !known && d.possiblyAlreadyApproved
    ? notice('warn', `<strong>This may already be approved for this disease.</strong>
       Its own record lists “${esc(d.possiblyAlreadyApproved)}” as an approved use, which overlaps this
       disease's name. Our known-drug list missed the connection.
       <a href="${NOVELTY_URL}" target="_blank" rel="noopener">Why this happens</a>.`)
    : '';
  const knownNote = known
    ? notice('info', `<strong>This is already a treatment for ${esc(r.name)}.</strong> We hid it from the engine,
       which still ranked it #${d.rank} of ${r.candidatesConsidered}. It's shown here as a check on the method.`)
    : '';
  const trialNote = trial
    ? notice('info', `<strong>Someone's already testing this.</strong> ClinicalTrials.gov lists
       ${plural(trial.trialsFound, 'trial')} of ${esc(d.name)} for ${esc(r.name)}:
       <ul class="trials">${trial.trials.map((t) => `<li><a href="https://clinicaltrials.gov/study/${esc(t.nctId)}" target="_blank" rel="noopener">${esc(t.nctId)}</a>
         ${esc(t.title)}${t.status ? ` <span class="tag plain">${esc(t.status.toLowerCase().replace(/_/g, ' '))}</span>` : ''}</li>`).join('')}</ul>`)
    : '';

  const facts = [
    d.mechanisms.length ? ['How it works', d.mechanisms.join('; ')] : null,
    ['Approved for', d.approvedFor.length ? d.approvedFor.join(', ') : 'Listed as approved; no indication recorded'],
    ['Drug type', `${d.drugType} · hits ${plural(d.geneCount, 'gene')} overall`],
  ].filter(Boolean);

  return `
    ${knownNote}
    <p class="why">${whySentence(d, paths[0], r.name, paths.length)}</p>
    <div class="routes">${paths.map((p, i) => routeBlock(d, p, i, r.name)).join('')}</div>
    <div class="drugfacts">${facts.map(([h, t]) => `<div class="fact"><h4>${h}</h4><p>${esc(t)}</p></div>`).join('')}</div>
    ${safety}
    ${novelty}
    ${trialNote}`;
}

boot();
