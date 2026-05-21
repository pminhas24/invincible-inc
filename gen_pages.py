"""Generate 3 new industry pages and 3 legal pages for ISG."""
import os

BASE = r'C:\xampp\htdocs\invincible-inc-copy'

# ─── Shared HTML snippets ────────────────────────────────────────────────────

TOP_BAR = '''  <div class="top-bar">
    <div class="container">
      <div class="top-bar-left">
        <span><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.6 19.79 19.79 0 0 1 1.64 5.11 2 2 0 0 1 3.62 3h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.6a16 16 0 0 0 6 6l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.72 18z"/></svg></span> <a href="tel:8773459239">877-345-9239</a></span>
        <span><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span> <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></span>
      </div>
      <div class="top-bar-right">
        <span>PPO License #122748</span>
        <span>&#124;</span>
        <span>Licensed &amp; Insured</span>
      </div>
    </div>
  </div>'''

NAVBAR_IND = '''  <nav class="navbar" role="navigation" aria-label="Main navigation">
    <div class="container">
      <a href="/index.html">
        <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">
      </a>
      <ul class="nav-links" role="list">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../about.html">About Us</a></li>
        <li>
          <a href="../index.html#services">Services <span class="chevron">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-label">Our Services</a>
            <a href="../services/unarmed-security.html">Unarmed Security</a>
            <a href="../services/armed-security.html">Armed Security</a>
            <a href="../services/mobile-patrol.html">Mobile Patrol</a>
            <a href="../services/fire-watch.html">Fire Watch</a>
            <a href="../services/concierge-security.html">Concierge Security</a>
            <a href="../other-services.html">Other Services</a>
          </div>
        </li>
        <li>
          <a href="#">Industries <span class="chevron">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-label">Industries We Serve</a>
            <a href="../industries/residential-communities.html">Residential Communities</a>
            <a href="../industries/warehouses-distribution.html">Warehouses &amp; Distribution</a>
            <a href="../industries/financial-institutions.html">Financial Institutions</a>
            <a href="../industries/commercial-industrial.html">Commercial &amp; Industrial</a>
            <a href="../industries/solar-energy-facilities.html">Solar Energy Facilities</a>
            <a href="../industries/construction-sites.html">Construction Sites</a>
            <a href="../industries/retail-stores.html">Retail Stores</a>
            <a href="../industries/events-crowd-control.html">Events &amp; Crowd Control</a>
            <a href="../industries/healthcare-facilities.html">Healthcare Facilities</a>
            <a href="../industries/educational-campuses.html">Educational Campuses</a>
            <a href="../industries/hospitality-hotels.html">Hospitality &amp; Hotels</a>
            <a href="../other-industries.html">Other Industries</a>
          </div>
        </li>
        <li><a href="../index.html#areas">Areas We Serve</a></li>
        <li><a href="../faq.html">FAQ</a></li>
        <li><a href="../get-a-quote.html">Contact</a></li>
      </ul>
      <a href="../get-a-quote.html" class="nav-cta">Get a Quote</a>
      <button class="hamburger" aria-label="Open mobile menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <div class="mobile-menu" role="dialog" aria-modal="true" aria-label="Mobile navigation">
    <button class="mobile-close" type="button" aria-label="Close menu">&times;</button>
    <nav class="mobile-nav-links" aria-label="Mobile navigation links">
      <a href="../index.html" class="mobile-top-link">Home</a>
      <a href="../about.html" class="mobile-top-link">About Us</a>
      <div class="mobile-nav-heading">Services</div>
      <div class="mobile-nav-group" aria-label="Services">
        <a href="../services/unarmed-security.html" class="mobile-sub">Unarmed Security</a>
        <a href="../services/armed-security.html" class="mobile-sub">Armed Security</a>
        <a href="../services/mobile-patrol.html" class="mobile-sub">Mobile Patrol</a>
        <a href="../services/fire-watch.html" class="mobile-sub">Fire Watch</a>
        <a href="../services/concierge-security.html" class="mobile-sub">Concierge Security</a>
        <a href="../other-services.html" class="mobile-sub">Other Services</a>
      </div>
      <div class="mobile-nav-heading">Industries</div>
      <div class="mobile-nav-group" aria-label="Industries">
        <a href="../industries/residential-communities.html" class="mobile-sub">Residential Communities</a>
        <a href="../industries/warehouses-distribution.html" class="mobile-sub">Warehouses &amp; Distribution</a>
        <a href="../industries/financial-institutions.html" class="mobile-sub">Financial Institutions</a>
        <a href="../industries/commercial-industrial.html" class="mobile-sub">Commercial &amp; Industrial</a>
        <a href="../industries/solar-energy-facilities.html" class="mobile-sub">Solar Energy Facilities</a>
        <a href="../industries/construction-sites.html" class="mobile-sub">Construction Sites</a>
        <a href="../industries/retail-stores.html" class="mobile-sub">Retail Stores</a>
        <a href="../industries/events-crowd-control.html" class="mobile-sub">Events &amp; Crowd Control</a>
        <a href="../industries/healthcare-facilities.html" class="mobile-sub">Healthcare Facilities</a>
        <a href="../industries/educational-campuses.html" class="mobile-sub">Educational Campuses</a>
        <a href="../industries/hospitality-hotels.html" class="mobile-sub">Hospitality &amp; Hotels</a>
        <a href="../other-industries.html" class="mobile-sub">Other Industries</a>
      </div>
      <a href="../index.html#areas" class="mobile-top-link">Areas We Serve</a>
      <a href="../faq.html" class="mobile-top-link">FAQ</a>
      <a href="../get-a-quote.html" class="mobile-top-link">Contact</a>
      <a href="../get-a-quote.html" class="btn btn-red mobile-menu-cta">Get a Free Quote</a>
    </nav>
  </div>

  <a href="../get-a-quote.html" class="floating-cta" aria-label="Get a Quote">Get a Quote</a>'''

FOOTER_IND = '''  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="/index.html">
            <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">
          </a>
        </div>
        <div class="footer-col">
          <p class="footer-tagline">Protecting People, Property, and Peace of Mind</p>
          <div class="footer-contact-item"><span class="fc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-6-5.33-6-11a6 6 0 0 1 12 0c0 5.67-6 11-6 11z"/><circle cx="12" cy="10" r="2.5"/></svg></span><span>6300 White Lane Suite G<br>Bakersfield, CA 93309</span></div>
          <div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.6 19.79 19.79 0 0 1 1.64 5.11 2 2 0 0 1 3.62 3h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.6a16 16 0 0 0 6 6l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.72 18z"/></svg></span></span><a href="tel:8773459239">877-345-9239</a></div>
          <div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span></span><a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></div>
          <div class="footer-contact-item"><span class="fc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></span><span>PPO License #122748 | Licensed &amp; Insured</span></div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <nav class="footer-links" aria-label="Footer quick links">
            <a href="../index.html">Home</a>
            <a href="../about.html">About Us</a>
            <a href="../services/unarmed-security.html">Services</a>
            <a href="../index.html#areas">Areas We Serve</a>
            <a href="../faq.html">FAQ</a>
            <a href="../get-a-quote.html">Contact Us</a>
            <a href="../get-a-quote.html">Get a Quote</a>
          </nav>
        </div>
        <div class="footer-col">
          <h4>Our Services</h4>
          <nav class="footer-links" aria-label="Footer services links">
            <a href="../services/unarmed-security.html">Unarmed Security</a>
            <a href="../services/armed-security.html">Armed Security</a>
            <a href="../services/mobile-patrol.html">Mobile Patrol</a>
            <a href="../services/fire-watch.html">Fire Watch</a>
            <a href="../services/concierge-security.html">Concierge Security</a>
          </nav>
        </div>
      </div>
    </div>
    <div class="footer-bottom"><div class="container">&copy; 2026 Invincible Security Group. All Rights Reserved. | Bakersfield, CA | <a href="/privacy-policy.html" style="color:inherit;">Privacy Policy</a> | <a href="/terms-conditions.html" style="color:inherit;">Terms &amp; Conditions</a> | <a href="/cookie-policy.html" style="color:inherit;">Cookie Policy</a></div></div>
  </footer>
  <script src="../js/main.js"></script>'''

ANALYTICS = '''  <!-- Google Analytics 4 -->
  <script async defer src="https://www.googletagmanager.com/gtag/js?id=G-EG7JCG2R1Z"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-EG7JCG2R1Z');
  </script>

  <!-- Microsoft Clarity -->
  <script type="text/javascript" defer>
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wkg1a7mvwq");
  </script>'''

def build_service_card(title, desc, link, icon_svg, delay=''):
    d = f' reveal-delay-{delay}' if delay else ''
    return f'''<div class="service-card reveal{d}"><div class="service-card-icon"><svg viewBox="0 0 24 24">{icon_svg}</svg></div><h3>{title}</h3><p>{desc}</p><a href="{link}" class="btn btn-outline-red">Learn More</a></div>'''

def build_feature_card(title, desc, icon_svg, delay=''):
    d = f' reveal-delay-{delay}' if delay else ''
    return f'''<div class="feature-card reveal{d}"><div class="feature-card-icon"><svg viewBox="0 0 24 24">{icon_svg}</svg></div><div><h4>{title}</h4><p>{desc}</p></div></div>'''

def build_quote_form(source_page, preselect_value, preselect_label, desc_text, why_items):
    why = ''.join(f'<div class="why-item"><span class="why-dot"></span>{item}</div>' for item in why_items)
    select_opts = ''
    opts = [
        ('unarmed','Unarmed Security Services'),
        ('armed','Armed Security Services'),
        ('patrol','Mobile Patrol Services'),
        ('firewatch','Fire Watch Services'),
        ('concierge','Concierge Security Services'),
        ('multiple','Multiple / Not Sure'),
    ]
    for val, lbl in opts:
        sel = ' selected' if val == preselect_value else ''
        select_opts += f'<option value="{val}"{sel}>{lbl}</option>'
    return f'''<section class="quote-section section-pad" id="quote"><div class="container"><div class="quote-grid"><div class="quote-info"><span class="section-eyebrow reveal">Free Consultation</span><h2 class="section-title reveal reveal-delay-1">Request a Free<br>Security Quote</h2><p class="section-intro reveal reveal-delay-2">{desc_text}</p><div class="quote-contact reveal reveal-delay-2"><div class="quote-contact-item"><div class="qci-icon"><svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.31.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1C9.56 21 3 14.44 3 6c0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.26 1.01L6.6 10.8z"/></svg></div><div><div class="qci-label">Phone</div><a href="tel:8773459239" class="qci-value">877-345-9239</a></div></div><div class="quote-contact-item"><div class="qci-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div><div><div class="qci-label">Email</div><a href="mailto:info@invinciblesecuritygroup.com" class="qci-value">info@invinciblesecuritygroup.com</a></div></div><div class="quote-contact-item"><div class="qci-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></div><div><div class="qci-label">License</div><div class="qci-value">PPO #122748</div></div></div></div><div class="why-choose-list reveal reveal-delay-3">{why}</div></div><div class="quote-form-card reveal reveal-delay-2"><h3>Get Your Free Quote</h3><form class="quote-form" action="/thank-you.html" method="post" data-netlify="true" name="quote-request" novalidate><input type="hidden" name="form-name" value="quote-request" />
<input type="hidden" name="bot-field" /><input type="hidden" name="source-page" value="{source_page}" /><div class="form-row"><div class="form-group"><label for="name">Full Name *</label><input type="text" id="name" name="name" placeholder="John Smith" required /></div><div class="form-group"><label for="company">Company / Organization</label><input type="text" id="company" name="company" placeholder="Acme Corp" /></div></div><div class="form-row"><div class="form-group"><label for="phone">Phone Number *</label><input type="tel" id="phone" name="phone" placeholder="(555) 000-0000" required /></div><div class="form-group"><label for="email">Email Address *</label><input type="email" id="email" name="email" placeholder="you@example.com" required /></div></div><div class="form-group"><label for="service">Service Needed</label><select id="service" name="service"><option value="">- Select a Service -</option>{select_opts}</select></div><div class="form-group"><label for="location">City / Location *</label><input type="text" id="location" name="location" placeholder="Bakersfield, CA" required /></div><div class="form-group"><label for="message">Tell Us About Your Needs</label><textarea id="message" name="message" placeholder="Describe your facility, number of posts needed, hours of coverage, any specific requirements..."></textarea></div><div data-netlify-recaptcha="true"></div><button type="submit" class="btn btn-red form-submit">Submit Request</button><p class="form-note">We respect your privacy. Your information is never shared or sold.</p></form></div></div></div></section>'''

def build_industry_page(
    filename, title, meta_desc, og_url, slug,
    breadcrumb_name, h1, hero_tagline,
    overview_h2, overview_p1, overview_p2, overview_p3, best_fit,
    sidebar_priorities, sidebar_facts,
    services_intro, service_cards_html,
    features_intro, feature_cards_html,
    cta_h2, cta_p, cta_btn_text,
    quote_desc, quote_why, preselect_value
):
    sidebar_p_items = ''.join(f'<li class="sidebar-item"><span class="sidebar-bullet"></span>{p}</li>' for p in sidebar_priorities)
    sidebar_f_items = ''.join(f'<li class="sidebar-item"><span class="sidebar-bullet"></span>{f}</li>' for f in sidebar_facts)
    quote_section = build_quote_form(slug, preselect_value, '', quote_desc, quote_why)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
  <meta name="description" content="{meta_desc}" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/styles.css" />
  <script type="application/ld+json">
    {{"@context":"https://schema.org","@graph":[{{"@type":"LocalBusiness","@id":"https://invinciblesecuritygroup.com/#business","name":"Invincible Security Group","telephone":"+1-877-345-9239","email":"info@invinciblesecuritygroup.com","areaServed":"California","priceRange":"$$","description":"California security company providing BSIS licensed security guards for healthcare, education, hospitality, and commercial facilities.","identifier":"PPO #122748"}},{{"@type":"Service","name":"{h1}","description":"{meta_desc}","serviceType":"{h1}","areaServed":"California","provider":{{"@id":"https://invinciblesecuritygroup.com/#business"}}}}]}}
  </script>
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta_desc}" />
  <meta property="og:url" content="{og_url}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://invinciblesecuritygroup.com/images/og-image.jpg" />

{ANALYTICS}
</head>
<body>
{TOP_BAR}

{NAVBAR_IND}

<section class="service-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span class="breadcrumb-sep">&gt;</span><a href="../index.html#industries">Industries</a><span class="breadcrumb-sep">&gt;</span><span class="breadcrumb-current">{breadcrumb_name}</span></nav><h1 class="reveal">{h1}</h1><p class="service-hero-tagline reveal reveal-delay-1">{hero_tagline}</p></div></section>
  <section class="overview-section section-pad"><div class="container"><div class="overview-grid"><div class="overview-text"><span class="section-eyebrow reveal">Industry Overview</span><h2 class="section-title reveal reveal-delay-1">{overview_h2}</h2><p class="reveal reveal-delay-2">{overview_p1}</p><p class="reveal reveal-delay-2">{overview_p2}</p><p class="reveal reveal-delay-2">{overview_p3}</p><div class="overview-highlight reveal reveal-delay-3"><strong>Best fit:</strong> {best_fit}</div></div><div class="overview-sidebar reveal reveal-delay-2"><h4>Operational Priorities</h4><ul class="sidebar-list">{sidebar_p_items}</ul><div class="sidebar-divider"></div><h4>Quick Facts</h4><ul class="sidebar-list">{sidebar_f_items}</ul></div></div></div></section>
  <section class="services-section section-pad"><div class="container"><div class="services-header"><span class="section-eyebrow reveal">Recommended Coverage</span><h2 class="section-title reveal reveal-delay-1">Which ISG services apply</h2><p class="section-intro reveal reveal-delay-2">{services_intro}</p></div><div class="services-grid">{service_cards_html}</div></div></section>
  <section class="features-section section-pad"><div class="container"><div class="features-header"><span class="section-eyebrow reveal">Key Benefits</span><h2 class="section-title reveal reveal-delay-1">What sets our approach apart</h2><p class="section-intro reveal reveal-delay-2">{features_intro}</p></div><div class="features-grid">{feature_cards_html}</div></div></section>
  <section class="cta-banner" style="background: var(--navy);"><div class="container"><h2 class="reveal">{cta_h2}</h2><p class="reveal reveal-delay-1">{cta_p}</p><a href="#quote" class="btn btn-white btn-lg reveal reveal-delay-2">{cta_btn_text}</a></div></section>
  {quote_section}
{FOOTER_IND}
</body>
</html>
'''
    return html


# ─── HEALTHCARE FACILITIES ───────────────────────────────────────────────────

HEALTHCARE_SERVICES = (
    build_service_card(
        'Unarmed Security Services',
        'Professional unarmed officers managing visitor access, conducting rounds, and maintaining a safe environment in patient care and administrative areas.',
        '../services/unarmed-security.html',
        '<path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>'
    ) +
    build_service_card(
        'Concierge Security Services',
        'Professionally trained officers who balance security responsibilities with patient and visitor assistance at reception desks and hospital lobbies.',
        '../services/concierge-security.html',
        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
        '1'
    ) +
    build_service_card(
        'Mobile Patrol Services',
        'Scheduled and random vehicle patrols of parking structures, exterior grounds, and secondary access points across large medical campuses.',
        '../services/mobile-patrol.html',
        '<rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 5v3h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
        '2'
    )
)

HEALTHCARE_FEATURES = (
    build_feature_card('Visitor Access Control', 'Officers verify and log all visitor credentials, enforce restricted area policies, and maintain controlled entry to patient zones and administrative offices.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>') +
    build_feature_card('Staff & Patient Protection', 'Trained officers provide a protective presence in high-risk areas, de-escalate disruptive behavior, and ensure the safety of staff, patients, and visitors at all times.', '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>', '1') +
    build_feature_card('24/7 Monitoring', 'Round-the-clock security coverage ensures that every shift transition, late-night period, and weekend is fully staffed with licensed California officers.', '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm.5 5H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/>', '2') +
    build_feature_card('HIPAA-Aware Officers', 'Our guards are trained to respect patient privacy requirements, handle sensitive situations discreetly, and operate within healthcare compliance frameworks.', '<path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/>', '3') +
    build_feature_card('Emergency Response', 'Officers are trained to coordinate with clinical staff during medical emergencies, manage evacuation procedures, and liaise with first responders.', '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.6 19.79 19.79 0 0 1 1.64 5.11 2 2 0 0 1 3.62 3h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.6a16 16 0 0 0 6 6l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.72 18z"/>') +
    build_feature_card('Compliance Reporting', 'Detailed activity logs and incident reports support internal audits, risk management review, and regulatory compliance documentation.', '<path d="M3 3h18v2H3zm0 16h18v2H3zm0-8h18v2H3z"/>', '1')
)

healthcare = build_industry_page(
    filename='healthcare-facilities.html',
    title='Healthcare Facility Security Guards California | Invincible Security Group',
    meta_desc='BSIS licensed healthcare security guards in California. Invincible Security Group provides access control, staff protection, and compliance-focused security for medical facilities.',
    og_url='https://invinciblesecuritygroup.com/industries/healthcare-facilities.html',
    slug='healthcare-facilities',
    breadcrumb_name='Healthcare Facilities',
    h1='Healthcare Facility Security',
    hero_tagline='BSIS licensed security officers for hospitals, medical offices, and healthcare campuses across California — protecting patients, staff, and sensitive environments.',
    overview_h2='Security challenges in healthcare environments',
    overview_p1='Healthcare facilities face a unique combination of security challenges that few other industries encounter. Open public access, emotionally charged situations, and the presence of vulnerable patients create environments where trained security personnel must balance firm access control with compassionate, professional conduct. Managing visitor flow, protecting restricted areas such as pharmacies and server rooms, and preventing unauthorized entry to patient care zones all require officers who understand the sensitivity of the healthcare setting.',
    overview_p2='Staff safety is increasingly a priority in healthcare security planning. Incidents involving agitated patients, distraught family members, or individuals under the influence require officers who are trained in de-escalation and conflict management. At the same time, healthcare environments are subject to federal and state compliance requirements — including HIPAA — that affect how security personnel are trained, how incidents are documented, and how patient information is handled during security responses.',
    overview_p3='Invincible Security Group provides BSIS licensed security officers for California healthcare facilities who are trained for the specific demands of medical environments. From visitor management at the front desk to after-hours patrol of large hospital campuses, our officers integrate seamlessly with clinical operations while maintaining the high standards of professionalism and discretion that healthcare clients require.',
    best_fit='Hospitals, medical office buildings, outpatient clinics, urgent care centers, long-term care facilities, and behavioral health campuses.',
    sidebar_priorities=['Visitor access management', 'Restricted area enforcement', 'Staff and patient protection', 'De-escalation and conflict response', 'After-hours and parking security'],
    sidebar_facts=['BSIS licensed California officers', 'HIPAA-aware training and protocols', 'Scalable staffing for large campuses', 'Serving healthcare facilities statewide'],
    services_intro='Healthcare clients typically need a combination of front-desk security, after-hours monitoring, and parking and campus patrol to maintain a safe environment at all hours.',
    service_cards_html=HEALTHCARE_SERVICES,
    features_intro='Effective healthcare security integrates seamlessly with clinical operations, supports compliance objectives, and maintains a professional presence that reassures patients and staff.',
    feature_cards_html=HEALTHCARE_FEATURES,
    cta_h2='Protect your patients, staff, and facility',
    cta_p='Request a customized security proposal for your California healthcare facility. We build plans around your patient population, campus layout, and compliance requirements.',
    cta_btn_text='Request a Healthcare Security Quote',
    quote_desc='Tell us about your healthcare facility and we will build a customized security proposal with no obligation.',
    quote_why=['BSIS licensed California officers', 'HIPAA-aware training and procedures', 'Visitor management and access control', 'After-hours and campus patrol options', 'Serving healthcare facilities statewide'],
    preselect_value='unarmed'
)


# ─── EDUCATIONAL CAMPUSES ────────────────────────────────────────────────────

EDUCATIONAL_SERVICES = (
    build_service_card(
        'Unarmed Security Services',
        'Professional unarmed officers providing a visible security presence, monitoring building access, and deterring unauthorized entry on school and university campuses.',
        '../services/unarmed-security.html',
        '<path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>'
    ) +
    build_service_card(
        'Mobile Patrol Services',
        'Marked patrol vehicles conducting scheduled and random perimeter sweeps of parking lots, athletic fields, and secondary campus access points.',
        '../services/mobile-patrol.html',
        '<rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 5v3h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
        '1'
    ) +
    build_service_card(
        'Armed Security Services',
        'Licensed armed officers providing maximum deterrence for campuses with elevated risk profiles, after-hours events, or active threat preparedness requirements.',
        '../services/armed-security.html',
        '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
        '2'
    )
)

EDUCATIONAL_FEATURES = (
    build_feature_card('Active Threat Deterrence', 'Visible, uniformed officers serve as a strong deterrent against active threat situations, reducing risk and improving emergency preparedness across the campus.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>') +
    build_feature_card('Visitor Screening', 'Officers verify visitor credentials at main entry points, enforce campus sign-in procedures, and ensure that only authorized individuals enter school buildings and restricted zones.', '<path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1"/><path d="M9 12h6M9 16h4"/>', '1') +
    build_feature_card('After-Hours Patrol', 'Scheduled and random patrols of buildings, parking structures, and campus grounds after hours, on weekends, and during school breaks when facilities are most vulnerable.', '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm.5 5H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/>', '2') +
    build_feature_card('Access Control', 'Officers monitor and enforce controlled access to buildings, laboratories, athletic facilities, and administrative offices, ensuring compliance with campus security policies.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>', '3') +
    build_feature_card('Incident Reporting', 'Guards submit detailed activity logs and incident reports in real time, providing administrators with documentation for review, insurance, and policy improvement.', '<path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8z"/><polyline points="14 2 14 8 20 8"/>') +
    build_feature_card('Trained & Certified Officers', 'All Invincible Security Group officers are BSIS licensed by the State of California, background checked, drug screened, and trained for the specific demands of educational environments.', '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>', '1')
)

educational = build_industry_page(
    filename='educational-campuses.html',
    title='Educational Campus Security Guards California | Invincible Security Group',
    meta_desc='Professional campus security guards for schools and universities in California. BSIS licensed officers providing active threat deterrence and access control.',
    og_url='https://invinciblesecuritygroup.com/industries/educational-campuses.html',
    slug='educational-campuses',
    breadcrumb_name='Educational Campuses',
    h1='Educational Campus Security',
    hero_tagline='BSIS licensed security officers for K-12 schools, community colleges, and universities across California — creating safer learning environments through visible, professional security.',
    overview_h2='Security challenges on school and university campuses',
    overview_p1='Educational campuses present some of the most complex security environments in any sector. The combination of large, open grounds, high student populations, multiple access points, and the fundamental need to maintain a safe learning environment creates challenges that require careful planning and experienced security personnel. Schools and universities must balance open access for authorized students, staff, and visitors with the need to detect and deter unauthorized individuals, manage after-hours activity, and maintain a visible security presence that reassures the campus community.',
    overview_p2='Active threat deterrence has become a central concern for educational institutions of all sizes. BSIS licensed security officers provide a visible deterrent that discourages unauthorized entry and creates a security baseline that complements any existing access control systems or emergency response plans. Officers trained for educational environments understand how to manage high-volume traffic during class changes, sporting events, and public gatherings while maintaining situational awareness and the ability to respond quickly to incidents.',
    overview_p3='Invincible Security Group provides professional, BSIS licensed security guards for California schools, community colleges, and universities. Our officers are selected for their professionalism, communication skills, and understanding of the unique dynamics of educational campuses. From daily visitor screening to after-hours patrol and event security, we build security programs that support a safe and productive learning environment.',
    best_fit='K-12 schools, community colleges, universities, vocational training centers, daycare facilities, and educational administrative campuses.',
    sidebar_priorities=['Campus entry and access control', 'Visitor screening and credentialing', 'After-hours and weekend patrol', 'Active threat deterrence', 'Event and crowd management'],
    sidebar_facts=['BSIS licensed California officers', 'Experience with high-traffic campus environments', 'Scalable coverage for large campuses', 'Serving educational institutions statewide'],
    services_intro='Educational campuses typically require a layered security approach combining visible daily patrols, controlled access management, and rapid response capability for after-hours and event coverage.',
    service_cards_html=EDUCATIONAL_SERVICES,
    features_intro='Campus security for schools and universities requires officers who understand the unique dynamics of educational environments — balancing open, welcoming spaces with firm, professional access control.',
    feature_cards_html=EDUCATIONAL_FEATURES,
    cta_h2='Create a safer learning environment',
    cta_p='Request a customized campus security proposal for your California school or university. We build plans around your campus layout, student population, and specific security goals.',
    cta_btn_text='Request a Campus Security Quote',
    quote_desc='Tell us about your school or university campus and we will build a customized security proposal with no obligation.',
    quote_why=['BSIS licensed California officers', 'Active threat deterrence training', 'Visitor screening and access control', 'After-hours and event security', 'Serving educational campuses statewide'],
    preselect_value='unarmed'
)


# ─── HOSPITALITY & HOTELS ────────────────────────────────────────────────────

HOSPITALITY_SERVICES = (
    build_service_card(
        'Concierge Security Services',
        'Professionally presented security officers who deliver both premium guest service and firm access control — projecting the polished image your property demands while keeping every guest safe.',
        '../services/concierge-security.html',
        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>'
    ) +
    build_service_card(
        'Unarmed Security Services',
        'Professional unarmed officers providing discreet security coverage across your property — monitoring common areas, managing late-night activity, and responding quickly to incidents.',
        '../services/unarmed-security.html',
        '<path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>',
        '1'
    ) +
    build_service_card(
        'Mobile Patrol Services',
        'Scheduled and random vehicle patrols of parking areas, exterior grounds, secondary entrances, and multi-building resort properties for comprehensive coverage.',
        '../services/mobile-patrol.html',
        '<rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 5v3h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
        '2'
    )
)

HOSPITALITY_FEATURES = (
    build_feature_card('Guest Safety', 'Officers ensure guests feel safe throughout their stay — from lobby check-in to late-night common area management — creating a secure environment that enhances the guest experience.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>') +
    build_feature_card('Discrete Security Presence', 'Our officers are trained to blend seamlessly into upscale hospitality environments, providing firm security without disrupting the ambiance or guest experience your property has worked to create.', '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>', '1') +
    build_feature_card('Surveillance Monitoring', 'Officers can be stationed at surveillance control centers to monitor camera feeds across the property, identifying and escalating incidents before they affect guests or staff.', '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>', '2') +
    build_feature_card('Lobby & Access Control', 'Professional officers manage lobby access, verify guest credentials, control after-hours entry, and enforce policies for restricted areas such as pool facilities, fitness centers, and business lounges.', '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>', '3') +
    build_feature_card('Event Security', 'Trained event security staff for weddings, conferences, corporate events, and large group gatherings — maintaining order, managing entry, and ensuring every event runs smoothly and safely.', '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>') +
    build_feature_card('Asset Protection', 'Officers protect property assets including equipment, vehicles, and inventory from theft, vandalism, and unauthorized access — reducing loss and protecting your bottom line.', '<path d="M3 3h18v2H3zm0 16h18v2H3zm0-8h18v2H3z"/>', '1')
)

hospitality = build_industry_page(
    filename='hospitality-hotels.html',
    title='Hotel & Hospitality Security Guards California | Invincible Security Group',
    meta_desc='Discrete, professional hotel and hospitality security in California. Invincible Security Group provides concierge-style security for hotels, resorts, and venues.',
    og_url='https://invinciblesecuritygroup.com/industries/hospitality-hotels.html',
    slug='hospitality-hotels',
    breadcrumb_name='Hospitality & Hotels',
    h1='Hotel & Hospitality Security',
    hero_tagline='Discrete, professional security for hotels, resorts, venues, and hospitality properties across California — protecting guests, staff, and assets without disrupting your experience.',
    overview_h2='Security challenges in hospitality environments',
    overview_p1='Hotels and hospitality properties operate 24 hours a day, welcoming hundreds or thousands of guests while managing complex security challenges that range from late-night disturbances to asset theft, unauthorized access, and large-scale event management. The open-access nature of hotel lobbies, restaurants, pools, and conference facilities makes it difficult to balance the warm, welcoming atmosphere guests expect with the firm access control and incident response that property managers require.',
    overview_p2='Guest safety and experience are inextricably linked in the hospitality industry. A visible but discrete security presence reassures guests without creating an institutional atmosphere that undermines your brand. Officers assigned to hotel and resort environments must be professionally presented, trained in guest relations, and capable of handling sensitive situations — from managing intoxicated guests to coordinating with law enforcement — with discretion and professionalism that reflects positively on the property.',
    overview_p3='Invincible Security Group provides BSIS licensed security officers for California hotels, resorts, casinos, entertainment venues, and hospitality properties. Our concierge-style security approach means our officers are selected for their communication skills and professional presentation as much as their security training. We build customized security programs around your property layout, guest profile, and specific risk areas — delivering protection that enhances the guest experience rather than diminishing it.',
    best_fit='Hotels, resorts, boutique properties, conference centers, entertainment venues, casinos, event spaces, and multi-tenant hospitality campuses.',
    sidebar_priorities=['Lobby and main entry control', 'Guest safety and incident response', 'Late-night and overnight coverage', 'Event and conference security', 'Asset and parking protection'],
    sidebar_facts=['BSIS licensed California officers', 'Concierge-style training and presentation', 'Scalable coverage for large properties', 'Serving hospitality venues statewide'],
    services_intro='Hospitality security requires officers who combine professional guest service skills with firm, reliable security coverage — protecting guests and assets without disrupting the property\'s atmosphere.',
    service_cards_html=HOSPITALITY_SERVICES,
    features_intro='Effective hotel security enhances the guest experience, protects property assets, and maintains a professional environment that reflects your brand standards.',
    feature_cards_html=HOSPITALITY_FEATURES,
    cta_h2='Protect your guests, staff, and property',
    cta_p='Request a customized hospitality security proposal for your California hotel or venue. We build plans around your property layout, guest profile, and specific security requirements.',
    cta_btn_text='Request a Hospitality Security Quote',
    quote_desc='Tell us about your hotel, resort, or venue and we will build a customized security proposal with no obligation.',
    quote_why=['BSIS licensed California officers', 'Concierge-style security training', 'Discrete guest-facing presence', 'Event and conference security', 'Serving hospitality properties statewide'],
    preselect_value='concierge'
)


# ─── Write industry pages ────────────────────────────────────────────────────

pages = [
    ('industries/healthcare-facilities.html', healthcare),
    ('industries/educational-campuses.html', educational),
    ('industries/hospitality-hotels.html', hospitality),
]

for relpath, content in pages:
    fullpath = os.path.join(BASE, relpath)
    with open(fullpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {relpath}')


# ─── LEGAL PAGES (Task 5) ────────────────────────────────────────────────────

NAVBAR_ROOT = '''  <nav class="navbar" role="navigation" aria-label="Main navigation">
    <div class="container">
      <a href="/index.html">
        <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">
      </a>
      <ul class="nav-links" role="list">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About Us</a></li>
        <li>
          <a href="index.html#services">Services <span class="chevron">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-label">Our Services</a>
            <a href="services/unarmed-security.html">Unarmed Security</a>
            <a href="services/armed-security.html">Armed Security</a>
            <a href="services/mobile-patrol.html">Mobile Patrol</a>
            <a href="services/fire-watch.html">Fire Watch</a>
            <a href="services/concierge-security.html">Concierge Security</a>
            <a href="other-services.html">Other Services</a>
          </div>
        </li>
        <li>
          <a href="#">Industries <span class="chevron">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-label">Industries We Serve</a>
            <a href="industries/residential-communities.html">Residential Communities</a>
            <a href="industries/warehouses-distribution.html">Warehouses &amp; Distribution</a>
            <a href="industries/financial-institutions.html">Financial Institutions</a>
            <a href="industries/commercial-industrial.html">Commercial &amp; Industrial</a>
            <a href="industries/solar-energy-facilities.html">Solar Energy Facilities</a>
            <a href="industries/construction-sites.html">Construction Sites</a>
            <a href="industries/retail-stores.html">Retail Stores</a>
            <a href="industries/events-crowd-control.html">Events &amp; Crowd Control</a>
            <a href="industries/healthcare-facilities.html">Healthcare Facilities</a>
            <a href="industries/educational-campuses.html">Educational Campuses</a>
            <a href="industries/hospitality-hotels.html">Hospitality &amp; Hotels</a>
            <a href="other-industries.html">Other Industries</a>
          </div>
        </li>
        <li><a href="index.html#areas">Areas We Serve</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="get-a-quote.html">Contact</a></li>
      </ul>
      <a href="get-a-quote.html" class="nav-cta">Get a Quote</a>
      <button class="hamburger" aria-label="Open mobile menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <div class="mobile-menu" role="dialog" aria-modal="true" aria-label="Mobile navigation">
    <button class="mobile-close" type="button" aria-label="Close menu">&times;</button>
    <nav class="mobile-nav-links" aria-label="Mobile navigation links">
      <a href="index.html" class="mobile-top-link">Home</a>
      <a href="about.html" class="mobile-top-link">About Us</a>
      <div class="mobile-nav-heading">Services</div>
      <div class="mobile-nav-group" aria-label="Services">
        <a href="services/unarmed-security.html" class="mobile-sub">Unarmed Security</a>
        <a href="services/armed-security.html" class="mobile-sub">Armed Security</a>
        <a href="services/mobile-patrol.html" class="mobile-sub">Mobile Patrol</a>
        <a href="services/fire-watch.html" class="mobile-sub">Fire Watch</a>
        <a href="services/concierge-security.html" class="mobile-sub">Concierge Security</a>
        <a href="other-services.html" class="mobile-sub">Other Services</a>
      </div>
      <div class="mobile-nav-heading">Industries</div>
      <div class="mobile-nav-group" aria-label="Industries">
        <a href="industries/residential-communities.html" class="mobile-sub">Residential Communities</a>
        <a href="industries/warehouses-distribution.html" class="mobile-sub">Warehouses &amp; Distribution</a>
        <a href="industries/financial-institutions.html" class="mobile-sub">Financial Institutions</a>
        <a href="industries/commercial-industrial.html" class="mobile-sub">Commercial &amp; Industrial</a>
        <a href="industries/solar-energy-facilities.html" class="mobile-sub">Solar Energy Facilities</a>
        <a href="industries/construction-sites.html" class="mobile-sub">Construction Sites</a>
        <a href="industries/retail-stores.html" class="mobile-sub">Retail Stores</a>
        <a href="industries/events-crowd-control.html" class="mobile-sub">Events &amp; Crowd Control</a>
        <a href="industries/healthcare-facilities.html" class="mobile-sub">Healthcare Facilities</a>
        <a href="industries/educational-campuses.html" class="mobile-sub">Educational Campuses</a>
        <a href="industries/hospitality-hotels.html" class="mobile-sub">Hospitality &amp; Hotels</a>
        <a href="other-industries.html" class="mobile-sub">Other Industries</a>
      </div>
      <a href="index.html#areas" class="mobile-top-link">Areas We Serve</a>
      <a href="faq.html" class="mobile-top-link">FAQ</a>
      <a href="get-a-quote.html" class="mobile-top-link">Contact</a>
      <a href="get-a-quote.html" class="btn btn-red mobile-menu-cta">Get a Free Quote</a>
    </nav>
  </div>

  <a href="get-a-quote.html" class="floating-cta" aria-label="Get a Quote">Get a Quote</a>'''

FOOTER_ROOT = '''  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="/index.html">
            <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">
          </a>
        </div>
        <div class="footer-col">
          <p class="footer-tagline">Protecting People, Property, and Peace of Mind</p>
          <div class="footer-contact-item"><span class="fc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-6-5.33-6-11a6 6 0 0 1 12 0c0 5.67-6 11-6 11z"/><circle cx="12" cy="10" r="2.5"/></svg></span><span>6300 White Lane Suite G<br>Bakersfield, CA 93309</span></div>
          <div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.6 19.79 19.79 0 0 1 1.64 5.11 2 2 0 0 1 3.62 3h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.6a16 16 0 0 0 6 6l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.72 18z"/></svg></span></span><a href="tel:8773459239">877-345-9239</a></div>
          <div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span></span><a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></div>
          <div class="footer-contact-item"><span class="fc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></span><span>PPO License #122748 | Licensed &amp; Insured</span></div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <nav class="footer-links" aria-label="Footer quick links">
            <a href="index.html">Home</a>
            <a href="about.html">About Us</a>
            <a href="services/unarmed-security.html">Services</a>
            <a href="index.html#areas">Areas We Serve</a>
            <a href="faq.html">FAQ</a>
            <a href="get-a-quote.html">Contact Us</a>
            <a href="get-a-quote.html">Get a Quote</a>
          </nav>
        </div>
        <div class="footer-col">
          <h4>Our Services</h4>
          <nav class="footer-links" aria-label="Footer services links">
            <a href="services/unarmed-security.html">Unarmed Security</a>
            <a href="services/armed-security.html">Armed Security</a>
            <a href="services/mobile-patrol.html">Mobile Patrol</a>
            <a href="services/fire-watch.html">Fire Watch</a>
            <a href="services/concierge-security.html">Concierge Security</a>
          </nav>
        </div>
      </div>
    </div>
    <div class="footer-bottom"><div class="container">&copy; 2026 Invincible Security Group. All Rights Reserved. | Bakersfield, CA | <a href="/privacy-policy.html" style="color:inherit;">Privacy Policy</a> | <a href="/terms-conditions.html" style="color:inherit;">Terms &amp; Conditions</a> | <a href="/cookie-policy.html" style="color:inherit;">Cookie Policy</a></div></div>
  </footer>
  <script src="js/main.js"></script>'''

LEGAL_STYLE = '''  <style>
    .legal-hero { background: var(--navy); color: var(--white); padding: 80px 0 60px; text-align: center; }
    .legal-hero h1 { font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; margin-bottom: 12px; }
    .legal-hero .last-updated { font-size: 0.9rem; opacity: 0.75; }
    .legal-content { max-width: 860px; margin: 0 auto; padding: 60px 24px; }
    .legal-content h2 { font-size: 1.4rem; font-weight: 700; color: var(--navy); margin: 40px 0 12px; border-bottom: 2px solid #e8e8e8; padding-bottom: 8px; }
    .legal-content h3 { font-size: 1.1rem; font-weight: 700; color: var(--navy); margin: 28px 0 8px; }
    .legal-content p { font-size: 0.95rem; line-height: 1.8; color: var(--gray-text); margin-bottom: 16px; }
    .legal-content ul { list-style: disc; padding-left: 28px; margin-bottom: 16px; }
    .legal-content ul li { font-size: 0.95rem; line-height: 1.8; color: var(--gray-text); margin-bottom: 6px; }
    .legal-content a { color: var(--red); text-decoration: underline; }
  </style>'''

def build_legal_page(title, h1, last_updated, content_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
{LEGAL_STYLE}
{ANALYTICS}
</head>
<body>
{TOP_BAR}

{NAVBAR_ROOT}

  <div class="legal-hero">
    <div class="container">
      <h1>{h1}</h1>
      <p class="last-updated">Last Updated: {last_updated}</p>
    </div>
  </div>

  <main>
    <div class="legal-content">
{content_html}
    </div>
  </main>

{FOOTER_ROOT}
</body>
</html>
'''

# ── Privacy Policy ──────────────────────────────────────────────────────────

PRIVACY_CONTENT = '''      <h2>Introduction</h2>
      <p>Invincible Security Group ("ISG," "we," "us," or "our") respects your privacy and is committed to protecting your personal information. This Privacy Policy explains how we collect, use, disclose, and safeguard information when you visit our website at <a href="https://www.invinciblesecuritygroup.com">invinciblesecuritygroup.com</a> or contact us in connection with our security services. Please read this policy carefully. If you do not agree with its terms, please discontinue use of our site.</p>

      <h2>Information We Collect</h2>

      <h3>Personal Information</h3>
      <p>When you request a quote, contact us, or use our forms, we may collect:</p>
      <ul>
        <li>Full name, company name, and job title</li>
        <li>Email address and phone number</li>
        <li>Physical address or service location</li>
        <li>Security service requirements and project details</li>
        <li>Any other information you voluntarily provide</li>
      </ul>

      <h3>Mobile &amp; Text Messaging Information</h3>
      <p>If you opt in to receive SMS communications from Invincible Security Group, we collect your mobile phone number and maintain a record of your consent. Your mobile number and SMS opt-in consent will not be shared with third parties or affiliates for marketing purposes. Message frequency may vary. Standard message and data rates may apply. You may opt out at any time by replying STOP to any SMS message. Reply HELP for assistance.</p>

      <h3>Automatically Collected Information</h3>
      <p>When you visit our website, we may automatically collect certain technical information, including your IP address, browser type, operating system, referring URLs, pages visited, and time spent on each page. This information is collected through cookies and similar technologies.</p>

      <h2>How We Use Your Information</h2>
      <p>We use the information we collect to:</p>
      <ul>
        <li>Respond to inquiries and provide security service quotes</li>
        <li>Communicate with you about your service request or contract</li>
        <li>Send follow-up and administrative communications via email or SMS (where you have opted in)</li>
        <li>Improve our website, services, and customer experience</li>
        <li>Comply with legal obligations and protect our legal rights</li>
        <li>Prevent fraud and maintain the security of our platform</li>
      </ul>

      <h2>Sharing of Information</h2>

      <h3>Service Providers</h3>
      <p>We may share your information with trusted third-party service providers who assist us in operating our website, processing form submissions, and delivering communications. These providers are contractually obligated to protect your information and may not use it for any purpose other than providing services to ISG.</p>

      <h3>Legal Requirements</h3>
      <p>We may disclose your information if required to do so by law or in response to valid requests by public authorities, including to meet national security or law enforcement requirements.</p>

      <h3>Business Protection</h3>
      <p>We may disclose your information when we believe disclosure is necessary to investigate, prevent, or respond to fraud, misuse of our services, or other unlawful activities.</p>

      <h3>SMS Data Protection</h3>
      <p>Mobile opt-in data and SMS consent will not be shared with any third parties or affiliates for marketing or promotional purposes. This data is used solely to deliver messages you have requested from Invincible Security Group.</p>

      <h2>Cookies and Tracking</h2>
      <p>Our website uses cookies and similar tracking technologies to enhance your browsing experience and collect analytics data. We use Google Analytics and Microsoft Clarity to understand how visitors interact with our site. You can control cookie preferences through your browser settings. Please see our <a href="/cookie-policy.html">Cookie Policy</a> for more information.</p>

      <h2>Data Security</h2>
      <p>We implement reasonable administrative, technical, and physical safeguards designed to protect the personal information we collect. However, no method of transmission over the internet or electronic storage is 100% secure. We cannot guarantee the absolute security of your information.</p>

      <h2>Data Retention</h2>
      <p>We retain your personal information for as long as necessary to fulfill the purposes described in this Privacy Policy, comply with our legal obligations, resolve disputes, and enforce our agreements. When your information is no longer needed, we will securely delete or anonymize it.</p>

      <h2>Your Privacy Rights</h2>
      <p>Depending on your location, you may have certain rights with respect to your personal information, including the right to access, correct, or delete your data. To exercise these rights, please contact us using the information provided below.</p>

      <h2>California Privacy Rights (CCPA/CPRA)</h2>
      <p>If you are a California resident, you have specific rights under the California Consumer Privacy Act (CCPA) as amended by the California Privacy Rights Act (CPRA), including the right to know what personal information we collect, the right to delete your personal information, the right to opt out of the sale or sharing of your personal information, and the right to non-discrimination for exercising these rights. To submit a California privacy rights request, please contact us at <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a>.</p>
      <p>We do not sell personal information to third parties.</p>

      <h2>Children\'s Privacy</h2>
      <p>Our website and services are not directed to individuals under the age of 16. We do not knowingly collect personal information from children. If you believe we have inadvertently collected information from a minor, please contact us immediately so we can delete it.</p>

      <h2>Third-Party Links</h2>
      <p>Our website may contain links to third-party websites. We are not responsible for the privacy practices or content of those sites. We encourage you to review the privacy policies of any third-party sites you visit.</p>

      <h2>Changes to This Policy</h2>
      <p>We may update this Privacy Policy from time to time. The updated policy will be posted on this page with a revised "Last Updated" date. Your continued use of our website after any changes constitutes your acceptance of the updated policy.</p>

      <h2>Contact Information</h2>
      <p>If you have questions or concerns about this Privacy Policy or our data practices, please contact us at:</p>
      <ul>
        <li><strong>Email:</strong> <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></li>
        <li><strong>Phone:</strong> <a href="tel:8773459239">877-345-9239</a></li>
        <li><strong>Address:</strong> 6300 White Lane Suite G, Bakersfield, CA 93309</li>
      </ul>

      <h2>SMS Communications Terms</h2>
      <p>By providing your mobile phone number and opting in to receive SMS communications from Invincible Security Group, you consent to receive text messages related to your inquiry, quote request, or service agreement. Consent to receive SMS communications is not a condition of using our services.</p>
      <ul>
        <li>To opt out of SMS communications, reply <strong>STOP</strong> to any message at any time.</li>
        <li>For help, reply <strong>HELP</strong> to any message or contact us at <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a>.</li>
        <li>Standard message and data rates may apply depending on your carrier plan.</li>
        <li>Consent to receive SMS communications is not required to use our security services.</li>
      </ul>'''

# ── Terms & Conditions ───────────────────────────────────────────────────────

TERMS_CONTENT = '''      <h2>Acceptance of Terms</h2>
      <p>By accessing or using the website of Invincible Security Group ("ISG," "we," "us," or "our") at invinciblesecuritygroup.com, you agree to be bound by these Terms and Conditions. If you do not agree to these terms, please discontinue use of our website immediately. These terms apply to all visitors, users, and others who access or use our site.</p>

      <h2>Use of Website</h2>
      <p>You may use our website for lawful purposes only. You agree not to use our website in any way that violates applicable laws or regulations, infringes on the rights of others, or interferes with the operation of the site. We reserve the right to restrict or terminate access to our website for any user who violates these terms or engages in conduct we deem harmful or inappropriate.</p>
      <p>You may not use automated systems, bots, scrapers, or other tools to access our website in a manner that places excessive load on our servers or circumvents any security measures.</p>

      <h2>Services Offered</h2>
      <p>Invincible Security Group is a California-licensed Private Patrol Operator (PPO License #122748) providing professional security guard services including unarmed security, armed security, mobile patrol, fire watch, and concierge security across the State of California. Information on our website is provided for general informational purposes and does not constitute a binding service agreement. Actual services are governed by a separate written contract between ISG and the client.</p>

      <h2>Information Accuracy</h2>
      <p>We make reasonable efforts to ensure that information on our website is accurate and up to date. However, we make no warranties or representations, express or implied, about the completeness, accuracy, reliability, or suitability of the information provided. Any reliance you place on such information is strictly at your own risk.</p>

      <h2>Intellectual Property</h2>
      <p>All content on this website, including but not limited to text, graphics, logos, images, and software, is the property of Invincible Security Group or its content suppliers and is protected by applicable intellectual property laws. You may not reproduce, distribute, modify, create derivative works from, or exploit any content from this website without our express written permission.</p>

      <h2>Limitation of Liability</h2>
      <p>To the fullest extent permitted by applicable law, Invincible Security Group and its officers, directors, employees, agents, and affiliates shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including but not limited to loss of revenue, loss of data, or business interruption, arising out of or in connection with your use of our website or services, even if we have been advised of the possibility of such damages.</p>
      <p>Our total liability to you for any claim arising out of or relating to these terms or your use of our website shall not exceed one hundred dollars ($100).</p>

      <h2>Disclaimer of Warranties</h2>
      <p>Our website is provided on an "as is" and "as available" basis without any warranties of any kind, either express or implied, including but not limited to implied warranties of merchantability, fitness for a particular purpose, or non-infringement. We do not warrant that the website will be uninterrupted, error-free, or free of viruses or other harmful components.</p>

      <h2>Third-Party Links</h2>
      <p>Our website may contain links to third-party websites that are not owned or controlled by Invincible Security Group. We have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party websites. We encourage you to review the terms and privacy policies of any third-party sites you visit.</p>

      <h2>Privacy</h2>
      <p>Your use of our website is also governed by our <a href="/privacy-policy.html">Privacy Policy</a>, which is incorporated by reference into these Terms and Conditions. Please review our Privacy Policy to understand our practices regarding the collection and use of your personal information.</p>

      <h2>Governing Law</h2>
      <p>These Terms and Conditions are governed by and construed in accordance with the laws of the State of California, without regard to its conflict of law provisions. Any legal action or proceeding arising out of or relating to these terms shall be brought exclusively in the state or federal courts located in Kern County, California.</p>

      <h2>Changes to These Terms</h2>
      <p>We reserve the right to modify these Terms and Conditions at any time. Updated terms will be posted on this page with a revised "Last Updated" date. Your continued use of our website after any changes constitutes your acceptance of the updated terms.</p>

      <h2>Contact Information</h2>
      <p>If you have questions about these Terms and Conditions, please contact us:</p>
      <ul>
        <li><strong>Email:</strong> <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></li>
        <li><strong>Phone:</strong> <a href="tel:8773459239">877-345-9239</a></li>
        <li><strong>Address:</strong> 6300 White Lane Suite G, Bakersfield, CA 93309</li>
      </ul>'''

# ── Cookie Policy ────────────────────────────────────────────────────────────

COOKIE_CONTENT = '''      <h2>What Are Cookies</h2>
      <p>Cookies are small text files that are stored on your device (computer, tablet, or mobile phone) when you visit a website. They are widely used to make websites work efficiently, to remember your preferences, and to provide information to website owners about how visitors interact with their site.</p>
      <p>This Cookie Policy explains what cookies we use on the Invincible Security Group website at invinciblesecuritygroup.com, why we use them, and how you can control them.</p>

      <h2>Types of Cookies We Use</h2>

      <h3>Essential Cookies</h3>
      <p>Essential cookies are necessary for our website to function properly. They enable core features such as form submission, navigation, and security. These cookies cannot be disabled because the website would not work without them. They do not collect personal information for marketing purposes.</p>

      <h3>Analytics Cookies</h3>
      <p>We use analytics cookies to understand how visitors interact with our website — including which pages are visited most frequently, how long visitors stay, and how they navigate through the site. This information helps us improve our content, structure, and user experience. Analytics cookies collect aggregated, anonymized data and do not identify you personally.</p>

      <h3>Performance Cookies</h3>
      <p>Performance cookies help us understand how our website performs under various conditions and identify areas for technical improvement. They collect information about loading times, error rates, and device types to help us deliver a faster and more reliable experience.</p>

      <h2>Specific Cookies Used</h2>

      <h3>Google Analytics</h3>
      <p>We use Google Analytics, a web analytics service provided by Google LLC. Google Analytics places cookies on your device to collect standard internet log information and visitor behavior information in an anonymized form. The information generated by these cookies — including your IP address — is transmitted to and stored by Google on servers in the United States. Google uses this information to evaluate your use of our website, compile reports on website activity, and provide other services relating to website activity and internet usage.</p>
      <p>You can opt out of Google Analytics tracking by installing the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer">Google Analytics Opt-out Browser Add-on</a>.</p>

      <h3>Microsoft Clarity</h3>
      <p>We use Microsoft Clarity, a behavioral analytics tool provided by Microsoft Corporation. Clarity records anonymized session replays and generates heatmaps that help us understand how visitors interact with specific pages and elements on our website. Clarity does not collect personally identifiable information. The data collected is used solely to improve the usability and effectiveness of our website.</p>
      <p>For more information about Microsoft Clarity\'s data practices, please review the <a href="https://privacy.microsoft.com/en-us/privacystatement" target="_blank" rel="noopener noreferrer">Microsoft Privacy Statement</a>.</p>

      <h2>How to Control Cookies</h2>
      <p>You can control and manage cookies in several ways:</p>
      <ul>
        <li><strong>Browser Settings:</strong> Most web browsers allow you to control cookies through their settings. You can set your browser to refuse cookies, delete existing cookies, or alert you when a cookie is being placed. Note that disabling cookies may affect the functionality of our website.</li>
        <li><strong>Google Analytics Opt-out:</strong> Install the Google Analytics Opt-out Browser Add-on available at tools.google.com/dlpage/gaoptout.</li>
        <li><strong>Do Not Track:</strong> Some browsers include a "Do Not Track" feature that sends a signal to websites requesting that they not track your browsing activity. Our website acknowledges this signal where technically feasible.</li>
      </ul>

      <h2>Cookie Consent</h2>
      <p>By continuing to use our website, you consent to the use of cookies as described in this Cookie Policy. If you do not wish to accept cookies, you should adjust your browser settings or discontinue use of our site.</p>

      <h2>Changes to This Policy</h2>
      <p>We may update this Cookie Policy from time to time to reflect changes in our practices or for other operational, legal, or regulatory reasons. The updated policy will be posted on this page with a revised "Last Updated" date.</p>

      <h2>Contact Information</h2>
      <p>If you have questions about our use of cookies or this Cookie Policy, please contact us:</p>
      <ul>
        <li><strong>Email:</strong> <a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></li>
        <li><strong>Phone:</strong> <a href="tel:8773459239">877-345-9239</a></li>
        <li><strong>Address:</strong> 6300 White Lane Suite G, Bakersfield, CA 93309</li>
      </ul>'''

legal_pages = [
    ('privacy-policy.html', 'Privacy Policy | Invincible Security Group', 'Privacy Policy', 'January 1, 2026', PRIVACY_CONTENT),
    ('terms-conditions.html', 'Terms & Conditions | Invincible Security Group', 'Terms &amp; Conditions', 'January 1, 2026', TERMS_CONTENT),
    ('cookie-policy.html', 'Cookie Policy | Invincible Security Group', 'Cookie Policy', 'January 1, 2026', COOKIE_CONTENT),
]

for fname, title, h1, last_updated, content in legal_pages:
    fullpath = os.path.join(BASE, fname)
    html = build_legal_page(title, h1, last_updated, content)
    with open(fullpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: {fname}')

print('All pages created.')
