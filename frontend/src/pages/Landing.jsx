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

export default function Landing() {
  return (
    <main className="relative grain" style={{ background: "var(--bg)", color: "var(--fg)" }} data-testid="landing-root">
      <LoadingIntro />
      <SmoothScroll />
      <CustomCursor />
      <Navigation />
      <Hero />
      <About />
      <Metrics />
      <Experience />
      <Projects />
      <Skills />
      <Contact />
    </main>
  );
}
