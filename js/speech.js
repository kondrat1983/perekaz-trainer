// Голос: синтез (speechSynthesis) і розпізнавання (SpeechRecognition), якщо вони є в браузері.
const hasTTS = 'speechSynthesis' in window;
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition || null;

export const canSpeak = hasTTS;
export const canListen = Boolean(Recognition);

export function ukrainianVoices() {
  if (!hasTTS) return [];
  return speechSynthesis.getVoices().filter((voice) => /^uk/i.test(voice.lang));
}

export function pickVoice(preferredName) {
  const voices = ukrainianVoices();
  return (
    voices.find((voice) => voice.name === preferredName) ||
    voices.find((voice) => /lesya|леся/i.test(voice.name)) ||
    voices[0] ||
    null
  );
}

export function speak(text, { rate = 0.95, voiceName = '' } = {}) {
  if (!hasTTS) return false;
  try {
    speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'uk-UA';
    utterance.rate = rate;
    const voice = pickVoice(voiceName);
    if (voice) utterance.voice = voice;
    speechSynthesis.speak(utterance);
    return true;
  } catch {
    return false;
  }
}

// Слухає одну фразу. onResult получает список варіантів розпізнавання.
export function listen({ onResult, onEnd }) {
  if (!Recognition) {
    onEnd?.();
    return null;
  }
  try {
    const recognition = new Recognition();
    recognition.lang = 'uk-UA';
    recognition.maxAlternatives = 5;
    recognition.interimResults = false;
    recognition.onresult = (event) => {
      const result = event.results[0];
      const alternatives = [];
      for (let i = 0; i < result.length; i += 1) alternatives.push(result[i].transcript);
      onResult(alternatives);
    };
    recognition.onend = () => onEnd?.();
    recognition.onerror = () => onEnd?.();
    recognition.start();
    return recognition;
  } catch {
    onEnd?.();
    return null;
  }
}
