/**
 * Blog UX — vanilla JS, progressive enhancement
 */
(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function smoothScrollTo(top) {
    if (prefersReducedMotion) {
      window.scrollTo(0, top);
    } else {
      window.scrollTo({ top: top, behavior: "smooth" });
    }
  }

  /* Reading progress */
  function initProgress() {
    var article = document.querySelector(".article-content");
    if (!article) return;

    var bar = document.createElement("div");
    bar.className = "scroll-progress";
    bar.setAttribute("role", "progressbar");
    bar.setAttribute("aria-valuemin", "0");
    bar.setAttribute("aria-valuemax", "100");
    bar.setAttribute("aria-valuenow", "0");
    document.body.appendChild(bar);

    function update() {
      var rect = article.getBoundingClientRect();
      var start = window.scrollY + rect.top;
      var height = article.offsetHeight;
      var view = window.innerHeight;
      var scrolled = window.scrollY - start + view * 0.2;
      var pct = Math.min(100, Math.max(0, (scrolled / height) * 100));
      bar.style.width = pct + "%";
      bar.setAttribute("aria-valuenow", String(Math.round(pct)));
    }

    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  /* TOC active state */
  function initToc() {
    var links = document.querySelectorAll(".article-toc-link");
    if (!links.length) return;

    var sections = [];
    links.forEach(function (link) {
      var id = link.getAttribute("href");
      if (!id || id.charAt(0) !== "#") return;
      var el = document.querySelector(id);
      if (el) sections.push({ el: el, link: link });
    });
    if (!sections.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            links.forEach(function (l) {
              l.classList.remove("is-active");
            });
            var match = sections.find(function (s) {
              return s.el === entry.target;
            });
            if (match) match.link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-20% 0px -65% 0px", threshold: 0 }
    );

    sections.forEach(function (s) {
      observer.observe(s.el);
    });
  }

  /* Reveal on scroll */
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;

    if (prefersReducedMotion) {
      els.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );

    els.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* Relevance bar animation */
  function initRelevanceBars() {
    var rows = document.querySelectorAll(".relevance-row");
    if (!rows.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
          }
        });
      },
      { threshold: 0.3 }
    );

    rows.forEach(function (row) {
      observer.observe(row);
      if (prefersReducedMotion) row.classList.add("is-visible");
    });
  }

  /* Copy link on h2 */
  function initCopyLinks() {
    document.querySelectorAll(".article-section[id] h2").forEach(function (h2) {
      var section = h2.closest(".article-section");
      if (!section || !section.id) return;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "copy-link-btn";
      btn.setAttribute("aria-label", "Copy link to section");
      btn.textContent = "#";
      btn.addEventListener("click", function () {
        var url = window.location.href.split("#")[0] + "#" + section.id;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(
            function () {
              btn.classList.add("is-copied");
              setTimeout(function () {
                btn.classList.remove("is-copied");
              }, 2000);
            },
            function () {}
          );
        }
      });
      h2.appendChild(btn);
    });
  }

  /* Back to top */
  function initBackToTop() {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = "↑";
    document.body.appendChild(btn);

    window.addEventListener(
      "scroll",
      function () {
        if (window.scrollY > 400) {
          btn.classList.add("is-visible");
        } else {
          btn.classList.remove("is-visible");
        }
      },
      { passive: true }
    );

    btn.addEventListener("click", function () {
      smoothScrollTo(0);
    });
  }

  /* Tab panels — syllabus tabs and chapter tabs */
  function initTabs() {
    document.querySelectorAll("[role='tablist']").forEach(function (tablist) {
      var tabs = Array.from(tablist.querySelectorAll("[role='tab']"));
      if (!tabs.length) return;

      function activate(tab) {
        tabs.forEach(function (t) {
          var panelId = t.getAttribute("aria-controls");
          var panel = panelId ? document.getElementById(panelId) : null;
          var isSelected = t === tab;
          t.setAttribute("aria-selected", String(isSelected));
          if (panel) {
            if (isSelected) {
              panel.classList.add("is-active");
            } else {
              panel.classList.remove("is-active");
            }
          }
        });
      }

      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          activate(tab);
        });

        tab.addEventListener("keydown", function (e) {
          var idx = tabs.indexOf(tab);
          if (e.key === "ArrowRight") {
            e.preventDefault();
            var next = tabs[(idx + 1) % tabs.length];
            next.focus();
            activate(next);
          } else if (e.key === "ArrowLeft") {
            e.preventDefault();
            var prev = tabs[(idx - 1 + tabs.length) % tabs.length];
            prev.focus();
            activate(prev);
          } else if (e.key === "Home") {
            e.preventDefault();
            tabs[0].focus();
            activate(tabs[0]);
          } else if (e.key === "End") {
            e.preventDefault();
            tabs[tabs.length - 1].focus();
            activate(tabs[tabs.length - 1]);
          }
        });
      });

      /* Ensure initial state is consistent */
      var selected = tabs.find(function (t) {
        return t.getAttribute("aria-selected") === "true";
      });
      if (selected) {
        activate(selected);
      } else if (tabs[0]) {
        activate(tabs[0]);
      }
    });
  }

  function init() {
    document.body.setAttribute("data-js", "1");
    initProgress();
    initToc();
    initReveal();
    initRelevanceBars();
    initCopyLinks();
    initBackToTop();
    initTabs();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
