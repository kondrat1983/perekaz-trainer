import { matchesAnswer, normalizeAnswer } from './normalize.js';
import { loadState, saveState, resetState } from './store.js';
import { speak, ukrainianVoices, canSpeak, canListen, listen } from './speech.js';

const LEVELS = ['L1', 'L2', 'L3'];
const PARENT_QUESTION = 'Скільки буде 7 × 8?';
const PARENT_ANSWER = '56';

const ICON_BOOK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h12a2 2 0 0 1 2 2v14H7a2 2 0 0 1-2-2Z"/><path d="M5 18a2 2 0 0 1 2-2h12"/></svg>';
const ICON_CITY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11L12 4L21 11V20H14V14H10V20H3Z"/></svg>';
const ICON_PAIR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 8h11l-3-3M17 16H6l3 3"/></svg>';
const ICON_PERSON = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/></svg>';

const app = document.getElementById('app');
let data = null;
let library = [];
let workId = null;
const workCache = {};
let state = loadState();
let session = null;
let parentOpen = false;

const esc = (value) => String(value).replace(/[&<>"']/g, (c) => (
  { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
));

const shuffle = (items) => {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
};

const work = () => library.find((w) => w.id === workId);
const base = () => `#/w/${workId}`;
const total = () => data.scenes.length;
// Прогрес кожного твору окремо.
const prog = (id = workId) => {
  state.works[id] ||= { scenes: {}, errors: {} };
  return state.works[id];
};
const sceneByNum = (n) => data.scenes.find((scene) => scene.num === n);
const charOf = (id) => data.characters[id];
const isDone = (n) => Boolean(prog().scenes[n]?.done);
const isUnlocked = (n) => n === 1 || state.settings.openAll || isDone(n - 1);
const nextNum = () => data.scenes.find((scene) => isUnlocked(scene.num) && !isDone(scene.num))?.num ?? null;
const doneCount = () => data.scenes.filter((scene) => isDone(scene.num)).length;

function say(text, rate = 0.95) {
  speak(text, { rate, voiceName: state.settings.voice });
}

function markClean(n, level) {
  const entry = { ...(prog().scenes[n] || {}), [level]: true };
  entry.done = LEVELS.every((l) => entry[l]);
  prog().scenes[n] = entry;
  saveState(state);
}

function recordError(key) {
  prog().errors[key] = (prog().errors[key] || 0) + 1;
  saveState(state);
}

function go(hash) {
  if (location.hash === hash) route();
  else location.hash = hash;
}

// ---------- Сцена ----------

function newSceneSession(n) {
  const next = {
    kind: 'scene', n, queue: [...LEVELS], index: 0, attempts: {}, finished: false,
    listening: false,
  };
  startSceneRound(next);
  return next;
}

function currentSceneQuestion() {
  const level = session.queue[session.index];
  return { level, q: sceneByNum(session.n).questions[level] };
}

function startSceneRound(current) {
  const q = sceneByNum(current.n).questions[current.queue[current.index]];
  current.options = shuffle(q.options);
  current.missed = [];
  current.hinted = false;
  current.locked = false;
  current.feedback = '';
  current.announce = true;
}

function pickScene(id) {
  if (session.locked) return;
  const { level, q } = currentSceneQuestion();
  if (id === q.answer) {
    if (!session.hinted && !session.attempts[level]) markClean(session.n, level);
    session.locked = true;
    session.feedback = 'Так!';
    draw();
    const current = session;
    setTimeout(() => {
      if (session === current) advanceScene();
    }, 900);
    return;
  }
  session.attempts[level] = (session.attempts[level] || 0) + 1;
  session.missed.push(id);
  recordError(`${session.n}.${level}`);
  // Повторити питання через одну картку, а не одразу.
  session.queue.splice(session.index + 2, 0, level);
  session.feedback = `Ще раз. ${q.hint}`;
  draw();
}

function advanceScene() {
  session.index += 1;
  if (session.index >= session.queue.length) {
    session.finished = true;
  } else {
    startSceneRound(session);
  }
  draw();
}

function listenScene() {
  const { q } = currentSceneQuestion();
  session.listening = true;
  session.feedback = 'Слухаю…';
  const current = session;
  listen({
    onResult: (alternatives) => {
      if (session !== current) return;
      if (alternatives.some((text) => matchesAnswer(text, q.accepted || []))) {
        pickScene(q.answer);
      } else {
        session.feedback = 'Не розчула. Спробуй ще або торкнись картинки.';
        draw();
      }
    },
    onEnd: () => {
      if (session !== current) return;
      session.listening = false;
      draw();
    },
  });
  draw();
}

const CITY_BG = 'images/backdrop.svg';

// Один актор на картинці: персонаж (char) або предмет (img). full — накладка на весь кадр (дощ).
function actorView(actor, lit = false) {
  if (actor.full) return `<img class="overlay" src="${actor.img}" alt="">`;
  const c = actor.char ? charOf(actor.char) : null;
  const src = c ? (actor.pose && c.poses?.[actor.pose]) || c.img : actor.img;
  const alt = c ? c.name : actor.alt || '';
  const cls = `actor${lit ? ' lit' : ''}${actor.grey ? ' grey' : ''}`;
  return `<img class="${cls}" src="${src}" alt="${esc(alt)}" style="left:${actor.x}%;bottom:${actor.bottom}%;height:${actor.h}%">`;
}

function picture(bg, actors, lit = false) {
  return `<img class="backdrop" src="${bg || CITY_BG}" alt="">${actors.map((a) => actorView(a, lit)).join('')}`;
}

function sceneStage(scene, target) {
  const actors = target ? scene.stage.filter((st) => st.char === target) : scene.stage;
  return picture(scene.bg, actors, Boolean(target));
}

function sceneView() {
  const scene = sceneByNum(session.n);
  const head = `
    <nav class="bar">
      <a class="back" href="${base()}">← Назад</a>
      <span>Сцена ${scene.num} з ${total()}</span>
    </nav>
    <h1 class="title">${esc(scene.title)}</h1>`;

  if (session.finished) return head + sceneEndView(scene);

  const { level, q } = currentSceneQuestion();
  const options = session.options.map((o) => {
    const src = o.char ? charOf(o.char).img : o.img;
    const pic = src ? `<img src="${src}" alt="">` : '';
    const miss = session.missed.includes(o.id) ? ' miss' : '';
    return `<button class="opt${pic ? ' pic' : ''}${miss}" data-action="pick" data-id="${o.id}" ${session.locked ? 'disabled' : ''}>${pic}<span>${esc(o.text)}</span></button>`;
  }).join('');
  const mic = canListen && level === 'L1'
    ? `<button class="round mic" data-action="listen" aria-label="Відповісти голосом" ${session.listening ? 'disabled' : ''}>🎤</button>`
    : '';

  return `${head}
    <div class="stage">${sceneStage(scene, q.target)}</div>
    <p class="prompt">${esc(q.prompt)}</p>
    <div class="speech">
      <button class="round" data-action="replay" aria-label="Повторити">🔊</button>
      <button class="round" data-action="slow" aria-label="Повільніше">🐢</button>
      ${mic}
    </div>
    <div class="options">${options}</div>
    <p class="feedback" role="status" aria-live="polite">${esc(session.feedback)}</p>
    <div class="row">
      <button class="btn ghost" data-action="hint" ${session.hinted || session.locked ? 'disabled' : ''}>Підказка</button>
      <a class="btn ghost" href="${base()}/scene/${scene.num}/retell">Переказ</a>
    </div>`;
}

function sceneEndView(scene) {
  const done = isDone(scene.num);
  const next = data.scenes.find((s) => s.num === scene.num + 1);
  const nextOpen = next && isUnlocked(next.num);
  return `
    <section class="card end">
      <p class="big">${done ? 'Сцену пройдено!' : 'Майже! Спробуємо ще раз?'}</p>
      <p>${done
        ? 'Тепер ця сцена світиться на карті.'
        : 'Ця сцена ще не пройдена без підказок. Так запам’ятається краще.'}</p>
    </section>
    <div class="row">
      ${done && nextOpen ? `<a class="btn" href="${base()}/scene/${next.num}">Далі: сцена ${next.num}</a>` : ''}
      ${done ? '' : '<button class="btn" data-action="restart">Ще раз</button>'}
      <a class="btn ghost" href="${base()}/scene/${scene.num}/retell">Переказ</a>
      <a class="btn ghost" href="${base()}">До сцен</a>
    </div>`;
}

// ---------- Переказ ----------

// Підкреслюємо слова еталону, які Гравець сказав сам (від 4 літер).
function markHeard(text, heardWords) {
  if (!heardWords.size) return esc(text);
  return text.split(/(\s+)/).map((part) => {
    const word = normalizeAnswer(part);
    return word.length >= 4 && heardWords.has(word) ? `<u class="hit">${esc(part)}</u>` : esc(part);
  }).join('');
}

function retellView() {
  const scene = sceneByNum(session.n);
  const frames = scene.frames.map((f, i) => `
    <button class="frame${session.active === i ? ' on' : ''}" data-action="zoom" data-i="${i}" aria-label="Кадр ${i + 1}">
      ${picture(f.bg, f.actors)}
      <span class="frame-num">${i + 1}</span>
    </button>`).join('');
  const heardWords = new Set(normalizeAnswer(session.heard).split(' ').filter(Boolean));
  const phrases = scene.frames.map((f, i) => `
    <li><button class="phrase${session.active === i ? ' on' : ''}" data-action="phrase" data-i="${i}">
      <span class="phrase-num">${i + 1}</span><span>${markHeard(f.text, heardWords)}</span>
    </button></li>`).join('');
  const zoomed = session.zoom != null ? scene.frames[session.zoom] : null;
  return `
    <nav class="bar">
      <a class="back" href="${base()}/scene/${scene.num}">← Сцена</a>
      <span>Переказ</span>
    </nav>
    <h1 class="title">${esc(scene.title)}</h1>
    <div class="storyboard">${frames}</div>
    <p class="prompt">Розкажи, що сталося в цій сцені.</p>
    <div class="row">
      ${canListen ? `<button class="btn" data-action="retell-listen" ${session.listening ? 'disabled' : ''}>🎤 Говорити</button>` : ''}
      <button class="btn ghost" data-action="reveal">${session.revealed ? 'Сховати переказ' : 'Показати переказ'}</button>
    </div>
    ${session.heard ? `<p class="feedback">Почули: ${esc(session.heard)}</p>` : ''}
    ${session.revealed ? `<ol class="phrases">${phrases}</ol>` : ''}
    ${zoomed ? `
      <div class="zoom" role="dialog" aria-label="Кадр ${session.zoom + 1}">
        <div class="stage">${picture(zoomed.bg, zoomed.actors)}</div>
        ${session.revealed ? `<p class="zoom-text">${esc(zoomed.text)}</p>` : ''}
        <button class="btn" data-action="zoom-close">Закрити</button>
      </div>` : ''}`;
}

function retellListen() {
  session.listening = true;
  const current = session;
  listen({
    onResult: (alternatives) => {
      if (session !== current) return;
      session.heard = alternatives[0];
      draw();
    },
    onEnd: () => {
      if (session !== current) return;
      session.listening = false;
      draw();
    },
  });
  draw();
}

// ---------- Пари ----------

function newPariSession() {
  const queue = [];
  data.pairs.forEach(([a, b]) => {
    queue.push({ a, b, target: a });
    queue.push({ a, b, target: b });
  });
  const next = { kind: 'pari', queue: shuffle(queue), index: 0, errors: 0, finished: false };
  startPariRound(next);
  return next;
}

function startPariRound(current) {
  const round = current.queue[current.index];
  current.cards = shuffle([round.a, round.b]);
  current.locked = false;
  current.wrong = false;
  current.feedback = '';
  current.announce = true;
}

function pariPick(id) {
  if (session.locked) return;
  const round = session.queue[session.index];
  const current = session;
  session.locked = true;
  if (id === round.target) {
    session.feedback = 'Так!';
    draw();
    setTimeout(() => {
      if (session === current) pariNext(false);
    }, 900);
    return;
  }
  session.wrong = true;
  session.errors += 1;
  recordError('pari');
  const right = charOf(round.target);
  session.feedback = `Ось так виглядає: ${right.lname}.`;
  draw();
}

function pariNext(requeue) {
  const round = session.queue[session.index];
  if (requeue) session.queue.splice(session.index + 2, 0, round);
  session.index += 1;
  if (session.index >= session.queue.length) {
    session.finished = true;
  } else {
    startPariRound(session);
  }
  draw();
}

function pariView() {
  const head = `
    <nav class="bar"><span>Пари</span><span>${Math.min(session.index + 1, session.queue.length)} з ${session.queue.length}</span></nav>
    <h1 class="title">Знайди, хто це</h1>`;
  if (session.finished) {
    return `${head}
      <section class="card end">
        <p class="big">Пари пройдено</p>
        <p>Помилок у цьому колі: ${session.errors}.</p>
      </section>
      <div class="row">
        <button class="btn" data-action="pari-restart">Ще раз</button>
        <a class="btn ghost" href="${base()}">До сцен</a>
      </div>`;
  }
  const round = session.queue[session.index];
  const target = charOf(round.target);
  const cards = session.cards.map((id, i) => {
    const c = charOf(id);
    const isRight = id === round.target;
    const reveal = session.wrong && isRight;
    const label = reveal
      ? `<span class="tag">Це ${esc(c.lname)}</span><small>${esc(c.features.join(', '))}</small>`
      : '';
    return `<button class="pcard${reveal ? ' right' : ''}" data-action="pari-pick" data-id="${id}" aria-label="Картка ${i + 1}" ${session.locked ? 'disabled' : ''}>
      <img src="${c.img}" alt="">${label}
    </button>`;
  }).join('');
  return `${head}
    <p class="prompt">Покажи: ${esc(target.acc)}</p>
    <div class="speech">
      <button class="round" data-action="replay" aria-label="Повторити">🔊</button>
    </div>
    <div class="pari">${cards}</div>
    <p class="feedback" role="status" aria-live="polite">${esc(session.feedback)}</p>
    ${session.wrong ? '<div class="row"><button class="btn" data-action="pari-next">Далі</button></div>' : ''}`;
}

// ---------- Батькам ----------

function parentView() {
  if (!parentOpen) {
    return `
      <nav class="bar"><span>Для батьків</span></nav>
      <section class="card">
        <form data-form="gate" class="gate">
          <label>${PARENT_QUESTION}
            <input id="gate-answer" inputmode="numeric" autocomplete="off">
          </label>
          <button class="btn" type="submit">Відкрити</button>
          <p class="note" id="gate-note"></p>
        </form>
      </section>`;
  }
  const summary = library.filter((w) => w.status !== 'soon').map((w) => {
    const p = state.works[w.id] || { scenes: {}, errors: {} };
    const done = Object.values(p.scenes).filter((e) => e.done).length;
    const errors = Object.values(p.errors).reduce((sum, n) => sum + n, 0);
    return `<tr><td>${esc(w.title)}</td><td>${done}/${w.scenes}</td><td>${errors}</td></tr>`;
  }).join('');
  const rows = !data ? '' : data.scenes.map((scene) => {
    const entry = prog().scenes[scene.num] || {};
    const status = entry.done ? 'Пройдено'
      : LEVELS.some((l) => entry[l]) ? 'Частково'
        : isUnlocked(scene.num) ? 'Не почато' : 'Закрито';
    const errors = LEVELS.reduce((sum, l) => sum + (prog().errors[`${scene.num}.${l}`] || 0), 0);
    return `<tr><td>${scene.num}</td><td>${esc(scene.title)}</td><td>${status}</td><td>${errors}</td></tr>`;
  }).join('');
  const voices = ukrainianVoices();
  const voiceOptions = ['<option value="">Авто</option>']
    .concat(voices.map((v) => `<option value="${esc(v.name)}" ${state.settings.voice === v.name ? 'selected' : ''}>${esc(v.name)}</option>`))
    .join('');
  return `
    <nav class="bar"><span>Для батьків</span></nav>
    <section class="card">
      <h2>Твори</h2>
      <table class="stats">
        <thead><tr><th>Твір</th><th>Сцени</th><th>Помилки</th></tr></thead>
        <tbody>${summary}</tbody>
      </table>
    </section>
    ${data ? `<section class="card">
      <h2>Сцени: ${esc(work().title)}</h2>
      <table class="stats">
        <thead><tr><th>№</th><th>Сцена</th><th>Стан</th><th>Помилки</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <p class="note">Помилки в парах: ${prog().errors.pari || 0}</p>
    </section>` : ''}
    <section class="card">
      <h2>Налаштування</h2>
      <label class="check"><input type="checkbox" data-setting="openAll" ${state.settings.openAll ? 'checked' : ''}> Відкрити всі сцени</label>
      <label>Голос<select data-setting="voice">${voiceOptions}</select></label>
      ${canSpeak && voices.length === 0 ? '<p class="note">Український голос не знайдено. Текст можна прочитати разом із дитиною.</p>' : ''}
    </section>
    <section class="card">
      <h2>Дані</h2>
      <div class="row">
        <button class="btn ghost" data-action="export">Експорт</button>
        <label class="btn ghost">Імпорт<input type="file" accept="application/json" data-import hidden></label>
      </div>
      ${session.askReset
        ? '<div class="row"><button class="btn" data-action="reset-confirm">Так, скинути</button><button class="btn ghost" data-action="reset-cancel">Ні</button></div>'
        : '<div class="row"><button class="btn ghost" data-action="reset">Скинути прогрес</button></div>'}
      <p class="note" role="status">${esc(session.note || '')}</p>
    </section>`;
}

// ---------- Головна ----------

function tabs(active) {
  const item = (key, href, label, icon) => `
    <a class="tab${active === key ? ' on' : ''}" href="${href}" ${active === key ? 'aria-current="page"' : ''}>
      ${icon}<span>${label}</span>
    </a>`;
  return `<nav class="tabs" aria-label="Головне меню">
    ${item('library', '#/', 'Бібліотека', ICON_BOOK)}
    ${workId ? item('home', base(), 'Сцени', ICON_CITY) : ''}
    ${workId && data.pairs?.length ? item('pari', `${base()}/pari`, 'Пари', ICON_PAIR) : ''}
    ${item('parent', '#/parent', 'Батькам', ICON_PERSON)}
  </nav>`;
}

function placeView(scene) {
  const [x, y] = work().map.pos[scene.num];
  const status = sceneStatus(scene);
  const label = { done: 'пройдено', locked: 'закрито', next: 'наступна', open: 'відкрито' }[status];
  const attrs = status === 'locked' ? 'disabled' : `data-go="${base()}/scene/${scene.num}"`;
  return `<button class="place ${status}" style="left:${x / 6}%;top:${y / 4.2}%" aria-label="Сцена ${scene.num}: ${esc(scene.title)}, ${label}" ${attrs}>${status === 'done' ? '✓' : scene.num}</button>`;
}

function homeView() {
  const next = nextNum();
  const current = next ? sceneByNum(next) : null;
  const done = doneCount();
  const leaves = Array.from({ length: total() }, (_, i) => `<span class="leaf${i < done ? ' on' : ''}"></span>`).join('');
  const card = current
    ? `<section class="card now" aria-label="Наступна сцена">
        <img class="thumb" src="${charOf(current.stage[0].char).img}" alt="">
        <div class="now-text">
          <span class="muted">Сцена ${current.num} з ${total()}</span>
          <span class="now-title">${esc(current.title)}</span>
          <span class="pills">${LEVELS.map((l) => `<span class="pill${prog().scenes[current.num]?.[l] ? ' on' : ''}">${l}${prog().scenes[current.num]?.[l] ? ' ✓' : ''}</span>`).join('')}</span>
        </div>
        <a class="btn" href="${base()}/scene/${current.num}">Продовжити</a>
      </section>`
    : `<section class="card now">
        <div class="now-text"><span class="now-title">Усі сцени пройдено</span>
        <span class="muted">Можна повторити будь-яку сцену.</span></div>
        <a class="btn" href="${base()}/scene/1">Сцена 1</a>
      </section>`;
  return `
    <nav class="bar">
      <a class="back" href="#/">← Бібліотека</a>
      <span>${esc(work().author)}</span>
    </nav>
    <h1 class="title">${esc(work().title)}</h1>
    ${card}
    ${work().map ? `
    <section class="map" aria-label="Карта">
      <img class="map-bg" src="${work().map.img}" alt="">
      ${data.scenes.map(placeView).join('')}
    </section>
    <div class="gold-row">
      <span>Золота роздано</span>
      <span class="leaves" aria-hidden="true">${leaves}</span>
      <span class="count">${done}/${total()}</span>
    </div>` : pathView()}
    <a class="pari-card" href="${base()}/pari"><span class="pari-title">Пари</span><span>Знайди, хто це</span></a>
    ${tabs('home')}`;
}

function sceneStatus(scene) {
  return isDone(scene.num) ? 'done'
    : !isUnlocked(scene.num) ? 'locked'
      : scene.num === nextNum() ? 'next' : 'open';
}

// Доріжка сцен для творів без карти.
function pathView() {
  const steps = data.scenes.map((scene) => {
    const status = sceneStatus(scene);
    const attrs = status === 'locked' ? 'disabled' : `data-go="${base()}/scene/${scene.num}"`;
    return `<li class="step ${status}">
      <button class="step-btn" ${attrs} aria-label="Сцена ${scene.num}: ${esc(scene.title)}">
        <span class="step-pic">${picture(scene.bg, scene.stage)}</span>
        <span class="step-num">${status === 'done' ? '✓' : scene.num}</span>
        <span class="step-title">${esc(scene.title)}</span>
      </button>
    </li>`;
  }).join('');
  return `<ol class="path" aria-label="Сцени">${steps}</ol>
    <p class="note">Пройдено ${doneCount()} з ${total()}</p>`;
}

// ---------- Бібліотека ----------

function libraryView() {
  const cards = library.map((w) => {
    const done = Object.values(state.works[w.id]?.scenes || {}).filter((e) => e.done).length;
    const ready = w.status !== 'soon';
    const kind = w.kind === 'poem' ? 'Вірш' : w.kind === 'tale' ? 'Казка' : '';
    const inner = `
      <img class="cover" src="${w.cover}" alt="">
      <span class="work-text">
        <span class="work-title">${esc(w.title)}</span>
        <span class="muted">${esc(w.author)}${kind ? ` · ${kind}` : ''}</span>
        ${ready
          ? `<span class="work-bar"><span style="width:${(done / w.scenes) * 100}%"></span></span>
             <span class="muted">${done} з ${w.scenes}</span>`
          : '<span class="muted">Скоро</span>'}
      </span>`;
    return ready
      ? `<a class="card work" href="#/w/${w.id}">${inner}</a>`
      : `<div class="card work soon">${inner}</div>`;
  }).join('');
  return `
    <header class="top">
      <div class="brand"><span class="leaf-logo" aria-hidden="true"></span>Переказ</div>
    </header>
    <h1 class="title">Бібліотека</h1>
    <p class="note">Українська література, 5 клас</p>
    <div class="works">${cards}</div>
    ${tabs('library')}`;
}

// ---------- Роутинг і малювання ----------

async function loadWork(id) {
  if (!workCache[id]) {
    const get = (file) => fetch(`data/works/${id}/${file}`).then((r) => {
      if (!r.ok) throw new Error(file);
      return r.json();
    });
    const [scenes, characters] = await Promise.all([get('scenes.json'), get('characters.json')]);
    workCache[id] = { pairs: scenes.pairs || [], scenes: scenes.scenes, characters };
  }
  return workCache[id];
}

async function route() {
  const parts = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean);
  // Старі адреси без твору ведуть у «Щасливого принца».
  if (parts[0] === 'scene' || parts[0] === 'pari') return go(`#/w/happy-prince/${parts.join('/')}`);
  if (parts[0] === 'parent') {
    session = { kind: 'parent', askReset: false, note: '' };
    return draw();
  }
  if (parts[0] !== 'w') {
    session = { kind: 'library' };
    return draw();
  }
  const [, id, page, arg, sub] = parts;
  if (!library.some((w) => w.id === id && w.status !== 'soon')) return go('#/');
  if (workId !== id) {
    try {
      data = await loadWork(id);
      workId = id;
    } catch {
      app.innerHTML = '<p class="note">Не вдалося завантажити твір. Перевірте з’єднання і оновіть сторінку.</p>';
      return undefined;
    }
  }
  if (page === 'scene') {
    const n = Number(arg);
    if (!sceneByNum(n)) return go(base());
    session = sub === 'retell'
      ? { kind: 'retell', n, revealed: false, heard: '', listening: false, active: null, zoom: null }
      : newSceneSession(n);
    return draw();
  }
  if (page === 'pari' && data.pairs.length) {
    session = newPariSession();
    return draw();
  }
  session = { kind: 'home' };
  return draw();
}

function view() {
  if (session.kind === 'scene') return `<main class="screen">${sceneView()}</main>`;
  if (session.kind === 'retell') return `<main class="screen">${retellView()}</main>`;
  if (session.kind === 'pari') return `<main class="screen">${pariView()}${tabs('pari')}</main>`;
  if (session.kind === 'parent') return `<main class="screen">${parentView()}${tabs('parent')}</main>`;
  if (session.kind === 'library') return `<main class="screen">${libraryView()}</main>`;
  return `<main class="screen">${homeView()}</main>`;
}

function draw() {
  app.innerHTML = view();
  if (session?.announce) {
    session.announce = false;
    say(currentPrompt());
  }
}

function currentPrompt() {
  if (session.kind === 'scene') return currentSceneQuestion().q.prompt;
  if (session.kind === 'pari') return `Покажи: ${charOf(session.queue[session.index].target).acc}`;
  return '';
}

// ---------- Події ----------

function exportProgress() {
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'perekaz-progres.json';
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function importProgress(file) {
  file.text()
    .then((text) => {
      const parsed = JSON.parse(text);
      const ok = parsed && (typeof parsed.works === 'object' || typeof parsed.scenes === 'object');
      if (!ok) throw new Error('bad format');
      const incoming = migrate(parsed);
      state = { ...state, works: { ...state.works, ...incoming.works }, settings: { ...state.settings, ...(parsed.settings || {}) } };
      saveState(state);
      session.note = 'Прогрес відновлено.';
    })
    .catch(() => {
      session.note = 'Не вдалося прочитати файл. Потрібен файл, збережений через «Експорт».';
    })
    .finally(draw);
}

app.addEventListener('click', (event) => {
  const link = event.target.closest('[data-go]');
  if (link) {
    go(link.dataset.go);
    return;
  }
  const button = event.target.closest('[data-action]');
  if (!button) return;
  switch (button.dataset.action) {
    case 'replay': say(currentPrompt()); break;
    case 'slow': say(currentPrompt(), 0.6); break;
    case 'pick': pickScene(button.dataset.id); break;
    case 'hint':
      session.hinted = true;
      session.feedback = currentSceneQuestion().q.hint;
      draw();
      break;
    case 'listen': listenScene(); break;
    case 'restart': session = newSceneSession(session.n); draw(); break;
    case 'retell-listen': retellListen(); break;
    case 'reveal': session.revealed = !session.revealed; draw(); break;
    case 'zoom': session.zoom = Number(button.dataset.i); draw(); break;
    case 'zoom-close': session.zoom = null; draw(); break;
    case 'phrase': {
      const i = Number(button.dataset.i);
      session.active = i;
      say(sceneByNum(session.n).frames[i].text);
      draw();
      break;
    }
    case 'pari-pick': pariPick(button.dataset.id); break;
    case 'pari-next': pariNext(true); break;
    case 'pari-restart': session = newPariSession(); draw(); break;
    case 'export': exportProgress(); break;
    case 'reset': session.askReset = true; draw(); break;
    case 'reset-cancel': session.askReset = false; draw(); break;
    case 'reset-confirm':
      state = resetState();
      session.askReset = false;
      session.note = 'Прогрес скинуто.';
      draw();
      break;
    default: break;
  }
});

app.addEventListener('submit', (event) => {
  const form = event.target.closest('[data-form="gate"]');
  if (!form) return;
  event.preventDefault();
  const answer = form.querySelector('#gate-answer').value.trim();
  if (answer === PARENT_ANSWER) {
    parentOpen = true;
    draw();
  } else {
    form.querySelector('#gate-note').textContent = 'Ні, спробуйте ще раз.';
  }
});

app.addEventListener('change', (event) => {
  const setting = event.target.dataset.setting;
  if (setting) {
    state.settings[setting] = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    saveState(state);
    return;
  }
  if (event.target.matches('[data-import]') && event.target.files[0]) {
    importProgress(event.target.files[0]);
  }
});

// ---------- Старт ----------

// Прогрес з першої версії (лише «Щасливий принц») переносимо у твори.
function migrate(saved) {
  const next = { ...saved, works: { ...(saved.works || {}) } };
  if (saved.scenes || saved.errors) {
    next.works['happy-prince'] = { scenes: saved.scenes || {}, errors: saved.errors || {} };
    delete next.scenes;
    delete next.errors;
  }
  return next;
}

async function init() {
  try {
    const r = await fetch('data/works.json');
    if (!r.ok) throw new Error('works');
    library = (await r.json()).works;
  } catch {
    app.innerHTML = '<p class="note">Не вдалося завантажити дані. Перевірте з’єднання і оновіть сторінку.</p>';
    return;
  }
  state = migrate(state);
  saveState(state);
  window.addEventListener('hashchange', route);
  route();
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
}

init();
