import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

/**
 * Full-screen intro overlay. Shows briefly on first paint, then lifts.
 */
export default function LoadingIntro() {
  const [visible, setVisible] = useState(true);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let p = 0;
    const int = setInterval(() => {
      p += Math.random() * 14 + 6;
      if (p >= 100) {
        p = 100;
        setProgress(100);
        clearInterval(int);
        setTimeout(() => setVisible(false), 350);
      } else {
        setProgress(Math.floor(p));
      }
    }, 120);
    return () => clearInterval(int);
  }, []);

  return (
    <AnimatePresence>
      {visible ? (
        <motion.div
          initial={{ y: 0 }}
          exit={{ y: "-100%" }}
          transition={{ duration: 1.1, ease: [0.76, 0, 0.24, 1] }}
          className="fixed inset-0 z-[9000] flex flex-col justify-between bg-[#050505] p-6 md:p-10"
          data-testid="loading-intro"
        >
          <div className="flex items-center justify-between font-mono text-[11px] uppercase tracking-[0.22em] text-white/60">
            <span>Samadhan Mishra — Portfolio</span>
            <span>2025 / 12</span>
          </div>

          <div className="flex items-end justify-between">
            <motion.div
              initial={{ y: 30, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
              className="font-display text-[clamp(3rem,12vw,11rem)] font-light leading-[0.85] tracking-[-0.04em] text-white"
            >
              hello<span className="text-white/30">.</span>
            </motion.div>
            <div className="font-mono text-sm tabular-nums text-white/60 md:text-base">
              {String(progress).padStart(3, "0")}%
            </div>
          </div>

          <div className="relative h-px w-full bg-white/10">
            <motion.div
              animate={{ width: `${progress}%` }}
              transition={{ duration: 0.3 }}
              className="absolute left-0 top-0 h-px bg-white"
            />
          </div>
        </motion.div>
      ) : null}
    </AnimatePresence>
  );
}
