import { motion, useScroll, useTransform } from "framer-motion";
import { useRef, useState } from "react";
import { Section } from "./Reveal";
import { profile } from "../data/profile";

function TimelineItem({ item, index, total }) {
  const [open, setOpen] = useState(index === 0);
  return (
    <motion.li
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-10%" }}
      transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
      className="relative border-t border-white/10 py-8"
      data-testid={`experience-item-${index}`}
    >
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="group grid w-full grid-cols-12 items-start gap-4 text-left"
        data-cursor={open ? "close" : "expand"}
      >
        <div className="col-span-12 flex items-baseline gap-4 font-mono text-[10px] uppercase tracking-[0.22em] text-white/40 md:col-span-2">
          <span className="text-white/70">
            {String(index + 1).padStart(2, "0")}
          </span>
          <span>/{String(total).padStart(2, "0")}</span>
        </div>

        <div className="col-span-12 md:col-span-7">
          <div className="font-display text-2xl font-light leading-tight tracking-tight text-white md:text-4xl">
            {item.role}
          </div>
          <div className="mt-2 font-body text-sm text-white/60 md:text-base">
            {item.company} · {item.location}
          </div>
        </div>

        <div className="col-span-12 flex items-start justify-between md:col-span-3 md:justify-end">
          <div className="font-mono text-[11px] uppercase tracking-[0.22em] text-white/50">
            {item.period}
          </div>
          <motion.span
            aria-hidden
            animate={{ rotate: open ? 45 : 0 }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
            className="ml-6 inline-flex h-6 w-6 items-center justify-center border border-white/30 text-white/80"
          >
            +
          </motion.span>
        </div>
      </button>

      <motion.div
        initial={false}
        animate={{ height: open ? "auto" : 0, opacity: open ? 1 : 0 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="overflow-hidden"
      >
        <div className="mt-6 grid grid-cols-12 gap-4 md:gap-8">
          <div className="col-span-12 md:col-span-2" />
          <div className="col-span-12 md:col-span-7">
            <p className="font-body text-base text-white/70 md:text-lg">
              {item.blurb}
            </p>
            <ul className="mt-6 space-y-3">
              {item.points.map((p, i) => (
                <li
                  key={i}
                  className="flex items-start gap-3 font-body text-sm text-white/60"
                >
                  <span className="mt-2 inline-block h-px w-4 flex-shrink-0 bg-white/30" />
                  <span>{p}</span>
                </li>
              ))}
            </ul>
          </div>
          <div className="col-span-12 md:col-span-3">
            <div className="font-mono text-[10px] uppercase tracking-[0.22em] text-white/40">
              Stack / tools
            </div>
            <ul className="mt-4 flex flex-wrap gap-2">
              {item.stack.map((s) => (
                <li
                  key={s}
                  className="border border-white/15 px-2.5 py-1 font-mono text-[10px] uppercase tracking-[0.18em] text-white/70"
                >
                  {s}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </motion.div>
    </motion.li>
  );
}

export default function Experience() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  const lineY = useTransform(scrollYProgress, [0, 1], ["0%", "100%"]);

  return (
    <Section id="experience" label="04 / Experience">
      <div className="mb-14 grid grid-cols-1 gap-10 md:grid-cols-12">
        <h2 className="col-span-12 font-display text-4xl font-light leading-[1.02] tracking-[-0.03em] text-white md:col-span-8 md:text-6xl">
          From ECIL mainframes to
          <br />
          <span className="italic text-white/80">AI at insurance scale.</span>
        </h2>
        <p className="col-span-12 font-body text-base text-white/60 md:col-span-4 md:self-end">
          Eight roles. Product from 0→1, SaaS growth, enterprise FinTech, and
          AI/ML at scale — in that order.
        </p>
      </div>

      <div ref={ref} className="relative">
        {/* progress line */}
        <div
          aria-hidden
          className="pointer-events-none absolute left-0 top-0 hidden h-full w-px bg-white/10 md:block"
        >
          <motion.div
            style={{ height: lineY }}
            className="absolute left-0 top-0 w-px bg-white/70"
          />
        </div>

        <ul className="md:pl-8">
          {profile.experience.map((e, i) => (
            <TimelineItem
              key={`${e.company}-${i}`}
              item={e}
              index={i}
              total={profile.experience.length}
            />
          ))}
          <li className="border-t border-white/10" />
        </ul>
      </div>
    </Section>
  );
}
