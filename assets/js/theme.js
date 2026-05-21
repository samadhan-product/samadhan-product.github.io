/**
 * Site-wide light/dark theme system.
 * Reads localStorage key 'site-theme', falls back to prefers-color-scheme.
 * Sets html[data-theme="dark"|"light"] before first paint to prevent FOUC.
 */
(function () {
  'use strict';

  var KEY = 'site-theme';
  var html = document.documentElement;

  function getPreferred() {
    try {
      var saved = localStorage.getItem(KEY);
      if (saved === 'dark' || saved === 'light') return saved;
    } catch (e) {}
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function apply(theme) {
    html.setAttribute('data-theme', theme);
    try { localStorage.setItem(KEY, theme); } catch (e) {}
  }

  function syncButtons() {
    var theme = html.getAttribute('data-theme') || 'dark';
    var isDark = theme === 'dark';
    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      var icon = btn.querySelector('.theme-toggle-icon');
      if (icon) icon.textContent = isDark ? '☀' : '◑'; // ☀ or ◑
      btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('title', isDark ? 'Light mode' : 'Dark mode');
    });
  }

  /* Apply immediately — before CSS renders — to prevent flash */
  apply(getPreferred());

  document.addEventListener('DOMContentLoaded', function () {
    syncButtons();

    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var current = html.getAttribute('data-theme') || 'dark';
        apply(current === 'dark' ? 'light' : 'dark');
        syncButtons();
      });
    });
  });
})();
