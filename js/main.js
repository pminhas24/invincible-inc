/* ============================================================
   INVINCIBLE SECURITY GROUP — main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Sticky Navbar Shadow ---------- */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 10);
    });
  }

  /* ---------- Hamburger / Mobile Menu ---------- */
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileClose = document.querySelector('.mobile-close');

  function openMobile() {
    if (!mobileMenu || !hamburger) return;
    mobileMenu.classList.add('active');
    hamburger.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeMobile() {
    if (!mobileMenu || !hamburger) return;
    mobileMenu.classList.remove('active');
    hamburger.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (hamburger) hamburger.addEventListener('click', openMobile);
  if (mobileClose) mobileClose.addEventListener('click', closeMobile);
  if (mobileMenu) {
    mobileMenu.addEventListener('click', function (e) {
      if (e.target === mobileMenu) closeMobile();
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMobile();
  });

  /* ---------- Desktop Dropdowns ---------- */
  const dropdownItems = Array.from(document.querySelectorAll('.nav-links > li')).filter(function (item) {
    return item.querySelector('.dropdown-menu');
  });

  function closeDropdowns(except) {
    dropdownItems.forEach(function (item) {
      if (item !== except) item.classList.remove('is-open');
    });
  }

  dropdownItems.forEach(function (item) {
    const trigger = item.querySelector(':scope > a');
    if (!trigger) return;

    item.addEventListener('mouseenter', function () {
      if (window.innerWidth <= 768) return;
      closeDropdowns(item);
      item.classList.add('is-open');
    });

    item.addEventListener('mouseleave', function () {
      item.classList.remove('is-open');
      trigger.classList.remove('active');
    });

    item.addEventListener('focusin', function () {
      if (window.innerWidth <= 768) return;
      closeDropdowns(item);
      item.classList.add('is-open');
    });

    item.addEventListener('focusout', function (e) {
      if (!item.contains(e.relatedTarget)) {
        item.classList.remove('is-open');
        trigger.classList.remove('active');
      }
    });

    trigger.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) return;
      if (trigger.getAttribute('href') === '#') {
        closeDropdowns(item);
        item.classList.toggle('is-open');
        trigger.classList.toggle('active', item.classList.contains('is-open'));
        e.preventDefault();
      } else {
        item.classList.remove('is-open');
        trigger.classList.remove('active');
      }
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-links')) {
      closeDropdowns();
      dropdownItems.forEach(function (item) {
        const trigger = item.querySelector(':scope > a');
        if (trigger) trigger.classList.remove('active');
      });
    }
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth <= 768) {
      closeDropdowns();
      dropdownItems.forEach(function (item) {
        const trigger = item.querySelector(':scope > a');
        if (trigger) trigger.classList.remove('active');
      });
    }
  });

  /* ---------- FAQ Accordion ---------- */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    if (!btn || !answer) return;

    btn.addEventListener('click', function () {
      const isOpen = btn.classList.contains('active');
      // Close all
      faqItems.forEach(function (i) {
        i.querySelector('.faq-q').classList.remove('active');
        const a = i.querySelector('.faq-a');
        if (a) a.style.maxHeight = '0';
      });
      // Open clicked if was closed
      if (!isOpen) {
        btn.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 40 + 'px';
      }
    });
  });

  /* ---------- Smooth Scroll for Anchor Links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        closeMobile();
        const offset = (navbar ? navbar.offsetHeight : 72) + 16;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  /* ---------- Scroll Reveal (IntersectionObserver) ---------- */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    const revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    reveals.forEach(function (el) { revealObserver.observe(el); });
  } else {
    // Fallback: show all
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Active Nav Link ---------- */
  const currentPath = window.location.pathname.replace(/\/$/, '');
  document.querySelectorAll('.nav-links a').forEach(function (link) {
    const rawHref = link.getAttribute('href') || '';
    if (!rawHref || rawHref === '#' || rawHref.startsWith('#')) return;
    const linkPath = new URL(link.href, window.location.origin).pathname.replace(/\/$/, '');
    if (linkPath === currentPath) link.classList.add('active');
  });

  /* ---------- Form Submissions (prevent default, show message) ---------- */
  document.querySelectorAll('form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = form.querySelector('.form-submit, [type="submit"]');
      if (btn) {
        const orig = btn.textContent;
        btn.textContent = 'Message Sent! We\'ll be in touch shortly.';
        btn.style.background = '#2e7d32';
        btn.disabled = true;
        setTimeout(function () {
          btn.textContent = orig;
          btn.style.background = '';
          btn.disabled = false;
          form.reset();
        }, 4000);
      }
    });
  });

});
