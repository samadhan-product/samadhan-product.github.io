import { motion } from "framer-motion";
import ShaderBackground from "./ShaderBackground";
import MagneticButton from "./MagneticButton";
import { RevealText } from "./Reveal";
import { profile } from "../data/profile";

export default function Hero() {
  return (
    <section
      id="top"
      className="relative flex min-h-[100svh] w-full flex-col overflow-hidden"
      data-testid="hero-section"
    >
      <ShaderBackground />

      {/* Vignette overlay */}
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-black" />

      {/* Top meta */}
      <div className="relative z-10 mx-auto flex w-full max-w-7xl items-center justify-between px-6 pt-28 font-mono text-[11px] uppercase tracking-[0.22em] text-white/50 md:px-12 md:pt-32">
        <span data-testid="hero-meta-location">{profile.location}</span>
        <span className="hidden md:inline">{profile.availability}</span>
        <span>PORTFOLIO / 2025</span>
      </div>

      {/* Spacer */}
      <div className="flex-1" />

      {/* Main content */}
      <div className="relative z-10 mx-auto w-full max-w-7xl px-6 pb-16 md:px-12 md:pb-20">
        <div className="mb-6 flex items-center gap-4 font-mono text-[11px] uppercase tracking-[0.22em] text-white/60">
          <span className="inline-block h-1.5 w-1.5 rounded-full bg-white" />
          <span>01 / INTRODUCTION</span>
        </div>

        <h1
          className="font-display text-[clamp(3rem,11vw,12rem)] font-light leading-[0.88] tracking-[-0.04em] text-white"
          data-testid="hero-heading"
        >
          <RevealText text="Samadhan" as="span" className="block" />
          <RevealText
            text="Mishra."
            as="span"
            className="block italic"
            delay={0.15}
          />
        </h1>

        <div className="mt-10 grid grid-cols-1 gap-10 md:grid-cols-12">
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.6 }}
            className="md:col-span-6 md:col-start-1 font-body text-base text-white/70 md:text-lg"
          >
            {profile.role} — {profile.years} across{" "}
            <span className="text-white">HealthTech</span>,{" "}
            <span className="text-white">FinTech</span>,{" "}
            <span className="text-white">EdTech</span>, and{" "}
            <span className="text-white">enterprise SaaS</span>. {profile.tagline}
          </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.85 }}
              className="flex flex-col items-start gap-4 md:col-span-5 md:col-start-8 md:items-end"
            >
              <motion.div className="flex flex-wrap items-center gap-3 md:justify-end">
                <MagneticButton
                  href="/portfolio/"
                  shape="pill"
                  variant="primary"
                  data-testid="hero-portfolio-button"
                  data-cursor="portfolio"
                >
                  <span>View Portfolio</span>
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 14 14"
                    fill="none"
                    className="transition-transform duration-500 group-hover:translate-x-1"
                  >
                    <path
                      d="M1 7h12M8 2l5 5-5 5"
                      stroke="currentColor"
                      strokeWidth="1.2"
                    />
                  </svg>
                </MagneticButton>

                <MagneticButton
                  href="/blog/"
                  shape="pill"
                  variant="primary"
                  data-testid="hero-blog-button"
                  data-cursor="blog"
                >
                  <span>Read Blog</span>
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 14 14"
                    fill="none"
                    className="transition-transform duration-500 group-hover:translate-x-1"
                  >
                    <path
                      d="M1 7h12M8 2l5 5-5 5"
                      stroke="currentColor"
                      strokeWidth="1.2"
                    />
                  </svg>
                </MagneticButton>
              </motion.div>

              <motion.div className="flex flex-wrap items-center gap-3 md:justify-end">
                <MagneticButton
                  href="/blog/ai-learning/"
                  shape="pill"
                  variant="ghost"
                  data-testid="hero-ai-learning-button"
                  data-cursor="ai learning"
                >
                  <span>AI Learning</span>
                  <svg
                    width="12"
                    height="12"
                    viewBox="0 0 12 12"
                    fill="none"
                    className="transition-transform duration-500 group-hover:-translate-y-0.5 group-hover:translate-x-0.5"
                  >
                    <path
                      d="M2.5 9.5 9.5 2.5M4 2.5h5.5V8"
                      stroke="currentColor"
                      strokeWidth="1.2"
                    />
                  </svg>
                </MagneticButton>

                <MagneticButton
                  href={profile.social.linkedin}
                  shape="pill"
                  variant="ghost"
                  data-testid="hero-linkedin-button"
                  data-cursor="linkedin"
                >
                  <span>LinkedIn</span>
                  <svg
                    width="12"
                    height="12"
                    viewBox="0 0 12 12"
                    fill="none"
                    className="transition-transform duration-500 group-hover:-translate-y-0.5 group-hover:translate-x-0.5"
                  >
                    <path
                      d="M2.5 9.5 9.5 2.5M4 2.5h5.5V8"
                      stroke="currentColor"
                      strokeWidth="1.2"
                    />
                  </svg>
                </MagneticButton>
              </motion.div>
            </motion.div>
        </div>
      </div>

      {/* Scroll indicator */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.4, duration: 1 }}
        className="relative z-10 mx-auto flex w-full max-w-7xl items-center justify-between border-t border-white/10 px-6 py-5 font-mono text-[10px] uppercase tracking-[0.22em] text-white/40 md:px-12"
      >
        <span>Scroll to explore</span>
        <div className="flex items-center gap-3">
          <span className="h-px w-20 bg-white/20 md:w-40" />
          <span className="inline-block h-1.5 w-1.5 rounded-full bg-white/70" />
        </div>
        <span>v.2025.12</span>
      </motion.div>
    </section>
  );
}
