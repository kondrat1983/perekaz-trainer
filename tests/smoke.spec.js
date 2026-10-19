import { test, expect } from '@playwright/test';

// Режим «Вибір»: проходимо сцену 1 і перевіряємо, що прогрес збережено після перезавантаження.
test('scene 1 can be passed and progress survives reload', async ({ page }) => {
  await page.goto('/#/');
  await expect(page.getByRole('heading', { name: 'Щасливий принц' })).toBeVisible();
  await expect(page.getByRole('button', { name: /Сцена 1: Статуя/ })).toBeVisible();

  await page.goto('/#/scene/1');
  await page.getByRole('button', { name: 'Щасливий принц', exact: true }).click();
  await page.getByRole('button', { name: 'стоїть', exact: true }).click();
  await page.getByRole('button', { name: 'Бо статуя нічого не робить для людей' }).click();
  await expect(page.getByText('Сцену пройдено!')).toBeVisible();

  await page.reload();
  await page.goto('/#/');
  await expect(page.getByRole('button', { name: /Сцена 1: Статуя, пройдено/ })).toBeVisible();
  await expect(page.getByRole('button', { name: /Сцена 2: .*наступна/ })).toBeVisible();
});

test('parent gate opens with the sum answer', async ({ page }) => {
  await page.goto('/#/parent');
  await page.getByLabel('Скільки буде 7 × 8?').fill('56');
  await page.getByRole('button', { name: 'Відкрити' }).click();
  await expect(page.getByRole('heading', { name: 'Сцени' })).toBeVisible();
});
