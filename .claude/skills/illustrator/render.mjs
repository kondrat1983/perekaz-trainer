// Рендер листа превью для SVG-картинок: крупно, 56 px и в оттенках серого.
// Запуск: node .claude/skills/illustrator/render.mjs images/a.svg images/b.svg [--out папка]
import { chromium } from 'playwright';
import { mkdirSync, readFileSync } from 'node:fs';
import { resolve, basename } from 'node:path';
import { tmpdir } from 'node:os';

const args = process.argv.slice(2);
const outIndex = args.indexOf('--out');
const outDir = outIndex >= 0 ? resolve(args[outIndex + 1]) : resolve(tmpdir(), 'illustrator');
const files = args.filter((a, i) => a.endsWith('.svg') && i !== outIndex + 1);
if (files.length === 0) {
  console.error('Укажи хотя бы один .svg файл.');
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });

const dataUri = (file) => `data:image/svg+xml;base64,${readFileSync(file).toString('base64')}`;
const cell = (file, size, grey) => `
  <figure style="margin:0;display:flex;flex-direction:column;align-items:center;gap:4px">
    <div style="width:${size}px;height:${size}px;background:#FFF4D6;border-radius:12px;position:relative;overflow:hidden">
      <img src="${dataUri(file)}" style="position:absolute;inset:4%;width:92%;height:92%;object-fit:contain;${grey ? 'filter:grayscale(1)' : ''}">
    </div>
    <figcaption style="font:12px sans-serif;color:#5B6475">${basename(file)}${grey ? ' · серый' : ''}</figcaption>
  </figure>`;

const row = (size, grey = false) => `<div style="display:flex;gap:12px;align-items:flex-end">${files.map((f) => cell(f, size, grey)).join('')}</div>`;
const html = `<body style="margin:0;padding:16px;background:#F6F1E7;display:flex;flex-direction:column;gap:16px">
  ${row(260)}${row(56)}${row(140, true)}</body>`;

const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const page = await browser.newPage({ viewport: { width: Math.max(400, files.length * 280), height: 600 } });
await page.setContent(html);
await page.waitForTimeout(300);
const out = resolve(outDir, 'sheet.png');
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log(out);
