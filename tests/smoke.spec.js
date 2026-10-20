import { test, expect } from '@playwright/test';

// Режим «Вибір»: проходимо сцену 1 і перевіряємо, що прогрес збережено після перезавантаження.
test('scene 1 can be passed and progress survives reload', async ({ page }) => {
  await page.goto('/#/');
  await expect(page.getByRole('heading', { name: 'Бібліотека' })).toBeVisible();
  await page.getByRole('link', { name: /Щасливий принц/ }).click();
  await expect(page.getByRole('heading', { name: 'Щасливий принц' })).toBeVisible();
  await expect(page.getByRole('button', { name: /Сцена 1: Статуя/ })).toBeVisible();

  await page.goto('/#/w/happy-prince/scene/1');
  await page.getByRole('button', { name: 'Щасливий принц', exact: true }).click();
  await page.getByRole('button', { name: 'стоїть', exact: true }).click();
  await page.getByRole('button', { name: 'Бо статуя нічого не робить для людей' }).click();
  await expect(page.getByText('Сцену пройдено!')).toBeVisible();

  await page.reload();
  await page.goto('/#/w/happy-prince');
  await expect(page.getByRole('button', { name: /Сцена 1: Статуя, пройдено/ })).toBeVisible();
  await expect(page.getByRole('button', { name: /Сцена 2: .*наступна/ })).toBeVisible();
});

test('parent gate opens with the sum answer', async ({ page }) => {
  await page.goto('/#/parent');
  await page.getByLabel('Скільки буде 7 × 8?').fill('56');
  await page.getByRole('button', { name: 'Відкрити' }).click();
  await expect(page.getByRole('heading', { name: 'Твори' })).toBeVisible();
});

test('retell shows three frames and highlights the tapped phrase', async ({ page }) => {
  await page.goto('/#/w/happy-prince/scene/2/retell');
  await expect(page.locator('.frame')).toHaveCount(3);
  await page.getByRole('button', { name: 'Показати переказ' }).click();
  await page.getByRole('button', { name: /Вона закохалась в Очерет/ }).click();
  await expect(page.getByRole('button', { name: 'Кадр 2' })).toHaveClass(/on/);
  await page.getByRole('button', { name: 'Кадр 1' }).click();
  await expect(page.getByRole('dialog', { name: 'Кадр 1' })).toBeVisible();
  await page.getByRole('button', { name: 'Закрити' }).click();
  await expect(page.getByRole('dialog')).toHaveCount(0);
});

test('old progress without works moves into the happy prince', async ({ page }) => {
  await page.addInitScript(() => {
    localStorage.setItem('perekaz.v1', JSON.stringify({ scenes: { 1: { L1: true, L2: true, L3: true, done: true } }, errors: {}, settings: {} }));
  });
  await page.goto('/#/scene/1');
  await expect(page).toHaveURL(/#\/w\/happy-prince\/scene\/1/);
  await page.goto('/#/w/happy-prince');
  await expect(page.getByRole('button', { name: /Сцена 1: Статуя, пройдено/ })).toBeVisible();
});

// Вірш: одна сцена з питаннями, без переказу.
test('a poem is a quiz without retell', async ({ page }) => {
  const res = await page.request.get('/data/works/learn-read/scenes.json');
  const { scenes } = await res.json();
  await page.goto('/#/w/learn-read/scene/1');
  for (const q of Object.values(scenes[0].questions)) {
    await expect(page.getByText(q.prompt)).toBeVisible();
    await expect(page.getByRole('link', { name: 'Переказ' })).toHaveCount(0);
    const right = q.options.find((o) => o.id === q.answer).text;
    await page.getByRole('button', { name: right, exact: true }).click();
  }
  await expect(page.getByText('Сцену пройдено!')).toBeVisible();
});
