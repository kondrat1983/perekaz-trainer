import test from 'node:test';
import assert from 'node:assert/strict';
import { normalizeAnswer, matchesAnswer } from '../js/normalize.js';

const table = [
  ['Щасливий Принц!', 'щасливий принц'],
  ['  Ластівка. ', 'ластівка'],
  ['Ластівку', 'ластівку'],
  ["Кравчиня’", 'кравчиня'],
  ["Дівчинка з сірниками", 'дівчинка з сірниками'],
  ['Бо статуя — нічого', 'бо статуя нічого'],
  ['  Ти   правильно (вибрав)  ', 'ти правильно вибрав'],
  ['', ''],
  [undefined, ''],
];

for (const [input, expected] of table) {
  test(`normalizeAnswer(${JSON.stringify(input)}) → ${JSON.stringify(expected)}`, () => {
    assert.equal(normalizeAnswer(input), expected);
  });
}

test('matchesAnswer accepts a normalized match', () => {
  assert.equal(matchesAnswer('Ластівка!', ['ластівка', 'ластівку']), true);
});

test('matchesAnswer rejects another character', () => {
  assert.equal(matchesAnswer('Очерет', ['ластівка']), false);
});

test('matchesAnswer rejects an empty answer', () => {
  assert.equal(matchesAnswer('   ', ['ластівка']), false);
});
