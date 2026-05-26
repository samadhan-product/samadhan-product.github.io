#!/usr/bin/env python3
"""Generate consulting/SEO static HTML pages for samadhanmishra.com."""
from __future__ import annotations

import json
import pathlib
import html

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "data" / "seo-content.json"
SITE = "https://samadhanmishra.com"
OG_IMAGE = f"{SITE}/assets/og/samadhan-mishra-ai-product-leader.png"
LINKEDIN = "https://www.linkedin.com/in/samadhan-mishra/"

GTAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XWSM8RBV2S"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XWSM8RBV2S');
  </script>
"""

NAV = """  <header class="site-nav" data-testid="top-nav">
    <div class="site-nav-inner">
      <a class="site-brand" href="/">
        <span class="site-logo-box">SM</span>
        <span class="site-brand-text">/ Samadhan</span>
      </a>
      <nav class="site-menu" aria-label="Primary">
        <a class="site-menu-link" href="/" data-nav="home">Home</a>
        <a class="site-menu-link" href="/case-studies/" data-nav="case-studies">Case Studies</a>
        <a class="site-menu-link" href="/insights/" data-nav="insights">Insights</a>
        <a class="site-menu-link" href="/work-with-me/" data-nav="work-with-me">Work With Me</a>
        <a class="site-menu-link" href="/portfolio/" data-nav="portfolio">Portfolio</a>
        <a class="site-menu-link" href="/blog/" data-nav="blog">Blog</a>
      </nav>
      <div class="site-nav-meta">
        <div class="site-time" aria-live="polite">
          <span class="site-time-dot" aria-hidden="true"></span>
          <span data-nav-clock></span>
        </div>
        <button type="button" class="site-theme-toggle theme-toggle" aria-label="Toggle theme" title="Toggle theme">
          <span class="theme-toggle-icon">◑</span>
        </button>
        <button type="button" class="site-nav-toggle" aria-label="Toggle menu" aria-expanded="false" data-nav-toggle>
          <span class="site-nav-toggle-bar"></span>
          <span class="site-nav-toggle-bar"></span>
        </button>
      </div>
    </div>
    <div class="site-nav-mobile" data-nav-mobile hidden>
      <nav aria-label="Mobile">
        <a class="site-menu-link" href="/" data-nav="home">Home</a>
        <a class="site-menu-link" href="/case-studies/" data-nav="case-studies">Case Studies</a>
        <a class="site-menu-link" href="/insights/" data-nav="insights">Insights</a>
        <a class="site-menu-link" href="/work-with-me/" data-nav="work-with-me">Work With Me</a>
        <a class="site-menu-link" href="/portfolio/" data-nav="portfolio">Portfolio</a>
        <a class="site-menu-link" href="/blog/" data-nav="blog">Blog</a>
      </nav>
    </div>
  </header>
"""

FOOTER = """  <footer class="cg-footer">© 2026 Samadhan Mishra · <a href="/work-with-me/">Work With Me</a></footer>
  <script src="/assets/js/theme.js"></script>
  <script src="/assets/js/nav.js"></script>
"""


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def person_schema() -> dict:
    return {
        "@type": "Person",
        "name": "Samadhan Mishra",
        "url": SITE + "/",
        "jobTitle": [
            "AI Product Leader",
            "AI Product Management Consultant",
            "Product Head",
            "Product Strategy Consultant",
        ],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Pune",
            "addressCountry": "IN",
        },
        "sameAs": [LINKEDIN],
        "knowsAbout": [
            "AI Product Management",
            "AI Agents",
            "Generative AI",
            "RAG",
            "MCP",
            "Healthcare Automation",
            "Insurance TPA",
            "Product Strategy",
            "Product Leadership",
            "Workflow Automation",
        ],
    }


def ld_json(*graphs: dict) -> str:
    payload = {"@context": "https://schema.org", "@graph": list(graphs)}
    return json.dumps(payload, indent=2, ensure_ascii=False)


def breadcrumbs(items: list[tuple[str, str]]) -> str:
    els = []
    for i, (name, url) in enumerate(items, 1):
        els.append(
            f'{{ "@type": "ListItem", "position": {i}, "name": "{esc(name)}", "item": "{esc(url)}" }}'
        )
    return (
        '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n    '
        + ",\n    ".join(els)
        + "\n  ]\n}\n</script>"
    )


def faq_schema(faqs: list[dict]) -> str:
    main = [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
        }
        for f in faqs
    ]
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": main,
            },
            indent=2,
        )
        + "\n</script>"
    )


def render_faq_block(faqs: list[dict]) -> str:
    parts = ['<section class="cg-section cg-reveal" id="faq">', "<h2>Frequently asked questions</h2>"]
    for f in faqs:
        parts.append(f"<h3>{esc(f['q'])}</h3>")
        parts.append(f"<p>{f['a']}</p>")
    parts.append("</section>")
    return "\n".join(parts)


def render_geo_block(answers: list[dict]) -> str:
    parts = [
        '<section class="cg-section cg-reveal" id="geo-answers">',
        "<h2>Quick answers</h2>",
        '<p class="cg-section-desc">Concise, factual summaries for search and AI answer engines.</p>',
    ]
    for a in answers:
        parts.append(f'<div class="cg-card" style="margin-top:16px;">')
        parts.append(f"<h3>{esc(a['q'])}</h3>")
        parts.append(f"<p>{a['a']}</p>")
        parts.append("</div>")
    parts.append("</section>")
    return "\n".join(parts)


def cta_block(primary: str = "Work With Me", primary_href: str = "/work-with-me/") -> str:
    return f"""<section class="cg-section cg-reveal" id="cta">
      <div class="cg-card large glow">
        <h2>Ready to move from AI pilots to production?</h2>
        <p>Share your workflow, constraints, and timeline. I will respond with a clear view on fit, approach, and next steps.</p>
        <div class="cg-hero-actions" style="margin-top:20px;">
          <a class="cg-btn primary" href="{esc(primary_href)}">{esc(primary)}</a>
          <a class="cg-btn secondary" href="/case-studies/">View case studies</a>
        </div>
      </div>
    </section>"""


def page(
    *,
    path: str,
    title: str,
    description: str,
    h1: str,
    body_html: str,
    data_page: str,
    breadcrumbs_items: list[tuple[str, str]],
    schema_graphs: list[dict],
    faqs: list[dict] | None = None,
    geo_answers: list[dict] | None = None,
) -> str:
    url = SITE + path
    crumbs_html = ""
    if len(breadcrumbs_items) > 1:
        crumbs_html = '<nav class="cg-breadcrumbs" aria-label="Breadcrumb">\n'
        for i, (name, href) in enumerate(breadcrumbs_items):
            if i:
                crumbs_html += '<span class="sep">→</span>\n'
            if i == len(breadcrumbs_items) - 1:
                crumbs_html += f'<span class="current">{esc(name)}</span>\n'
            else:
                crumbs_html += f'<a href="{esc(href)}">{esc(name)}</a>\n'
        crumbs_html += "</nav>\n"

    extra = ""
    if geo_answers:
        extra += render_geo_block(geo_answers)
    if faqs:
        extra += render_faq_block(faqs)

    schemas = breadcrumbs(breadcrumbs_items)
    schemas += f'\n<script type="application/ld+json">\n{ld_json(*schema_graphs)}\n</script>\n'
    if faqs:
        schemas += faq_schema(faqs) + "\n"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{esc(description)}" />
  <title>{esc(title)}</title>
  <link rel="canonical" href="{esc(url)}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:url" content="{esc(url)}" />
  <meta property="og:site_name" content="Samadhan Mishra" />
  <meta property="og:image" content="{OG_IMAGE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(description)}" />
  <meta name="twitter:image" content="{OG_IMAGE}" />
  <script>!function(){{var t=localStorage.getItem('site-theme')||'dark';document.documentElement.setAttribute('data-theme',t)}}();</script>
  <link rel="stylesheet" href="/assets/css/style.css" />
{schemas}
</head>
<body class="cg-blog-theme portal-page" data-page="{esc(data_page)}">
  <div class="animated-dot-field" aria-hidden="true"></div>
{NAV}
{crumbs_html}
  <header class="cg-hero cg-hero-compact cg-reveal">
    <div class="cg-hero-content" style="max-width:800px;">
      <span class="cg-pill">Samadhan Mishra · AI Product Consulting</span>
      <h1 class="cg-hero-title" style="font-size:clamp(2rem,5vw,3rem);">{h1}</h1>
      <p class="cg-hero-subtitle">{esc(description)}</p>
    </div>
  </header>
  <main class="cg-main cg-article-content" style="max-width:800px;margin:0 auto;padding:0 24px 80px;">
{body_html}
{extra}
{cta_block()}
  </main>
{FOOTER}
</body>
</html>
"""


def case_study_page(cs: dict) -> str:
    slug = cs["slug"]
    path = f"/case-studies/{slug}/"
    sections = [
        ("Context", cs["context"]),
        ("Business problem", cs["problem"]),
        ("User or operational pain", cs["pain"]),
        ("Product intervention", cs["intervention"]),
        ("AI capability used", cs["ai"]),
        ("Samadhan's role", cs["role"]),
        ("Business outcome", cs["outcome"]),
        ("Lessons for other companies", cs["lessons"]),
    ]
    body = ""
    for h, p in sections:
        body += f'<section class="cg-article-section"><h2>{esc(h)}</h2><p>{p}</p></section>\n'
    body += f'<p><a class="cg-read-link" href="/case-studies/">← All case studies</a></p>'

    service = cs.get("service_link", "/ai-product-management-consultant/")
    body += f'<p style="margin-top:16px;">Related service: <a href="{esc(service)}">{esc(cs.get("service_label", "AI Product Consulting"))}</a> · <a href="/insights/">Insights</a></p>'

    return page(
        path=path,
        title=cs["title"] + " | Case Study — Samadhan Mishra",
        description=cs["description"],
        h1=cs["h1"],
        body_html=body,
        data_page="case-studies",
        breadcrumbs_items=[
            ("Home", SITE + "/"),
            ("Case Studies", SITE + "/case-studies/"),
            (cs["short_title"], SITE + path),
        ],
        schema_graphs=[
            person_schema(),
            {
                "@type": "Article",
                "headline": cs["h1"],
                "description": cs["description"],
                "author": {"@type": "Person", "name": "Samadhan Mishra"},
                "url": SITE + path,
            },
        ],
    )


def main() -> None:
    import sys

    sys.path.insert(0, str(ROOT / "scripts"))
    from seo_landing_definitions import build_landing_pages

    data = json.loads(DATA.read_text(encoding="utf-8"))
    written = []
    shared_faqs = data.get("shared_faqs", [])
    shared_geo = data.get("shared_geo", [])
    landing_pages = build_landing_pages(shared_faqs, shared_geo)

    for p in landing_pages:
        out = ROOT / p["file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        crumbs = [
            (b[0], b[1] if str(b[1]).startswith("http") else SITE + b[1])
            for b in p["breadcrumbs"]
        ]
        graphs = [person_schema()] + p.get("schema", [])
        html_out = page(
            path=p["path"],
            title=p["title"],
            description=p["description"],
            h1=p["h1"],
            body_html=p["body"],
            data_page=p["data_page"],
            breadcrumbs_items=crumbs,
            schema_graphs=graphs,
            faqs=p.get("faqs") if p.get("faqs") is not None else None,
            geo_answers=p.get("geo_answers") if p.get("geo_answers") is not None else None,
        )
        out.write_text(html_out, encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    for cs in data["case_studies"]:
        out = ROOT / "case-studies" / cs["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(case_study_page(cs), encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    print(f"Wrote {len(written)} pages")

if __name__ == "__main__":
    main()
