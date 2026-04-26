import { defineConfig } from '@playwright/test';
export default defineConfig({
  use: {
    // All requests go to this API-endpoint.
    baseURL: 'https://api.github.com',
    extraHTTPHeaders: {
      // Bt GitHub recommendations.
      'Accept': 'application/vnd.github.v3+json',
      // Autorisation tocken to all requests.
      'Authorization': `token ${process.env.API_TOKEN}`,
    },
  }
});