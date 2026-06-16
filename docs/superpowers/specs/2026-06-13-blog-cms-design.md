# Blog / Articles CMS — Design Spec

**Date:** 2026-06-13
**Project:** Invincible Security Group website (`invincible-inc`)
**Goal:** Add a self-service blog/articles section so the company can publish SEO content without a developer.

---

## Summary

Add a statically-generated blog to the existing static HTML site, powered by a headless CMS.

**Stack:** **Sanity** (CMS, free tier) → **Astro** (static build, blog-only) → **Netlify** (build + host) → **Sanity webhook** triggers a Netlify rebuild on publish.

Non-technical staff log into Sanity Studio, write a post, upload an image, and click Publish. A webhook rebuilds the site and the article goes live in ~1–2 minutes. No code, no git, no developer.

---

## 1. Current architecture (as inspected)

| Aspect | Reality |
|---|---|
| Framework | **None.** Pure static HTML/CSS/JS. Hand-coded `.html` files + Python generator scripts (`gen_pages.py`, `fix_isg.py`, `update_existing.py`) that stamp pages from string templates. No Node, no `package.json`, no React. |
| Routing | File-based. URLs map 1:1 to physical files (`/services/fire-watch.html`, `/industries/construction-sites.html`). |
| Build | No build step. Python generators run locally; footer injected client-side via `fetch('./footer.html')`. |
| Hosting | **Netlify**, auto-deploy on `git push` (confirmed). `_headers` file present. |
| SEO (existing) | Strong: per-page titles/descriptions, canonical, OG tags, JSON-LD (`LocalBusiness` + `Service`), `sitemap.xml`, `robots.txt`, GA4 + Microsoft Clarity. |

**Why Sanity is a fit (with a caveat):** Sanity's standard integration assumes a JS framework rendering pages. This site has none. So "add Sanity" requires introducing a static-site generator (Astro) to turn CMS content into crawlable HTML at build time. With that piece in place, Sanity is an excellent fit.

---

## 2. CMS recommendation

**Chosen: Sanity** (free tier).

| | **Sanity** ⭐ | Contentful | Strapi | Headless WordPress |
|---|---|---|---|---|
| Cost (this scale) | **$0** generous free tier | $0, tighter limits | $0 only if self-hosted → server to maintain | Hosting $$ or self-host + patching |
| Editor UX (non-tech) | Clean modern Studio, great image upload/crop | Clean, polished | Decent | Familiar but cluttered |
| Maintenance | None (hosted) | None (hosted) | **You patch the server** | **You patch WP + plugins (security)** |
| Image pipeline | **Built-in CDN, on-the-fly resize/format** | CDN included | Configure yourself | Needs plugins |
| Fit | ✅ all 3 constraints | ✅ runner-up | ❌ server upkeep | ❌ cost + maintenance + security |

**Why Sanity:** It is the only option satisfying all three hard constraints — **$0/month, zero servers to maintain, simple editor for non-technical staff** — while feeding a static build for clean SEO. Strapi and WordPress reintroduce a server to babysit. Contentful is a fine runner-up but its free tier is more restrictive and gets expensive sooner.

**Generator: Astro** — outputs plain static HTML/CSS (no heavy JS runtime), reuses the existing `styles.css` so the blog matches the site, first-class Sanity/image/RSS/sitemap support. Netlify runs `astro build`.

**Scope decision: blog-only.** Astro builds only `/blog` and `/blog/[slug]`. The 30+ existing hand-coded pages remain untouched as build passthrough. Lowest risk, smallest change. (Full-site Astro migration is a possible future phase, not in scope.)

---

## 3. Blog requirements

### Routes
- `/blog` — listing page: featured image, title, excerpt, category, date, reading time. Paginated if needed.
- `/blog/[slug]` — article page.

### Content model (Sanity schemas)

**`post`**
- title
- slug (auto-generated from title)
- excerpt
- featuredImage (+ **required** alt text)
- body (rich text / Portable Text)
- publishedAt
- category (reference)
- author (reference)
- seoTitle
- seoDescription
- ogImage (optional — overrides featuredImage for social)

**`category`** — title, slug, description. Seeded to match SEO targets: *Security Guard Services, Fire Watch, Mobile Patrol, Construction Site Security, Event Security*.

**`author`** — name, photo, role, short bio.

### Behavior
- **Drafts & publish** are native to Sanity — an unpublished doc is automatically a draft. No custom status field.
- **Reading time** and **Table of Contents** are computed at build time from the body (headings → TOC; word count → minutes). No editor input.
- **Related posts** = up to 3 from the same category, newest first.

---

## 4. SEO requirements

| Requirement | Implementation |
|---|---|
| Meta title / description | From `seoTitle` / `seoDescription`, falling back to title / excerpt |
| Open Graph + Twitter cards | Built per-post; `og:image` = featured image (or `ogImage`) via Sanity CDN |
| Structured data | JSON-LD `BlogPosting` (headline, image, datePublished/Modified, author, publisher) + `BreadcrumbList` |
| Canonical URLs | Absolute, single fixed host (see §9 risk 1 and clarification 2) |
| Sitemap | Generate `/blog-sitemap.xml` from Sanity at build; reference it in `robots.txt` alongside existing `sitemap.xml` |
| Internal linking | Each post links to the relevant service/industry page (fire-watch post → `/services/fire-watch.html`); categories mirror service lines; optional phase-2 "Related articles" block on service pages |

**Primary SEO goals (target keywords):** security guard services, fire watch services, mobile patrol services, construction site security, event security, California local searches. Category taxonomy and internal links are aligned to these.

---

## 5. Content workflow (non-technical editor)

1. Go to the Sanity Studio URL (hosted free by Sanity, e.g. `invincible.sanity.studio`) and log in (Google or email).
2. Click **Post → New**; type title / excerpt / body; pick category + author.
3. **Upload an image** by dragging it into the featured-image field (Sanity stores + serves from its CDN; crop in-browser).
4. Click **Publish** (or close to keep it a draft).
5. Sanity's webhook pings Netlify's build hook → Netlify runs `astro build` → article is **live in ~1–2 minutes**. No code, no git, no developer.

---

## 6. Cost analysis

| Item | Cost at this scale |
|---|---|
| Sanity | **$0** — free tier covers a small team (verify current seat count at signup; historically ~3, matches 1–3 editors) and far more content/bandwidth than a few posts/month needs |
| Netlify | **$0** — 300 build-min + 100 GB bandwidth/month free; a rebuild is ~1 min |
| Astro | **$0** open source |
| **Total** | **$0/month. Free tiers are sufficient.** First paid trigger would be >3 editors or very high traffic — far away. |

Assumptions: small business, few posts/month, 1–3 content editors.

---

## 7. Technical design

**Folder structure**
```
repo/
  public/            <- current site, UNTOUCHED passthrough (see clarification 1)
    index.html
    about.html
    services/ industries/
    css/ js/ images/
    sitemap.xml  robots.txt  _headers  ...
  src/
    pages/blog/
      index.astro    <- /blog listing
      [slug].astro   <- /blog/[slug] article
    pages/
      blog-sitemap.xml.ts   <- generated blog sitemap
    components/      <- Header, Footer, ArticleCard, TOC, RelatedPosts, Seo
    layouts/         <- BlogLayout
    lib/             <- sanityClient, imageUrl, queries (GROQ), readingTime, toc
  sanity/            <- schemas: post, category, author
  astro.config.mjs
  package.json
  .env               <- gitignored
```

**Environment variables**
- `SANITY_PROJECT_ID`
- `SANITY_DATASET` (= `production`)
- `SANITY_API_VERSION` (pinned date, e.g. `2024-01-01`)
- optional `SANITY_READ_TOKEN` (dataset can stay public-read; token only if private)

Set in Netlify UI for production; `.env` locally (gitignored).

**API architecture / data fetching**
- Build-time only. `@sanity/client` runs GROQ queries during `astro build`.
- `getStaticPaths()` generates one static HTML file per published slug.
- **Zero client-side CMS calls** — content is baked into HTML for SEO.

**Image handling**
- `@sanity/image-url` builds responsive `srcset` (WebP, multiple widths) off Sanity's CDN.
- `loading="lazy"` on in-body images; featured image eager + doubles as OG image.

---

## 8. Deployment strategy

**One-time production changes**
- Move current files into `public/` (only after inspection + local passthrough test — clarification 1).
- Add Astro config + Netlify build command (`astro build`, publish dir `dist`).
- Set env vars in Netlify.
- Create a Netlify **build hook** (a URL that triggers a build).
- Add that URL as a **Sanity webhook** firing on document publish/update.

**Rebuilds required?** Yes — but automatic and invisible to editors. Publishing in Sanity triggers the rebuild.

**Webhooks?** Yes: Sanity (on publish) → Netlify build hook. This is what makes posts appear automatically.

**How updates appear live:** publish in Studio → webhook → `astro build` on Netlify → new static HTML deployed → live in ~1–2 min.

---

## 9. Risks & decisions

1. **www vs non-www** — the existing site mixes them (canonical uses `www.`; robots/OG use non-www). Must standardize on one host before launch or SEO equity splits. **Decision (clarification 2): standardize on `https://invinciblesecuritygroup.com` (non-www) unless the existing production setup clearly prefers www.** Apply to all canonicals, sitemap URLs, robots.txt, OG URLs, and blog URLs; 301 the other host.
2. **Header/footer duplication** — blog gets its own Astro header/footer copy; changing the main nav later means updating two places. Mitigated long-term by the optional full-Astro migration.
3. **Build-time content lag** — ~1–2 min between Publish and live. Acceptable for a blog; sets expectations.
4. **First-ever build step** — the repo gains a Node/Astro build. Netlify handles it; only matters when cloning/building locally.
5. **Sanity free-tier seat count** — verify the current limit covers all editors at signup.

---

## Pre-implementation clarifications (authoritative)

These refine and, where they conflict, **override** the body above.

1. **Do not move the current website files into `public/`** until the current file structure is inspected and static passthrough is verified working locally. The migration of existing files is gated on a successful local passthrough test (existing pages, CSS, JS, images, and root-relative paths all resolve correctly under Astro's output).

2. **Standardize on a single domain** for all canonical URLs, sitemap URLs, `robots.txt`, Open Graph URLs, and blog URLs:
   `https://invinciblesecuritygroup.com`
   unless the existing production setup (Netlify primary domain / DNS) clearly prefers `www`. Confirm the Netlify primary domain before finalizing; whichever is primary wins, and the other 301-redirects to it.

3. **Sanity preview/draft-preview is optional** and **not part of Phase 1** unless it proves easy and low-risk. Phase 1 ships published-only static content.

4. **Phase 1 priority (build these first, in this order of importance):**
   - `/blog` listing page
   - `/blog/[slug]` article page
   - Sanity schemas (post, category, author)
   - SEO metadata (meta, OG, JSON-LD, canonical)
   - sitemap (`/blog-sitemap.xml` + robots.txt reference)
   - Netlify webhook rebuild (Sanity publish → build hook)

   Deferred to later phases: related posts, table of contents, reading time, "Related articles" block on service pages, draft preview, full-site Astro migration.

---

## Out of scope (this spec)

- Full-site migration to Astro.
- Comments, search, tags (beyond category), newsletter.
- Multi-language.
- Draft preview environment (Phase 1) — see clarification 3.
