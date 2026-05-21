import { motion } from "framer-motion";
import { useState } from "react";
import { Section } from "./Reveal";
import { profile } from "../data/profile";

function ProjectRow({ project, index }) {
  const [hover, setHover] = useState(false);
  return (
    <motion.a
      href="#contact"
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-10%" }}
      transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
      className="group relative block border-t border-white/10"
      data-testid={`project-row-${project.id}`}
      data-cursor="case study"
    >
      <div className="grid grid-cols-12 items-center gap-4 px-2 py-8 md:py-12">
        <div className="col-span-1 font-mono text-[11px] uppercase tracking-[0.22em] text-white/40">
          /{String(index + 1).padStart(2, "0")}
        </div>
        <div className="col-span-8 md:col-span-6">
          <motion.div
            animate={{ x: hover ? 16 : 0 }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-3xl font-light tracking-[-0.02em] text-white md:text-6xl"
          >
            {project.title}
          </motion.div>
          <div className="mt-2 font-mono text-[10px] uppercase tracking-[0.22em] text-white/50 md:hidden">
            {project.tag}
          </div>
        </div>
        <div className="col-span-3 hidden font-mono text-[11px] uppercase tracking-[0.22em] text-white/60 md:block">
          {project.tag}
        </div>
        <div className="col-span-3 flex items-center justify-end gap-4 font-mono text-[11px] uppercase tracking-[0.22em] text-white/60 md:col-span-2">
          <span>{project.year}</span>
          <motion.span
            aria-hidden
            animate={{ x: hover ? 8 : 0, opacity: hover ? 1 : 0.5 }}
            transition={{ duration: 0.5 }}
            className="inline-flex h-8 w-8 items-center justify-center border border-white/30"
          >
            →
          </motion.span>
        </div>
      </div>

    </motion.a>
  );
}

export default function Projects() {
  return (
    <Section id="projects" label="05 / Selected Products">
      <div className="mb-14 grid grid-cols-1 gap-8 md:grid-cols-12">
        <h2 className="col-span-12 font-display text-4xl font-light leading-[1.02] tracking-[-0.03em] text-white md:col-span-8 md:text-6xl">
          A decade of products.
          <br />
          <span className="italic text-white/80">A few worth naming.</span>
        </h2>
      </div>

      <div className="border-b border-white/10">
        {profile.projects.map((p, i) => (
          <ProjectRow key={p.id} project={p} index={i} />
        ))}
      </div>
    </Section>
  );
}
