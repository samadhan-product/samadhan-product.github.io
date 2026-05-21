import { useEffect } from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
import Landing from "@/pages/Landing";

function GitHubPagesRedirect() {
  const navigate = useNavigate();

  useEffect(() => {
    const redirect = sessionStorage.getItem("gh-pages-redirect");
    if (redirect) {
      sessionStorage.removeItem("gh-pages-redirect");
      navigate(redirect, { replace: true });
    }
  }, [navigate]);

  return null;
}

export default function App() {
  return (
    <div className="App">
      <div className="animated-dot-field" aria-hidden="true" />
      <BrowserRouter>
        <GitHubPagesRedirect />
        <Routes>
          <Route path="/" element={<Landing />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
