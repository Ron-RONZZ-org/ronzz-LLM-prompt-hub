import { defineConfig } from 'astro/config';

// The prompt store is built inside the GitHub push mirror and deployed to
// GitHub Pages under the ronzz.org custom domain:
//   https://prompts.ronzz.org/
//
// `base` is '/' because the site is served from the domain root. For the
// default project-site URL (https://<owner>.github.io/<repo>/) set `site` to
// that origin and `base` to '/ronzz-LLM-prompt-hub'.
export default defineConfig({
  site: 'https://prompts.ronzz.org',
  base: '/',
  outDir: '../_site',
  build: { assets: 'assets' },
});
