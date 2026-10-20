import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';

const scenes = JSON.parse(readFileSync('data/scenes.json', 'utf8')).scenes;
const characters = JSON.parse(readFileSync('data/characters.json', 'utf8'));
const sw = readFileSync('sw.js', 'utf8');

const paths = new Set(Object.values(characters).map((c) => c.img));
for (const c of Object.values(characters)) for (const p of Object.values(c.poses || {})) paths.add(p);
for (const scene of scenes) {
  if (scene.bg) paths.add(scene.bg);
  for (const q of Object.values(scene.questions)) {
    for (const o of q.options) if (o.img) paths.add(o.img);
  }
  for (const f of scene.frames) {
    if (f.bg) paths.add(f.bg);
    for (const a of f.actors) if (a.img) paths.add(a.img);
  }
}

test('every scene has three frames whose phrases make up the summary', () => {
  for (const scene of scenes) {
    assert.equal(scene.frames.length, 3, `scene ${scene.num}`);
    assert.equal(scene.frames.map((f) => f.text).join(' '), scene.summary, `scene ${scene.num}`);
  }
});

test('every frame character exists', () => {
  for (const scene of scenes) {
    for (const f of scene.frames) {
      for (const a of f.actors) {
        if (a.char) assert.ok(characters[a.char], `${scene.num}: ${a.char}`);
        if (a.pose) assert.ok(characters[a.char].poses?.[a.pose], `${scene.num}: ${a.char}-${a.pose}`);
      }
    }
  }
});

for (const path of paths) {
  test(`${path} exists and is cached offline`, () => {
    assert.ok(existsSync(path), 'file is missing');
    assert.ok(sw.includes(`'${path}'`), 'not listed in sw.js');
  });
}
