import { motion } from "framer-motion";
import { Section, RevealText } from "./Reveal";
import { profile } from "../data/profile";
import { consulting } from "../data/consulting";

export default function About() {
  return (
    <Section id="about" label="About Samadhan Mishra">
      <div className="grid grid-cols-1 gap-16 md:grid-cols-12 md:gap-12">
        {/* Left — tag + portrait */}
        <div className="md:col-span-5">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-20%" }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
            className="relative aspect-[4/5] w-full overflow-hidden border border-white/10"
          >
            <div
              className="absolute inset-0 bg-cover transition-all duration-[1500ms] hover:scale-[1.02]"
              style={{
                backgroundImage: "url('/images/portrait.jpeg')",
                backgroundPosition: "center 20%"
              }}
              data-testid="about-portrait"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent" />
            <div className="absolute inset-x-4 bottom-4 flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.22em] text-white/70">
              <span>{profile.name}</span>
              <span>{profile.location}</span>
            </div>
            <div className="absolute left-4 top-4 font-mono text-[10px] uppercase tracking-[0.22em] text-white/60">
              <span className="inline-block h-1.5 w-1.5 translate-y-[-2px] bg-emerald-400 blink" />{" "}
              available
            </div>
          </motion.div>

          <div className="mt-6 grid grid-cols-2 gap-4 font-mono text-[11px] uppercase tracking-[0.2em] text-white/50">
            <div className="border-t border-white/10 pt-3">
              <div className="text-white/40">Based in</div>
              <div className="mt-1 text-white">{profile.location}</div>
            </div>
            <div className="border-t border-white/10 pt-3">
              <div className="text-white/40">Years</div>
              <div className="mt-1 text-white">{profile.years} in product</div>
            </div>
          </div>
        </div>

        {/* Right — bio */}
        <div className="md:col-span-7">
          <h2
            className="font-display text-4xl font-light leading-[1.02] tracking-[-0.03em] text-white md:text-5xl"
            data-testid="about-heading"
          >
            <RevealText text="About Samadhan Mishra" as="span" className="block" />
          </h2>

          <p className="mt-8 font-body text-base text-white/75 md:text-lg">
            {consulting.entityBio}
          </p>

          <div className="mt-12 space-y-7 font-body text-base text-white/70 md:text-lg">
            {profile.bio.map((p, i) => (
              <motion.p
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-10%" }}
                transition={{
                  duration: 0.9,
                  ease: [0.16, 1, 0.3, 1],
                  delay: 0.1 + i * 0.1
                }}
                data-testid={`about-paragraph-${i}`}
              >
                {p}
              </motion.p>
            ))}
          </div>

          {/* Mini signature grid */}
          <div className="mt-16 grid grid-cols-2 gap-10 border-t border-white/10 pt-10 md:grid-cols-4">
            {[
              { k: "Role", v: "AI Product Leader" },
              { k: "Focus", v: "InsurTech · AI/ML" },
              { k: "Experience", v: profile.years },
              { k: "Open to", v: "Senior PM / Dir roles" }
            ].map((it) => (
              <div key={it.k}>
                <div className="font-mono text-[10px] uppercase tracking-[0.22em] text-white/40">
                  {it.k}
                </div>
                <div className="mt-2 font-display text-lg text-white">
                  {it.v}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
}
