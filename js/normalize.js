// Нормалізація відповідей: нижній регістр, без апострофа і розділових знаків.
export function normalizeAnswer(text) {
  return String(text ?? '')
    .toLowerCase()
    .replace(/[’ʼ'`´]/g, '')
    .replace(/[.,!?;:"«»()[\]…\-–—]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function matchesAnswer(input, accepted) {
  const normalized = normalizeAnswer(input);
  return normalized !== '' && accepted.some((answer) => normalizeAnswer(answer) === normalized);
}
