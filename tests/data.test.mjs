import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';

const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'));
const library = readJson('data/works.json').works;
const sw = readFileSync('sw.js', 'utf8');

test('works.json lists ready works with matching scene counts', () => {
  for (const work of library.filter((w) => w.status !== 'soon')) {
    const scenes = readJson(`data/works/${work.id}/scenes.json`).scenes;
    assert.equal(scenes.length, work.scenes, work.id);
    assert.ok(sw.includes(`'data/works/${work.id}/scenes.json'`), `${work.id} scenes not cached`);
    assert.ok(sw.includes(`'data/works/${work.id}/characters.json'`), `${work.id} characters not cached`);
  }
});

for (const work of library.filter((w) => w.status !== 'soon')) {
const scenes = readJson(`data/works/${work.id}/scenes.json`).scenes;
const characters = readJson(`data/works/${work.id}/characters.json`);

const paths = new Set(Object.values(characters).map((c) => c.img));
paths.add(work.cover);
if (work.map) paths.add(work.map.img);
for (const c of Object.values(characters)) for (const p of Object.values(c.poses || {})) paths.add(p);
for (const scene of scenes) {
  if (scene.bg) paths.add(scene.bg);
  for (const q of Object.values(scene.questions)) {
    for (const o of q.options) if (o.img) paths.add(o.img);
  }
  for (const f of scene.frames || []) {
    if (f.bg) paths.add(f.bg);
    for (const a of f.actors) if (a.img) paths.add(a.img);
  }
}

test(`${work.id}: every scene has three frames whose phrases make up the summary`, () => {
  for (const scene of scenes) {
    // Вірші й фольклор — без переказу: лише питання і одна картинка.
    if (!scene.frames) {
      assert.ok(['poem', 'folk'].includes(work.kind), `scene ${scene.num}: frames missing`);
      continue;
    }
    assert.equal(scene.frames.length, 3, `scene ${scene.num}`);
    assert.equal(scene.frames.map((f) => f.text).join(' '), scene.summary, `scene ${scene.num}`);
  }
});

test(`${work.id}: every character and pose on stage, in frames and in answers exists`, () => {
  for (const scene of scenes) {
    const used = [...scene.stage, ...(scene.frames || []).flatMap((f) => f.actors)];
    for (const q of Object.values(scene.questions)) {
      used.push(...q.options);
      assert.ok(q.options.length >= 2 && q.hint, `${scene.num}: options and hint`);
      assert.ok(q.options.some((o) => o.id === q.answer), `${scene.num}: answer ${q.answer}`);
      if (q.target) assert.ok(characters[q.target], `${scene.num}: target ${q.target}`);
    }
    for (const a of used) {
      if (a.char) assert.ok(characters[a.char], `${scene.num}: ${a.char}`);
      if (a.pose) assert.ok(characters[a.char].poses?.[a.pose], `${scene.num}: ${a.char}-${a.pose}`);
    }
  }
});

for (const path of paths) {
  test(`${work.id}: ${path} exists and is cached offline`, () => {
    assert.ok(existsSync(path), 'file is missing');
    assert.ok(sw.includes(`'${path}'`), 'not listed in sw.js');
  });
}
}
