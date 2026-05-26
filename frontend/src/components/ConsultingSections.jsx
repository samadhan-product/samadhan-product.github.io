import { motion } from "framer-motion";
import { Section, RevealText } from "./Reveal";
import MagneticButton from "./MagneticButton";
import { consulting } from "../data/consulting";
import { profile } from "../data/profile";

const fade = {
  initial: { opacity: 0, y: 24 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true, margin: "-15%" },
  transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] }
};

export function WhatIBuild() {
  return (
    <Section id="build" label="What I Help Companies Build">
      <h2 className="font-display text-3xl font-light text-white md:text-5xl">
        <RevealText text="What I help companies build" as="span" />
      </h2>
      <div className="mt-12 grid gap-6 md:grid-cols-2">
        {consulting.buildItems.map((item) => (
          <motion.article
            key={item.title}
            {...fade}
            className="border border-white/10 bg-white/[0.02] p-6"
          >
            <h3 className="font-display text-xl text-white">{item.title}</h3>
            <p className="mt-3 font-body text-sm text-white/65 md:text-base">{item.desc}</p>
          </motion.article>
        ))}
      </div>
    </Section>
  );
}

export function LeadershipExpertise() {
  return (
    <Section id="expertise" label="AI Product Leadership Expertise">
      <h2 className="font-display text-3xl font-light text-white md:text-5xl">
        <RevealText text="AI product leadership expertise" as="span" />
      </h2>
      <motion.ul {...fade} className="mt-10 grid gap-3 md:grid-cols-2">
        {consulting.expertise.map((item) => (
          <li
            key={item}
            className="border-t border-white/10 py-4 font-body text-sm text-white/75 md:text-base"
          >
            {item}
          </li>
        ))}
      </motion.ul>
      <p className="mt-8 font-body text-white/60">
        <a href="/ai-product-leader/" className="text-white underline-offset-4 hover:underline">
          AI Product Leader
        </a>
        {" · "}
        <a
          href="/ai-product-management-consultant/"
          className="text-white underline-offset-4 hover:underline"
        >
          AI Product Management Consultant
        </a>
      </p>
    </Section>
  );
}

export function FeaturedCaseStudies() {
  return (
    <Section id="case-studies" label="Featured Case Studies">
      <div className="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
        <h2 className="font-display text-3xl font-light text-white md:text-5xl">
          <RevealText text="Featured case studies" as="span" />
        </h2>
        <a
          href="/case-studies/"
          className="font-mono text-[11px] uppercase tracking-[0.2em] text-white/50 hover:text-white"
        >
          View all →
        </a>
      </div>
      <div className="mt-10 grid gap-4 md:grid-cols-2">
        {consulting.caseStudies.map((cs) => (
          <motion.a
            key={cs.href}
            href={cs.href}
            {...fade}
            className="group block border border-white/10 p-6 transition-colors hover:border-white/25"
          >
            <span className="font-mono text-[10px] uppercase tracking-[0.2em] text-white/45">
              {cs.tag}
            </span>
            <h3 className="mt-2 font-display text-xl text-white group-hover:text-white">
              {cs.title}
            </h3>
          </motion.a>
        ))}
      </div>
    </Section>
  );
}

export function ConsultingServices() {
  return (
    <Section id="services" label="Consulting Services">
      <h2 className="font-display text-3xl font-light text-white md:text-5xl">
        <RevealText text="Consulting services" as="span" />
      </h2>
      <div className="mt-12 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {consulting.services.map((s) => (
          <motion.a
            key={s.href}
            href={s.href}
            {...fade}
            className="flex flex-col border border-white/10 p-6 transition-colors hover:border-white/25"
          >
            <h3 className="font-display text-lg text-white">{s.title}</h3>
            <p className="mt-3 flex-1 font-body text-sm text-white/60">{s.desc}</p>
            <span className="mt-4 font-mono text-[10px] uppercase tracking-[0.2em] text-white/40">
              Learn more →
            </span>
          </motion.a>
        ))}
      </div>
    </Section>
  );
}

export function ThoughtLeadership() {
  return (
    <Section id="thought-leadership" label="Thought Leadership">
      <h2 className="font-display text-3xl font-light text-white md:text-5xl">
        <RevealText text="Thought leadership" as="span" />
      </h2>
      <div className="mt-10 grid gap-4 md:grid-cols-2">
        <motion.a
          href="/blog/ai-learning/"
          {...fade}
          className="block border border-white/10 p-8 hover:border-white/25"
        >
          <h3 className="font-display text-2xl text-white">AI Learning</h3>
          <p className="mt-3 font-body text-white/65">
            Structured syllabus for product leaders—LLM mechanics, model landscape, RAG, agents.
          </p>
        </motion.a>
        <motion.a
          href="/insights/"
          {...fade}
          className="block border border-white/10 p-8 hover:border-white/25"
        >
          <h3 className="font-display text-2xl text-white">Insights</h3>
          <p className="mt-3 font-body text-white/65">
            Essays and notes on AI product strategy, production AI, and transformation.
          </p>
        </motion.a>
      </div>
      <motion.div {...fade} className="mt-6">
        <a
          href="/speaking-workshops/"
          className="font-mono text-[11px] uppercase tracking-[0.2em] text-white/50 hover:text-white"
        >
          Speaking & workshops →
        </a>
      </motion.div>
    </Section>
  );
}

export function GeoFaqSection() {
  return (
    <Section id="faq" label="FAQ">
      <h2 className="font-display text-3xl font-light text-white md:text-5xl">
        <RevealText text="Questions leaders ask" as="span" />
      </h2>
      <div className="mt-10 space-y-8">
        {consulting.geoAnswers.map((item) => (
          <motion.div key={item.q} {...fade} className="border-t border-white/10 pt-6">
            <h3 className="font-display text-lg text-white">{item.q}</h3>
            <p className="mt-2 font-body text-white/65">{item.a}</p>
          </motion.div>
        ))}
      </div>
      <p className="mt-10 font-body text-sm text-white/50">
        More answers on{" "}
        <a href="/work-with-me/" className="text-white/80 hover:text-white">
          Work With Me
        </a>{" "}
        and service pages.
      </p>
    </Section>
  );
}

export function WorkWithMeSection() {
  return (
    <Section id="work-with-me" label="Work With Me">
      <h2 className="font-display text-[clamp(2.5rem,8vw,6rem)] font-light leading-[0.92] text-white">
        <RevealText text="Work with me" as="span" className="block" />
      </h2>
      <motion.p {...fade} className="mt-8 max-w-2xl font-body text-lg text-white/70">
        Advisory, strategy sprints, and hands-on product leadership for AI initiatives. Share your
        workflow, constraints, and timeline—I respond to serious inquiries within one business day.
      </motion.p>
      <motion.div {...fade} className="mt-10 flex flex-wrap gap-4">
        <MagneticButton href="/work-with-me/" shape="pill" variant="primary">
          <span>Work With Me</span>
        </MagneticButton>
        <MagneticButton href={profile.social.linkedin} shape="pill" variant="ghost">
          <span>LinkedIn</span>
        </MagneticButton>
        <MagneticButton href={profile.social.email} shape="pill" variant="ghost">
          <span>Email</span>
        </MagneticButton>
      </motion.div>
    </Section>
  );
}
