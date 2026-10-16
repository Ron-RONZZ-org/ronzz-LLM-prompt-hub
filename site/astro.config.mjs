import { defineConfig } from 'astro/config';

// The prompt store is built inside the GitHub push mirror and deployed to
// GitHub Pages:
//   https://ron-ronzz-org.github.io/ronzz-LLM-prompt-hub/
//
// `base` MUST match the repository name for a project site. When serving from a
// custom domain (e.g. https://prompts.ronzz.org), set `site` to that domain and
// `base` to '/'.
export default defineConfig({
  site: 'https://ron-ronzz-org.github.io',
  base: '/ronzz-LLM-prompt-hub',
  outDir: '../_site',
  build: { assets: 'assets' },
});
