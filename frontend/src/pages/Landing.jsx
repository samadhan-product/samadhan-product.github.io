import Navigation from "../components/Navigation";
import Hero from "../components/Hero";
import About from "../components/About";
import Metrics from "../components/Metrics";
import Experience from "../components/Experience";
import Projects from "../components/Projects";
import Skills from "../components/Skills";
import Contact from "../components/Contact";
import CustomCursor from "../components/CustomCursor";
import SmoothScroll from "../components/SmoothScroll";
import LoadingIntro from "../components/LoadingIntro";
import {
  WhatIBuild,
  LeadershipExpertise,
  FeaturedCaseStudies,
  ConsultingServices,
  ThoughtLeadership,
  GeoFaqSection,
  WorkWithMeSection
} from "../components/ConsultingSections";

export default function Landing() {
  return (
    <main className="relative grain" data-testid="landing-root">
      <LoadingIntro />
      <SmoothScroll />
      <CustomCursor />
      <Navigation />
      <Hero />
      <About />
      <WhatIBuild />
      <LeadershipExpertise />
      <FeaturedCaseStudies />
      <ConsultingServices />
      <Metrics />
      <Experience />
      <Projects />
      <ThoughtLeadership />
      <Skills />
      <GeoFaqSection />
      <WorkWithMeSection />
      <Contact />
    </main>
  );
}
