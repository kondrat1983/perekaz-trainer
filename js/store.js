// Прогрес зберігається локально. Якщо сховище недоступне, працюємо в пам'яті.
const KEY = 'perekaz.v1';

function emptyState() {
  return { works: {}, settings: { voice: '', openAll: false, wait: 5 } };
}

let cache = null;

export function loadState() {
  if (cache) return cache;
  try {
    const raw = localStorage.getItem(KEY);
    cache = raw ? { ...emptyState(), ...JSON.parse(raw) } : emptyState();
  } catch {
    cache = emptyState();
  }
  return cache;
}

export function saveState(state) {
  cache = state;
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch {
    // Сховище недоступне (приватний режим, блокування). Прогрес живе до перезавантаження.
  }
}

export function resetState() {
  cache = emptyState();
  try {
    localStorage.removeItem(KEY);
  } catch {
    // Див. saveState.
  }
  return cache;
}
