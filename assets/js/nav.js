/**
 * Site nav — IST clock, mobile menu, active link state.
 */
(function () {
  "use strict";

  var MENU_LINKS = [
    { href: "/", label: "Home", nav: "home" },
    { href: "/case-studies/", label: "Case Studies", nav: "case-studies" },
    { href: "/insights/", label: "Insights", nav: "insights" },
    { href: "/work-with-me/", label: "Work With Me", nav: "work-with-me" },
    { href: "/portfolio/", label: "Portfolio", nav: "portfolio" },
    { href: "/blog/", label: "Blog", nav: "blog" }
  ];

  function currentNavKey() {
    var page = document.body.getAttribute("data-page");
    if (page) return page;
    var path = window.location.pathname.replace(/\/$/, "") || "/";
    if (path === "/" || path === "/index.html") return "home";
    if (path.indexOf("/portfolio") === 0) return "portfolio";
    if (path.indexOf("/blog") === 0) return "blog";
    if (path.indexOf("/case-studies") === 0) return "case-studies";
    if (path.indexOf("/insights") === 0) return "insights";
    if (path.indexOf("/work-with-me") === 0) return "work-with-me";
    if (path.indexOf("/services") === 0) return "services";
    if (path.indexOf("/ai-product") === 0 || path.indexOf("/healthcare") === 0 || path.indexOf("/product-leadership") === 0 || path.indexOf("/ai-agents") === 0) return "consulting";
    if (path.indexOf("/speaking") === 0) return "speaking-workshops";
    return "";
  }

  function markActive() {
    var key = currentNavKey();
    if (!key) return;
    document.querySelectorAll(".site-menu-link[data-nav]").forEach(function (a) {
      if (a.getAttribute("data-nav") === key) {
        a.classList.add("is-active");
        a.setAttribute("aria-current", "page");
      }
    });
  }

  function startClock() {
    var nodes = document.querySelectorAll("[data-nav-clock]");
    if (!nodes.length) return;
    function tick() {
      var parts = new Intl.DateTimeFormat("en-IN", {
        timeZone: "Asia/Kolkata",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
      }).format(new Date());
      nodes.forEach(function (el) {
        el.textContent = parts + " IST";
      });
    }
    tick();
    setInterval(tick, 1000);
  }

  function bindMobile() {
    var toggle = document.querySelector("[data-nav-toggle]");
    var panel = document.querySelector("[data-nav-mobile]");
    if (!toggle || !panel) return;

    function setOpen(open) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      panel.hidden = !open;
      document.documentElement.classList.toggle("site-nav-open", open);
    }

    toggle.addEventListener("click", function () {
      setOpen(panel.hidden);
    });

    panel.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        setOpen(false);
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    markActive();
    startClock();
    bindMobile();
  });
})();
