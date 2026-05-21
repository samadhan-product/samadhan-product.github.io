import { useEffect, useRef } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";
import { useTheme } from "../hooks/useTheme";

/**
 * Magnetic button — the button subtly follows the cursor on hover.
 * Pill / sharp based on `shape` prop.
 */
export default function MagneticButton({
  children,
  onClick,
  href,
  shape = "pill", // "pill" | "sharp"
  variant = "primary", // "primary" | "ghost"
  className = "",
  "data-testid": testId,
  ...rest
}) {
  const ref = useRef(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const sx = useSpring(x, { stiffness: 220, damping: 18, mass: 0.4 });
  const sy = useSpring(y, { stiffness: 220, damping: 18, mass: 0.4 });
  const { isDark } = useTheme();

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const handle = (e) => {
      const r = el.getBoundingClientRect();
      const relX = e.clientX - (r.left + r.width / 2);
      const relY = e.clientY - (r.top + r.height / 2);
      x.set(relX * 0.25);
      y.set(relY * 0.35);
    };
    const reset = () => {
      x.set(0);
      y.set(0);
    };
    el.addEventListener("mousemove", handle);
    el.addEventListener("mouseleave", reset);
    return () => {
      el.removeEventListener("mousemove", handle);
      el.removeEventListener("mouseleave", reset);
    };
  }, [x, y]);

  const base =
    "group relative inline-flex items-center justify-center gap-3 overflow-hidden px-7 py-4 font-mono text-[11px] uppercase tracking-[0.18em] transition-colors duration-500";
  const shapeCls = shape === "pill" ? "rounded-full" : "rounded-none";

  const variantCls = isDark
    ? variant === "primary"
      ? "border border-white/80 text-white hover:text-black"
      : "border border-white/20 text-white/80 hover:text-white"
    : variant === "primary"
      ? "border border-stone-700 text-stone-800 hover:text-white"
      : "border border-stone-400/70 text-stone-600 hover:text-stone-900";

  const fillBg = isDark ? "bg-white" : "bg-stone-800";

  const Tag = href ? motion.a : motion.button;
  const linkProps = href
    ? { href, target: href.startsWith("http") ? "_blank" : undefined, rel: "noreferrer" }
    : { onClick };

  return (
    <Tag
      ref={ref}
      style={{ x: sx, y: sy }}
      className={`${base} ${shapeCls} ${variantCls} ${className}`}
      data-testid={testId}
      {...linkProps}
      {...rest}
    >
      {/* fill */}
      <span
        aria-hidden
        className={`pointer-events-none absolute inset-0 -z-10 origin-bottom scale-y-0 ${fillBg} transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:origin-top group-hover:scale-y-100 ${shapeCls}`}
      />
      <span className="relative flex items-center gap-3">{children}</span>
    </Tag>
  );
}
