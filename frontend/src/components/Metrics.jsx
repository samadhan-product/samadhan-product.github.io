import { motion, useInView, useMotionValue, animate } from "framer-motion";
import { useEffect, useRef } from "react";
import { Section } from "./Reveal";
import { profile } from "../data/profile";

/**
 * Animated counter — parses "₹20M+" style strings, animates the numeric part.
 */
function AnimatedValue({ value }) {
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, margin: "-20%" });
  const mv = useMotionValue(0);
  const textRef = useRef(null);

  // Extract number + prefix + suffix
  const match = String(value).match(/^([^\d-]*)([\d.]+)(.*)$/);
  const prefix = match ? match[1] : "";
  const num = match ? parseFloat(match[2]) : 0;
  const suffix = match ? match[3] : "";

  useEffect(() => {
    if (!inView) return;
    const controls = animate(mv, num, {
      duration: 1.6,
      ease: [0.16, 1, 0.3, 1]
    });
    const unsub = mv.on("change", (v) => {
      if (!textRef.current) return;
      const isInt = Number.isInteger(num);
      const out = isInt ? Math.round(v) : v.toFixed(1);
      textRef.current.textContent = `${prefix}${out}${suffix}`;
    });
    return () => {
      controls.stop();
      unsub();
    };
  }, [inView, mv, num, prefix, suffix]);

  return (
    <span ref={ref}>
      <span ref={textRef}>
        {prefix}
        {Number.isInteger(num) ? 0 : "0.0"}
        {suffix}
      </span>
    </span>
  );
}

export default function Metrics() {
  return (
    <Section id="work" label="03 / By the numbers">
      <div className="mb-16 max-w-3xl">
        <h2 className="font-display text-3xl font-light leading-[1.05] tracking-[-0.02em] text-white md:text-5xl">
          Measurable outcomes,{" "}
          <span className="italic text-white/70">not slideware.</span>
        </h2>
      </div>

      <div
        className="grid grid-cols-2 border-l border-t border-white/10 md:grid-cols-4"
        data-testid="metrics-grid"
      >
        {profile.metrics.map((m, i) => (
          <motion.div
            key={m.label}
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-10%" }}
            transition={{
              duration: 0.8,
              ease: [0.16, 1, 0.3, 1],
              delay: i * 0.08
            }}
            className="group relative overflow-hidden border-b border-r border-white/10 p-8 md:p-12"
            data-testid={`metric-item-${i}`}
            data-cursor=""
          >
            <div
              aria-hidden
              className="pointer-events-none absolute inset-0 -z-10 origin-bottom scale-y-0 bg-white/[0.03] transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:scale-y-100"
            />
            <div className="font-mono text-[10px] uppercase tracking-[0.22em] text-white/40">
              / {String(i + 1).padStart(2, "0")}
            </div>
            <div className="mt-6 font-display text-5xl font-light tracking-[-0.03em] text-white md:text-7xl">
              <AnimatedValue value={m.value} />
            </div>
            <div className="mt-4 font-body text-sm text-white/60 md:text-base">
              {m.label}
            </div>
          </motion.div>
        ))}
      </div>
    </Section>
  );
}
