#!/usr/bin/env node
/**
 * prepare-content.mjs — turn the built prompts into data the Astro site renders.
 *
 * Source of truth is the repo-root `dist/` tree (expanded, copy-paste-ready
 * prompts). For each `dist/**\/*.prompt.md` we strip the two generated header
 * comment lines and any YAML frontmatter — exactly what `sync-owui.py` strips —
 * so the site's "Copy" button yields the same text users paste, and the
 * rendered body is the prompt itself, not repo bookkeeping.
 *
 * Outputs (all gitignored, regenerated on every build):
 *   site/src/data/prompts.json      — every prompt: metadata, raw text, HTML
 *   site/src/data/userguide.json    — rendered USERGUIDE.md
 *   site/src/data/contributing.json — rendered CONTRIBUTING.md
 *   site/public/search-index.json   — client-side full-text search index
 */
import {
  readFileSync,
  writeFileSync,
  readdirSync,
  statSync,
  mkdirSync,
  rmSync,
} from 'node:fs';
import { join, dirname, resolve, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SITE = resolve(__dirname, '..');
const ROOT = resolve(SITE, '..');
const DIST = join(ROOT, 'dist');
const DATA = join(SITE, 'src', 'data');
const PUBLIC = join(SITE, 'public');

// Must match `base` in astro.config.mjs. The store is served from the domain
// root (https://prompts.ronzz.org/), so site-internal links start at '/'.
const BASE = '';
const REPO_BLOB = 'https://github.com/Ron-RONZZ-org/ronzz-LLM-prompt-hub/blob/main';

// Generated header: one or more leading HTML comments + surrounding whitespace.
const HEADER_RE = /^\s*(?:<!--[\s\S]*?-->\s*)+/;
// Optional flat YAML frontmatter block at the very head of the file.
const FRONTMATTER_RE = /^---\n([\s\S]*?)\n---\n?/;

// Headings that name a *section*, not the prompt — never used as a title.
const GENERIC_HEADINGS = new Set([
  'task', 'tasks', 'requirements', 'context', 'article', 'topic', 'target',
  'source', 'sources', 'source(s) of truth', 'overview', 'instructions',
  'notes', 'rules',
]);

function walk(dir) {
  const found = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) found.push(...walk(path));
    else if (name.endsWith('.prompt.md')) found.push(path);
  }
  return found;
}

function unquote(value) {
  const v = value.trim();
  if (v.length >= 2 && (v[0] === '"' || v[0] === "'") && v.at(-1) === v[0]) {
    return v.slice(1, -1);
  }
  return v;
}

// Flat subset only — mirrors sync-owui.py's parser (`key: value`, `key: [a, b]`).
function parseScalar(value) {
  const v = value.trim();
  if (v.startsWith('[') && v.endsWith(']')) {
    const inner = v.slice(1, -1).trim();
    return inner ? inner.split(',').map((item) => unquote(item)) : [];
  }
  return unquote(v);
}

function parseFrontmatter(text) {
  const match = FRONTMATTER_RE.exec(text);
  if (!match) return [{}, text];
  const meta = {};
  for (const rawLine of match[1].split('\n')) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const colon = line.indexOf(':');
    if (colon === -1) continue;
    meta[line.slice(0, colon).trim()] = parseScalar(line.slice(colon + 1));
  }
  return [meta, text.slice(match[0].length)];
}

function cleanHeading(raw) {
  let text = raw.replace(/^#+\s*/, '').trim();
  text = text.replace(/^TASK\s*[:\-—]\s*/i, '');
  if (!text || GENERIC_HEADINGS.has(text.toLowerCase())) return null;
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function humanize(stem) {
  return stem
    .replace(/[_-]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .replace(/^\w/, (c) => c.toUpperCase());
}

function titleOf(stem, meta, body) {
  if (meta.name) return String(meta.name);
  const heading = /^#{1,3}\s+(.+)$/m.exec(body);
  if (heading) {
    const cleaned = cleanHeading(heading[1]);
    if (cleaned) return cleaned;
  }
  return humanize(stem);
}

function excerptOf(body) {
  const plain = body
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\!?\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/^[#>\-*+\d.\s]+/gm, '')
    .replace(/[*_`>#]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
  return plain.length > 200 ? `${plain.slice(0, 197)}…` : plain;
}

function rewriteLinks(html) {
  return html.replace(/href="([^"]+)"/g, (whole, href) => {
    if (/^(https?:|mailto:|#|\/)/.test(href)) return whole;
    const target = href.replace(/^\.\//, '');
    const [file, anchor] = target.split('#');
    const suffix = anchor ? `#${anchor}` : '';
    if (file === 'USERGUIDE.md') return `href="${BASE}/userguide/${suffix}"`;
    if (file === 'CONTRIBUTING.md') return `href="${BASE}/contributing/${suffix}"`;
    if (file === 'README.md') return `href="${BASE}/${suffix}"`;
    if (file.endsWith('.md')) return `href="${REPO_BLOB}/${file}${suffix}"`;
    return whole;
  });
}

function render(markdown) {
  return marked.parse(markdown, { gfm: true, async: false });
}

function buildPrompt(file) {
  const rel = relative(DIST, file).split(sep).join('/');
  const slug = rel.replace(/\.prompt\.md$/, '');
  const parts = slug.split('/');
  const stem = parts.at(-1);
  const groups = parts.slice(0, -1);

  const text = readFileSync(file, 'utf8').replace(HEADER_RE, '');
  const [meta, bodyRaw] = parseFrontmatter(text);
  const body = `${bodyRaw.replace(/^\n+/, '').replace(/\s+$/, '')}\n`;

  return {
    slug,
    stem,
    groups,
    kind: groups[0] === 'system-prompt' ? 'model' : 'prompt',
    title: titleOf(stem, meta, body),
    description: meta.description ? String(meta.description) : null,
    tags: Array.isArray(meta.tags) ? meta.tags.map(String) : [],
    baseModel: meta.base_model ? String(meta.base_model) : null,
    raw: body,
    html: render(body),
    excerpt: excerptOf(body),
  };
}

function buildDoc(file) {
  const html = rewriteLinks(render(readFileSync(file, 'utf8')));
  return { html };
}

function writeJson(path, value) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(value, null, 2)}\n`);
}

function main() {
  if (!statSync(DIST, { throwIfNoEntry: false })) {
    throw new Error(`dist/ not found at ${DIST} — run 'python3 build-prompts.py' first`);
  }

  const prompts = walk(DIST)
    .map(buildPrompt)
    .sort((a, b) => a.title.localeCompare(b.title));

  const searchIndex = prompts.map((p) => ({
    slug: p.slug,
    title: p.title,
    kind: p.kind,
    groups: p.groups,
    text: `${p.title} ${p.excerpt} ${p.raw}`.toLowerCase(),
  }));

  rmSync(DATA, { recursive: true, force: true });
  writeJson(join(DATA, 'prompts.json'), prompts);
  writeJson(join(DATA, 'userguide.json'), buildDoc(join(ROOT, 'USERGUIDE.md')));
  writeJson(join(DATA, 'contributing.json'), buildDoc(join(ROOT, 'CONTRIBUTING.md')));
  writeJson(join(PUBLIC, 'search-index.json'), searchIndex);

  const models = prompts.filter((p) => p.kind === 'model').length;
  console.log(
    `prepared ${prompts.length} prompts (${models} models) + 2 docs → site/src/data, site/public/search-index.json`,
  );
}

main();
