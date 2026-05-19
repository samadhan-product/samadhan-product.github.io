import { useEffect, useRef } from "react";
import * as THREE from "three";

/**
 * Full-screen GLSL shader canvas (shader.se inspired).
 * Renders an animated warped noise field, reacts to scroll + mouse.
 * Uses a single fullscreen triangle — cheap, smooth, beautiful.
 */
export default function ShaderBackground() {
  const hostRef = useRef(null);

  useEffect(() => {
    const host = hostRef.current;
    if (!host) return;

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance"
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x050505, 1);
    host.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

    const uniforms = {
      u_time: { value: 0 },
      u_res: { value: new THREE.Vector2(1, 1) },
      u_mouse: { value: new THREE.Vector2(0.5, 0.5) },
      u_scroll: { value: 0 }
    };

    const vert = /* glsl */ `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = vec4(position, 1.0);
      }
    `;

    // Warped domain FBM in grayscale with a thin glow band — shader.se vibe.
    const frag = /* glsl */ `
      precision highp float;
      varying vec2 vUv;
      uniform float u_time;
      uniform vec2  u_res;
      uniform vec2  u_mouse;
      uniform float u_scroll;

      // Hash / noise
      float hash(vec2 p) {
        return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453123);
      }
      float noise(vec2 p){
        vec2 i = floor(p); vec2 f = fract(p);
        float a = hash(i);
        float b = hash(i+vec2(1.,0.));
        float c = hash(i+vec2(0.,1.));
        float d = hash(i+vec2(1.,1.));
        vec2 u = f*f*(3.-2.*f);
        return mix(a,b,u.x) + (c-a)*u.y*(1.-u.x) + (d-b)*u.x*u.y;
      }
      float fbm(vec2 p){
        float s = 0.0; float a = 0.5;
        for(int i=0;i<5;i++){
          s += a * noise(p);
          p *= 2.02;
          a *= 0.5;
        }
        return s;
      }

      void main(){
        vec2 uv = (gl_FragCoord.xy - 0.5*u_res) / u_res.y;
        float t = u_time * 0.08 + u_scroll * 0.6;

        // Mouse influence
        vec2 m = u_mouse - 0.5;
        uv += m * 0.25;

        // Warped domain
        vec2 q = vec2(fbm(uv + vec2(0.0, t)),
                      fbm(uv + vec2(5.2, -t)));
        vec2 r = vec2(fbm(uv + 4.0*q + vec2(1.7, 9.2) + t),
                      fbm(uv + 4.0*q + vec2(8.3, 2.8) - t));
        float f = fbm(uv + 4.0*r);

        // Rings / contours
        float band = smoothstep(0.02, 0.0, abs(fract(f*6.0 + t*0.5) - 0.5) - 0.02);

        // Base grayscale field
        float g = pow(f, 1.6);
        vec3 col = vec3(g);

        // Vignette
        float vig = smoothstep(1.2, 0.2, length(uv));
        col *= vig;

        // Subtle warm highlight on contour
        col += band * vec3(0.85, 0.82, 0.78) * 0.35;

        // Desaturate → near-monochrome
        float lum = dot(col, vec3(0.299,0.587,0.114));
        col = mix(vec3(lum), col, 0.35);

        // Deep blacks
        col *= 0.65;
        col += 0.02;

        // Grain
        float n = (hash(gl_FragCoord.xy + u_time) - 0.5) * 0.04;
        col += n;

        gl_FragColor = vec4(col, 1.0);
      }
    `;

    const material = new THREE.ShaderMaterial({
      uniforms,
      vertexShader: vert,
      fragmentShader: frag
    });
    const geometry = new THREE.PlaneGeometry(2, 2);
    const mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);

    const resize = () => {
      const w = host.clientWidth;
      const h = host.clientHeight;
      renderer.setSize(w, h, false);
      uniforms.u_res.value.set(w, h);
    };
    resize();
    window.addEventListener("resize", resize);

    const onMove = (e) => {
      uniforms.u_mouse.value.set(
        e.clientX / window.innerWidth,
        1 - e.clientY / window.innerHeight
      );
    };
    const onScroll = () => {
      const max = Math.max(1, document.body.scrollHeight - window.innerHeight);
      uniforms.u_scroll.value = window.scrollY / max;
    };
    window.addEventListener("mousemove", onMove);
    window.addEventListener("scroll", onScroll, { passive: true });

    const start = performance.now();
    let raf = 0;
    const loop = () => {
      uniforms.u_time.value = (performance.now() - start) / 1000;
      renderer.render(scene, camera);
      raf = requestAnimationFrame(loop);
    };
    raf = requestAnimationFrame(loop);

    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener("resize", resize);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("scroll", onScroll);
      geometry.dispose();
      material.dispose();
      renderer.dispose();
      if (renderer.domElement.parentNode === host) {
        host.removeChild(renderer.domElement);
      }
    };
  }, []);

  return (
    <div
      ref={hostRef}
      aria-hidden
      data-testid="hero-shader-canvas"
      className="pointer-events-none absolute inset-0 h-full w-full"
      style={{ contain: "strict" }}
    />
  );
}
