import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";

/**
 * Staggered text reveal — splits on words, animates each in.
 */
export function RevealText({
  text,
  as: Tag = "span",
  className = "",
  delay = 0,
  stagger = 0.05,
  y = 40,
  once = true
}) {
  const words = String(text).split(" ");
  return (
    <Tag className={className}>
      {words.map((w, i) => (
        <span
          key={i}
          className="inline-block overflow-hidden align-bottom"
          style={{ marginRight: "0.28em" }}
        >
          <motion.span
            className="inline-block"
            initial={{ y, opacity: 0 }}
            whileInView={{ y: 0, opacity: 1 }}
            viewport={{ once, margin: "-10% 0px" }}
            transition={{
              duration: 0.9,
              ease: [0.16, 1, 0.3, 1],
              delay: delay + i * stagger
            }}
          >
            {w}
          </motion.span>
        </span>
      ))}
    </Tag>
  );
}

/**
 * Section wrapper with sticky label + generous padding.
 */
export function Section({ id, label, children, className = "" }) {
  return (
    <section
      id={id}
      className={`relative border-t border-white/10 py-24 md:py-36 ${className}`}
    >
      <div className="mx-auto max-w-7xl px-6 md:px-12">
        {label ? (
          <div className="mb-14 flex items-center gap-3 font-mono text-[11px] uppercase tracking-[0.22em] text-white/40">
            <span className="inline-block h-px w-8 bg-white/30" />
            <span>{label}</span>
          </div>
        ) : null}
        {children}
      </div>
    </section>
  );
}

/**
 * Parallax Y on scroll.
 */
export function Parallax({ children, speed = 40, className = "" }) {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  const y = useTransform(scrollYProgress, [0, 1], [speed, -speed]);
  return (
    <motion.div ref={ref} style={{ y }} className={className}>
      {children}
    </motion.div>
  );
}
