import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { profile } from "../data/profile";
import { NAV_LINKS } from "../data/navLinks";
import { useTheme } from "../hooks/useTheme";

const NAV_LINK_CLASS =
  "link-reveal shrink-0 whitespace-nowrap font-mono text-[11px] uppercase tracking-[0.12em]";

export default function Navigation() {
  const [time, setTime] = useState("");
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const { isDark, toggle } = useTheme();

  useEffect(() => {
    const fmt = () => {
      const parts = new Intl.DateTimeFormat("en-IN", {
        timeZone: "Asia/Kolkata",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
      }).format(new Date());
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

  const scrollTo = (id) => (e) => {
    e.preventDefault();
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    setOpen(false);
  };

  const navBg = scrolled
    ? isDark
      ? "rgba(5,5,5,0.55)"
      : "rgba(247,240,227,0.92)"
    : "transparent";
  const navBorder = scrolled
    ? isDark
      ? "1px solid rgba(255,255,255,0.08)"
      : "1px solid rgba(101,87,65,0.15)"
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

  const renderLink = (item, className, testIdPrefix) => {
    const cls = `${NAV_LINK_CLASS} ${linkCls} ${className}`;
    const content = item.blogDot ? (
      <span className="inline-flex items-center gap-2">
        <span
          className="inline-block h-1.5 w-1.5 shrink-0 rounded-full bg-emerald-400 blink"
          aria-hidden="true"
        />
        {item.label}
      </span>
    ) : (
      item.label
    );

    if (item.scrollId) {
      return (
        <a
          key={item.key}
          href={item.href}
          onClick={scrollTo(item.scrollId)}
          className={cls}
          data-testid={`${testIdPrefix}-${item.key}`}
          data-cursor="jump"
        >
          {content}
        </a>
      );
    }

    return (
      <a
        key={item.key}
        href={item.href}
        className={cls}
        data-testid={`${testIdPrefix}-${item.key}`}
      >
        {content}
      </a>
    );
  };

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
        <div className="site-nav-inner mx-auto grid max-w-7xl grid-cols-[auto_1fr_auto] items-center gap-3 px-6 py-4 md:gap-4 md:px-12 md:py-5">
          <a
            href="#top"
            onClick={scrollTo("top")}
            className="group flex shrink-0 items-center gap-2"
            data-testid="nav-logo"
            data-cursor="home"
          >
            <span
              className={`relative inline-flex h-7 w-7 items-center justify-center border ${smBorderCls} ${smHoverCls} font-mono text-[11px] transition-colors duration-500`}
            >
              SM
            </span>
            <span
              className={`hidden whitespace-nowrap font-mono text-[11px] uppercase tracking-[0.12em] sm:inline ${logoTextCls}`}
            >
              / {profile.name.split(" ")[0]}
            </span>
          </a>

          <nav className="hidden min-w-0 items-center justify-center gap-3 min-[1100px]:flex min-[1100px]:gap-4 lg:gap-5">
            {NAV_LINKS.map((item) => renderLink(item, "", "nav-link"))}
          </nav>

          <div className="flex shrink-0 items-center justify-end gap-3">
            <div
              className={`hidden items-center whitespace-nowrap font-mono text-[11px] uppercase tracking-[0.12em] ${clockCls} min-[768px]:flex`}
            >
              <span data-testid="nav-clock">{time}</span>
            </div>
            <button
              type="button"
              onClick={toggle}
              className={`hidden h-8 w-8 shrink-0 items-center justify-center border font-mono text-[13px] transition-colors duration-300 min-[768px]:inline-flex ${toggleCls}`}
              aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
              data-testid="theme-toggle"
            >
              {isDark ? "☀" : "◑"}
            </button>
            <button
              type="button"
              onClick={() => setOpen((v) => !v)}
              className="inline-flex min-[1100px]:hidden"
              aria-label="Toggle menu"
              aria-expanded={open}
              data-testid="nav-toggle"
            >
              <div
                className={`flex h-9 w-9 flex-col items-center justify-center gap-1.5 border ${hamburgerBorderCls}`}
              >
                <span
                  className={`h-px w-4 ${hamburgerBarCls} transition-transform duration-500 ${open ? "translate-y-[3px] rotate-45" : ""}`}
                />
                <span
                  className={`h-px w-4 ${hamburgerBarCls} transition-transform duration-500 ${open ? "-translate-y-[3px] -rotate-45" : ""}`}
                />
              </div>
            </button>
          </div>
        </div>
      </motion.header>

      <AnimatePresence>
        {open ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="fixed inset-0 z-40 min-[1100px]:hidden"
            style={{ background: "var(--bg)", color: "var(--fg)" }}
            data-testid="nav-mobile-sheet"
          >
            <nav className="flex h-full flex-col items-start justify-center gap-5 px-8">
              {NAV_LINKS.map((item, i) => (
                <motion.div
                  key={item.key}
                  initial={{ y: 40, opacity: 0 }}
                  animate={{ y: 0, opacity: 1 }}
                  transition={{
                    duration: 0.6,
                    ease: [0.16, 1, 0.3, 1],
                    delay: 0.08 + i * 0.05
                  }}
                >
                  {item.scrollId ? (
                    <a
                      href={item.href}
                      onClick={scrollTo(item.scrollId)}
                      className="block whitespace-nowrap font-display text-3xl tracking-tight sm:text-4xl"
                      style={{ color: "var(--fg)" }}
                      data-testid={`nav-mobile-link-${item.key}`}
                    >
                      {item.blogDot ? (
                        <span className="inline-flex items-center gap-3">
                          <span
                            className="inline-block h-2 w-2 rounded-full bg-emerald-400"
                            aria-hidden="true"
                          />
                          {item.label}
                        </span>
                      ) : (
                        item.label
                      )}
                    </a>
                  ) : (
                    <a
                      href={item.href}
                      onClick={() => setOpen(false)}
                      className="block whitespace-nowrap font-display text-3xl tracking-tight sm:text-4xl"
                      style={{ color: "var(--fg)" }}
                      data-testid={`nav-mobile-link-${item.key}`}
                    >
                      {item.blogDot ? (
                        <span className="inline-flex items-center gap-3">
                          <span
                            className="inline-block h-2 w-2 rounded-full bg-emerald-400"
                            aria-hidden="true"
                          />
                          {item.label}
                        </span>
                      ) : (
                        item.label
                      )}
                    </a>
                  )}
                </motion.div>
              ))}
              <motion.button
                type="button"
                onClick={toggle}
                initial={{ y: 40, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{
                  duration: 0.6,
                  ease: [0.16, 1, 0.3, 1],
                  delay: 0.08 + NAV_LINKS.length * 0.05
                }}
                className={`mt-4 font-mono text-[11px] uppercase tracking-[0.12em] ${clockCls}`}
                aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
              >
                {isDark ? "☀ Light mode" : "◑ Dark mode"}
              </motion.button>
              <div
                className={`font-mono text-[11px] uppercase tracking-[0.12em] ${clockCls}`}
              >
                {time}
              </div>
            </nav>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </>
  );
}
