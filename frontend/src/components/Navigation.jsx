import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { profile } from "../data/profile";
import { useTheme } from "../hooks/useTheme";

const SECTION_LINKS = [
  { id: "work", label: "Work" },
  { id: "experience", label: "Experience" },
  { id: "projects", label: "Projects" },
  { id: "about", label: "About" },
  { id: "contact", label: "Contact" }
];

const SITE_LINKS = [
  { href: "/portfolio/", label: "Portfolio" },
  { href: "/blog/", label: "Blog" }
];

export default function Navigation() {
  const [time, setTime] = useState("");
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const { isDark, toggle } = useTheme();

  useEffect(() => {
    const fmt = () => {
      const d = new Date();
      const parts = new Intl.DateTimeFormat("en-IN", {
        timeZone: "Asia/Kolkata",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
      }).format(d);
      setTime(`${parts} IST`);
    };
    fmt();
    const int = setInterval(fmt, 1000);
    const onScroll = () => setScrolled(window.scrollY > 10);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => {
      clearInterval(int);
      window.removeEventListener("scroll", onScroll);
    };
  }, []);

  const go = (id) => (e) => {
    e.preventDefault();
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    setOpen(false);
  };

  const navBg = scrolled
    ? isDark ? "rgba(5,5,5,0.55)" : "rgba(247,240,227,0.92)"
    : "transparent";
  const navBorder = scrolled
    ? isDark ? "1px solid rgba(255,255,255,0.08)" : "1px solid rgba(101,87,65,0.15)"
    : "1px solid transparent";

  const linkCls = isDark
    ? "text-white/60 hover:text-white"
    : "text-stone-500 hover:text-stone-900";
  const clockCls = isDark ? "text-white/50" : "text-stone-400";
  const smBorderCls = isDark ? "border-white/30" : "border-stone-400/60";
  const smHoverCls = isDark
    ? "group-hover:bg-white group-hover:text-black"
    : "group-hover:bg-stone-800 group-hover:text-white";
  const logoTextCls = isDark ? "text-white/70" : "text-stone-500";
  const hamburgerBorderCls = isDark ? "border-white/20" : "border-stone-400/40";
  const hamburgerBarCls = isDark ? "bg-white" : "bg-stone-700";
  const toggleCls = isDark
    ? "border-white/20 text-white/60 hover:text-white hover:border-white/40"
    : "border-stone-400/40 text-stone-500 hover:text-stone-800 hover:border-stone-500";

  return (
    <>
      <motion.header
        initial={{ y: -30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.2 }}
        className={`fixed inset-x-0 top-0 z-50 transition-all duration-500 ${scrolled ? "backdrop-blur-md" : ""}`}
        style={{ background: navBg, borderBottom: navBorder }}
        data-testid="top-nav"
      >
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5 md:px-12">
          {/* Logo */}
          <a
            href="#top"
            onClick={go("top")}
            className="group flex items-center gap-2"
            data-testid="nav-logo"
            data-cursor="home"
          >
            <span className={`relative inline-flex h-7 w-7 items-center justify-center border ${smBorderCls} ${smHoverCls} font-mono text-[11px] transition-colors duration-500`}>
              SM
            </span>
            <span className={`font-mono text-[11px] uppercase tracking-[0.22em] ${logoTextCls}`}>
              / {profile.name.split(" ")[0]}
            </span>
          </a>

          {/* Desktop links */}
          <nav className="hidden items-center gap-8 md:flex">
            {SECTION_LINKS.map((l) => (
              <a
                key={l.id}
                href={`#${l.id}`}
                onClick={go(l.id)}
                className={`link-reveal font-mono text-[11px] uppercase tracking-[0.22em] ${linkCls}`}
                data-testid={`nav-link-${l.id}`}
                data-cursor="jump"
              >
                {l.label}
              </a>
            ))}
            {SITE_LINKS.map((l) => (
              <a
                key={l.href}
                href={l.href}
                className={`link-reveal font-mono text-[11px] uppercase tracking-[0.22em] ${linkCls}`}
                data-testid={`nav-link-${l.href.replace(/\//g, "")}`}
              >
                {l.label}
              </a>
            ))}
          </nav>

          {/* Right meta + toggles */}
          <div className="flex items-center gap-4">
            <div className={`hidden items-center gap-3 font-mono text-[11px] uppercase tracking-[0.22em] ${clockCls} md:flex`}>
              <span className="inline-block h-1.5 w-1.5 rounded-full bg-emerald-400 blink" />
              <span data-testid="nav-clock">{time}</span>
            </div>
            {/* Theme toggle — desktop */}
            <button
              type="button"
              onClick={toggle}
              className={`hidden md:flex h-8 w-8 items-center justify-center border font-mono text-[13px] transition-colors duration-300 ${toggleCls}`}
              aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
              data-testid="theme-toggle"
            >
              {isDark ? "☀" : "◑"}
            </button>
            {/* Hamburger — mobile */}
            <button
              type="button"
              onClick={() => setOpen((v) => !v)}
              className="md:hidden"
              aria-label="Toggle menu"
              data-testid="nav-toggle"
            >
              <div className={`flex h-9 w-9 flex-col items-center justify-center gap-1.5 border ${hamburgerBorderCls}`}>
                <span className={`h-px w-4 ${hamburgerBarCls} transition-transform duration-500 ${open ? "translate-y-[3px] rotate-45" : ""}`} />
                <span className={`h-px w-4 ${hamburgerBarCls} transition-transform duration-500 ${open ? "-translate-y-[3px] -rotate-45" : ""}`} />
              </div>
            </button>
          </div>
        </div>
      </motion.header>

      {/* Mobile sheet */}
      <AnimatePresence>
        {open ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="fixed inset-0 z-40 md:hidden"
            style={{ background: "var(--bg)", color: "var(--fg)" }}
            data-testid="nav-mobile-sheet"
          >
            <nav className="flex h-full flex-col items-start justify-center gap-6 px-6">
              {SECTION_LINKS.map((l, i) => (
                <motion.a
                  key={l.id}
                  href={`#${l.id}`}
                  onClick={go(l.id)}
                  initial={{ y: 40, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1], delay: 0.1 + i * 0.07 }}
                  className="font-display text-4xl tracking-tight"
                  style={{ color: "var(--fg)" }}
                  data-testid={`nav-mobile-link-${l.id}`}
                >
                  {l.label}
                </motion.a>
              ))}
              {SITE_LINKS.map((l, i) => (
                <motion.a
                  key={l.href}
                  href={l.href}
                  initial={{ y: 40, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1], delay: 0.1 + (SECTION_LINKS.length + i) * 0.07 }}
                  className="font-display text-4xl tracking-tight"
                  style={{ color: "var(--fg)" }}
                  data-testid={`nav-mobile-link-${l.href.replace(/\//g, "")}`}
                >
                  {l.label}
                </motion.a>
              ))}
              {/* Theme toggle — mobile */}
              <motion.button
                type="button"
                onClick={toggle}
                initial={{ y: 40, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1], delay: 0.1 + (SECTION_LINKS.length + SITE_LINKS.length) * 0.07 }}
                className={`font-mono text-[11px] uppercase tracking-[0.22em] ${clockCls}`}
                aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
              >
                {isDark ? "☀ Light mode" : "◑ Dark mode"}
              </motion.button>
              <div className={`mt-4 font-mono text-[11px] uppercase tracking-[0.22em] ${clockCls}`}>
                {time}
              </div>
            </nav>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </>
  );
}
