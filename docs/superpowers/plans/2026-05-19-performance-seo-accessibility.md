# Performance, SEO & Accessibility Overhaul — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve Lighthouse Performance from 44→100, Best Practices from 92→100, Accessibility from 95→100, add cookie consent, FAQ schema, testimonials schema, and local SEO improvements for invinciblesecuritygroup.com.

**Architecture:** Static HTML/CSS/JS site on Netlify. All changes are direct file edits — no build pipeline. Performance wins come from self-hosting Inter, delaying GA4/Clarity behind a cookie consent gate, inlining critical CSS on index.html, and adding responsive srcset to the hero image.

**Tech Stack:** HTML5, CSS3, vanilla JS, Python 3 (Pillow) for image compression, PowerShell for font downloads, Netlify `_headers` file for security headers.

---

## Task 1: Self-Host Inter Font (Eliminates Cross-Origin Font Fetch → Fixes FCP)

**Files:**
- Create: `fonts/` directory with 6 WOFF2 files
- Modify: `css/styles.css` (add @font-face block, remove nothing yet)

- [ ] **Step 1: Download Inter WOFF2 files via PowerShell**

Run this in the project root. It fetches the Google Fonts CSS with a WOFF2 user agent, extracts the file URLs, and downloads each weight into `fonts/`:

```powershell
New-Item -ItemType Directory -Force -Path "fonts"

$weights = @("400", "500", "600", "700", "800", "900")
$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$family = "Inter:wght@" + ($weights -join ";")
$apiUrl = "https://fonts.googleapis.com/css2?family=$family&display=swap"

$css = (Invoke-WebRequest -Uri $apiUrl -UserAgent $ua).Content

$regex = [regex]'url\((https://fonts\.gstatic\.com/s/inter/[^)]+\.woff2)\)'
$matches = $regex.Matches($css)

foreach ($m in $matches) {
    $url = $m.Groups[1].Value
    $filename = $url.Split("/")[-1]
    if (-not (Test-Path "fonts/$filename")) {
        Invoke-WebRequest -Uri $url -OutFile "fonts/$filename"
        Write-Host "Downloaded: $filename"
    }
}

Write-Host "Done. Files in fonts/:"
Get-ChildItem fonts/*.woff2 | Select-Object Name, Length
```

Expected: 6 WOFF2 files downloaded to `fonts/`.

- [ ] **Step 2: Rename files to predictable names**

After the download, rename the files to predictable names based on their weight. Run this PowerShell to map weights from the Google Fonts CSS output:

```powershell
# List the downloaded files and inspect sizes to identify weights
Get-ChildItem fonts/*.woff2 | Sort-Object Length | Select-Object Name, @{N='KB';E={[math]::Round($_.Length/1KB,1)}}
```

Then rename each file manually or via script. The 6 files correspond to weights 400, 500, 600, 700, 800, 900 (sorted by file hash, not by weight — check the CSS output from Step 1 to match hash to weight).

Rename using this pattern (adjust the source names from actual downloaded filenames):
```powershell
# The CSS output from Step 1 lists each weight's URL in order.
# Match each URL's filename to its weight. Then rename:
# Example (actual filenames will differ — use what Step 1 downloaded):
# Rename-Item "fonts/UcC73FwrK3iLTeHuS_fvQtMwCp50KnMa1ZL7W0Q5nw.woff2" "fonts/inter-400.woff2"
# Repeat for 500, 600, 700, 800, 900
```

Parse the CSS output from Step 1 manually: find each `/* latin */` block with its `font-weight` value, note the filename in the `url()`, and rename accordingly:
```powershell
# After identifying all 6 filenames, run one rename per weight:
Get-ChildItem fonts/*.woff2 | Rename-Item  # use specific names from Step 1 output
```

- [ ] **Step 3: Add @font-face block to top of styles.css**

Open `css/styles.css`. After the opening comment block (line 3) and before `/* ---------- CSS Variables ---------- */` (line 5), add:

```css
/* ---------- Self-Hosted Inter Font ---------- */
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 400; font-display: swap; src: url('../fonts/inter-400.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 500; font-display: swap; src: url('../fonts/inter-500.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 600; font-display: swap; src: url('../fonts/inter-600.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 700; font-display: swap; src: url('../fonts/inter-700.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 800; font-display: swap; src: url('../fonts/inter-800.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 900; font-display: swap; src: url('../fonts/inter-900.woff2') format('woff2'); }
```

- [ ] **Step 4: Remove Google Fonts tags from index.html**

In `index.html`, remove these 4 lines (lines 20-23):
```html
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" /></noscript>
```

Then add this preload for the most-used font weight, immediately before `<link rel="stylesheet" href="css/styles.css" />`:
```html
  <link rel="preload" as="font" href="fonts/inter-600.woff2" type="font/woff2" crossorigin>
```

- [ ] **Step 5: Remove Google Fonts tags from all other HTML files**

The same 4-line block appears in every HTML file. Remove it from each of:
- `about.html`
- `faq.html`
- `get-a-quote.html`
- `contact.html`
- `footer.html`
- `armed-security.html`, `unarmed-security.html`, `mobile-patrol.html`, `fire-watch.html`, `concierge-security.html`
- All 11 `industries/*.html` files
- `other-services.html`, `other-industries.html`, `privacy-policy.html`, `terms-conditions.html`, `cookie-policy.html`, `thank-you.html`

Do NOT add the `<link rel="preload" as="font">` tag to non-index pages (it's only critical for index.html's LCP).

For service and industry pages, the `@font-face` paths use `../fonts/` — verify the CSS `src` URL is correct for subdirectory pages. Since service pages load `css/styles.css` with a relative path, the `../fonts/inter-*.woff2` path in the CSS is correct relative to the CSS file location.

- [ ] **Step 6: Commit**

```bash
git add fonts/ css/styles.css index.html about.html faq.html get-a-quote.html contact.html footer.html services/ industries/ other-services.html other-industries.html privacy-policy.html terms-conditions.html cookie-policy.html thank-you.html
git commit -m "perf: self-host Inter font, remove Google Fonts dependency"
```

---

## Task 2: Delay Analytics + Cookie Consent Banner

**Files:**
- Modify: `js/main.js` (add loadAnalytics + cookie consent logic)
- Modify: `css/styles.css` (add cookie banner styles)
- Modify: `index.html` (remove inline analytics scripts, add cookie banner HTML)
- Modify: all other HTML files (remove inline analytics scripts)

- [ ] **Step 1: Add cookie consent HTML to index.html**

In `index.html`, immediately after `<body>` (before the `<div class="top-bar">` div), add:

```html
<!-- COOKIE CONSENT BANNER -->
<div id="cookie-banner" role="dialog" aria-label="Cookie consent" aria-live="polite" style="display:none;">
  <div class="cookie-inner">
    <p>We use cookies and analytics to improve your experience. See our <a href="cookie-policy.html">Cookie Policy</a>.</p>
    <div class="cookie-btns">
      <button id="cookie-accept" class="btn btn-red btn-sm">Accept</button>
      <button id="cookie-decline" class="btn btn-outline-navy btn-sm">Decline</button>
    </div>
  </div>
</div>
```

Add the same block to all other HTML files (same position: immediately after `<body>`).

- [ ] **Step 2: Add cookie banner styles to styles.css**

Append to the bottom of `css/styles.css`:

```css
/* ---------- Cookie Consent Banner ---------- */
#cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--navy);
  color: var(--white);
  z-index: 9999;
  padding: 16px 24px;
  box-shadow: 0 -4px 20px rgba(0,0,0,0.3);
}
.cookie-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}
.cookie-inner p { font-size: 0.9rem; margin: 0; line-height: 1.5; }
.cookie-inner a { color: #ccd9f0; text-decoration: underline; }
.cookie-btns { display: flex; gap: 12px; flex-shrink: 0; }
.btn-sm { padding: 8px 20px; font-size: 0.82rem; }
```

- [ ] **Step 3: Remove inline analytics from index.html**

In `index.html`, remove these blocks entirely:

Remove (lines ~70-80, the Google Analytics + Clarity block in `<head>`):
```html
  <!-- Google Analytics 4 -->
    <script async defer src="https://www.googletagmanager.com/gtag/js?id=G-EG7JCG2R1Z"></script>

  <!-- Microsoft Clarity -->
  <script type="text/javascript" defer>
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wkg1a7mvwq");
  </script>
```

Remove (line ~868, the gtag config script just before `</body>`):
```html
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-EG7JCG2R1Z');</script>
```

- [ ] **Step 4: Remove inline analytics from all other HTML files**

Remove the same GA4 + Clarity script blocks from every other HTML file (they appear in `<head>` of each file). The files are: `about.html`, `faq.html`, `get-a-quote.html`, `contact.html`, `armed-security.html`, `unarmed-security.html`, `mobile-patrol.html`, `fire-watch.html`, `concierge-security.html`, all `industries/*.html`, `other-services.html`, `other-industries.html`, `privacy-policy.html`, `terms-conditions.html`, `cookie-policy.html`, `thank-you.html`.

- [ ] **Step 5: Add analytics loader + cookie consent logic to main.js**

At the top of `js/main.js`, before the `document.addEventListener('DOMContentLoaded', ...)` block, add:

```js
/* ---------- Cookie Consent & Deferred Analytics ---------- */
(function () {
  var GA_ID = 'G-EG7JCG2R1Z';
  var CLARITY_ID = 'wkg1a7mvwq';
  var CONSENT_KEY = 'analytics_consent';
  var analyticsLoaded = false;

  function loadAnalytics() {
    if (analyticsLoaded) return;
    analyticsLoaded = true;

    // GA4
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID);

    // Clarity
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_ID);
  }

  function scheduleAnalytics() {
    var consent = localStorage.getItem(CONSENT_KEY);
    if (consent === 'declined') return;
    if (consent === 'accepted') {
      // Already consented — delay 3s or first interaction
      var timer = setTimeout(loadAnalytics, 3000);
      var events = ['scroll', 'click', 'keydown', 'touchstart'];
      function onInteraction() {
        clearTimeout(timer);
        events.forEach(function (ev) { document.removeEventListener(ev, onInteraction); });
        loadAnalytics();
      }
      events.forEach(function (ev) { document.addEventListener(ev, onInteraction, { once: true, passive: true }); });
    }
    // If no consent yet, wait for banner interaction (handled below)
  }

  function showBanner() {
    var banner = document.getElementById('cookie-banner');
    if (!banner) return;
    banner.style.display = 'block';

    document.getElementById('cookie-accept').addEventListener('click', function () {
      localStorage.setItem(CONSENT_KEY, 'accepted');
      banner.style.display = 'none';
      scheduleAnalytics();
    });

    document.getElementById('cookie-decline').addEventListener('click', function () {
      localStorage.setItem(CONSENT_KEY, 'declined');
      banner.style.display = 'none';
    });
  }

  var consent = localStorage.getItem(CONSENT_KEY);
  if (consent === null) {
    // First visit — show banner
    document.addEventListener('DOMContentLoaded', showBanner);
  } else {
    // Returning visitor — run based on stored preference
    scheduleAnalytics();
  }
})();
```

- [ ] **Step 6: Commit**

```bash
git add js/main.js css/styles.css index.html about.html faq.html get-a-quote.html contact.html services/ industries/ other-services.html other-industries.html privacy-policy.html terms-conditions.html cookie-policy.html thank-you.html
git commit -m "perf: delay analytics behind cookie consent, add CCPA banner"
```

---

## Task 3: Critical CSS Inline + Deferred Stylesheet (index.html only)

**Files:**
- Modify: `index.html` (add inline `<style>` block, convert stylesheet to async load)

The goal is to inline only the CSS needed to render the visible viewport (top bar, navbar, hero section) so the browser can paint without waiting for the full `styles.css` download.

- [ ] **Step 1: Add inline critical CSS `<style>` block to index.html**

In `index.html`, immediately before the existing `<link rel="stylesheet" href="css/styles.css" />` line, add this `<style>` block. This contains the minimum CSS to render the top-bar, navbar, and hero above the fold without any flash:

```html
<style>
/* Critical CSS — above-the-fold styles for index.html */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:'Inter','Segoe UI',Arial,sans-serif;color:#1A1A1A;background:#fff;line-height:1.6;overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
ul{list-style:none}
button{cursor:pointer;border:none;background:none;font-family:inherit}
:root{--red:#CC0000;--red-dark:#A80000;--navy:#1B2A4A;--white:#fff;--light-gray:#F4F4F4;--dark-text:#1A1A1A;--gray-text:#555;--border-radius:6px;--shadow:0 4px 20px rgba(0,0,0,.10);--shadow-lg:0 8px 40px rgba(0,0,0,.18);--transition:0.3s ease;--max-width:1200px}
.container{width:100%;max-width:var(--max-width);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{line-height:1.2;font-weight:700}
h1{font-size:clamp(2rem,4vw,3.2rem)}
h2{font-size:clamp(1.6rem,3vw,2.4rem)}
h3{font-size:clamp(1.1rem,2vw,1.4rem)}
.top-bar{background:var(--red);color:#fff;font-size:.8rem;font-weight:600;padding:8px 0}
.top-bar .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
.top-bar a{color:#fff;text-decoration:none}
.top-bar-left{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
.top-bar-right{display:flex;gap:8px;align-items:center}
.icon-inline{display:inline-flex;align-items:center;vertical-align:middle;margin-right:4px}
.icon-inline svg{width:14px;height:14px}
.navbar{background:var(--navy);position:sticky;top:0;z-index:1000;transition:box-shadow .3s}
.navbar .container{display:flex;align-items:center;justify-content:space-between;padding-top:10px;padding-bottom:10px;gap:16px}
.nav-links{display:flex;gap:4px;align-items:center}
.nav-links a{color:#fff;font-size:.88rem;font-weight:600;padding:8px 12px;border-radius:4px;transition:background .2s}
.nav-links a:hover{background:rgba(255,255,255,.1)}
.nav-cta{background:var(--red);color:#fff!important;padding:10px 22px;border-radius:var(--border-radius);font-weight:700;font-size:.88rem;letter-spacing:.04em;text-transform:uppercase;transition:background .2s;white-space:nowrap}
.nav-cta:hover{background:var(--red-dark)}
.hamburger{display:none;flex-direction:column;gap:5px;padding:8px;background:none;border:none;cursor:pointer}
.hamburger span{display:block;width:24px;height:2px;background:#fff;transition:var(--transition)}
.hero{background:#0d1b35 url(images/hero.webp) center/cover no-repeat;position:relative;min-height:100vh;display:flex;align-items:center}
.hero::before{content:'';position:absolute;inset:0;background:linear-gradient(105deg,rgba(13,27,53,.88) 55%,rgba(13,27,53,.65))}
.hero .container{position:relative;z-index:1;padding-top:80px;padding-bottom:80px}
.hero-grid{display:grid;grid-template-columns:55% 45%;gap:48px;align-items:center}
.hero-left{color:#fff}
.hero-badge{display:inline-block;background:rgba(204,0,0,.25);border:1px solid rgba(204,0,0,.5);color:#fff;font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:6px 14px;border-radius:4px;margin-bottom:20px}
.hero h1{color:#fff;margin-bottom:20px;font-size:clamp(2rem,3.5vw,3rem)}
.hero-sub{font-size:1.05rem;color:rgba(255,255,255,.88);margin-bottom:32px;max-width:520px;line-height:1.7}
.hero-buttons{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:28px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 30px;border-radius:var(--border-radius);font-size:.95rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;transition:var(--transition);text-decoration:none;cursor:pointer}
.btn-red{background:var(--red);color:#fff;border:2px solid var(--red)}
.btn-red:hover{background:var(--red-dark);border-color:var(--red-dark)}
.btn-outline-white{background:transparent;color:#fff;border:2px solid #fff}
.btn-outline-white:hover{background:#fff;color:var(--navy)}
.trust-pills{display:flex;gap:12px;flex-wrap:wrap}
.trust-pill{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;font-size:.78rem;font-weight:600;padding:6px 14px;border-radius:50px}
.chk{color:var(--red);font-weight:900}
.hero-card{background:#fff;border-radius:10px;padding:32px;box-shadow:0 20px 60px rgba(0,0,0,.3);animation:floatUp .6s ease both}
@keyframes floatUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.card-title{color:var(--red);font-size:1.1rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-bottom:20px;text-align:center}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.form-group{display:flex;flex-direction:column;gap:6px;margin-bottom:12px}
.form-group label{font-size:.78rem;font-weight:600;color:var(--navy);letter-spacing:.04em;text-transform:uppercase}
.form-group input,.form-group select,.form-group textarea{padding:10px 14px;border:1.5px solid #ddd;border-radius:var(--border-radius);font-size:.9rem;font-family:inherit;transition:border-color .2s;width:100%}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{outline:none;border-color:var(--red)}
.form-submit{width:100%;background:var(--red);color:#fff;border:none;padding:14px;border-radius:var(--border-radius);font-size:1rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;cursor:pointer;transition:background .2s;margin-top:4px}
.form-submit:hover{background:var(--red-dark)}
.form-note{font-size:.78rem;color:#888;text-align:center;margin-top:10px;display:flex;align-items:center;justify-content:center;gap:4px}
.form-note svg{width:13px;height:13px}
@media(max-width:1100px){.hero-grid{gap:32px}}
@media(max-width:768px){.nav-links,.nav-cta{display:none}.hamburger{display:flex}.hero-grid{grid-template-columns:1fr}.hero{min-height:auto;padding-top:20px}.form-row{grid-template-columns:1fr}}
</style>
```

- [ ] **Step 2: Convert stylesheet link to async load**

Replace the existing stylesheet link in `index.html`:
```html
  <link rel="stylesheet" href="css/styles.css" />
```

With:
```html
  <link rel="preload" href="css/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="css/styles.css"></noscript>
```

- [ ] **Step 3: Verify visually**

Open `index.html` in a browser (via XAMPP at `http://localhost/invincible-inc-copy/`). The page should render immediately with correct styling on the hero and navbar. There should be no flash of unstyled content. Scroll down to verify the rest of the page loads styles correctly after the async CSS kicks in.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "perf: inline critical CSS and defer stylesheet on homepage"
```

---

## Task 4: Responsive Hero Image + Lazy Loading (Fixes LCP)

**Files:**
- Create: `images/hero-480w.webp`, `images/hero-900w.webp` (new compressed variants)
- Modify: `index.html` (add srcset/sizes to hero img tag)
- Modify: all HTML files (add loading="lazy" to below-fold images)

The hero image is the LCP element. At 15s LCP, it's almost certainly uncompressed or very large. We'll create mobile/tablet variants and add srcset so mobile devices download a fraction of the bytes.

- [ ] **Step 1: Check current hero image size**

```powershell
Get-Item "images/hero.webp" | Select-Object Name, @{N='KB';E={[math]::Round($_.Length/1KB,1)}}
```

- [ ] **Step 2: Install Pillow and generate compressed variants**

```powershell
pip install Pillow
```

Then run this Python script from the project root to generate compressed variants:

```python
# Run: python compress_images.py
from PIL import Image
import os

hero = Image.open("images/hero.webp")
w, h = hero.size
print(f"Original hero: {w}x{h}")

# 480w variant (mobile)
ratio = 480 / w
hero_480 = hero.resize((480, int(h * ratio)), Image.LANCZOS)
hero_480.save("images/hero-480w.webp", "WEBP", quality=78, method=6)
print(f"Saved hero-480w.webp")

# 900w variant (tablet)
ratio = 900 / w
hero_900 = hero.resize((900, int(h * ratio)), Image.LANCZOS)
hero_900.save("images/hero-900w.webp", "WEBP", quality=78, method=6)
print(f"Saved hero-900w.webp")

# Re-save original at better compression (keep same dimensions)
hero.save("images/hero-1440w.webp", "WEBP", quality=80, method=6)
print(f"Saved hero-1440w.webp (re-compressed original)")

# Report sizes
for f in ["images/hero.webp", "images/hero-480w.webp", "images/hero-900w.webp", "images/hero-1440w.webp"]:
    size = os.path.getsize(f)
    print(f"{f}: {size//1024}KB")
```

Save this as `compress_images.py` in the project root, run it, then delete the script:
```powershell
python compress_images.py
Remove-Item compress_images.py
```

- [ ] **Step 3: Update hero img tag in index.html with srcset**

Find the hero section in `index.html`. The hero background image is a CSS background on the `.hero` section, not an `<img>` tag. This means Lighthouse is measuring the CSS background image as the LCP element.

To make the hero image LCP-measurable and responsive, check the current hero implementation. If it's a pure CSS background:
- The `<link rel="preload" as="image" href="images/hero.webp" fetchpriority="high">` already in `<head>` is correct for preloading
- Add `imagesrcset` and `imagesizes` to the preload link to hint the correct variant:

Replace the existing hero preload link in `index.html`:
```html
  <link rel="preload" as="image" href="images/hero.webp" fetchpriority="high" />
```

With:
```html
  <link rel="preload" as="image" href="images/hero-900w.webp" fetchpriority="high" imagesrcset="images/hero-480w.webp 480w, images/hero-900w.webp 900w, images/hero-1440w.webp 1440w" imagesizes="100vw" />
```

Then update the hero CSS background to use `image-set()` for responsive loading. In `css/styles.css`, find the `.hero` rule and update the background:
```css
.hero {
  background: #0d1b35 image-set(
    url('../images/hero-480w.webp') 480w,
    url('../images/hero-900w.webp') 900w,
    url('../images/hero-1440w.webp') 1440w
  ) center/cover no-repeat;
  /* Fallback for browsers without image-set support: */
  background: #0d1b35 url('../images/hero.webp') center/cover no-repeat;
}
```

Note: `image-set()` with `w` descriptors has limited browser support. A simpler and more reliable approach for the CSS background is to keep the single hero image but use the re-compressed `hero-1440w.webp` as the source, and add a media query for mobile:

In `css/styles.css`, update the `.hero` background:
```css
.hero {
  background: #0d1b35 url('../images/hero-1440w.webp') center/cover no-repeat;
  /* ... rest of existing properties ... */
}
@media (max-width: 768px) {
  .hero {
    background-image: url('../images/hero-480w.webp');
  }
}
@media (min-width: 769px) and (max-width: 1100px) {
  .hero {
    background-image: url('../images/hero-900w.webp');
  }
}
```

Also update the inline critical CSS `<style>` block in `index.html` to reference the re-compressed version:
```css
/* In the inline <style> block, find: */
.hero{background:#0d1b35 url(images/hero.webp) center/cover no-repeat; ...}
/* Change to: */
.hero{background:#0d1b35 url(images/hero-1440w.webp) center/cover no-repeat; ...}
```

And add to the inline style:
```css
@media(max-width:768px){.hero{background-image:url(images/hero-480w.webp)}}
```

- [ ] **Step 4: Add loading="lazy" to below-fold images in index.html**

Below-fold images in `index.html` (everything below the hero section). Find all `<img>` tags that do NOT have `fetchpriority="high"` and add `loading="lazy"` if not already present.

Specifically ensure the client logo images already have `loading="lazy"` (they do, per the existing HTML). Check all `<img>` tags throughout the file.

- [ ] **Step 5: Commit**

```bash
git add images/hero-480w.webp images/hero-900w.webp images/hero-1440w.webp css/styles.css index.html
git commit -m "perf: responsive hero image with srcset, recompressed at quality 80"
```

---

## Task 5: Security Headers File (Best Practices → 100)

**Files:**
- Create: `_headers` (project root)

- [ ] **Step 1: Create _headers file**

Create `_headers` in the project root with the following content:

```
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://*.google-analytics.com https://*.googletagmanager.com https://*.clarity.ms https://www.google.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com https://www.gstatic.com; connect-src 'self' https://*.google-analytics.com https://*.googletagmanager.com https://*.clarity.ms; font-src 'self'; frame-src https://www.google.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
  Cross-Origin-Opener-Policy: same-origin-allow-popups
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
```

Notes on values chosen:
- `COOP: same-origin-allow-popups` instead of `same-origin` because the quote form and phone links may open popups in some browsers; strict `same-origin` can break GA4 cross-origin measurement.
- `X-Frame-Options: SAMEORIGIN` instead of `DENY` in case the Netlify admin embeds a preview; can be tightened to `DENY` after confirming.
- `frame-src https://www.google.com` allows the reCAPTCHA iframe on the quote form.
- `unsafe-inline` for `script-src` is required for the JSON-LD schema blocks in every HTML file's `<head>`.

- [ ] **Step 2: Verify headers locally (optional)**

If Netlify CLI is installed: `netlify dev` then check response headers in DevTools → Network. Otherwise, push to Netlify and verify in the deployed site's Network tab.

- [ ] **Step 3: Commit**

```bash
git add _headers
git commit -m "feat: add Netlify security headers (HSTS, CSP, COOP, X-Frame)"
```

---

## Task 6: Accessibility Fixes (95 → 100)

**Files:**
- Modify: `css/styles.css` (contrast fix)
- Modify: `index.html` (aria-labels, heading order)
- Modify: `faq.html` (heading order)
- Modify: `about.html` (heading order)
- Modify: `services/*.html` (aria-labels, heading order)

### 6A: Fix Contrast Ratio

- [ ] **Step 1: Fix gray-text contrast in styles.css**

`--gray-text: #555555` on `--light-gray: #F4F4F4` has a contrast ratio of ~4.0:1, failing WCAG AA (4.5:1 required for normal text). Darken it.

In `css/styles.css`, change line 13:
```css
/* FROM: */
  --gray-text: #555555;
/* TO: */
  --gray-text: #484848;
```

`#484848` on `#F4F4F4` has a ratio of ~5.1:1 — passes AA.

Also check: `.section-sub` uses `color: var(--gray-text)` on white and light-gray backgrounds — the darkened value covers both.

### 6B: Fix Aria-Labels on Repeated Links

- [ ] **Step 2: Add aria-labels to service card "Learn More" links in index.html**

Find the 6 service cards in `index.html` (`.svc-card`). Each has `<a href="..." class="svc-link">Learn More &#8594;</a>`. Add unique `aria-label` to each:

```html
<!-- Unarmed Security card -->
<a href="services/unarmed-security.html" class="svc-link" aria-label="Learn more about unarmed security services">Learn More &#8594;</a>

<!-- Armed Security card -->
<a href="services/armed-security.html" class="svc-link" aria-label="Learn more about armed security services">Learn More &#8594;</a>

<!-- Mobile Patrol card -->
<a href="services/mobile-patrol.html" class="svc-link" aria-label="Learn more about mobile patrol services">Learn More &#8594;</a>

<!-- Fire Watch card -->
<a href="services/fire-watch.html" class="svc-link" aria-label="Learn more about fire watch services">Learn More &#8594;</a>

<!-- Concierge Security card -->
<a href="services/concierge-security.html" class="svc-link" aria-label="Learn more about concierge security services">Learn More &#8594;</a>

<!-- Other Services card -->
<a href="other-services.html" class="svc-link" aria-label="Learn more about other security services">Learn More &#8594;</a>
```

- [ ] **Step 3: Add aria-labels to industry "Learn More" links in index.html**

Same pattern for the 12 industry cards. Add `aria-label="Learn more about security for [industry name]"` to each `<a class="ind-link">` element. Example:

```html
<a href="industries/residential-communities.html" class="ind-link" aria-label="Learn more about security for residential communities">Learn More &#8594;</a>
```

Apply to all 12 industry cards with the appropriate industry name in each label.

- [ ] **Step 4: Add aria-label to floating CTA (already present — verify)**

The floating CTA in `index.html` already has `aria-label="Get a Quote"`:
```html
<a href="get-a-quote.html" class="floating-cta" aria-label="Get a Quote">Get a Quote</a>
```
This is correct. No change needed.

### 6C: Fix Heading Order

- [ ] **Step 5: Check and fix heading hierarchy in index.html**

In `index.html`, the heading structure should be:
- H1: "California's Most Trusted Security Force" (hero — only H1 on the page) ✅
- H2: Each major section heading (About ISG, Our Security Services, Why Choose ISG, Industries We Serve, etc.)
- H3: Sub-items within sections (individual service names, industry names, FAQ questions)

Check the About section — the "Why Choose ISG" box uses `<h3>` inside a section that has no H2 parent in that column. The left column has `<h2>About Invincible Security Group</h2>` and the right column has `<h3>Why Choose ISG</h3>`. This is acceptable since both are inside the same section.

Verify FAQ preview buttons: they use `<button class="faq-q">` not headings — this is correct.

Check the reviews section heading is `<h2>` — it is ✅.

- [ ] **Step 6: Check and fix heading hierarchy in faq.html**

In `faq.html`, verify the structure:
- H1: "Frequently Asked Questions" ✅ (line 142)
- FAQ questions use `<button>` not headings — correct ✅
- The services teaser section (line 220): `<h2 class="section-heading">Explore What We Offer</h2>` — check this is H2 ✅
- CTA section (line 207): `<h2>Still Have Questions? We're Here to Help.</h2>` — H2 ✅

Check for any heading that jumps levels (H1 → H3 without H2). Fix any found.

- [ ] **Step 7: Check about.html heading hierarchy**

Open `about.html`, scan all H1-H4 tags and verify sequential order. The page should have exactly one H1 (the page title in the hero banner) and H2 for each major section. Fix any non-sequential headings.

- [ ] **Step 8: Commit**

```bash
git add css/styles.css index.html faq.html about.html services/
git commit -m "a11y: fix contrast ratio, add aria-labels, verify heading order"
```

---

## Task 7: FAQ Schema + Enhanced Local SEO Schema

**Files:**
- Modify: `faq.html` (add FAQPage JSON-LD)
- Modify: `index.html` (add FAQPage JSON-LD for preview, enhance LocalBusiness schema)
- Modify: `services/armed-security.html`, `services/unarmed-security.html`, `services/mobile-patrol.html`, `services/fire-watch.html`, `services/concierge-security.html` (add Service schema)

### 7A: FAQPage Schema on faq.html

- [ ] **Step 1: Add FAQPage JSON-LD to faq.html**

In `faq.html`, add the following `<script type="application/ld+json">` block inside `<head>`, after the existing meta tags. This covers all 10 FAQ items:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Invincible Security Group licensed in California?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Invincible Security Group holds a Bureau of Security & Investigative Services (BSIS) Private Patrol Operator license, PPO #122748. All of our security officers are individually licensed and permitted by the state of California."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between armed and unarmed security guards?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unarmed security officers provide visible deterrence, access control, patrols, and incident reporting without carrying a firearm. Armed security officers carry a firearm and are additionally trained and licensed under BSIS firearm permits. Armed guards are typically deployed in higher-risk environments such as banks, jewelry stores, or properties with a history of violent incidents."
      }
    },
    {
      "@type": "Question",
      "name": "How quickly can you deploy security officers to my location?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In many cases, we can deploy officers within 24-72 hours of contract execution. For urgent situations such as fire watch or emergency deployments, we can often respond within hours. Contact us at 877-345-9239 for urgent requests."
      }
    },
    {
      "@type": "Question",
      "name": "Do you require long-term contracts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. We offer flexible service agreements and can deploy on a short-term, trial, or ongoing basis. We believe in earning your business through the quality of our service, not locking you into a long-term commitment."
      }
    },
    {
      "@type": "Question",
      "name": "Is Invincible Security Group fully insured and bonded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We carry comprehensive commercial general liability insurance and workers' compensation insurance as required by California law. We are also fully bonded and can provide certificates of insurance upon contract execution."
      }
    },
    {
      "@type": "Question",
      "name": "How do you price your security services?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pricing depends on the type of service, number of officers, hours of coverage, and location. We provide customized quotes based on your specific needs. Submit your request through our online form or call 877-345-9239."
      }
    },
    {
      "@type": "Question",
      "name": "What background checks do your security officers go through?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All officers undergo criminal background checks, drug testing, employment history verification, and reference checks. All must hold valid California BSIS security guard registrations. Armed officers must also hold valid BSIS Firearm Permits."
      }
    },
    {
      "@type": "Question",
      "name": "Do you serve areas outside of Bakersfield?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. While headquartered in Bakersfield, CA, we serve clients throughout California including Los Angeles County, Fresno County, Orange County, Riverside County, Sacramento, San Diego County, and the Bay Area."
      }
    },
    {
      "@type": "Question",
      "name": "Can you create a custom security plan for my facility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Every client engagement begins with a consultation and site walk. We develop a site-specific security plan addressing your property's unique layout, risks, operating hours, and budget."
      }
    },
    {
      "@type": "Question",
      "name": "How do I get started with Invincible Security Group?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Submit a free quote request through our online form and we'll respond immediately. From there, we'll schedule a consultation, assess your needs, and present a custom proposal with no obligation. Most clients have officers on-site within 24-48 hours of agreeing to terms."
      }
    }
  ]
}
</script>
```

### 7B: FAQPage Schema on index.html (3-question preview)

- [ ] **Step 2: Add FAQPage JSON-LD to index.html**

In `index.html`, add this `<script type="application/ld+json">` block inside `<head>` after the existing schema blocks:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Invincible Security Group licensed in California?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Invincible Security Group holds a Bureau of Security & Investigative Services (BSIS) Private Patrol Operator license, PPO #122748. All security officers are individually licensed and permitted by the state of California."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between armed and unarmed security?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unarmed officers provide visible deterrence, access control, and incident reporting without a firearm. Armed officers carry a firearm and hold BSIS firearm permits, typically deployed in higher-risk environments such as banks or jewelry stores."
      }
    },
    {
      "@type": "Question",
      "name": "Do you require long-term contracts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. We offer flexible service agreements on a short-term, trial, or ongoing basis. Contact us to discuss the arrangement that works best for your facility."
      }
    }
  ]
}
</script>
```

### 7C: Enhanced LocalBusiness Schema on index.html

- [ ] **Step 3: Replace the LocalBusiness schema in index.html**

Find the existing `LocalBusiness` JSON-LD block in `index.html` (lines 27-48) and replace it with this enhanced version:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Invincible Security Group",
  "description": "Professional BSIS licensed security guard services across California including armed security, unarmed security, mobile patrol, fire watch, and concierge security.",
  "url": "https://www.invinciblesecuritygroup.com",
  "telephone": "+18773459239",
  "email": "info@invinciblesecuritygroup.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "6300 White Lane Suite G",
    "addressLocality": "Bakersfield",
    "addressRegion": "CA",
    "postalCode": "93309",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "35.3325", "longitude": "-119.0177" },
  "openingHours": "Mo-Su 00:00-23:59",
  "priceRange": "$$",
  "hasCredential": "BSIS PPO License #122748",
  "areaServed": [
    { "@type": "City", "name": "Bakersfield", "sameAs": "https://en.wikipedia.org/wiki/Bakersfield,_California" },
    { "@type": "AdministrativeArea", "name": "Los Angeles County" },
    { "@type": "AdministrativeArea", "name": "Fresno County" },
    { "@type": "AdministrativeArea", "name": "Orange County" },
    { "@type": "AdministrativeArea", "name": "Riverside County" },
    { "@type": "City", "name": "Sacramento" },
    { "@type": "AdministrativeArea", "name": "San Diego County" },
    { "@type": "AdministrativeArea", "name": "Bay Area" }
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Security Guard Services",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Unarmed Security Guards", "url": "https://www.invinciblesecuritygroup.com/services/unarmed-security.html" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Armed Security Guards", "url": "https://www.invinciblesecuritygroup.com/services/armed-security.html" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Mobile Patrol Security", "url": "https://www.invinciblesecuritygroup.com/services/mobile-patrol.html" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Fire Watch Security", "url": "https://www.invinciblesecuritygroup.com/services/fire-watch.html" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Concierge Security", "url": "https://www.invinciblesecuritygroup.com/services/concierge-security.html" } }
    ]
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "3",
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "author": { "@type": "Person", "name": "Maria T." },
      "reviewRating": { "@type": "Rating", "ratingValue": "5", "bestRating": "5" },
      "reviewBody": "Invincible Security Group has been protecting our residential community for over a year now. Response times are excellent, officers are professional, and residents feel noticeably safer. Highly recommend for any HOA looking for reliable security.",
      "datePublished": "2025-03-15"
    },
    {
      "@type": "Review",
      "author": { "@type": "Person", "name": "James R." },
      "reviewRating": { "@type": "Rating", "ratingValue": "5", "bestRating": "5" },
      "reviewBody": "We brought ISG in to secure our distribution warehouse and the difference was immediate. Theft dropped significantly. The guards are well-trained, punctual, and the management team is easy to work with.",
      "datePublished": "2025-04-02"
    },
    {
      "@type": "Review",
      "author": { "@type": "Person", "name": "Ashley K." },
      "reviewRating": { "@type": "Rating", "ratingValue": "5", "bestRating": "5" },
      "reviewBody": "We used ISG for event security at our annual outdoor festival. The team was organized, professional, and handled every situation with calm and confidence. We will definitely use them again.",
      "datePublished": "2025-04-20"
    }
  ]
}
</script>
```

Also remove the old Service schema block (lines 49-67) since it's now folded into `hasOfferCatalog` above.

### 7D: Service Schema on Each Service Page

- [ ] **Step 4: Add Service schema to unarmed-security.html**

In `services/unarmed-security.html`, add to `<head>`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Unarmed Security Guard Services",
  "description": "Professional unarmed security officers providing visible deterrence, access control, and incident response across California. BSIS licensed, PPO #122748.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Invincible Security Group",
    "url": "https://www.invinciblesecuritygroup.com",
    "telephone": "+18773459239"
  },
  "areaServed": [
    "Bakersfield, CA", "Los Angeles County, CA", "Fresno County, CA",
    "Orange County, CA", "Riverside County, CA", "Sacramento, CA",
    "San Diego County, CA", "Bay Area, CA"
  ],
  "serviceType": "Unarmed Security Guard Services",
  "url": "https://www.invinciblesecuritygroup.com/services/unarmed-security.html"
}
</script>
```

- [ ] **Step 5: Add Service schema to armed-security.html**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Armed Security Guard Services",
  "description": "Licensed and trained armed security officers delivering maximum protection for high-value or high-risk environments across California. BSIS licensed with Firearm Permits.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Invincible Security Group",
    "url": "https://www.invinciblesecuritygroup.com",
    "telephone": "+18773459239"
  },
  "areaServed": [
    "Bakersfield, CA", "Los Angeles County, CA", "Fresno County, CA",
    "Orange County, CA", "Riverside County, CA", "Sacramento, CA",
    "San Diego County, CA", "Bay Area, CA"
  ],
  "serviceType": "Armed Security Guard Services",
  "url": "https://www.invinciblesecuritygroup.com/services/armed-security.html"
}
</script>
```

- [ ] **Step 6: Add Service schema to mobile-patrol.html**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Mobile Patrol Security Services",
  "description": "Marked patrol vehicles conducting scheduled and random security inspections across your property or multiple California locations. BSIS licensed, PPO #122748.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Invincible Security Group",
    "url": "https://www.invinciblesecuritygroup.com",
    "telephone": "+18773459239"
  },
  "areaServed": [
    "Bakersfield, CA", "Los Angeles County, CA", "Fresno County, CA",
    "Orange County, CA", "Riverside County, CA", "Sacramento, CA",
    "San Diego County, CA", "Bay Area, CA"
  ],
  "serviceType": "Mobile Patrol Security",
  "url": "https://www.invinciblesecuritygroup.com/services/mobile-patrol.html"
}
</script>
```

- [ ] **Step 7: Add Service schema to fire-watch.html**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Fire Watch Security Services",
  "description": "Trained fire watch officers monitoring your California property 24/7 to meet NFPA and local fire code requirements. Licensed and insured, PPO #122748.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Invincible Security Group",
    "url": "https://www.invinciblesecuritygroup.com",
    "telephone": "+18773459239"
  },
  "areaServed": [
    "Bakersfield, CA", "Los Angeles County, CA", "Fresno County, CA",
    "Orange County, CA", "Riverside County, CA", "Sacramento, CA",
    "San Diego County, CA", "Bay Area, CA"
  ],
  "serviceType": "Fire Watch Security",
  "url": "https://www.invinciblesecuritygroup.com/services/fire-watch.html"
}
</script>
```

- [ ] **Step 8: Add Service schema to concierge-security.html**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Concierge Security Services",
  "description": "Professionally presented security officers delivering both premium customer service and access control at your California facility's front desk. BSIS licensed, PPO #122748.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Invincible Security Group",
    "url": "https://www.invinciblesecuritygroup.com",
    "telephone": "+18773459239"
  },
  "areaServed": [
    "Bakersfield, CA", "Los Angeles County, CA", "Fresno County, CA",
    "Orange County, CA", "Riverside County, CA", "Sacramento, CA",
    "San Diego County, CA", "Bay Area, CA"
  ],
  "serviceType": "Concierge Security",
  "url": "https://www.invinciblesecuritygroup.com/services/concierge-security.html"
}
</script>
```

- [ ] **Step 9: Commit**

```bash
git add faq.html index.html services/
git commit -m "seo: add FAQPage schema, enhance LocalBusiness schema, add Service schema to all service pages"
```

---

## Task 8: Final Verification + Cleanup

- [ ] **Step 1: Verify no Google Fonts references remain**

```powershell
Select-String -Path "*.html", "about.html", "faq.html", "get-a-quote.html", "contact.html", "footer.html", "services\*.html", "industries\*.html" -Pattern "fonts.googleapis.com" -Recurse
```

Expected: zero matches.

- [ ] **Step 2: Verify no inline analytics scripts remain in HTML files**

```powershell
Select-String -Path "*.html", "services\*.html", "industries\*.html" -Pattern "googletagmanager|clarity\.ms" -Recurse
```

Expected: zero matches (analytics are now loaded only from `main.js`).

- [ ] **Step 3: Verify _headers file syntax**

```powershell
Get-Content "_headers"
```

Confirm the file exists and has all 7 header lines under `/*`.

- [ ] **Step 4: Verify font files exist**

```powershell
Get-ChildItem fonts/*.woff2 | Select-Object Name, @{N='KB';E={[math]::Round($_.Length/1KB,1)}}
```

Expected: 6 files (inter-400.woff2 through inter-900.woff2).

- [ ] **Step 5: Final commit**

```bash
git status
git add -A
git commit -m "feat: complete performance, accessibility, and SEO overhaul"
```

---

## Spec Coverage Check

| Spec Requirement | Task |
|---|---|
| Self-host Inter font | Task 1 |
| Delay GA4 + Clarity | Task 2 |
| Cookie consent banner (CCPA) | Task 2 |
| Critical CSS inline (index.html) | Task 3 |
| Responsive hero image + compression | Task 4 |
| Security headers (_headers) | Task 5 |
| Contrast ratio fix | Task 6A |
| Aria-labels for repeated links | Task 6B |
| Heading order | Task 6C |
| FAQ schema (faq.html) | Task 7A |
| FAQ schema (index.html preview) | Task 7B |
| Enhanced LocalBusiness schema | Task 7C |
| Review schema on LocalBusiness | Task 7C |
| Service schema (5 pages) | Task 7D |
