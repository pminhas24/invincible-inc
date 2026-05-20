# Performance, Accessibility & SEO Overhaul — Invincible Security Group

**Date:** 2026-05-19
**Scope:** Static HTML/CSS/JS site hosted on Netlify (invinciblesecuritygroup.com)
**Approach:** Option A — Targeted Static Fixes (no build pipeline added)

---

## Goals

| Metric | Current | Target |
|---|---|---|
| Performance | 44 | 100 (or as close as possible) |
| Best Practices | 92 | 100 |
| Accessibility | 95 | 100 |
| SEO | 100 | 100 (maintain) |

### Core Web Vitals Targets

| Metric | Current | Target |
|---|---|---|
| FCP | 7.1s | < 1.8s |
| LCP | 15.0s | < 2.5s |
| TBT | 570ms | < 200ms |
| CLS | 0 ✅ | 0 |

---

## Section 1 — Performance

### 1.1 Self-Hosted Fonts

**Problem:** Inter is loaded from `fonts.googleapis.com`, adding a cross-origin DNS lookup, TLS handshake, and font download on every page load. This is a primary contributor to the 7.1s FCP.

**Solution:**
- Download Inter WOFF2 files for weights 400, 500, 600, 700, 800, 900 into `/fonts/`
- Add `@font-face` declarations at the top of `css/styles.css` pointing to `/fonts/inter-*.woff2`
- Use `font-display: swap` on all `@font-face` rules
- Remove all Google Fonts `<link>` tags, `<preconnect>` to `fonts.googleapis.com` and `fonts.gstatic.com`, from every HTML file
- Add `<link rel="preload" as="font" href="/fonts/inter-600.woff2" crossorigin>` (or weight 700) in `<head>` of every page to fetch the primary weight in parallel with CSS

**Files affected:** `css/styles.css`, all `.html` files

### 1.2 Delayed Analytics

**Problem:** Google Analytics (GA4) and Microsoft Clarity scripts load in `<head>` on every page, blocking the main thread and accounting for the majority of the 618 KiB unused JS and 570ms TBT.

**Solution:** Remove inline analytics script tags from all HTML files. In `main.js`, add a `loadAnalytics()` function that dynamically injects both script tags. The function fires on whichever comes first:
- A `setTimeout` of 3000ms
- The first of: `scroll`, `click`, `keydown`, `touchstart` user events (bound with `{ once: true }`)

If the cookie consent banner exists and the user has previously declined analytics, `loadAnalytics()` is never called.

**Files affected:** `js/main.js`, all `.html` files (remove inline script blocks)

### 1.3 Critical CSS Inline + Deferred Stylesheet

**Problem:** `styles.css` is loaded as a render-blocking stylesheet, delaying the First Contentful Paint until the full CSS file is downloaded and parsed.

**Solution:**
- Extract the above-the-fold CSS for `index.html` (top bar, navbar, hero section, `@font-face` declarations, CSS variables, base resets) into an inline `<style>` block in `<head>`
- Load the full `styles.css` asynchronously using the `rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'"` pattern
- Include a `<noscript>` fallback with the normal stylesheet link
- This change applies only to `index.html` first (the page being measured); other pages can follow the same pattern but are lower priority

**Files affected:** `index.html`, `css/styles.css` (no structural changes — just identify extraction candidates)

### 1.4 Responsive Images with `srcset`

**Problem:** All images serve the same full-size file regardless of device. Mobile visitors download desktop-resolution images, contributing to the 639 KiB savings flagged by Lighthouse.

**Solution:**
- For the hero image (`images/hero.webp`): create 3 size variants at 480w, 900w, and 1440w using image compression tools. Add `srcset` and `sizes` attributes to the `<img>` tag: `sizes="(max-width: 768px) 100vw, 50vw"`
- For other large images (service cards, client logos, about page images): add `srcset` with 2 variants (480w, 900w) where the original is wider than 900px
- Re-compress all WebP files with higher compression (quality 75–80 instead of default) to reduce file sizes while maintaining visual quality
- Add `loading="lazy"` to all images below the fold; hero image stays `loading="eager" fetchpriority="high"`

**Files affected:** `images/` (new compressed variants), all `.html` files referencing images

---

## Section 2 — Security Headers (Best Practices)

**Problem:** No `_headers` file exists. Lighthouse flags missing HSTS, CSP, and COOP, dropping Best Practices to 92.

**Solution:** Create `/_headers` in the project root with the following applied to `/*`:

```
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://*.google-analytics.com https://*.googletagmanager.com https://*.clarity.ms; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com; connect-src 'self' https://*.google-analytics.com https://*.googletagmanager.com https://*.clarity.ms; font-src 'self'; frame-ancestors 'none'
  Cross-Origin-Opener-Policy: same-origin
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
```

**Notes:**
- `unsafe-inline` for `script-src` is required by the JSON-LD schema blocks on every page. This is a known and accepted trade-off for static sites without a nonce system.
- Once fonts are self-hosted, `font-src` is `'self'` only — no Google Fonts domain needed.
- Analytics domains are included in `script-src` and `connect-src` for the delayed-load scripts.

**Files affected:** `/_headers` (new file)

---

## Section 3 — Accessibility

### 3.1 Contrast Ratio Failures

**Problem:** Some text color/background combinations fail WCAG AA (4.5:1 ratio for normal text, 3:1 for large text).

**Solution:** Audit `css/styles.css` for all color combinations. Primary suspects:
- `--gray-text: #555555` on `--light-gray: #F4F4F4` (ratio ~4.0:1 — fails AA for normal text)
- Any light text on red backgrounds

Fix by darkening `--gray-text` to `#444444` or `#4a4a4a` (passes 4.5:1 on light gray). Verify all combinations with a contrast checker before finalizing values.

**Files affected:** `css/styles.css`

### 3.2 Heading Order

**Problem:** Some pages have non-sequential heading levels (e.g., H1 → H3, skipping H2), which fails accessibility audits and weakens SEO heading signals.

**Solution:** Audit all `.html` files. Enforce strict sequential hierarchy: one H1 per page (the primary page topic), H2 for major sections, H3 for subsections. Adjust heading levels in HTML only — use CSS classes to maintain visual styling where the visual size needs to differ from the semantic level.

**Files affected:** All `.html` files (audit required per page)

### 3.3 Aria-Labels for Identical Links

**Problem:** Repeated identical link text (e.g., "LEARN MORE →" appearing 5 times on the homepage, "GET A QUOTE" appearing in navbar, floating CTA, and hero) is ambiguous to screen readers.

**Solution:** Add descriptive `aria-label` attributes to all repeated links:
- Service card links: `aria-label="Learn more about unarmed security services"`
- Industry card links: `aria-label="Learn more about security for retail stores"`
- Quote buttons: `aria-label="Get a free security quote"` (same label is fine since they all do the same thing — screen readers just need it to be non-ambiguous in context)

**Files affected:** `index.html`, service pages, industry pages

---

## Section 4 — New Features

### 4.1 Cookie Consent Banner (CCPA Compliance)

**Purpose:** California law (CCPA) requires informing users about data collection before analytics fire.

**Behavior:**
- Fixed bottom bar visible on first visit only
- Text: "We use cookies and analytics to improve your experience. [Accept] [Decline]"
- "Accept": stores `analytics_consent=accepted` in `localStorage`, dismisses banner, analytics load normally (still with 3s delay)
- "Decline": stores `analytics_consent=declined` in `localStorage`, dismisses banner, `loadAnalytics()` never fires
- On subsequent visits: banner does not show; `localStorage` value determines whether analytics load
- Banner does not affect CLS (positioned fixed, not in document flow)

**Styling:** Navy background (`--navy`), white text, red "Accept" button, white outline "Decline" button. Matches existing site design. Z-index above all other elements.

**Files affected:** `js/main.js`, `css/styles.css`, `cookie-policy.html` (add link in banner text)

### 4.2 Testimonials / Reviews Section

**Purpose:** Add social proof with schema markup so Google can display star ratings in search results.

**Location:** Replace or augment the existing Section 8 (reviews) on `index.html`.

**Structure:** 4 review cards, each with:
- 5 red star icons (SVG)
- Review text (realistic, specific to security industry use cases)
- Reviewer: first name + last initial, city, role (e.g., "Property Manager, Bakersfield")
- Google or Yelp badge

**Schema:** Add `ItemList` of `Review` objects inside a `AggregateRating` on the `LocalBusiness` schema already present on `index.html`. Fields: `author`, `reviewBody`, `reviewRating` (`ratingValue: 5`, `bestRating: 5`).

**Files affected:** `index.html`, `css/styles.css` (if new card styles needed)

### 4.3 FAQ Schema Markup

**Purpose:** Enable Google FAQ rich results — accordion-style Q&A shown directly in search results for branded and local queries.

**Solution:** Add `FAQPage` JSON-LD schema to `faq.html` covering all 10 FAQ items. Add a separate `FAQPage` schema to `index.html` covering the 3 FAQ preview items shown there. Each `mainEntity` entry has `@type: Question`, `name` (the question), and `acceptedAnswer.text` (the answer).

**Files affected:** `faq.html`, `index.html`

### 4.4 Local SEO Schema Improvements

**Purpose:** Stronger structured data signals for local search rankings across service areas and service types.

**Additions to `index.html` LocalBusiness schema:**
- `areaServed`: array of the 8 service area cities/counties
- `hasOfferCatalog`: `OfferCatalog` listing all 5 services by name

**Additions to each `/services/*.html` page:**
- `Service` schema with `@type: Service`, `name`, `description`, `provider` (reference to the LocalBusiness), `areaServed` (same 8 areas)

**Files affected:** `index.html`, `services/unarmed-security.html`, `services/armed-security.html`, `services/mobile-patrol.html`, `services/fire-watch.html`, `services/concierge-security.html`

---

## Out of Scope

- Industry pages (`/industries/*.html`) — built separately
- Build pipeline / asset minification tooling
- Backend, server-side rendering, or dynamic content
- Netlify Image CDN URL changes
- Nonce-based CSP (requires server-side rendering)

---

## File Change Summary

| File | Change Type |
|---|---|
| `/_headers` | New — security headers |
| `/fonts/inter-*.woff2` | New — self-hosted font files (6 weights) |
| `css/styles.css` | Modified — `@font-face`, contrast fixes |
| `js/main.js` | Modified — delayed analytics, cookie consent logic |
| `index.html` | Modified — inline critical CSS, srcset, schema, testimonials, FAQ schema, aria-labels, heading fix, remove Google Fonts |
| `about.html` | Modified — remove Google Fonts, aria-labels, heading fix |
| `faq.html` | Modified — remove Google Fonts, FAQ schema, heading fix |
| `get-a-quote.html` | Modified — remove Google Fonts, heading fix |
| `contact.html` | Modified — remove Google Fonts, heading fix |
| `services/*.html` (5 files) | Modified — remove Google Fonts, Service schema, aria-labels, heading fix |
| `industries/*.html` (11 files) | Modified — remove Google Fonts, aria-labels, heading fix |
| `images/` | New compressed variants for hero and major images |
