import { motion } from "framer-motion";
import { Section } from "./Reveal";
import { profile } from "../data/profile";

export default function Skills() {
  const rowA = profile.skills.slice(0, Math.ceil(profile.skills.length / 2));
  const rowB = profile.skills.slice(Math.ceil(profile.skills.length / 2));

  return (
    <Section id="skills" label="06 / Skills">
      <div className="mb-16 grid grid-cols-1 gap-10 md:grid-cols-12">
        <h2 className="col-span-12 font-display text-4xl font-light leading-[1.02] tracking-[-0.03em] text-white md:col-span-8 md:text-6xl">
          Tools, methods &amp;{" "}
          <span className="italic text-white/80">mental models.</span>
        </h2>
        <p className="col-span-12 font-body text-base text-white/60 md:col-span-4 md:self-end">
          A non-exhaustive list of things I reach for when building AI-first
          products.
        </p>
      </div>

      <div className="space-y-5 overflow-hidden">
        <Marquee items={rowA} direction="left" testId="skills-marquee-a" />
        <Marquee items={rowB} direction="right" testId="skills-marquee-b" />
      </div>

      {/* Precise grid */}
      <div className="mt-20 grid grid-cols-2 gap-px border-l border-t border-white/10 md:grid-cols-4">
        {profile.skills.slice(0, 12).map((s, i) => (
          <motion.div
            key={s}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-10%" }}
            transition={{
              duration: 0.7,
              ease: [0.16, 1, 0.3, 1],
              delay: i * 0.04
            }}
            className="group relative flex min-h-[110px] items-end overflow-hidden border-b border-r border-white/10 p-5 transition-colors duration-500 hover:bg-white hover:text-black"
            data-testid={`skill-cell-${i}`}
          >
            <div className="absolute left-5 top-5 font-mono text-[10px] uppercase tracking-[0.22em] text-white/40 group-hover:text-black/60">
              /{String(i + 1).padStart(2, "0")}
            </div>
            <div className="font-display text-xl font-light tracking-tight md:text-2xl">
              {s}
            </div>
          </motion.div>
        ))}
      </div>
    </Section>
  );
}

function Marquee({ items, direction = "left", testId }) {
  const trackCls =
    direction === "left" ? "marquee-track" : "marquee-track-reverse";
  return (
    <div className="flex overflow-hidden" data-testid={testId}>
      <div className={`flex shrink-0 items-center gap-12 pr-12 ${trackCls}`}>
        {[...items, ...items].map((s, i) => (
          <span
            key={`${s}-${i}`}
            className="flex shrink-0 items-center gap-6 font-display text-4xl font-light tracking-[-0.02em] text-white md:text-6xl"
          >
            <span>{s}</span>
            <span aria-hidden className="text-white/20">
              ✺
            </span>
          </span>
        ))}
      </div>
    </div>
  );
}
