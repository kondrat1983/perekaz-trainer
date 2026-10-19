import { defineConfig } from '@playwright/test';

// На CI і в сесії можна вказати свій Chromium через CHROME_PATH.
const executablePath = process.env.CHROME_PATH || undefined;

export default defineConfig({
  testDir: 'tests',
  testMatch: /.*\.spec\.js/,
  use: {
    baseURL: 'http://localhost:4173',
    launchOptions: executablePath ? { executablePath } : {},
    viewport: { width: 390, height: 844 },
  },
  webServer: {
    command: 'python3 -m http.server 4173',
    url: 'http://localhost:4173',
    reuseExistingServer: true,
  },
});
