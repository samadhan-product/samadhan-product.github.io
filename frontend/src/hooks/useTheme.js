import { useCallback, useEffect, useState } from "react";

const KEY = "site-theme";

function readTheme() {
  return document.documentElement.getAttribute("data-theme") || "dark";
}

export function useTheme() {
  const [theme, setTheme] = useState(readTheme);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    try { localStorage.setItem(KEY, theme); } catch (_) {}
  }, [theme]);

  const toggle = useCallback(() => {
    setTheme((prev) => (prev === "dark" ? "light" : "dark"));
  }, []);

  return { theme, toggle, isDark: theme === "dark" };
}
