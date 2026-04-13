import re, os

BASE = r'C:\xampp\htdocs\invincible-inc-copy'

ADDR_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-6-5.33-6-11a6 6 0 0 1 12 0c0 5.67-6 11-6 11z"/><circle cx="12" cy="10" r="2.5"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.6 19.79 19.79 0 0 1 1.64 5.11 2 2 0 0 1 3.62 3h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.6a16 16 0 0 0 6 6l.96-.96a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.72 18z"/></svg>'
EMAIL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
SHIELD_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>'

def get_contact_html(i):
    return (
        f'{i}<p class="footer-tagline">Protecting People, Property, and Peace of Mind</p>\n'
        f'{i}<div class="footer-contact-item"><span class="fc-icon">{ADDR_SVG}</span><span>6300 White Lane Suite G<br>Bakersfield, CA 93309</span></div>\n'
        f'{i}<div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true">{PHONE_SVG}</span></span><a href="tel:8773459239">877-345-9239</a></div>\n'
        f'{i}<div class="footer-contact-item"><span class="fc-icon"><span class="icon-inline" aria-hidden="true">{EMAIL_SVG}</span></span><a href="mailto:info@invinciblesecuritygroup.com">info@invinciblesecuritygroup.com</a></div>\n'
        f'{i}<div class="footer-contact-item"><span class="fc-icon">{SHIELD_SVG}</span><span>PPO License #122748 | Licensed &amp; Insured</span></div>'
    )

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # STEP 1: Footer - replace first footer-col (logo+contact) with two cols
    def footer_replacer(m):
        outer = m.group(1)
        inner = outer + '  '
        return (
            f'{outer}<div class="footer-col">\n'
            f'{inner}<a href="/index.html">\n'
            f'{inner}  <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">\n'
            f'{inner}</a>\n'
            f'{outer}</div>\n'
            f'{outer}<div class="footer-col">\n'
            + get_contact_html(inner) + '\n'
            + f'{outer}</div>'
        )

    pattern_footer = re.compile(
        r'^( +)<div class="footer-col">\s*'
        r'<a[^>]*class="isg-logo"[^>]*>[\s\S]*?</a>[\s\S]*?'
        r'</div>(?=\s*\n\s*<div class="footer-col">)',
        re.MULTILINE | re.DOTALL
    )
    content = pattern_footer.sub(footer_replacer, content, count=1)

    # STEP 2: Navbar - replace remaining isg-logo anchors
    def navbar_replacer(m):
        lead = m.group(1)
        return (
            f'{lead}<a href="/index.html">\n'
            f'{lead}  <img src="/images/logo-invincible-security-group.png" alt="Invincible Security Group" style="height:55px;width:auto;display:block;">\n'
            f'{lead}</a>'
        )
    pattern_navbar = re.compile(
        r'^( *)<a[^>]*class="isg-logo"[^>]*>[\s\S]*?</a>',
        re.MULTILINE | re.DOTALL
    )
    content = pattern_navbar.sub(navbar_replacer, content)

    # STEP 3: Copyright 2025 -> 2026
    content = content.replace('&copy; 2025 Invincible Security Group.', '&copy; 2026 Invincible Security Group.')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {os.path.relpath(filepath, BASE)}')
    else:
        print(f'No change: {os.path.relpath(filepath, BASE)}')

for root, dirs, files in os.walk(BASE):
    for fname in sorted(files):
        if fname.endswith('.html'):
            process_file(os.path.join(root, fname))

print('Done.')
