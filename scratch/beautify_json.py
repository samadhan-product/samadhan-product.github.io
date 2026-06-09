import json
import pathlib

ROOT = pathlib.Path("/Users/samadhan.mishra/Documents/Projects V2/Samadhan Papers/samadhan-product.github.io")
DATA_FILE = ROOT / "assets" / "data" / "seo-content.json"

def beautify_case_studies():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. bfhl-wellness-cohort
    for cs in data["case_studies"]:
        if cs["slug"] == "bfhl-wellness-cohort":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Wellness products often fail because they treat health as information.</p>
  
  <div class="cg-highlight-grid">
    <div class="cg-highlight-card">
      <h4>Information Dump</h4>
      <p>Give users articles, show them step counts, offer a one-time consultation, and send a few generic push notifications.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Engagement Drop</h4>
      <p>Without gamification, narrative progress, social pressure, or active care loops, user retention drops to near zero within days.</p>
    </div>
  </div>

  <p>When I moved into BFHL's Wellness cohort, the challenge was to build something more durable: a system that could help users stay active, get expert nutrition support, build healthier routines, and give corporate clients a credible wellness proposition.</p>

  <blockquote class="cg-editorial-quote">
    How do you turn wellness from a passive feature into a repeatable engagement and care-delivery engine?
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>The metrics that mattered</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">₹95 Lakhs</span>
      <span class="cg-stat-lbl">Annual Vendor Cost Saved</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">100%</span>
      <span class="cg-stat-lbl">In-House Care Delivery</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Active Users</span>
      <span class="cg-stat-lbl">Primary Engagement Goal</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>The situation</h2>
  <p>BFHL had a strong opportunity in corporate wellness. GMC customers and corporate clients were looking for more than insurance or one-time health benefits. They wanted engagement, prevention, lifestyle support, and visible employee participation.</p>
  <p>At the same time, users needed help with basic but difficult behaviour change: walking more, staying active consistently, improving diet, losing weight, getting expert guidance, and staying accountable beyond the first few days.</p>
</section>

<section class="cg-article-section">
  <h2>What was actually broken</h2>
  <p>The wellness problem was not lack of content. Most users already know they should walk more and eat better. The issue is that knowing does not create behaviour change.</p>

  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Vendor-Dependent Limitations</h4>
      <ul class="cg-compare-list">
        <li>High cost and low margins due to paying external dietician vendors.</li>
        <li>Fragmented consultations with zero continuity or post-call tracking.</li>
        <li>Passive step tracking with no social, milestone, or narrative triggers.</li>
        <li>Corporate dashboards showing enrollments instead of active participation.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Custom-Built In-House Model</h4>
      <ul class="cg-compare-list">
        <li>Custom dietician platform cutting vendor dependency entirely (₹95L saving).</li>
        <li>EMR records, follow-up scheduling, and chat built directly into the workflow.</li>
        <li>Gamified themed routes (Everest, Kilimanjaro) and team challenges.</li>
        <li>Measurable active engagement supporting corporate GMC retention.</li>
      </ul>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>The product insight</h2>
  <blockquote class="cg-editorial-quote">
    Wellness is not a content problem. It is a habit, motivation, and guided-care problem.
  </blockquote>
  <p>Instead of building disconnected wellness features, the cohort had to create two connected engines:</p>
  <ol>
    <li><strong>An engagement engine</strong> through gamified activity challenges.</li>
    <li><strong>A guided-care engine</strong> through an in-house dietician platform.</li>
  </ol>
</section>

<section class="cg-article-section">
  <h2>Track 1: Gamified activity and step-tracker challenges</h2>
  <p>We designed activity journeys where users could participate in themed challenges, complete daily tasks, compete on leaderboards, earn rewards, and progress through virtual routes. The goal was not only to count steps, but to make movement feel like progress.</p>

  <div class="cg-highlight-grid">
    <div class="cg-highlight-card">
      <h4>Narrative Progress</h4>
      <p>Everest and Kilimanjaro-style virtual journeys converting steps into visible milestones.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Social Pressure</h4>
      <p>Team challenges and real-time leaderboards creating positive peer accountability.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Completion Loops</h4>
      <p>Reward mechanics and status pills reinforcing daily physical activity goals.</p>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Track 2: Building the in-house dietician platform</h2>
  <p>We built a custom platform for in-house dieticians and launched it with 3 dieticians initially. The platform fully replaced external dietician vendors, saving ₹95 lakhs, and giving BFHL total control over the nutrition journey.</p>

  <div class="cg-flow-track">
    <div class="cg-flow-step">
      <div class="cg-flow-num">1</div>
      <div class="cg-flow-text">
        <h4>Comprehensive Assessment</h4>
        <p>Dieticians capture health history, medical conditions, food preferences, and a 24-hour diet recall.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">2</div>
      <div class="cg-flow-text">
        <h4>TAT-Driven Plan Creation</h4>
        <p>Personalized diet and nutrition plans are generated and assigned within strict Turnaround Time SLA limits.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">3</div>
      <div class="cg-flow-text">
        <h4>Follow-up Scheduling & Chat</h4>
        <p>Platform schedules next reviews automatically, sending notifications and enabling continuous chat support to resolve daily dietary doubts.</p>
      </div>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Why this mattered for BFHL</h2>
  <p>This project strengthened BFHL's wellness proposition in three ways:</p>
  <ul>
    <li><strong>It improved control:</strong> BFHL no longer had to depend on external dietician vendors.</li>
    <li><strong>It improved economics:</strong> Replacing external vendors generated ₹95 lakhs in recurring savings.</li>
    <li><strong>It improved product depth:</strong> Wellness became more than content, moving toward guided nutrition support, active gamification, and habit-building.</li>
  </ul>
</section>
"""

        # 2. bfhl-healthpay-qr-transition
        if cs["slug"] == "bfhl-healthpay-qr-transition":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Payment migrations look simple from the outside: replace one QR with another, move merchants to a new payment rail, sync transaction feeds, and roll out to the field. In reality, it is far more fragile.</p>
  
  <blockquote class="cg-editorial-quote">
    A QR code sitting at a doctor clinic, lab, or hospital is not just a payment artifact. It is tied to merchant onboarding, field sales, logistics, customer payment journeys, settlement visibility, refunds, support workflows, and reconciliation.
  </blockquote>

  <p>The HealthPay–BajajPay transition was a strategic initiative to move a live healthcare payment ecosystem onto BajajPay infrastructure while preserving business continuity, provider trust, customer experience, and operational control.</p>
</section>

<section class="cg-article-section">
  <h2>Project Parameters</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">Group Rail</span>
      <span class="cg-stat-lbl">BajajPay Migration</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Ecosystem</span>
      <span class="cg-stat-lbl">Doctors, Labs, Hospitals</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Zero</span>
      <span class="cg-stat-lbl">Disruption Tolerance</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>What was actually broken or risky</h2>
  
  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Migration Risks</h4>
      <ul class="cg-compare-list">
        <li>Existing QR standees mapped to incorrect UPI IDs causing failed settlements.</li>
        <li>Payment failures at hospitals/labs damaging provider trust and patience.</li>
        <li>Support escalation loops due to cross-company ownership gaps.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Mitigation Architecture</h4>
      <ul class="cg-compare-list">
        <li>Comprehensive transaction-to-merchant mapping layers linking UPI IDs.</li>
        <li>Coordinated support SOPs routing issues between BFHL and BFL teams.</li>
        <li>Structured field logistics and physicalstandee placement verification.</li>
      </ul>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>What I shaped</h2>
  <p>My contribution was concentrated around requirement definition, solutioning, merchant onboarding flows, QR migration planning, transaction and settlement feed requirements, logistics/service SOPs, support workflows, and UAT support.</p>

  <div class="cg-highlight-grid">
    <div class="cg-highlight-card">
      <h4>Merchant Onboarding</h4>
      <p>Designed bulk-upload templates and tailored onboarding flows for doctors (KYC, clinic details) and labs (center capacity, pricing packages).</p>
    </div>
    <div class="cg-highlight-card">
      <h4>QR Logistics & Lifecycle</h4>
      <p>Designed the printing, delivery, validation, and standee mapping process for physical QRs, establishing the field-force SOP.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Feed Synchronization</h4>
      <p>Drafted specifications for real-time transaction webhooks, settlement SFTP files, and error-handling mechanisms to feed partner portals.</p>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Support split and health-plan checkout</h2>
  <p>We designed a joint support model where client-facing issues were routed depending on checkout origin. In parallel, health-plan voucher consumption rules were mapped into the 3-in-1 application layout so users could check out using benefits seamlessly.</p>
</section>
"""

        # 3. bfhl-healthpay-recon-automation
        if cs["slug"] == "bfhl-healthpay-recon-automation":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Payment systems look simple when a transaction succeeds. But behind that simple moment sits a complicated financial chain: payment gateways, benefit consumption, voucher usage, claims, settlement reports, payout rails, reversals, and audit trails.</p>

  <blockquote class="cg-editorial-quote">
    In HealthPay, that complexity had become an operating problem. We needed to automate pay-in and payout reconciliation across multiple partners and payment rails.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Impact Metrics</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">Automated</span>
      <span class="cg-stat-lbl">Pay-In & Payout Recon</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">RazorpayX</span>
      <span class="cg-stat-lbl">Payout Rail Integration</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Audit-Ready</span>
      <span class="cg-stat-lbl">Financial Controls Layer</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>The Core Reconciliation Framework</h2>
  <p>We divided the financial validation layer into three critical pipelines, turning manual checks into automated rules:</p>

  <div class="cg-flow-track">
    <div class="cg-flow-step">
      <div class="cg-flow-num">1</div>
      <div class="cg-flow-text">
        <h4>Pay-In Reconciliation</h4>
        <p>Matches transaction logs from customers, payment gateways, and banking records to verify cash received.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">2</div>
      <div class="cg-flow-text">
        <h4>Benefit Consumption & Voucher Sync</h4>
        <p>Ensures that claims paid using corporate wellness benefits or insurance balances match actual account drawdowns without over-consumption.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">3</div>
      <div class="cg-flow-text">
        <h4>Payout & Settlement Automation</h4>
        <p>Integrates RazorpayX to trigger automatic vendor settlements while running verification checks for bank account validity, IFSC codes, and transaction states.</p>
      </div>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>What was actually broken</h2>
  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Manual Processing Pain</h4>
      <ul class="cg-compare-list">
        <li>Finance teams downloading spreadsheets from multiple payment gateways daily.</li>
        <li>Manual calculation of doctor payouts, room caps, and voucher splits.</li>
        <li>Settlement delays causing partner friction and ticket volume spikes.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Automated Financial Controls</h4>
      <ul class="cg-compare-list">
        <li>Automated file parsing and PG-to-internal transaction matching engines.</li>
        <li>Daily programmatic settlement triggers via RazorpayX APIs.</li>
        <li>Comprehensive transaction dashboards surfacing anomalies to operations teams.</li>
      </ul>
    </div>
  </div>
</section>
"""

        # 4. bfhl-service-guarantee
        if cs["slug"] == "bfhl-service-guarantee":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>A booking confirmation does not always mean the service will happen. In healthcare, a customer books a lab test or a doctor appointment, but the actual fulfillment still depends on clinic availability, sample collection logistics, and report delivery.</p>

  <blockquote class="cg-editorial-quote">
    If any one of those steps fails, the customer does not see a backend issue. They see broken trust.
  </blockquote>

  <p>The Service Guarantee initiative aimed to make lab test bookings and doctor appointments reliable by converting fragmented follow-ups into a structured, trackable, communication-led operating model.</p>
</section>

<section class="cg-article-section">
  <h2>Project Pillars</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">SFDC + HRx</span>
      <span class="cg-stat-lbl">System Orchestration</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Real-time</span>
      <span class="cg-stat-lbl">Status Mapping</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Fulfillment</span>
      <span class="cg-stat-lbl">Assurance Model</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>The Fulfillment Workflow</h2>
  
  <div class="cg-flow-track">
    <div class="cg-flow-step">
      <div class="cg-flow-num">1</div>
      <div class="cg-flow-text">
        <h4>Booking Orchestration</h4>
        <p>Syncs clinic slot availability, doctor calendars, and partner locations to prevent duplicate booking slips.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">2</div>
      <div class="cg-flow-text">
        <h4>Logistics & Phlebo Tracking</h4>
        <p>Tracks sample collector assignments, home collection check-ins, and sample transit timestamps in real time.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">3</div>
      <div class="cg-flow-text">
        <h4>Report Upload SLA Control</h4>
        <p>Flags delayed reports, automatically triggering SMS/WhatsApp reminders to partner labs, and routing exceptions to operational recovery queues.</p>
      </div>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Before and After the Revamp</h2>
  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Fragmented Booking Journey</h4>
      <ul class="cg-compare-list">
        <li>Confirmation sent without verifying doctor availability.</li>
        <li>No visibility on whether a phlebotomist actually visited.</li>
        <li>Users calling customer support to ask for report status.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Structured Service Guarantee</h4>
      <ul class="cg-compare-list">
        <li>Real-time sync between booking system, provider portal, and partner PMS.</li>
        <li>Automated collector mapping with physical check-in status.</li>
        <li>Proactive alert engines signaling SLA breaches for quick intervention.</li>
      </ul>
    </div>
  </div>
</section>
"""

        # 5. bfhl-opd-reimbursement-claims
        if cs["slug"] == "bfhl-opd-reimbursement-claims":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Claims processing problems rarely announce themselves as product problems. On the surface, the issues look operational: claims taking time, agents switching screens, missing documents, duplicate requests, and mounting backlogs.</p>

  <blockquote class="cg-editorial-quote">
    I went to the call center and sat with the claim processing agents. This was not just a Salesforce workflow project. It was a redesign of how OPD reimbursement claims should be processed, prioritized, and moved toward assisted decisioning.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Core Outcome</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">+73%</span>
      <span class="cg-stat-lbl">Processing Efficiency Gain</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">From 75</span>
      <span class="cg-stat-lbl">Claims Per Processor/Day</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">To 130</span>
      <span class="cg-stat-lbl">Claims Per Processor/Day</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>What was actually broken</h2>
  
  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Legacy Claims Processing</h4>
      <ul class="cg-compare-list">
        <li>Processors searching through multiple screens and tabs for customer details.</li>
        <li>Manual calculation of deductibles, allowed limits, and Room Rent Caps.</li>
        <li>Double-entries and spreadsheets used to cross-verify document authenticity.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Revamped claims workbench</h4>
      <ul class="cg-compare-list">
        <li>Unified Customer 360 view surfacing active benefits and past claims.</li>
        <li>Embedded rule engine automatically computing allowed claim amounts.</li>
        <li>Structured OCR extraction validating bills against invoice records.</li>
      </ul>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>What I shaped</h2>
  <p>I led the functional redesign of the claims processor interface in Salesforce. By studying the manual steps of top performers, I mapped keyboard shortcuts, split-screen PDF viewers, and inline validation rule calculations into the system workflow, dramatically cutting down the clicks needed to verify a single document line item.</p>
</section>
"""

        # 6. highradius-autonomous-collections
        if cs["slug"] == "highradius-autonomous-collections":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>In large enterprises, accounts receivable collections involve thousands of customers, millions of invoices, disputed deductions, customer AP portals, follow-up emails, and collector capacity limits.</p>

  <blockquote class="cg-editorial-quote">
    At HighRadius, I worked as a Senior PM on the Autonomous Collections product. The goal was to help enterprise finance teams reduce past dues, improve cash flow, and move collections from reactive chasing to automated priority lists.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Product Core Values</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">Autonomous</span>
      <span class="cg-stat-lbl">Receivables Matching</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Multi-ERP</span>
      <span class="cg-stat-lbl">Ledger Integration</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Predictive</span>
      <span class="cg-stat-lbl">Payment Propensity Models</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Key Product Components</h2>
  <p>The product transformation focused on shifting human collectors away from routine administrative tasks toward targeted, high-value dispute resolutions:</p>

  <div class="cg-highlight-grid">
    <div class="cg-highlight-card">
      <h4>Smart Priority Lists</h4>
      <p>Prioritizes collections lists based on payment delay probability, invoice size, and historical payment behaviors instead of chronological sorting.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Automated AP Portals</h4>
      <p>Pushes invoices, statements of accounts, and proof-of-delivery documents directly to customer Accounts Payable systems via APIs.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Promise-to-Pay Workflows</h4>
      <p>Tracks customer payment commitments, flags delayed payments, and automatically adjusts collector schedules to schedule escalations.</p>
    </div>
  </div>
</section>
"""

        # 7. creanovation-edtech-saas
        if cs["slug"] == "creanovation-edtech-saas":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Most education institutions lose prospective students in the gaps: slow follow-ups, missing document verification, un-reconciled fees, and complete lack of visibility over the admissions funnel.</p>

  <blockquote class="cg-editorial-quote">
    Forms Dot Star started as a way to digitize application forms. As the product matured under my direction, we expanded it from online forms into a complete student relationship management (CRM) SaaS suite.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Product Scope</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">SaaS</span>
      <span class="cg-stat-lbl">CRM Platform Model</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Unified</span>
      <span class="cg-stat-lbl">Funnel Tracking</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Self-Serve</span>
      <span class="cg-stat-lbl">Document Verification</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>From simple forms to student lifecycle</h2>
  <p>We expanded the product to cover the entire student enrollment and verification lifecycle:</p>

  <div class="cg-flow-track">
    <div class="cg-flow-step">
      <div class="cg-flow-num">1</div>
      <div class="cg-flow-text">
        <h4>Digitized Admissions Funnel</h4>
        <p>Allows institutions to set up application forms, track counselors' call notes, and scoring lead quality.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">2</div>
      <div class="cg-flow-text">
        <h4>Self-Serve Student Verification</h4>
        <p>A mobile portal where prospective students upload academic certificates, identity cards, and verify document status.</p>
      </div>
    </div>
    <div class="cg-flow-step">
      <div class="cg-flow-num">3</div>
      <div class="cg-flow-text">
        <h4>Automated Fee Reconciliation</h4>
        <p>Connects digital payment gateways directly with institutional ledgers, clearing payouts and admitting students automatically.</p>
      </div>
    </div>
  </div>
</section>
"""

        # 8. ai-led-pre-auth-automation (IPD cashless / network claims)
        if cs["slug"] == "ai-led-pre-auth-automation":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Hospital pre-authorization is a critical operations gateway in medical insurance. The turnaround time directly impacts patient anxiety, hospital bed allocations, and insurer leakages.</p>

  <blockquote class="cg-editorial-quote">
    We designed and deployed an AI-assisted cashless pre-auth decision workbench. It reads medical intake files, classifies records, runs limit checks, and generates decision confidence indexes.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Key Design Elements</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">AI-Assisted</span>
      <span class="cg-stat-lbl">Pre-Auth Workbench</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Allowed Amt</span>
      <span class="cg-stat-lbl">Rule Engine Mapping</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Operator</span>
      <span class="cg-stat-lbl">Confidence Indicators</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Reconciliation and Rule Engines</h2>
  <p>The product intervention focused on wrapping complex claims routing rules into structured operator assistance flows:</p>

  <div class="cg-highlight-grid">
    <div class="cg-highlight-card">
      <h4>Document Chronology DMS</h4>
      <p>Visual split-screen console arranging documents chronologically (Est. Bills, Reports, KYC) with missing-file warning badges.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Allowed Amount Engine</h4>
      <p>System automatically maps hospital room caps, surgery tariffs, and diagnostic limits directly on top of billing lists.</p>
    </div>
    <div class="cg-highlight-card">
      <h4>Exception Routing</h4>
      <p>Redirects low-confidence OCR reads to senior auditors, logging correction reasons to build future training datasets.</p>
    </div>
  </div>
</section>
"""

        # 9. ai-powered-cognitive-decision-engine
        if cs["slug"] == "ai-powered-cognitive-decision-engine":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Cognitive automation platforms fail when they treat AI recommendations as absolute decisions. Operators bypass rules because they don't understand the model's evidence.</p>

  <blockquote class="cg-editorial-quote">
    The Enigma platform automated unstructured medical document extraction and validation by presenting confidence intervals side-by-side with source files.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Engine Parameters</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">CV & NLP</span>
      <span class="cg-stat-lbl">Multi-Modal Extraction</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Explainable</span>
      <span class="cg-stat-lbl">Confidence Ranges</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Human-in-Loop</span>
      <span class="cg-stat-lbl">Override Audit Logs</span>
    </div>
  </div>
</section>
"""

        # 10. bfhl-partner-center-revamp
        if cs["slug"] == "bfhl-partner-center-revamp":
            cs["custom_body"] = """
<section class="cg-article-section">
  <p>Provider portals often become dumping grounds where partners can log in, download a report, and check a few transactions. They exist, but they do not change behavior: partners still call RMs or message on WhatsApp.</p>

  <blockquote class="cg-editorial-quote">
    We revamped the legacy Provider Portal into a unified self-serve operating center (Partner Center) to allow labs, hospitals, and merchants to resolve issues and manage appointments on their own.
  </blockquote>
</section>

<section class="cg-article-section">
  <h2>Key Design Elements</h2>
  <div class="cg-stats-grid">
    <div class="cg-stat-card">
      <span class="cg-stat-val">Unified</span>
      <span class="cg-stat-lbl">Partner Dashboard</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Self-Serve</span>
      <span class="cg-stat-lbl">Settlements & Reports</span>
    </div>
    <div class="cg-stat-card">
      <span class="cg-stat-val">Role-Based</span>
      <span class="cg-stat-lbl">Superuser Hierarchy</span>
    </div>
  </div>
</section>

<section class="cg-article-section">
  <h2>Operating Portal Revamp</h2>
  <div class="cg-comparison-grid">
    <div class="cg-compare-card before">
      <h4 class="cg-compare-title">Legacy Provider Portal</h4>
      <ul class="cg-compare-list">
        <li>Partners calling RMs to check if transactions were settled.</li>
        <li>Repetitive manual ticket creation for report adjustments.</li>
        <li>Shared logins across center staff with no role restriction.</li>
      </ul>
    </div>
    <div class="cg-compare-card after">
      <h4 class="cg-compare-title">Partner Operating Center</h4>
      <ul class="cg-compare-list">
        <li>Interactive filters showing real-time settlement status.</li>
        <li>Direct self-serve document upload and dispute logs.</li>
        <li>Granular superuser and branch user access control.</li>
      </ul>
    </div>
  </div>
</section>
"""

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Successfully beautified all case studies in json.")

if __name__ == "__main__":
    beautify_case_studies()
