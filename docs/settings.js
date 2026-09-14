/**
 * settings.js
 * Gulistan Reader Settings Controller
 * Handles typography (Mehr Nastaliq, Noto Nastaliq, Noto Naskh), text scaling,
 * themes (Light, Sepia, Dark), and localStorage persistence.
 */

(function() {
  const STORAGE_KEY = 'gulistan_reader_settings';

  const DEFAULTS = {
    urduFont: 'mehr',
    persianFont: 'amiri',
    textSize: 'md',
    theme: 'emerald'
  };

  function loadSettings() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      return stored ? Object.assign({}, DEFAULTS, JSON.parse(stored)) : Object.assign({}, DEFAULTS);
    } catch (e) {
      return Object.assign({}, DEFAULTS);
    }
  }

  function saveSettings(settings) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
    } catch (e) {}
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
    // Urdu Font
    document.querySelectorAll('[data-setting="urdu-font"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.urduFont);
    });

    // Persian Font
    document.querySelectorAll('[data-setting="persian-font"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.persianFont);
    });

    // Text Size
    document.querySelectorAll('[data-setting="text-size"] .opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.textSize);
    });

    // Theme
    document.querySelectorAll('[data-setting="theme"] .theme-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.val === settings.theme);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    let settings = loadSettings();
    applySettings(settings);

    const overlay = document.getElementById('settingsOverlay');
    const toggleBtn = document.getElementById('settingsToggle');
    const closeBtn = document.getElementById('settingsClose');
    const resetBtn = document.getElementById('settingsReset');

    function openSettings() {
      if (overlay) {
        overlay.classList.add('open');
        overlay.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeSettings() {
      if (overlay) {
        overlay.classList.remove('open');
        overlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    }

    if (toggleBtn) {
      toggleBtn.addEventListener('click', openSettings);
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', closeSettings);
    }

    if (overlay) {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
          closeSettings();
        }
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay && overlay.classList.contains('open')) {
        closeSettings();
      }
    });

    // Option Button Clicks
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

      saveSettings(settings);
      applySettings(settings);
    });

    // Reset Defaults
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        settings = Object.assign({}, DEFAULTS);
        saveSettings(settings);
        applySettings(settings);
      });
    }

    // Cover Lightbox Modal
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

    if (viewCoverBtn) {
      viewCoverBtn.addEventListener('click', openLightbox);
    }
    if (closeLightboxBtn) {
      closeLightboxBtn.addEventListener('click', closeLightbox);
    }
    if (lightbox) {
      lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
          closeLightbox();
        }
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox && lightbox.classList.contains('open')) {
        closeLightbox();
      }
    });

    // Global English Study Notes Accordion Toggle (Expand / Collapse All English Notes)
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
