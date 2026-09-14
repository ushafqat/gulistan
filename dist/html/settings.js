/**
 * settings.js
 * Gulistan Reader Controller
 * - Typography (Mehr Nastaliq, Noto Nastaliq, Noto Naskh), text scaling, themes
 * - Table of Contents (ToC) modal drawer with Sections & Page Jump grid
 * - Reading progress tracker (iOS Safari compatible localStorage + IntersectionObserver)
 * - Resume Reading quick jump (in ToC and floating toast)
 * - Cover art lightbox & Study notes global toggle
 */

(function() {
  const SETTINGS_KEY = 'gulistan_reader_settings';
  const PROGRESS_KEY = 'gulistan_reading_progress';

  const DEFAULTS = {
    urduFont: 'mehr',
    persianFont: 'amiri',
    textSize: 'md',
    theme: 'emerald'
  };

  function toUrduDigits(n) {
    const digits = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'};
    return String(n).replace(/[0-9]/g, d => digits[d] || d);
  }

  // Safe localStorage helpers (Guards against iOS Safari private mode quota restrictions)
  function getStorage(key) {
    try {
      const val = localStorage.getItem(key);
      return val ? JSON.parse(val) : null;
    } catch (e) {
      return null;
    }
  }

  function setStorage(key, val) {
    try {
      localStorage.setItem(key, JSON.stringify(val));
    } catch (e) {}
  }

  function loadSettings() {
    const stored = getStorage(SETTINGS_KEY);
    return stored ? Object.assign({}, DEFAULTS, stored) : Object.assign({}, DEFAULTS);
  }

  function applySettings(settings) {
    const targets = [document.documentElement, document.body];
    targets.forEach(el => {
      if (!el) return;
      el.setAttribute('data-font-urdu', settings.urduFont);
      el.setAttribute('data-font-persian', settings.persianFont);
      el.setAttribute('data-size', settings.textSize);
      el.setAttribute('data-theme', settings.theme);
    });
    updateActiveButtons(settings);
  }

  function updateActiveButtons(settings) {
    document.querySelectorAll('[data-setting="urdu-font"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.urduFont);
    });
    document.querySelectorAll('[data-setting="persian-font"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.persianFont);
    });
    document.querySelectorAll('[data-setting="text-size"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.textSize);
    });
    document.querySelectorAll('[data-setting="theme"] .theme-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.theme);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    let settings = loadSettings();
    applySettings(settings);

    // ============================================================
    // 1. SETTINGS DRAWER
    // ============================================================
    const settingsOverlay = document.getElementById('settingsOverlay');
    const settingsToggle = document.getElementById('settingsToggle');
    const settingsClose = document.getElementById('settingsClose');
    const resetBtn = document.getElementById('settingsReset');

    function openSettings() {
      if (settingsOverlay) {
        settingsOverlay.classList.add('open');
        settingsOverlay.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeSettings() {
      if (settingsOverlay) {
        settingsOverlay.classList.remove('open');
        settingsOverlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    }

    if (settingsToggle) settingsToggle.addEventListener('click', openSettings);
    if (settingsClose) settingsClose.addEventListener('click', closeSettings);
    if (settingsOverlay) {
      settingsOverlay.addEventListener('click', (e) => {
        if (e.target === settingsOverlay) closeSettings();
      });
    }

    // Option Buttons Inside Settings
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('button[data-val]');
      if (!btn) return;

      const container = btn.closest('[data-setting]');
      if (!container) return;

      const settingType = container.dataset.setting;
      const val = btn.dataset.val;

      if (settingType === 'urdu-font') {
        settings.urduFont = val;
      } else if (settingType === 'persian-font') {
        settings.persianFont = val;
      } else if (settingType === 'text-size') {
        settings.textSize = val;
      } else if (settingType === 'theme') {
        settings.theme = val;
      }

      setStorage(SETTINGS_KEY, settings);
      applySettings(settings);
    });

    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        settings = Object.assign({}, DEFAULTS);
        setStorage(SETTINGS_KEY, settings);
        applySettings(settings);
      });
    }

    // ============================================================
    // 2. TABLE OF CONTENTS (ToC) DRAWER
    // ============================================================
    const tocOverlay = document.getElementById('tocOverlay');
    const tocToggle = document.getElementById('tocToggle');
    const tocClose = document.getElementById('tocClose');

    function openToC() {
      if (tocOverlay) {
        tocOverlay.classList.add('open');
        tocOverlay.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        refreshToCBanner();
      }
    }

    function closeToC() {
      if (tocOverlay) {
        tocOverlay.classList.remove('open');
        tocOverlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    }

    if (tocToggle) tocToggle.addEventListener('click', openToC);
    if (tocClose) tocClose.addEventListener('click', closeToC);
    if (tocOverlay) {
      tocOverlay.addEventListener('click', (e) => {
        if (e.target === tocOverlay) closeToC();
      });
    }

    // ToC Tabs (Sections vs Pages)
    document.querySelectorAll('.toc-tab-btn').forEach(tabBtn => {
      tabBtn.addEventListener('click', () => {
        const targetTab = tabBtn.dataset.tocTab;
        document.querySelectorAll('.toc-tab-btn').forEach(b => b.classList.remove('active'));
        tabBtn.classList.add('active');

        const secContent = document.getElementById('tocTabSections');
        const pagesContent = document.getElementById('tocTabPages');
        if (secContent && pagesContent) {
          secContent.classList.toggle('active', targetTab === 'sections');
          pagesContent.classList.toggle('active', targetTab === 'pages');
        }
      });
    });

    // Smooth scroll for ToC navigation links
    document.querySelectorAll('.toc-section-link, .page-chip').forEach(link => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          e.preventDefault();
          closeToC();
          const targetEl = document.querySelector(href);
          if (targetEl) {
            targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            history.replaceState(null, '', href);
          }
        }
      });
    });

    // Keyboard ESC handles both modals
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (settingsOverlay && settingsOverlay.classList.contains('open')) closeSettings();
        if (tocOverlay && tocOverlay.classList.contains('open')) closeToC();
        if (lightbox && lightbox.classList.contains('open')) closeLightbox();
      }
    });

    // ============================================================
    // 3. READING PROGRESS & RESUME (iOS Safari Resilient)
    // ============================================================
    const tocResumeBanner = document.getElementById('tocResumeBanner');
    const tocResumeTitle = document.getElementById('tocResumeTitle');
    const tocResumeBtn = document.getElementById('tocResumeBtn');

    const resumeToast = document.getElementById('resumeToast');
    const resumeToastText = document.getElementById('resumeToastText');
    const resumeToastBtn = document.getElementById('resumeToastBtn');
    const resumeToastDismiss = document.getElementById('resumeToastDismiss');

    function refreshToCBanner() {
      const saved = getStorage(PROGRESS_KEY);
      if (saved && saved.pageId && document.getElementById(saved.pageId)) {
        if (tocResumeBanner && tocResumeTitle) {
          tocResumeTitle.textContent = saved.pageTitle || ('صفحہ ' + saved.bookPage);
          tocResumeBanner.style.display = 'flex';
        }
      } else if (tocResumeBanner) {
        tocResumeBanner.style.display = 'none';
      }
    }

    function jumpToSavedPage() {
      const saved = getStorage(PROGRESS_KEY);
      if (saved && saved.pageId) {
        const el = document.getElementById(saved.pageId);
        if (el) {
          closeToC();
          if (resumeToast) resumeToast.classList.remove('show');
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }

    if (tocResumeBtn) tocResumeBtn.addEventListener('click', jumpToSavedPage);
    if (resumeToastBtn) resumeToastBtn.addEventListener('click', jumpToSavedPage);
    if (resumeToastDismiss) {
      resumeToastDismiss.addEventListener('click', () => {
        if (resumeToast) resumeToast.classList.remove('show');
      });
    }

    // Track active page via IntersectionObserver
    const trackedLeaves = document.querySelectorAll('.book-page-leaf, .foreword-article');
    if (trackedLeaves.length && 'IntersectionObserver' in window) {
      const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && entry.intersectionRatio >= 0.25) {
            const id = entry.target.id;
            let rawNum = id.replace('page_', '');
            let pageNum = toUrduDigits(rawNum);
            let title = 'صفحہ ' + pageNum;
            if (id === 'pesh_lafz') {
              pageNum = '۱';
              title = 'پیش لفظ (صفحہ ۱ تا ۴)';
            }
            const progress = {
              pageId: id,
              bookPage: pageNum,
              pageTitle: title,
              updatedAt: Date.now()
            };
            setStorage(PROGRESS_KEY, progress);
            refreshToCBanner();
          }
        });
      }, { threshold: [0.25, 0.5] });

      trackedLeaves.forEach(leaf => progressObserver.observe(leaf));
    }

    // Initial Resume Toast on Page Load (if user opens site at top)
    const initialProgress = getStorage(PROGRESS_KEY);
    if (initialProgress && initialProgress.pageId && document.getElementById(initialProgress.pageId)) {
      refreshToCBanner();
      if (window.scrollY < 250) {
        setTimeout(() => {
          if (resumeToast && resumeToastText && window.scrollY < 300) {
            resumeToastText.textContent = 'آخری مطالعہ: ' + (initialProgress.pageTitle || ('صفحہ ' + initialProgress.bookPage));
            resumeToast.classList.add('show');
            resumeToast.setAttribute('aria-hidden', 'false');

            // Auto-hide after 8 seconds or on substantial user scroll
            const dismissTimer = setTimeout(() => {
              resumeToast.classList.remove('show');
            }, 8000);

            function onUserScroll() {
              if (window.scrollY > 400) {
                resumeToast.classList.remove('show');
                clearTimeout(dismissTimer);
                window.removeEventListener('scroll', onUserScroll);
              }
            }
            window.addEventListener('scroll', onUserScroll, { passive: true });
          }
        }, 1200);
      }
    }

    // ============================================================
    // 4. COVER LIGHTBOX
    // ============================================================
    const viewCoverBtn = document.getElementById('viewCoverModalBtn');
    const lightbox = document.getElementById('coverLightbox');
    const closeLightboxBtn = document.getElementById('closeLightbox');

    function openLightbox() {
      if (lightbox) {
        lightbox.classList.add('open');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeLightbox() {
      if (lightbox) {
        lightbox.classList.remove('open');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    }

    if (viewCoverBtn) viewCoverBtn.addEventListener('click', openLightbox);
    if (closeLightboxBtn) closeLightboxBtn.addEventListener('click', closeLightbox);
    if (lightbox) {
      lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeLightbox();
      });
    }

    // ============================================================
    // 5. GLOBAL ENGLISH STUDY NOTES TOGGLE (Study Edition)
    // ============================================================
    const toggleAllNotesBtn = document.getElementById('toggleAllNotesBtn');
    const toggleAllNotesText = document.getElementById('toggleAllNotesText');
    if (toggleAllNotesBtn) {
      let allExpanded = false;
      toggleAllNotesBtn.addEventListener('click', () => {
        allExpanded = !allExpanded;
        const detailsList = document.querySelectorAll('details.en-study-collapse');
        detailsList.forEach(d => {
          d.open = allExpanded;
        });
        if (toggleAllNotesText) {
          toggleAllNotesText.textContent = allExpanded 
            ? 'انگریزی نوٹس و ترجمہ چھپائیں (Hide English Notes & Translation)' 
            : 'انگریزی نوٹس و ترجمہ کھولیں (Show English Notes & Translation)';
        }
      });
    }
  });
})();
