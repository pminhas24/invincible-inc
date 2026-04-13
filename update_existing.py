import re, os

BASE = r'C:\xampp\htdocs\invincible-inc-copy'

# New industry pages HTML for root-level files (desktop dropdown)
NEW_IND_ROOT_DESKTOP = (
    '<a href="industries/healthcare-facilities.html">Healthcare Facilities</a>\n'
    '            <a href="industries/educational-campuses.html">Educational Campuses</a>\n'
    '            <a href="industries/hospitality-hotels.html">Hospitality &amp; Hotels</a>\n'
    '            <a href="other-industries.html">Other Industries</a>'
)

# New industry pages HTML for subdirectory-level files (desktop dropdown)
NEW_IND_SUB_DESKTOP = (
    '<a href="../industries/healthcare-facilities.html">Healthcare Facilities</a>\n'
    '            <a href="../industries/educational-campuses.html">Educational Campuses</a>\n'
    '            <a href="../industries/hospitality-hotels.html">Hospitality &amp; Hotels</a>\n'
    '            <a href="../other-industries.html">Other Industries</a>'
)

# New industry pages HTML for root-level files (mobile menu)
NEW_IND_ROOT_MOBILE = (
    '<a href="industries/healthcare-facilities.html" class="mobile-sub">Healthcare Facilities</a>\n'
    '        <a href="industries/educational-campuses.html" class="mobile-sub">Educational Campuses</a>\n'
    '        <a href="industries/hospitality-hotels.html" class="mobile-sub">Hospitality &amp; Hotels</a>\n'
    '        <a href="other-industries.html" class="mobile-sub">Other Industries</a>'
)

# New industry pages HTML for subdirectory-level files (mobile menu)
NEW_IND_SUB_MOBILE = (
    '<a href="../industries/healthcare-facilities.html" class="mobile-sub">Healthcare Facilities</a>\n'
    '        <a href="../industries/educational-campuses.html" class="mobile-sub">Educational Campuses</a>\n'
    '        <a href="../industries/hospitality-hotels.html" class="mobile-sub">Hospitality &amp; Hotels</a>\n'
    '        <a href="../other-industries.html" class="mobile-sub">Other Industries</a>'
)

# Footer-bottom replacements
OLD_FOOTER_BOTTOM = '&copy; 2026 Invincible Security Group. All Rights Reserved. | Bakersfield, CA</div></div>'

FOOTER_BOTTOM_ROOT = (
    '&copy; 2026 Invincible Security Group. All Rights Reserved. | Bakersfield, CA | '
    '<a href="/privacy-policy.html" style="color:inherit;">Privacy Policy</a> | '
    '<a href="/terms-conditions.html" style="color:inherit;">Terms &amp; Conditions</a> | '
    '<a href="/cookie-policy.html" style="color:inherit;">Cookie Policy</a>'
    '</div></div>'
)

FOOTER_BOTTOM_SUB = (
    '&copy; 2026 Invincible Security Group. All Rights Reserved. | Bakersfield, CA | '
    '<a href="/privacy-policy.html" style="color:inherit;">Privacy Policy</a> | '
    '<a href="/terms-conditions.html" style="color:inherit;">Terms &amp; Conditions</a> | '
    '<a href="/cookie-policy.html" style="color:inherit;">Cookie Policy</a>'
    '</div></div>'
)

# Skip newly created pages (they already have correct content)
SKIP_FILES = {
    'healthcare-facilities.html',
    'educational-campuses.html',
    'hospitality-hotels.html',
    'privacy-policy.html',
    'terms-conditions.html',
    'cookie-policy.html',
    'gen_pages.py',
    'fix_isg.py',
    'update_existing.py',
}

def process_file(filepath):
    rel = os.path.relpath(filepath, BASE)
    fname = os.path.basename(filepath)

    # Skip newly generated pages
    if fname in SKIP_FILES:
        print(f'Skipped: {rel}')
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Determine if this is a root-level or subdirectory file
    subdir = os.path.dirname(os.path.relpath(filepath, BASE))
    is_sub = subdir != '' and subdir != '.'

    # 1. Update desktop navbar dropdown (Events & Crowd Control line → add new industries before Other Industries)
    if is_sub:
        # Pattern: Events & Crowd Control followed by Other Industries in subdirectory files
        content = re.sub(
            r'<a href="\.\./industries/events-crowd-control\.html">Events &amp; Crowd Control</a>\s*\n\s*<a href="\.\./other-industries\.html">Other Industries</a>',
            '<a href="../industries/events-crowd-control.html">Events &amp; Crowd Control</a>\n'
            '            ' + NEW_IND_SUB_DESKTOP,
            content
        )
        # Mobile menu
        content = re.sub(
            r'<a href="\.\./industries/events-crowd-control\.html" class="mobile-sub">Events &amp; Crowd Control</a>\s*\n\s*<a href="\.\./other-industries\.html" class="mobile-sub">Other Industries</a>',
            '<a href="../industries/events-crowd-control.html" class="mobile-sub">Events &amp; Crowd Control</a>\n'
            '        ' + NEW_IND_SUB_MOBILE,
            content
        )
    else:
        # Root-level files
        content = re.sub(
            r'<a href="industries/events-crowd-control\.html">Events &amp; Crowd Control</a>\s*\n\s*<a href="other-industries\.html">Other Industries</a>',
            '<a href="industries/events-crowd-control.html">Events &amp; Crowd Control</a>\n'
            '            ' + NEW_IND_ROOT_DESKTOP,
            content
        )
        # Mobile menu
        content = re.sub(
            r'<a href="industries/events-crowd-control\.html" class="mobile-sub">Events &amp; Crowd Control</a>\s*\n\s*<a href="other-industries\.html" class="mobile-sub">Other Industries</a>',
            '<a href="industries/events-crowd-control.html" class="mobile-sub">Events &amp; Crowd Control</a>\n'
            '        ' + NEW_IND_ROOT_MOBILE,
            content
        )

    # 2. Update footer-bottom legal links
    content = content.replace(OLD_FOOTER_BOTTOM, FOOTER_BOTTOM_ROOT)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {rel}')
    else:
        print(f'No change: {rel}')

for root, dirs, files in os.walk(BASE):
    # Skip hidden dirs and node_modules etc
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fname in sorted(files):
        if fname.endswith('.html'):
            process_file(os.path.join(root, fname))

print('Done.')
