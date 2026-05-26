"""Landing and service page definitions for generate_seo_pages.py."""

SITE = "https://samadhanmishra.com"


def service_schema(name: str, desc: str, url: str) -> dict:
    return {
        "@type": "Service",
        "name": name,
        "description": desc,
        "provider": {"@type": "Person", "name": "Samadhan Mishra", "url": SITE + "/"},
        "areaServed": "Worldwide",
        "url": url,
    }


def links_block(items: list[tuple[str, str]]) -> str:
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in items)
    return f'<ul class="cg-toc-list" style="margin:16px 0;">{lis}</ul>'


def build_landing_pages(shared_faqs, shared_geo) -> list[dict]:
    pages = []

    def add(
        file_path,
        path,
        title,
        description,
        h1,
        body,
        data_page,
        crumbs,
        service_schema_obj=None,
        faqs=None,
        geo=None,
    ):
        graphs = [{"@type": "WebPage", "name": title, "url": SITE + path, "description": description}]
        if service_schema_obj:
            graphs.append(service_schema_obj)
        pages.append(
            {
                "file": file_path,
                "path": path,
                "title": title,
                "description": description,
                "h1": h1,
                "body": body,
                "data_page": data_page,
                "breadcrumbs": crumbs,
                "schema": graphs,
                "faqs": faqs or shared_faqs,
                "geo_answers": geo or shared_geo,
            }
        )

    # —— Main landing pages ——
    add(
        "ai-product-leader/index.html",
        "/ai-product-leader/",
        "AI Product Leader | Samadhan Mishra",
        "Samadhan Mishra is an AI Product Leader helping companies ship AI-native products, agentic workflows, and healthcare automation with accountable product governance.",
        "AI Product Leader for Production-Grade AI Products",
        """<section class="cg-article-section"><h2>What an AI Product Leader brings</h2>
<p>An AI Product Leader connects strategy, workflow design, model decisions, and execution governance. The role is not to chase demos—it is to ship features that survive compliance, cost, and operational reality.</p>
<h2>How I work with leadership teams</h2>
<p>Engagements typically include portfolio prioritization, model and architecture choices, eval design, operating rituals, and hands-on product direction for high-stakes workflows.</p>
<h2>Representative outcomes</h2>
<p>Health insurance TPA portfolios with measurable TAT reduction, settlement accuracy, and scaled PM teams—grounded in production systems, not slideware.</p>
""" + links_block([
            ("Case studies", "/case-studies/"),
            ("AI Product Management Consultant", "/ai-product-management-consultant/"),
            ("Work with me", "/work-with-me/"),
        ]),
        "ai-product-leader",
        [("Home", "/"), ("AI Product Leader", "/ai-product-leader/")],
    )

    add(
        "ai-product-management-consultant/index.html",
        "/ai-product-management-consultant/",
        "AI Product Management Consultant | Samadhan Mishra",
        "AI Product Management Consultant for startups and enterprises—use-case selection, RAG, agents, evals, model tiering, and production roadmaps.",
        "AI Product Management Consultant",
        """<section class="cg-article-section"><h2>When companies hire an AI PM consultant</h2>
<p>Teams hire when pilots multiply but production stalls: unclear evals, rising token costs, inconsistent safety, or no shared decision framework across product and engineering.</p>
<h2>What I deliver</h2>
<p>Clarity on what to build, how to measure it, which models and patterns fit, and how to govern releases—documented in memos your leadership can defend.</p>
<h2>Services</h2>
""" + links_block([
            ("AI Product Strategy", "/services/ai-product-strategy/"),
            ("RAG & knowledge systems", "/services/rag-knowledge-systems/"),
            ("AI agents", "/services/ai-agents-workflow-automation/"),
            ("Healthcare & insurance AI", "/services/healthcare-insurance-ai/"),
        ]),
        "ai-product-management-consultant",
        [("Home", "/"), ("AI Product Management Consultant", "/ai-product-management-consultant/")],
        service_schema(
            "AI Product Management Consulting",
            "Consulting for AI product strategy, evals, RAG, agents, and production roadmaps.",
            SITE + "/ai-product-management-consultant/",
        ),
    )

    add(
        "ai-agents-consultant/index.html",
        "/ai-agents-consultant/",
        "AI Agents Consultant | Samadhan Mishra",
        "AI agents consultant for workflow automation—scope, tools, HITL, observability, cost per run, and blast-radius controls.",
        "AI Agents Consultant for Governed Workflow Automation",
        """<section class="cg-article-section"><h2>Agents are a product problem first</h2>
<p>Tool lists and prompts are not a strategy. I help teams define agent scope, stopping conditions, human checkpoints, and what “done” means for operational workflows.</p>
<h2>Typical engagements</h2>
<p>Agent PRDs, tool permission design, eval suites for multi-step runs, cost models per workflow, and production observability requirements.</p>
""" + links_block([
            ("Network claims case study", "/case-studies/network-claims-automation/"),
            ("AI agents service page", "/services/ai-agents-workflow-automation/"),
            ("Insights", "/insights/"),
        ]),
        "ai-agents-consultant",
        [("Home", "/"), ("AI Agents Consultant", "/ai-agents-consultant/")],
        service_schema("AI Agents Consulting", "Agent scope, tools, HITL, and production governance.", SITE + "/ai-agents-consultant/"),
    )

    add(
        "healthcare-ai-product-consultant/index.html",
        "/healthcare-ai-product-consultant/",
        "Healthcare AI Product Consultant | Samadhan Mishra",
        "Healthcare AI product consultant for TPA, claims, pre-auth, and clinical operations—workflow-first automation with compliance-aware design.",
        "Healthcare AI Product Consultant",
        """<section class="cg-article-section"><h2>Healthcare AI requires workflow truth</h2>
<p>Claims, pre-auth, and provider operations fail when AI is bolted onto broken handoffs. I start with systems of record, operator journeys, and audit requirements.</p>
<h2>Domains</h2>
<p>Pre-authorization, claims adjudication, network operations, document understanding, and payment/settlement automation.</p>
""" + links_block([
            ("Pre-auth case study", "/case-studies/ai-led-pre-auth-automation/"),
            ("Cognitive decision engine case study", "/case-studies/ai-powered-cognitive-decision-engine/"),
            ("Healthcare AI service", "/services/healthcare-insurance-ai/"),
        ]),
        "healthcare-ai-product-consultant",
        [("Home", "/"), ("Healthcare AI Product Consultant", "/healthcare-ai-product-consultant/")],
        service_schema("Healthcare AI Product Consulting", "TPA, claims, and clinical workflow AI products.", SITE + "/healthcare-ai-product-consultant/"),
    )

    add(
        "product-leadership-advisory/index.html",
        "/product-leadership-advisory/",
        "Product Leadership Advisory | Samadhan Mishra",
        "Product leadership advisory for AI portfolios—operating models, rituals, hiring bar, and executive decision frameworks.",
        "Product Leadership Advisory for AI Portfolios",
        """<section class="cg-article-section"><h2>Advisory for founders and product executives</h2>
<p>I advise on building AI product practice: intake, prioritization, model selection discipline, release governance, and cross-functional alignment.</p>
<h2>Formats</h2>
<p>Monthly advisory, strategy sprints, board-ready narratives, and interim product leadership for critical initiatives.</p>
""" + links_block([
            ("AI product practice case study", "/case-studies/ai-product-practice-operating-model/"),
            ("Operating model service", "/services/product-operating-model/"),
            ("Speaking", "/speaking-workshops/"),
        ]),
        "product-leadership-advisory",
        [("Home", "/"), ("Product Leadership Advisory", "/product-leadership-advisory/")],
        service_schema("Product Leadership Advisory", "Advisory for AI product operating models and portfolios.", SITE + "/product-leadership-advisory/"),
    )

    add(
        "case-studies/index.html",
        "/case-studies/",
        "AI Product Case Studies | Samadhan Mishra",
        "Case studies in healthcare AI, pre-auth automation, cognitive engines, network claims, EdTech AI, and AI product practice.",
        "AI Product Case Studies",
        """<section class="cg-article-section cg-case-study-list">
<p>Production-oriented case studies across health insurance TPA, cognitive automation, agentic workflow mapping, and AI education platforms.</p>
<div class="cg-case-study-cards">
<a class="cg-card glow is-link" href="/case-studies/ai-led-pre-auth-automation/"><h3>AI-Led Pre-Authorisation Automation</h3><p>Insurance pre-authorisation turnaround and governance.</p></a>
<a class="cg-card glow is-link" href="/case-studies/ai-powered-cognitive-decision-engine/"><h3>AI-Powered Cognitive Decision Engine</h3><p>Document understanding and decision support.</p></a>
<a class="cg-card glow is-link" href="/case-studies/network-claims-automation/"><h3>AI-Led Network Claims Automation</h3><p>Agentic mapping across claims and FinOps.</p></a>
<a class="cg-card glow is-link" href="/case-studies/ai-learning-platform-for-schools/"><h3>AI Learning Platform for Schools</h3><p>Structured AI education for institutions.</p></a>
<a class="cg-card glow is-link" href="/case-studies/ai-product-practice-operating-model/"><h3>AI Product Practice Operating Model</h3><p>Portfolio governance for AI initiatives.</p></a>
</div>
</section>""",
        "case-studies",
        [("Home", "/"), ("Case Studies", "/case-studies/")],
        faqs=None,
        geo=None,
    )

    add(
        "speaking-workshops/index.html",
        "/speaking-workshops/",
        "Speaking & Workshops | Samadhan Mishra",
        "Talks and workshops on AI product leadership, agents, RAG, healthcare automation, and product operating models for leadership teams.",
        "Speaking & Workshops",
        """<section class="cg-article-section"><h2>Topics</h2>
<ul><li>From AI pilots to production</li><li>Agentic workflows and HITL design</li><li>RAG and knowledge systems for enterprises</li><li>Healthcare and insurance automation</li><li>AI product operating models</li></ul>
<p>Formats: executive briefings, product team workshops, and conference keynotes. <a href="/work-with-me/">Request a speaking engagement</a>.</p></section>""",
        "speaking-workshops",
        [("Home", "/"), ("Speaking & Workshops", "/speaking-workshops/")],
        faqs=[],
        geo=[],
    )

    add(
        "insights/index.html",
        "/insights/",
        "Insights | Samadhan Mishra — AI Product Leadership",
        "Essays and structured learning on AI product management, agents, RAG, and production AI—by Samadhan Mishra.",
        "Insights on AI Product Leadership",
        """<section class="cg-article-section"><h2>Writing & learning</h2>
<p>Long-form product thinking and structured AI learning for product leaders.</p>
<a class="cg-card glow is-link" href="/blog/ai-learning/"><h3>AI Learning — structured syllabus</h3><p>Modules on LLM mechanics, model landscape, prompting, RAG, and agents.</p></a>
<a class="cg-card glow is-link" href="/blog/" style="margin-top:12px;display:block;"><h3>Blog</h3><p>Notes on AI product management and digital transformation.</p></a>
<p style="margin-top:16px;">Related: <a href="/ai-product-management-consultant/">AI Product Management Consultant</a> · <a href="/case-studies/">Case studies</a></p></section>""",
        "insights",
        [("Home", "/"), ("Insights", "/insights/")],
        faqs=[],
        geo=[],
    )

    add(
        "work-with-me/index.html",
        "/work-with-me/",
        "Work With Me | Samadhan Mishra — AI Product Consulting",
        "Engage Samadhan Mishra for AI product strategy, agents, RAG, healthcare automation, and product leadership advisory.",
        "Work With Me",
        """<section class="cg-article-section"><h2>Engagement types</h2>
<ul><li><strong>Advisory</strong> — ongoing product leadership for AI portfolios</li>
<li><strong>Strategy sprint</strong> — 2–4 week focus on use case, architecture, and roadmap</li>
<li><strong>Hands-on product leadership</strong> — embedded leadership for critical initiatives</li>
<li><strong>Speaking</strong> — <a href="/speaking-workshops/">workshops and executive sessions</a></li></ul>
<h2>How to start</h2>
<p>Email <a href="mailto:me@samadhanmishra.com">me@samadhanmishra.com</a> or connect on <a href="https://www.linkedin.com/in/samadhan-mishra/" rel="noopener">LinkedIn</a> with:</p>
<ul><li>Company context and industry</li><li>Workflow or product area</li><li>Timeline and decision makers</li><li>What success looks like in 90 days</li></ul>
<p>I reply to serious inquiries within one business day.</p></section>""",
        "work-with-me",
        [("Home", "/"), ("Work With Me", "/work-with-me/")],
        faqs=shared_faqs,
        geo=shared_geo,
    )

    # Service detail pages are generated from assets/data/service-pages.json

    return pages
