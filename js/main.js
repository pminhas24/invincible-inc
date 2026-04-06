/* ============================================================
   INVINCIBLE INC — main.js
   Shared JavaScript for all pages
   ============================================================ */

(function () {
  'use strict';

  /* ── Hamburger / Mobile Nav ──────────────────────────── */
  const hamburger   = document.querySelector('.hamburger');
  const navMenu     = document.querySelector('.nav-menu');
  const navOverlay  = document.createElement('div');

  navOverlay.className = 'nav-overlay';
  navOverlay.style.cssText = `
    position:fixed; inset:0; background:rgba(0,0,0,0.6);
    z-index:998; display:none; backdrop-filter:blur(2px);
  `;
  document.body.appendChild(navOverlay);

  function openNav() {
    hamburger.classList.add('open');
    navMenu.classList.add('open');
    navOverlay.style.display = 'block';
    document.body.style.overflow = 'hidden';
    hamburger.setAttribute('aria-expanded', 'true');
  }

  function closeNav() {
    hamburger.classList.remove('open');
    navMenu.classList.remove('open');
    navOverlay.style.display = 'none';
    document.body.style.overflow = '';
    hamburger.setAttribute('aria-expanded', 'false');
  }

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.contains('open') ? closeNav() : openNav();
    });
  }

  navOverlay.addEventListener('click', closeNav);

  /* ── Mobile Services Dropdown toggle ─────────────────── */
  const dropdownTrigger = document.querySelector('.nav-item .nav-link[data-has-dropdown]');
  if (dropdownTrigger) {
    dropdownTrigger.addEventListener('click', function (e) {
      if (window.innerWidth <= 640) {
        e.preventDefault();
        const dropdown = this.nextElementSibling;
        if (dropdown) dropdown.classList.toggle('mobile-open');
      }
    });
  }

  /* ── Close nav on link click (mobile) ────────────────── */
  document.querySelectorAll('.nav-link:not([data-has-dropdown]), .dropdown a').forEach(link => {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 640) closeNav();
    });
  });

  /* ── Scroll Reveal (IntersectionObserver) ────────────── */
  function initScrollReveal() {
    const elements = document.querySelectorAll('.reveal');
    if (!elements.length) return;

    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    elements.forEach(el => observer.observe(el));
  }

  /* ── FAQ Accordion ───────────────────────────────────── */
  function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    if (!faqItems.length) return;

    faqItems.forEach(function (item) {
      const question = item.querySelector('.faq-question');
      if (!question) return;

      question.addEventListener('click', function () {
        const isOpen = item.classList.contains('open');

        // Close all
        faqItems.forEach(i => i.classList.remove('open'));

        // Open clicked (if it wasn't already open)
        if (!isOpen) {
          item.classList.add('open');
        }
      });
    });
  }

  /* ── Floating CTA → scroll to #quote ─────────────────── */
  function initFloatingCTA() {
    const floatingLink = document.querySelector('.floating-quote a');
    if (!floatingLink) return;

    floatingLink.addEventListener('click', function (e) {
      const target = document.querySelector('#quote');
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  /* ── Active nav link on scroll (index only) ──────────── */
  function initActiveNav() {
    const sections  = document.querySelectorAll('section[id]');
    const navLinks  = document.querySelectorAll('.nav-link[href^="#"]');
    if (!sections.length || !navLinks.length) return;

    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          navLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === '#' + id);
          });
        }
      });
    }, {
      threshold: 0.3,
      rootMargin: '-80px 0px -50% 0px'
    });

    sections.forEach(section => observer.observe(section));
  }

  /* ── Sticky top bar + navbar offset for scroll ────────── */
  function initStickyNav() {
    const topBar = document.querySelector('.top-bar');
    const navbar = document.querySelector('.navbar');
    if (!topBar || !navbar) return;

    function handleScroll() {
      if (window.scrollY > 60) {
        topBar.style.display = 'none';
        navbar.style.position = 'fixed';
        navbar.style.top = '0';
        navbar.style.width = '100%';
      } else {
        topBar.style.display = '';
        navbar.style.position = 'sticky';
        navbar.style.top = '0';
      }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
  }

  /* ── Quote form: smooth submission feedback ───────────── */
  function initQuoteForm() {
    const forms = document.querySelectorAll('.quote-form');
    forms.forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        const btn = form.querySelector('.form-submit');
        const orig = btn.textContent;
        btn.textContent = 'Sending…';
        btn.disabled = true;

        setTimeout(function () {
          btn.textContent = '✓ Request Received!';
          btn.style.background = '#2a7a2a';
          setTimeout(function () {
            btn.textContent = orig;
            btn.style.background = '';
            btn.disabled = false;
            form.reset();
          }, 3000);
        }, 1200);
      });
    });
  }

  /* ── Nav Home link active on load ─────────────────────── */
  function initNavActiveOnLoad() {
    const path = window.location.pathname.split('/').pop() || 'index.html';

    // Match top-level nav links
    document.querySelectorAll('.nav-link').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const linkFile = href.split('/').pop().split('#')[0] || 'index.html';
      if (linkFile === path || (path === '' && linkFile === 'index.html')) {
        link.classList.add('active');
      }
    });

    // Mark parent "Services" nav link active if a dropdown child matches
    document.querySelectorAll('.dropdown a').forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const linkFile = href.split('/').pop().split('#')[0];
      if (linkFile === path) {
        const parentLink = link.closest('.nav-item') && link.closest('.nav-item').querySelector('.nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    });
  }

  /* ── Init ─────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    initScrollReveal();
    initFAQ();
    initFloatingCTA();
    initActiveNav();
    initStickyNav();
    initQuoteForm();
    initNavActiveOnLoad();
  });

})();
