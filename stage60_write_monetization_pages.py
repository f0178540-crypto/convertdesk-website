from pathlib import Path

ROOT = Path(r"D:\ConvertDesk_Website")

INSTALLER_URL = "https://github.com/f0178540-crypto/convertdesk-website/releases/download/v1.0.1/ConvertDeskSetup_1.0.1.exe"
SHA256 = "8ea4575180ebedf7a8ca6dc777caa52932453f645eeec7fdb757b816d4668f56"

COMMON_FOOTER = """  <footer>
    <p>© 2026 AppLab. All rights reserved.</p>
    <p>ConvertDesk is a software product by AppLab.</p>
    <p>
      <a href="roadmap.html">Roadmap</a>
      <span>·</span>
      <a href="changelog.html">Changelog</a>
      <span>·</span>
      <a href="privacy.html">Privacy Policy</a>
      <span>·</span>
      <a href="terms.html">Terms</a>
      <span>·</span>
      <a href="refund.html">Refund Policy</a>
      <span>·</span>
      <a href="support.html">Support</a>
    </p>
  </footer>"""

COMMON_HEADER = """  <header class="site-header">
    <div class="brand">
      <div class="brand-mark">A</div>
      <div>
        <div class="brand-name">AppLab</div>
        <div class="brand-subtitle">ConvertDesk</div>
      </div>
    </div>

    <nav>
      <a href="index.html">Home</a>
      <a href="download.html">Download</a>
      <a href="pro.html">Pro</a>
      <a href="business.html">Business</a>
      <a href="pricing.html">Pricing</a>
      <a href="resources.html">Resources</a>
      <a href="support.html">Support</a>
    </nav>
  </header>"""

download_thanks = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Your Download Is Ready — ConvertDesk</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Download ConvertDesk for Windows and learn about ConvertDesk Pro, Business licensing, safety checks and recommended file workflow resources.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
{COMMON_HEADER}

  <main>
    <section class="hero">
      <p class="eyebrow">ConvertDesk download</p>
      <h1>Your download is ready.</h1>
      <p class="hero-text">
        Download ConvertDesk 1.0.1 for Windows. Keep the installer from this official release page and verify the SHA256 checksum if needed.
      </p>

      <div class="hero-actions">
        <a class="button primary" href="{INSTALLER_URL}">Download ConvertDesk 1.0.1</a>
        <a class="button secondary" href="downloads/ConvertDesk_1.0.1_SHA256.txt">View SHA256 checksums</a>
      </div>

      <p class="note">
        File: ConvertDeskSetup_1.0.1.exe
      </p>
    </section>

    <section class="section highlight">
      <h2>Verify the installer</h2>
      <p>
        SHA256:
      </p>
      <div class="card faq-card">
        <h3>{SHA256}</h3>
        <p>On Windows, run: certutil -hashfile ConvertDeskSetup_1.0.1.exe SHA256</p>
      </div>
    </section>

    <section class="section">
      <h2>Upgrade path</h2>
      <div class="grid">
        <div class="card">
          <h3>ConvertDesk Free</h3>
          <p>Good for basic local file conversion and testing the workflow.</p>
        </div>
        <div class="card">
          <h3>ConvertDesk Pro</h3>
          <p>Planned for unlimited conversions, batch workflows, multi-output conversion, full history and commercial use.</p>
          <p><a href="pro.html">View Pro plan</a></p>
        </div>
        <div class="card">
          <h3>ConvertDesk Business</h3>
          <p>Planned for company use, priority support, invoice-friendly purchase and deployment notes.</p>
          <p><a href="business.html">View Business plan</a></p>
        </div>
      </div>
    </section>

    <section class="section highlight">
      <h2>Recommended file workflow resources</h2>
      <p>
        This section is reserved for carefully selected sponsor or affiliate recommendations related to file backup,
        PDF workflows, cloud storage and file security. Recommendations will be clearly labeled when added.
      </p>

      <div class="grid">
        <div class="card">
          <h3>Backup before conversion</h3>
          <p>Recommended space for a cloud backup or file protection partner.</p>
        </div>
        <div class="card">
          <h3>PDF workflow tools</h3>
          <p>Recommended space for a PDF productivity partner.</p>
        </div>
        <div class="card">
          <h3>Secure file storage</h3>
          <p>Recommended space for secure storage or business productivity tools.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Get launch updates</h2>
      <p>
        ConvertDesk Pro checkout, license activation and the final official domain are planned for later stages.
        Early users may receive launch discounts when Pro becomes available.
      </p>
      <div class="card faq-card">
        <h3>Email signup placeholder</h3>
        <p>Email capture will be connected later through a proper mailing provider. No signup form is active yet.</p>
      </div>
    </section>
  </main>

{COMMON_FOOTER}
</body>
</html>
"""

pro = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ConvertDesk Pro — Unlimited Local File Conversion</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="ConvertDesk Pro is planned for unlimited local file conversion, batch workflows, multi-output conversion, full history and commercial use.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
""" + COMMON_HEADER + """

  <main>
    <section class="hero">
      <p class="eyebrow">ConvertDesk Pro</p>
      <h1>For users who convert files seriously.</h1>
      <p class="hero-text">
        ConvertDesk Pro is planned as the paid version for unlimited local conversion, batch processing,
        multi-output workflows, full history and commercial use.
      </p>

      <div class="hero-actions">
        <a class="button primary" href="pricing.html">View pricing</a>
        <a class="button secondary" href="download.html">Download Free</a>
      </div>

      <p class="note">
        Checkout is not live yet. Pro licensing will be enabled in a later release stage.
      </p>
    </section>

    <section class="section">
      <h2>Planned Pro features</h2>
      <div class="grid">
        <div class="card">
          <h3>Unlimited local conversions</h3>
          <p>Remove daily Free limits and convert locally on your Windows machine.</p>
        </div>
        <div class="card">
          <h3>Batch conversion</h3>
          <p>Process larger queues and workflows without manual repetition.</p>
        </div>
        <div class="card">
          <h3>Multi-output conversion</h3>
          <p>Create multiple output formats from the same source file.</p>
        </div>
        <div class="card">
          <h3>Full history</h3>
          <p>Review previous conversions, outputs and workflow activity.</p>
        </div>
        <div class="card">
          <h3>Advanced presets</h3>
          <p>Use saved conversion profiles for repeatable professional workflows.</p>
        </div>
        <div class="card">
          <h3>Commercial use</h3>
          <p>Use ConvertDesk Pro for professional and commercial file workflows.</p>
        </div>
      </div>
    </section>

    <section class="section highlight">
      <h2>Planned pricing</h2>
      <div class="grid">
        <div class="card">
          <h3>Pro Monthly</h3>
          <p>Planned: 5.99 EUR / month.</p>
        </div>
        <div class="card">
          <h3>Pro Yearly</h3>
          <p>Planned: 39.99 EUR / year.</p>
        </div>
        <div class="card">
          <h3>Lifetime</h3>
          <p>Planned: 59.99 EUR one-time. Launch discount may be offered.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>License activation</h2>
      <p>
        ConvertDesk Pro will use license-key activation, device-bound validation and server-side license checks.
        This protects paid access while keeping the Free version usable.
      </p>
    </section>
  </main>

""" + COMMON_FOOTER + """
</body>
</html>
"""

business = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ConvertDesk Business — File Conversion for Teams and Companies</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="ConvertDesk Business is planned for commercial and company file conversion workflows, priority support and invoice-friendly licensing.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
""" + COMMON_HEADER + """

  <main>
    <section class="hero">
      <p class="eyebrow">ConvertDesk Business</p>
      <h1>For companies that need reliable local file conversion.</h1>
      <p class="hero-text">
        ConvertDesk Business is planned for professional use, company workflows, priority support,
        invoice-friendly purchase and later multi-device licensing.
      </p>

      <div class="hero-actions">
        <a class="button primary" href="pricing.html">View planned pricing</a>
        <a class="button secondary" href="support.html">Contact support</a>
      </div>

      <p class="note">
        Business checkout is not live yet. This page prepares the commercial licensing path.
      </p>
    </section>

    <section class="section">
      <h2>Business plan includes</h2>
      <div class="grid">
        <div class="card">
          <h3>Commercial/company use</h3>
          <p>Designed for professional environments where file conversion is part of daily work.</p>
        </div>
        <div class="card">
          <h3>Priority support</h3>
          <p>Business customers will receive a higher support priority once official support email is active.</p>
        </div>
        <div class="card">
          <h3>Invoice-friendly checkout</h3>
          <p>Planned through a Merchant of Record provider such as Paddle or FastSpring.</p>
        </div>
        <div class="card">
          <h3>Deployment notes</h3>
          <p>Guidance for installing and using ConvertDesk in business environments.</p>
        </div>
        <div class="card">
          <h3>Future multi-device licensing</h3>
          <p>Centralized team/device licensing may be added in a later release.</p>
        </div>
        <div class="card">
          <h3>Stable release channel</h3>
          <p>Business users should use signed, verified and documented releases.</p>
        </div>
      </div>
    </section>

    <section class="section highlight">
      <h2>Planned pricing</h2>
      <div class="grid">
        <div class="card">
          <h3>Business Yearly</h3>
          <p>Planned: 149 EUR / year.</p>
        </div>
        <div class="card">
          <h3>Business Lifetime</h3>
          <p>Planned: 299 EUR one-time.</p>
        </div>
        <div class="card">
          <h3>Launch offer</h3>
          <p>Early business pricing may be offered during the first public Pro rollout.</p>
        </div>
      </div>
    </section>
  </main>

""" + COMMON_FOOTER + """
</body>
</html>
"""

resources = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Resources — ConvertDesk</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="ConvertDesk resources for file conversion, backup, PDF workflows, verification and Windows file productivity.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
""" + COMMON_HEADER + """

  <main>
    <section class="hero">
      <p class="eyebrow">Resources</p>
      <h1>File conversion workflow resources.</h1>
      <p class="hero-text">
        Guides, recommendations and workflow resources for safer and more efficient file conversion on Windows.
      </p>
    </section>

    <section class="section">
      <h2>Core resources</h2>
      <div class="grid">
        <div class="card">
          <h3>Verify downloads</h3>
          <p>Learn how to verify a ConvertDesk installer with SHA256 before installing.</p>
        </div>
        <div class="card">
          <h3>Back up files first</h3>
          <p>Recommended workflow: keep backups of important files before converting or batch processing.</p>
        </div>
        <div class="card">
          <h3>Offline file conversion</h3>
          <p>Why local-first conversion can be better for privacy and repeatable workflows.</p>
        </div>
        <div class="card">
          <h3>Batch workflows</h3>
          <p>How to organize sources, output formats, presets and queues.</p>
        </div>
      </div>
    </section>

    <section class="section highlight">
      <h2>Recommended tools section</h2>
      <p>
        This page will later contain clearly labeled sponsor or affiliate recommendations related to backup,
        storage, PDF workflows, security and productivity.
      </p>
      <div class="grid">
        <div class="card">
          <h3>Backup and storage</h3>
          <p>Reserved for a file backup or cloud storage partner.</p>
        </div>
        <div class="card">
          <h3>PDF productivity</h3>
          <p>Reserved for PDF editing or document workflow recommendations.</p>
        </div>
        <div class="card">
          <h3>Security tools</h3>
          <p>Reserved for reputable security and file protection tools.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Planned SEO guides</h2>
      <div class="grid">
        <div class="card">
          <h3>PNG to JPG</h3>
          <p>Guide page planned.</p>
        </div>
        <div class="card">
          <h3>JPG to PDF</h3>
          <p>Guide page planned.</p>
        </div>
        <div class="card">
          <h3>MP4 to MP3</h3>
          <p>Guide page planned.</p>
        </div>
        <div class="card">
          <h3>CSV to XLSX</h3>
          <p>Guide page planned.</p>
        </div>
      </div>
    </section>
  </main>

""" + COMMON_FOOTER + """
</body>
</html>
"""

pages = {
    "download-thanks.html": download_thanks,
    "pro.html": pro,
    "business.html": business,
    "resources.html": resources,
}

for filename, content in pages.items():
    (ROOT / filename).write_text(content, encoding="utf-8", newline="\n")
    print(f"OK wrote {filename}")

download = ROOT / "download.html"
text = download.read_text(encoding="utf-8")
text = text.replace(INSTALLER_URL, "download-thanks.html")
text = text.replace('href="downloads/ConvertDeskSetup_1.0.1.exe"', 'href="download-thanks.html"')
download.write_text(text, encoding="utf-8", newline="\n")
print("OK updated download.html to route through download-thanks.html")