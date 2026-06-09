import json
import pathlib

ROOT = pathlib.Path("/Users/samadhan.mishra/Documents/Projects V2/Samadhan Papers/samadhan-product.github.io")
ORIGINAL_DATA_FILE = ROOT / "scratch" / "seo-content-original.json"
TARGET_DATA_FILE = ROOT / "assets" / "data" / "seo-content.json"

def beautify_preserving_content():
    with open(ORIGINAL_DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for cs in data["case_studies"]:
        slug = cs["slug"]
        body = cs.get("custom_body", "")
        if not body:
            # If no custom_body, continue or build from other fields (should have custom_body for all modified ones)
            continue

        # 1. Global: Convert all standard blockquotes to editorial quotes
        body = body.replace("<blockquote>", '<blockquote class="cg-editorial-quote">')

        # 2. Case study specific visual injections (preserving all surrounding text)
        if slug == "bfhl-wellness-cohort":
            # Inject stats grid right before "The situation" section
            stats_html = """
<div class="cg-stats-grid">
  <div class="cg-stat-card">
    <span class="cg-stat-val">₹95 Lakhs</span>
    <span class="cg-stat-lbl">Annual Vendor Cost Saved</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">3 dieticians</span>
    <span class="cg-stat-lbl">Initial In-House Team</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Active Users</span>
    <span class="cg-stat-lbl">Primary Engagement Goal</span>
  </div>
</div>
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            # Inject comparison grid right after "The actual gaps were different." in "What was actually broken"
            comparison_html = """
<div class="cg-comparison-grid">
  <div class="cg-compare-card before">
    <h4 class="cg-compare-title">Legacy Limitations</h4>
    <ul class="cg-compare-list">
      <li>High operational costs from external dietician vendors.</li>
      <li>Passive activity tracking with zero social or themed hooks.</li>
      <li>One-off consultations lacking EMR history or scheduled follow-ups.</li>
      <li>No visible employee participation stats for corporate clients.</li>
    </ul>
  </div>
  <div class="cg-compare-card after">
    <h4 class="cg-compare-title">Custom In-House Platform</h4>
    <ul class="cg-compare-list">
      <li>₹95 Lakhs saved by cutting out external vendors.</li>
      <li>Gamified step tracker with Kilimanjaro & Everest routes.</li>
      <li>Complete structured care loop (Assessment, Plan, Chat, Follow-ups).</li>
      <li>Real-time engagement dashboards validating corporate value.</li>
    </ul>
  </div>
</div>
"""
            body = body.replace('<h3 style="margin-top:16px;">Activity tracking was too passive</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Activity tracking was too passive</h3>')

        elif slug == "bfhl-healthpay-qr-transition":
            # Inject stats grid before "The situation"
            stats_html = """
<div class="cg-stats-grid">
  <div class="cg-stat-card">
    <span class="cg-stat-val">BajajPay Rails</span>
    <span class="cg-stat-lbl">Payment Infrastructure</span>
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
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            # Inject comparison grid inside "What was actually broken or risky"
            comparison_html = """
<div class="cg-comparison-grid">
  <div class="cg-compare-card before">
    <h4 class="cg-compare-title">Transition Risks</h4>
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
      <li>Structured field logistics and physical standee placement verification.</li>
    </ul>
  </div>
</div>
"""
            body = body.replace('<h3 style="margin-top:16px;">Provider migration risk</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Provider migration risk</h3>')

        elif slug == "bfhl-healthpay-recon-automation":
            # Inject stats grid before "The situation" or after intro
            stats_html = """
<div class="cg-stats-grid">
  <div class="cg-stat-card">
    <span class="cg-stat-val">RazorpayX</span>
    <span class="cg-stat-lbl">Payout Integration Rail</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Automated</span>
    <span class="cg-stat-lbl">PG-to-Bank Reconciliation</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Audit-Ready</span>
    <span class="cg-stat-lbl">Financial Controls Layer</span>
  </div>
</div>
"""
            # We want to find a place to put this. Let's see: before "The situation"
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            # Inject comparison grid before "Pay-in reconciliation"
            comparison_html = """
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
"""
            body = body.replace('<h3 style="margin-top:16px;">Pay-in reconciliation</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Pay-in reconciliation</h3>')

        elif slug == "bfhl-service-guarantee":
            stats_html = """
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
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            comparison_html = """
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
"""
            body = body.replace('<h3 style="margin-top:16px;">Appointment and lab slot bookings did not sync</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Appointment and lab slot bookings did not sync</h3>')

        elif slug == "bfhl-opd-reimbursement-claims":
            stats_html = """
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
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            comparison_html = """
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
    <h4 class="cg-compare-title">Revamped Claims Workbench</h4>
    <ul class="cg-compare-list">
      <li>Unified Customer 360 view surfacing active benefits and past claims.</li>
      <li>Embedded rule engine automatically computing allowed claim amounts.</li>
      <li>Structured OCR extraction validating bills against invoice records.</li>
    </ul>
  </div>
</div>
"""
            body = body.replace('<h3 style="margin-top:16px;">Processor work required too many screens</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Processor work required too many screens</h3>')

        elif slug == "highradius-autonomous-collections":
            stats_html = """
<div class="cg-stats-grid">
  <div class="cg-stat-card">
    <span class="cg-stat-val">Autonomous</span>
    <span class="cg-stat-lbl">Receivables Matching</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Predictive</span>
    <span class="cg-stat-lbl">Payment Propensity</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Multi-ERP</span>
    <span class="cg-stat-lbl">Ledger Integration</span>
  </div>
</div>
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

        elif slug == "creanovation-edtech-saas":
            stats_html = """
<div class="cg-stats-grid">
  <div class="cg-stat-card">
    <span class="cg-stat-val">CRM SaaS</span>
    <span class="cg-stat-lbl">Student Lifecycle</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Self-Serve</span>
    <span class="cg-stat-lbl">Document Uploads</span>
  </div>
  <div class="cg-stat-card">
    <span class="cg-stat-val">Automated</span>
    <span class="cg-stat-lbl">Fee Reconciliation</span>
  </div>
</div>
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

        elif slug == "bfhl-partner-center-revamp":
            stats_html = """
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
    <span class="cg-stat-lbl">Access Control</span>
  </div>
</div>
"""
            body = body.replace('<h2>The situation</h2>', stats_html + '\n<h2>The situation</h2>')

            comparison_html = """
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
"""
            body = body.replace('<h3 style="margin-top:16px;">Partners lacked self-serve visibility</h3>', comparison_html + '\n<h3 style="margin-top:16px;">Partners lacked self-serve visibility</h3>')

        elif slug == "ai-led-pre-auth-automation":
            stats_html = """
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
"""
            body = body.replace('<h2>Context</h2>', stats_html + '\n<h2>Context</h2>')

        elif slug == "ai-powered-cognitive-decision-engine":
            stats_html = """
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
"""
            body = body.replace('<h2>Context</h2>', stats_html + '\n<h2>Context</h2>')

        cs["custom_body"] = body

    with open(TARGET_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Successfully beautified all case studies inline, keeping 100% of original content.")

if __name__ == "__main__":
    beautify_preserving_content()
