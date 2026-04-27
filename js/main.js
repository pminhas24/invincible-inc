/* ============================================================
   INVINCIBLE SECURITY GROUP — main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Sticky Navbar Shadow ---------- */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', function() {
      navbar.classList.toggle('scrolled', window.scrollY > 10);
    });
  }

  /* ---------- Hamburger / Mobile Menu ---------- */
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileMenuLinks = document.querySelectorAll('.mobile-nav-links a');

  function openMobile() {
    if (!mobileMenu) return;
    mobileMenu.classList.add('active');
    if (hamburger) {
      hamburger.classList.add('open');
      hamburger.setAttribute('aria-expanded', 'true');
    }
    document.body.style.overflow = 'hidden';
  }
  function closeMobile() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove('active');
    if (hamburger) {
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    }
    document.body.style.overflow = '';
  }

  if (hamburger) hamburger.addEventListener('click', openMobile);

  document.querySelectorAll('.mobile-close').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      closeMobile();
    });
  });

  mobileMenuLinks.forEach(function (link) {
    link.addEventListener('click', closeMobile);
  });

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

  /* ---------- Form Validation & Submission ---------- */

  /* ---------- Phone Number Formatting ---------- */
  document.querySelectorAll('input[type="tel"]').forEach(function(phone) {
    phone.addEventListener('input', function() {
      let digits = phone.value.replace(/\D/g, '').slice(0, 10);
      if (digits.length >= 7) {
        phone.value = '(' + digits.slice(0,3) + ') ' + digits.slice(3,6) + '-' + digits.slice(6);
      } else if (digits.length >= 4) {
        phone.value = '(' + digits.slice(0,3) + ') ' + digits.slice(3);
      } else if (digits.length > 0) {
        phone.value = '(' + digits;
      }
    });
    /* ---------- Block non-numeric keys on phone fields ---------- */
  document.querySelectorAll('input[type="tel"]').forEach(function(phone) {
    phone.addEventListener('keydown', function(e) {
      var allowed = [
        'Backspace', 'Delete', 'Tab', 'Enter', 'ArrowLeft',
        'ArrowRight', 'ArrowUp', 'ArrowDown', 'Home', 'End'
      ];
      if (allowed.indexOf(e.key) !== -1) return;
      if (e.ctrlKey || e.metaKey) return;
      if (!/^\d$/.test(e.key)) {
        e.preventDefault();
      }
    });
  });
  });

  document.querySelectorAll('form[data-netlify="true"]').forEach(function(form) {

    form.querySelectorAll('input, select, textarea').forEach(function(field) {
      field.addEventListener('invalid', function(e) {
        e.preventDefault();
        field.classList.add('input-error');

        let msg = '';
        if (field.validity.valueMissing) msg = 'This field is required';
        else if (field.validity.typeMismatch && field.type === 'email') msg = 'Please enter a valid email address';
        else if (field.validity.patternMismatch && field.name === 'phone') msg = 'Please enter a valid phone number e.g. (661) 000-0000';
        else if (field.validity.tooShort) msg = 'Please enter at least ' + field.minLength + ' characters';
        else msg = field.title || 'Please fill out this field correctly';

        let errorEl = field.parentElement.querySelector('.field-error');
        if (!errorEl) {
          errorEl = document.createElement('span');
          errorEl.className = 'field-error';
          field.parentElement.appendChild(errorEl);
        }
        errorEl.textContent = msg;
      });

      field.addEventListener('input', function() {
        field.classList.remove('input-error');
        const errorEl = field.parentElement.querySelector('.field-error');
        if (errorEl) errorEl.remove();
      });

      field.addEventListener('change', function() {
        field.classList.remove('input-error');
        const errorEl = field.parentElement.querySelector('.field-error');
        if (errorEl) errorEl.remove();
      });
    });

    form.addEventListener('submit', function(e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.querySelectorAll('input, select, textarea').forEach(function(field) {
          if (!field.checkValidity()) {
            field.dispatchEvent(new Event('invalid'));
          }
        });
        return;
      }

      const btn = form.querySelector('.form-submit, [type="submit"]');
      const formData = new FormData(form);

      if (btn) {
        btn.textContent = 'Sending...';
        btn.disabled = true;
      }

      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(formData).toString()
      })
      .then(function() {
        window.location.href = '/thank-you.html';
      })
      .catch(function() {
        if (btn) {
          btn.textContent = 'Something went wrong. Please call us at 877-345-9239';
          btn.style.background = '#cc0000';
          setTimeout(function() {
            btn.textContent = 'Submit Request';
            btn.style.background = '';
            btn.disabled = false;
          }, 4000);
        }
      });
    });

  });

  /* ---------- FAQ Accordion ---------- */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    if (!btn || !answer) return;

    btn.addEventListener('click', function () {
      const isOpen = btn.classList.contains('active');
      faqItems.forEach(function (i) {
        i.querySelector('.faq-q').classList.remove('active');
        const a = i.querySelector('.faq-a');
        if (a) a.style.maxHeight = '0';
      });
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
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

/* ---------- Active Nav Link ---------- */
var currentPath = window.location.pathname.replace(/\/$/, '');
var currentHash = window.location.hash;

document.querySelectorAll('.nav-links a').forEach(function (link) {
  link.classList.remove('active');

  var rawHref = link.getAttribute('href') || '';
  if (!rawHref || rawHref === '#') return;

  var linkUrl = new URL(link.href, window.location.href);
  var linkPath = linkUrl.pathname.replace(/\/$/, '');
  var linkHash = linkUrl.hash;

  if (currentHash) {
    if (linkPath === currentPath && linkHash === currentHash) {
      link.classList.add('active');
    }
    return;
  }

  if (!linkHash && linkPath === currentPath) {
    link.classList.add('active');
  }
});

});
