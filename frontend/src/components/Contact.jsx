import { motion } from "framer-motion";
import { Section, RevealText } from "./Reveal";
import MagneticButton from "./MagneticButton";
import { profile } from "../data/profile";

const socials = [
  {
    key: "linkedin",
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/samadhan-mishra/",
    handle: "/in/samadhan-mishra"
  },
  {
    key: "email",
    label: "Email",
    href: profile.social.email,
    handle: "me@samadhanmishra.com"
  }
];

export default function Contact() {
  return (
    <Section id="contact" label="07 / Contact" className="pb-0">
      <div className="grid grid-cols-1 gap-16 md:grid-cols-12">
        <div className="md:col-span-12">
          <h2
            className="font-display text-[clamp(3rem,10vw,10rem)] font-light leading-[0.9] tracking-[-0.04em] text-white"
            data-testid="contact-heading"
          >
            <RevealText text="Have an idea?" as="span" className="block" />
            <RevealText
              text="Let's build it."
              as="span"
              className="block italic"
              delay={0.1}
            />
          </h2>
        </div>

        <div className="md:col-span-7">
          <p className="font-body text-base text-white/70 md:text-lg">
            I'm currently {profile.availability.toLowerCase()}. The fastest way
            to reach me is LinkedIn — I reply to most serious conversations
            within a working day.
          </p>

          <div className="mt-10 flex flex-wrap gap-4">
            <MagneticButton
              href={profile.social.linkedin}
              shape="pill"
              variant="primary"
              data-testid="contact-hire-me-button"
              data-cursor="hire me"
            >
              <span>Hire Me</span>
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
              href={profile.social.email}
              shape="pill"
              variant="ghost"
              data-testid="contact-email-button"
              data-cursor="write"
            >
              <span>Write an email</span>
            </MagneticButton>
          </div>
        </div>

        <div className="md:col-span-5">
          <ul className="divide-y divide-white/10 border-y border-white/10">
            {socials.map((s) => (
              <li
                key={s.key}
                className="group relative overflow-hidden transition-colors duration-500"
              >
                <a
                  href={s.href}
                  target={s.href.startsWith("http") ? "_blank" : undefined}
                  rel="noreferrer"
                  className="grid grid-cols-12 items-center gap-4 px-2 py-5"
                  data-testid={`social-${s.key}`}
                  data-cursor={s.label.toLowerCase()}
                >
                  <div className="col-span-1 font-mono text-[10px] uppercase tracking-[0.22em] text-white/40">
                    ↗
                  </div>
                  <div className="col-span-5 font-display text-xl text-white md:text-2xl">
                    {s.label}
                  </div>
                  <div className="col-span-6 text-right font-mono text-[11px] uppercase tracking-[0.22em] text-white/60">
                    {s.handle}
                  </div>
                </a>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Big name footer */}
      <div className="relative mt-24 overflow-hidden border-t border-white/10 pt-10">
        <motion.div
          initial={{ y: 40, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true, margin: "-10%" }}
          transition={{ duration: 1.1, ease: [0.16, 1, 0.3, 1] }}
          className="pointer-events-none select-none font-display text-[clamp(4rem,18vw,20rem)] font-light leading-[0.82] tracking-[-0.05em] text-white"
          data-testid="footer-name-block"
        >
          SAMADHAN
        </motion.div>
        <motion.div
          initial={{ y: 40, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          viewport={{ once: true, margin: "-10%" }}
          transition={{
            duration: 1.1,
            ease: [0.16, 1, 0.3, 1],
            delay: 0.1
          }}
          className="pointer-events-none select-none text-right font-display text-[clamp(4rem,18vw,20rem)] font-light italic leading-[0.82] tracking-[-0.05em] text-white/60"
        >
          MISHRA.
        </motion.div>

        <div className="mt-10 border-t border-white/10 py-6 font-mono text-[11px] uppercase tracking-[0.22em] text-white/40">
          <span>© 2025 — Samadhan Mishra</span>
        </div>
      </div>
    </Section>
  );
}
