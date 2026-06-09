#!/usr/bin/env python3
"""Generate consulting/SEO static HTML pages for samadhanmishra.com."""
from __future__ import annotations

import json
import pathlib
import html

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "data" / "seo-content.json"
SERVICE_DATA = ROOT / "assets" / "data" / "service-pages.json"
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

NAV = (ROOT / "assets/partials/site-nav.html").read_text(encoding="utf-8").strip()

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
  <header class="cg-hero cg-hero-compact">
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


def service_schema(name: str, desc: str, url: str) -> dict:
    return {
        "@type": "Service",
        "name": name,
        "description": desc,
        "provider": {
            "@type": "Person",
            "name": "Samadhan Mishra",
            "url": SITE + "/",
            "jobTitle": "AI Product Leader and Product Management Consultant",
            "description": "AI Product Leader for Healthcare, Insurance, Agentic Workflows and AI-Native Product Transformation",
        },
        "areaServed": "Worldwide",
        "url": url,
    }


def render_svc_list(items: list[str]) -> str:
    lis = "".join(f"<li>{esc(x)}</li>" for x in items)
    return f'<ul class="svc-list">{lis}</ul>'


def render_svc_links(links: list[dict]) -> str:
    cards = "".join(
        f'<a class="svc-link-card" href="{esc(l["href"])}">{esc(l["label"])}</a>'
        for l in links
    )
    return f'<div class="svc-link-grid">{cards}</div>'


def render_service_body(svc: dict) -> str:
    process_steps = "".join(
        f'<li class="svc-process-step"><span class="svc-process-num">{i}</span>'
        f'<span class="svc-process-text">{esc(step)}</span></li>'
        for i, step in enumerate(svc["process"], 1)
    )
    faq_html = render_faq_block(svc["faqs"]).replace('class="cg-section cg-reveal"', 'class="cg-section svc-section"')

    return f"""
<section class="svc-section svc-section--problem">
  <h2>Why this matters</h2>
  <p>{svc["why_matters"]}</p>
</section>

<section class="svc-section">
  <h2>What I Help With</h2>
  <div class="svc-card-grid svc-card-grid--2">
    {render_svc_list(svc["help_with"])}
  </div>
</section>

<section class="svc-section">
  <h2>What You Get</h2>
  <div class="svc-card svc-card--deliverables">
    {render_svc_list(svc["deliverables"])}
  </div>
</section>

<section class="svc-section">
  <h2>Who This Is For</h2>
  {render_svc_list(svc["audience"])}
</section>

<section class="svc-section">
  <h2>Expected Outcomes</h2>
  {render_svc_list(svc["outcomes"])}
</section>

<section class="svc-section svc-section--proof">
  <h2>Relevant Experience</h2>
  <p>{svc["experience"]}</p>
</section>

<section class="svc-section">
  <h2>How I Work</h2>
  <ol class="svc-process">{process_steps}</ol>
</section>

<section class="svc-section svc-geo-block" id="geo-answer">
  <h2 class="svc-geo-label">Quick answer</h2>
  <p class="svc-geo-text">{svc["geo_answer"]}</p>
</section>

{faq_html}

<section class="svc-section svc-section--related">
  <h2>Related links</h2>
  <h3 class="svc-related-kicker">Case studies</h3>
  {render_svc_links(svc["related_case_studies"])}
  <h3 class="svc-related-kicker">Other services</h3>
  {render_svc_links(svc["related_services"])}
  <p class="svc-related-more">
    <a href="/insights/">Insights</a>
    <span class="sep">·</span>
    <a href="/work-with-me/">Work With Me</a>
    <span class="sep">·</span>
    <a href="/case-studies/">All case studies</a>
  </p>
</section>
"""


def service_page(svc: dict) -> str:
    slug = svc["slug"]
    path = f"/services/{slug}/"
    url = SITE + path
    title = svc["meta_title"]
    description = svc["meta_description"]
    h1 = svc["h1"]
    hero = svc["hero_paragraph"]
    breadcrumb_label = svc["breadcrumb_label"]
    schema_name = svc["service_schema_name"]

    crumbs_html = '<nav class="cg-breadcrumbs" aria-label="Breadcrumb">\n'
    crumbs = [
        ("Home", SITE + "/"),
        ("Services", SITE + "/ai-product-management-consultant/"),
        (breadcrumb_label, url),
    ]
    for i, (name, href) in enumerate(crumbs):
        if i:
            crumbs_html += '<span class="sep">→</span>\n'
        if i == len(crumbs) - 1:
            crumbs_html += f'<span class="current">{esc(name)}</span>\n'
        else:
            crumbs_html += f'<a href="{esc(href)}">{esc(name)}</a>\n'
    crumbs_html += "</nav>\n"

    body_html = render_service_body(svc)
    faqs = svc["faqs"]

    schemas = breadcrumbs(crumbs)
    graphs = [
        person_schema(),
        {
            "@type": "WebPage",
            "name": title,
            "url": url,
            "description": description,
        },
        service_schema(schema_name, description, url),
    ]
    schemas += f'\n<script type="application/ld+json">\n{ld_json(*graphs)}\n</script>\n'
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
<body class="cg-blog-theme portal-page svc-page" data-page="service-{esc(slug)}">
  <div class="animated-dot-field" aria-hidden="true"></div>
{NAV}
{crumbs_html}
  <header class="cg-hero cg-hero-compact svc-hero">
    <div class="cg-hero-content svc-hero-inner">
      <span class="cg-pill">Samadhan Mishra · AI Product Consulting</span>
      <h1 class="cg-hero-title svc-hero-title">{h1}</h1>
      <p class="cg-hero-subtitle svc-hero-lede">{esc(hero)}</p>
      <div class="cg-hero-actions svc-hero-actions">
        <a class="cg-btn primary" href="/work-with-me/">Work With Me</a>
        <a class="cg-btn secondary" href="/case-studies/">View Case Studies</a>
      </div>
    </div>
  </header>
  <main class="cg-main svc-main">
{body_html}
{cta_block()}
  </main>
{FOOTER}
</body>
</html>
"""


CASE_STUDY_METRICS = {
    "ai-led-pre-auth-automation": {
        "role": "Lead Product Manager",
        "domain": "Healthcare TPA Operations",
        "product": "IPD Cashless Pre-Auth Workbench",
        "outcomes": [
            {"val": "Assistive AI", "lbl": "Clinical Summarization"},
            {"val": "Strict Sequence", "lbl": "Deductions Guardrails"},
            {"val": "Discharge Lane", "lbl": "Expedited Queue Routing"}
        ]
    },
    "ai-powered-cognitive-decision-engine": {
        "role": "Lead Product Manager",
        "domain": "Healthcare Operations AI",
        "product": "Enigma Cognitive DMS Engine",
        "outcomes": [
            {"val": "Multi-Modal", "lbl": "CV & NLP Models"},
            {"val": "Explainable", "lbl": "Visual Proofing Grid"},
            {"val": "Audit Logs", "lbl": "Override Verification"}
        ]
    },
    "bfhl-wellness-cohort": {
        "role": "Lead Product Manager",
        "domain": "Digital Health & Corporate Wellness",
        "product": "Wellness Engagement System",
        "outcomes": [
            {"val": "₹95 Lakhs", "lbl": "Annual Vendor Cost Saved"},
            {"val": "In-House", "lbl": "Dietician-led Care model"},
            {"val": "Gamified", "lbl": "Everest/Kilimanjaro Steps"}
        ]
    },
    "bfhl-healthpay-qr-transition": {
        "role": "Lead Product Manager (Integration)",
        "domain": "FinTech & Payment Rails",
        "product": "HealthPay-BajajPay QR Transition",
        "outcomes": [
            {"val": "Zero Downtime", "lbl": "Ecosystem Migration"},
            {"val": "Automated", "lbl": "Merchant Mapping Feed"},
            {"val": "Shared Support", "lbl": "Cross-Company SOP"}
        ]
    },
    "bfhl-partner-center-revamp": {
        "role": "Lead Product Manager",
        "domain": "B2B SaaS / Partner Portals",
        "product": "Partner Operating Center",
        "outcomes": [
            {"val": "Self-Serve", "lbl": "Settlements & Reports"},
            {"val": "Superuser", "lbl": "Hierarchical RBAC"},
            {"val": "Reduced Load", "lbl": "RM & Support Dependency"}
        ]
    },
    "bfhl-healthpay-recon-automation": {
        "role": "Lead Product Manager",
        "domain": "FinTech / Financial Operations",
        "product": "HealthPay Payout & Recon Engine",
        "outcomes": [
            {"val": "RazorpayX", "lbl": "API Payout Integration"},
            {"val": "Automated", "lbl": "Daily PG Reconciliation"},
            {"val": "Audit-Ready", "lbl": "Internal Payout Controls"}
        ]
    },
    "bfhl-service-guarantee": {
        "role": "Lead Product Manager",
        "domain": "Healthcare Service Operations",
        "product": "Fulfillment Assurance Platform",
        "outcomes": [
            {"val": "SFDC + HRx", "lbl": "System Sync Integration"},
            {"val": "Real-Time", "lbl": "Phlebo Check-in Track"},
            {"val": "Proactive", "lbl": "SLA-Breach Alerts"}
        ]
    },
    "bfhl-opd-reimbursement-claims": {
        "role": "Lead Product Manager",
        "domain": "Health Insurance Claims",
        "product": "OPD Claims Salesforce Workbench",
        "outcomes": [
            {"val": "+73%", "lbl": "Claims Processing Speed"},
            {"val": "From 75", "lbl": "Original Daily Claims/Agent"},
            {"val": "To 130", "lbl": "Revamped Daily Claims/Agent"}
        ]
    },
    "highradius-autonomous-collections": {
        "role": "Senior Product Manager",
        "domain": "Enterprise FinTech SaaS",
        "product": "Autonomous Receivables Platform",
        "outcomes": [
            {"val": "Smart Priorities", "lbl": "Delinquency Scoring Lists"},
            {"val": "Auto AP Sync", "lbl": "Direct Portal Posting"},
            {"val": "Promise-to-Pay", "lbl": "Commitment Auditing"}
        ]
    },
    "creanovation-edtech-saas": {
        "role": "Lead Product Manager",
        "domain": "EdTech CRM / SaaS",
        "product": "Forms Dot Star Admissions Suite",
        "outcomes": [
            {"val": "Unified Funnel", "lbl": "Student Lifecycle"},
            {"val": "Self-Serve", "lbl": "Document Upload Hub"},
            {"val": "Automated", "lbl": "Fee Reconciliation"}
        ]
    },
    "ai-learning-platform-for-schools": {
        "role": "Lead Product Manager",
        "domain": "EdTech AI",
        "product": "Personalized Learning Suite",
        "focus": "Adaptive Exercises & Curriculum",
        "outcomes": [
            {"val": "Adaptive", "lbl": "Personalized Exercises"},
            {"val": "Multi-Curricula", "lbl": "Automatic Content Maps"},
            {"val": "Insights", "lbl": "Teacher Feedback Portal"}
        ]
    },
    "ai-product-practice-operating-model": {
        "role": "Consultant / Practice Lead",
        "domain": "Product Practice Operating Model",
        "product": "Practice COE",
        "focus": "PM Operating Playbooks & Evals",
        "outcomes": [
            {"val": "Standardized", "lbl": "PM Operating Playbooks"},
            {"val": "Eval Sprints", "lbl": "Systematic Evals"},
            {"val": "Structured Governance", "lbl": "Model Choice Frameworks"}
        ]
    }
}


def case_study_page(cs: dict) -> str:
    import re
    slug = cs["slug"]
    path = f"/case-studies/{slug}/"
    
    if "custom_body" in cs:
        body = cs["custom_body"]
    else:
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
            body += f'<section class="cg-article-section"><h2>{esc(h)}</h2><div>{p}</div></section>\n'

    # Global conversion: Translate all standard blockquotes to editorial quotes
    body = body.replace("<blockquote>", '<blockquote class="cg-editorial-quote">')

    # Convert standard callouts to premium labels
    body = body.replace('class="cg-callout insight"', 'class="cs-callout insight"')
    body = body.replace('class="cg-callout product"', 'class="cs-callout judgment"')
    body = body.replace('class="cg-callout warning"', 'class="cs-callout principle"')
    
    body = body.replace('class="cg-callout-title"', 'class="cs-callout-header"')

    # Inject premium headers and custom tags for sections
    h2_pattern = re.compile(r'<h2>(.*?)</h2>')
    headers = h2_pattern.findall(body)
    
    toc = []
    for h in headers:
        clean_text = re.sub(r'<.*?>', '', h).strip()
        h_id = re.sub(r'[^a-z0-9]+', '-', clean_text.lower()).strip('-')
        toc.append((clean_text, h_id))

    sections_split = body.split('<section class="cg-article-section">')
    new_sections = []
    if sections_split[0].strip():
        new_sections.append(sections_split[0])
        
    chapter_num = 1
    for s in sections_split[1:]:
        h2_match = h2_pattern.search(s)
        if h2_match:
            h_text = h2_match.group(1)
            clean_text = re.sub(r'<.*?>', '', h_text).strip()
            h_id = re.sub(r'[^a-z0-9]+', '-', clean_text.lower()).strip('-')
            
            section_label = f'<span class="cs-section-label">{chapter_num:02d}. {clean_text}</span>\n<h2 id="{h_id}">{h_text}</h2>'
            s_modified = h2_pattern.sub(section_label, s, 1)
            new_sections.append(f'<section class="cg-article-section">\n{s_modified.strip()}')
            chapter_num += 1
        else:
            new_sections.append(f'<section class="cg-article-section">\n{s.strip()}')
            
    body_formatted = "".join(new_sections)

    # Add related links footer
    footer_links = f'<p style="margin-top:32px; border-top: 1px solid var(--soft); padding-top:24px;"><a class="cg-read-link" href="/case-studies/">← All case studies</a></p>'
    service = cs.get("service_link", "/ai-product-management-consultant/")
    footer_links += f'<p style="margin-top:16px;">Related service: <a href="{esc(service)}">{esc(cs.get("service_label", "AI Product Consulting"))}</a> · <a href="/insights/">Insights</a></p>'
    body_formatted += footer_links

    # Fetch metadata
    meta = CASE_STUDY_METRICS.get(slug, {
        "role": "AI Product Leader",
        "domain": "Product Strategy & Operations",
        "product": "Product Consulting Project",
        "focus": "Product Advisory",
        "outcomes": [
            {"val": "Delivered", "lbl": "Strategy Framework"},
            {"val": "Audit-Ready", "lbl": "Process SOPs"},
            {"val": "Operational", "lbl": "Production Evals"}
        ]
    })

    role = meta["role"]
    domain = meta["domain"]
    product = meta["product"]
    focus = meta.get("focus", "AI Product Strategy")
    
    outcome_cards_html = ""
    for o in meta["outcomes"]:
        outcome_cards_html += f"""
        <div class="cs-snapshot-card">
          <span class="cs-snapshot-val">{esc(o["val"])}</span>
          <span class="cs-snapshot-lbl">{esc(o["lbl"])}</span>
        </div>
        """

    # Build TOC navigation HTML
    toc_items_html = ""
    for clean_text, h_id in toc:
        toc_items_html += f'<li class="cs-toc-item"><a href="#{h_id}">{esc(clean_text)}</a></li>\n'

    title = cs["title"] + " | Case Study — Samadhan Mishra"
    description = cs["description"]
    h1 = cs["h1"]
    url = SITE + path

    schemas = breadcrumbs([
        ("Home", SITE + "/"),
        ("Case Studies", SITE + "/case-studies/"),
        (cs["short_title"], SITE + path),
    ])
    
    graphs = [
        person_schema(),
        {
            "@type": "Article",
            "headline": cs["h1"],
            "description": cs["description"],
            "author": {"@type": "Person", "name": "Samadhan Mishra"},
            "url": SITE + path,
        },
    ]
    schemas += f'\n<script type="application/ld+json">\n{ld_json(*graphs)}\n</script>\n'

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
<body class="cg-blog-theme portal-page case-study-premium" data-page="case-studies">
  <div class="animated-dot-field" aria-hidden="true"></div>
{NAV}

  <header class="cs-hero">
    <div class="cs-hero-container">
      <span class="cs-hero-eyebrow">Product Case Study</span>
      <h1 class="cs-hero-title">{esc(h1)}</h1>
      <p class="cs-hero-desc">{esc(description)}</p>
      <div class="cs-hero-chips">
        <span class="cs-hero-chip">Role: {esc(role)}</span>
        <span class="cs-hero-chip">Domain: {esc(domain)}</span>
        <span class="cs-hero-chip">Product: {esc(product)}</span>
        <span class="cs-hero-chip">Focus: {esc(focus)}</span>
      </div>
      <div class="cs-snapshot-row">
        {outcome_cards_html}
      </div>
    </div>
  </header>

  <main class="cs-layout">
    <div class="cs-content-area">
      <div class="cs-mobile-toc" id="mobile-toc">
        <button class="cs-mobile-toc-trigger" onclick="toggleMobileTOC()">
          <span>Jump to section</span>
        </button>
        <div class="cs-mobile-toc-content">
          <ul class="cs-toc-list">
            {toc_items_html}
          </ul>
        </div>
      </div>

      {body_formatted}
    </div>

    <aside class="cs-toc-sidebar">
      <nav aria-label="Table of Contents">
        <div class="cs-toc-title">On this page</div>
        <ul class="cs-toc-list">
          {toc_items_html}
        </ul>
      </nav>
    </aside>
  </main>

{FOOTER}

<script>
  function toggleMobileTOC() {{
    const el = document.getElementById('mobile-toc');
    el.classList.toggle('open');
  }}

  // Active section scroll tracking
  document.addEventListener('DOMContentLoaded', () => {{
    const observer = new IntersectionObserver(entries => {{
      entries.forEach(entry => {{
        const id = entry.target.getAttribute('id');
        if (!id) return;
        const links = document.querySelectorAll(`.cs-toc-list a[href="#${{id}}"]`);
        if (links.length === 0) return;
        if (entry.intersectionRatio > 0) {{
          document.querySelectorAll('.cs-toc-item').forEach(item => item.classList.remove('active'));
          links.forEach(link => link.parentElement.classList.add('active'));
        }}
      }});
    }}, {{ rootMargin: '-100px 0px -70% 0px' }});

    document.querySelectorAll('.cs-content-area h2[id]').forEach(h2 => {{
      observer.observe(h2);
    }});
  }});
</script>
</body>
</html>
"""


CASE_STUDY_REDIRECTS = {
    "enigma-cognitive-engine": "ai-powered-cognitive-decision-engine",
    "ai-school-hub": "ai-learning-platform-for-schools",
    "product-hero-ai-product-practice": "ai-product-practice-operating-model",
}


def redirect_page(old_slug: str, new_slug: str) -> str:
    target = f"/case-studies/{new_slug}/"
    canonical = SITE + target
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url={target}" />
  <link rel="canonical" href="{canonical}" />
  <title>Redirecting…</title>
  <script>location.replace("{target}");</script>
</head>
<body><p><a href="{target}">Continue to case study</a></p></body>
</html>
"""


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

    for old_slug, new_slug in CASE_STUDY_REDIRECTS.items():
        out = ROOT / "case-studies" / old_slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(redirect_page(old_slug, new_slug), encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    service_data = json.loads(SERVICE_DATA.read_text(encoding="utf-8"))
    for svc in service_data["services"]:
        out = ROOT / "services" / svc["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(service_page(svc), encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    print(f"Wrote {len(written)} pages")

if __name__ == "__main__":
    main()
