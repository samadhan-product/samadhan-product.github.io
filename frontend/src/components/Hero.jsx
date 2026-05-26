import { motion } from "framer-motion";
import MagneticButton from "./MagneticButton";
import { consulting } from "../data/consulting";
import { profile } from "../data/profile";

export default function Hero() {
  return (
    <section
      id="top"
      className="relative flex min-h-[100svh] w-full flex-col overflow-hidden"
      data-testid="hero-section"
    >
      <div className="hero-vignette" aria-hidden="true" />

      <div className="relative z-10 mx-auto flex w-full max-w-7xl items-center justify-between px-6 pt-28 font-mono text-[11px] uppercase tracking-[0.22em] text-white/50 md:px-12 md:pt-32">
        <span data-testid="hero-meta-location">{profile.location}</span>
        <span className="hidden md:inline">AI Product Leader · Consultant</span>
        <span>CONSULTING / 2026</span>
      </div>

      <div className="flex-1" />

      <div className="relative z-10 mx-auto w-full max-w-7xl px-6 pb-16 md:px-12 md:pb-20">
        <div className="mb-6 flex items-center gap-4 font-mono text-[11px] uppercase tracking-[0.22em] text-white/60">
          <span className="inline-block h-1.5 w-1.5 rounded-full bg-white" />
          <span>Samadhan Mishra</span>
        </div>

        <h1
          className="max-w-5xl font-display text-[clamp(2rem,6vw,4.5rem)] font-light leading-[1.05] tracking-[-0.03em] text-white"
          data-testid="hero-heading"
        >
          AI Product Leader for AI-Native Products, Agentic Workflows and Product Transformation
        </h1>

        <div className="mt-10 grid grid-cols-1 gap-10 md:grid-cols-12">
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.4 }}
            className="md:col-span-7 font-body text-base text-white/70 md:text-lg"
          >
            {consulting.heroSubcopy}
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.6 }}
            className="flex flex-col items-start gap-4 md:col-span-5 md:items-end"
          >
            <div className="flex flex-wrap items-center gap-3 md:justify-end">
              <MagneticButton
                href="/work-with-me/"
                shape="pill"
                variant="primary"
                data-testid="hero-work-with-me"
              >
                <span>Work With Me</span>
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
                  <path
                    d="M1 7h12M8 2l5 5-5 5"
                    stroke="currentColor"
                    strokeWidth="1.2"
                  />
                </svg>
              </MagneticButton>

              <MagneticButton
                href="/case-studies/"
                shape="pill"
                variant="ghost"
                data-testid="hero-case-studies"
              >
                <span>View AI Product Case Studies</span>
              </MagneticButton>

              <MagneticButton
                href="/portfolio/"
                shape="pill"
                variant="ghost"
                data-testid="hero-portfolio-button"
              >
                <span>Portfolio</span>
              </MagneticButton>
            </div>
          </motion.div>
        </div>
      </div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.2, duration: 1 }}
        className="relative z-10 mx-auto flex w-full max-w-7xl items-center justify-between border-t border-white/10 px-6 py-5 font-mono text-[10px] uppercase tracking-[0.22em] text-white/40 md:px-12"
      >
        <span>Scroll to explore</span>
        <div className="flex items-center gap-3">
          <span className="h-px w-20 bg-white/20 md:w-40" />
          <span className="inline-block h-1.5 w-1.5 rounded-full bg-white/70" />
        </div>
        <span>v.2026.05</span>
      </motion.div>
    </section>
  );
}
