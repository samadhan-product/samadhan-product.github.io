import { useEffect, useRef, useState } from "react";

/**
 * Custom cursor with mix-blend-mode: difference.
 * Grows on hoverable elements, displays a label when hovering [data-cursor].
 */
export default function CustomCursor() {
  const dotRef = useRef(null);
  const ringRef = useRef(null);
  const [label, setLabel] = useState("");
  const [hover, setHover] = useState(false);
  const pos = useRef({ x: -100, y: -100 });
  const target = useRef({ x: -100, y: -100 });
  const ringPos = useRef({ x: -100, y: -100 });

  useEffect(() => {
    // Respect reduced-motion + touch devices
    const isTouch = matchMedia("(hover: none)").matches;
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (isTouch || reduce) return;

    document.documentElement.classList.add("has-custom-cursor");

    const move = (e) => {
      target.current = { x: e.clientX, y: e.clientY };
    };
    const over = (e) => {
      const el = e.target.closest(
        "a, button, [role='button'], input, textarea, [data-cursor]"
      );
      if (el) {
        setHover(true);
        const lbl = el.getAttribute("data-cursor");
        setLabel(lbl || "");
      } else {
        setHover(false);
        setLabel("");
      }
    };

    let raf = 0;
    const tick = () => {
      pos.current.x += (target.current.x - pos.current.x) * 0.35;
      pos.current.y += (target.current.y - pos.current.y) * 0.35;
      ringPos.current.x += (target.current.x - ringPos.current.x) * 0.16;
      ringPos.current.y += (target.current.y - ringPos.current.y) * 0.16;
      if (dotRef.current) {
        dotRef.current.style.transform = `translate3d(${pos.current.x}px, ${pos.current.y}px, 0) translate(-50%, -50%)`;
      }
      if (ringRef.current) {
        ringRef.current.style.transform = `translate3d(${ringPos.current.x}px, ${ringPos.current.y}px, 0) translate(-50%, -50%)`;
      }
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);

    window.addEventListener("mousemove", move);
    window.addEventListener("mouseover", over);

    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener("mousemove", move);
      window.removeEventListener("mouseover", over);
      document.documentElement.classList.remove("has-custom-cursor");
    };
  }, []);

  return (
    <>
      <div
        ref={dotRef}
        aria-hidden
        className="pointer-events-none fixed left-0 top-0 z-[9999] h-1.5 w-1.5 rounded-full bg-white"
        style={{ mixBlendMode: "difference" }}
      />
      <div
        ref={ringRef}
        aria-hidden
        className="pointer-events-none fixed left-0 top-0 z-[9999] flex items-center justify-center rounded-full border border-white/70 transition-[width,height,background] duration-300"
        style={{
          mixBlendMode: "difference",
          width: hover ? (label ? 104 : 56) : 36,
          height: hover ? (label ? 104 : 56) : 36,
          background: hover && label ? "#fff" : "transparent"
        }}
      >
        {label ? (
          <span
            className="font-mono text-[10px] uppercase tracking-widest text-black"
            style={{ mixBlendMode: "normal" }}
          >
            {label}
          </span>
        ) : null}
      </div>
    </>
  );
}
