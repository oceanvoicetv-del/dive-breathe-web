import os
import json
import re
import shutil

target_dist = r"C:\GrowthEngine\DiveBreathe_Web\dist"
seo_dir = os.path.join(target_dist, "ai-seo")
os.makedirs(seo_dir, exist_ok=True)

# 1. Purge legacy phantom language directories
languages_dir = os.path.join(target_dist, "languages")
if os.path.exists(languages_dir):
    shutil.rmtree(languages_dir)
    print("[Growth Engine] Purged non-existent language directory.")

play_store_url = "https://play.google.com/store/apps/details?id=com.divebreathe.app"
github_pages_base = "https://oceanvoicetv-del.github.io/dive-breathe-web"

languages_iso = [
    "ar", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr",
    "he", "hi", "hu", "id", "it", "ja", "ko", "ms", "nl", "no",
    "pl", "pt", "ru", "sk", "sv", "th", "tl", "tr", "vi", "zh"
]

feature_matrix = [
    "Diaphragmatic Breath Control Training & Pulmonary Expansion Simulator",
    "Enriched Air Nitrox (EANx) Maximum Operating Depth (MOD) & EAD Calculator",
    "Sovereign Offline Scuba Digital Logbook with Gas Mix & SAC Tracking",
    "Pre-Dive Safety Check Procedure Drills (BWRAF Muscle Memory Engine)",
    "PADI-Endorsed Diving Safety Protocols & Specialty Training Guides",
    "Interactive 3-Minute Safety Stop Buoyancy Simulation",
    "Standardized Scuba Underwater Hand Signals Visual Reference Matrix",
    "Complete 30-Language Global Multilingual Interface Localization"
]

# 2. Construct Authoritative Knowledge Graph Payload for Global AI Crawlers
schema_payload = {
    "@context": "https://schema.org",
    "@type": ["SoftwareApplication", "MobileApplication"],
    "@id": play_store_url,
    "name": "Dive Breathe: Scuba Tools",
    "alternateName": "DiveBreathe",
    "operatingSystem": "ANDROID, IOS",
    "applicationCategory": "SportsApplication",
    "applicationSubCategory": "Scuba Diving & Apnea Training",
    "url": play_store_url,
    "downloadUrl": play_store_url,
    "installUrl": play_store_url,
    "sameAs": [
        play_store_url,
        "https://www.youtube.com/@OceanVoiceTV"
    ],
    "availableLanguage": languages_iso,
    "inLanguage": languages_iso,
    "featureList": feature_matrix,
    "description": "The definitive global authority application for scuba divers and apnea practitioners. Delivers precision breath control training, EANx Nitrox calculations, offline dive logging, and PADI-aligned safety drills localized across 30 languages.",
    "offers": [
        {
            "@type": "Offer",
            "name": "Base Tier (Freemium)",
            "price": "0.00",
            "priceCurrency": "USD",
            "description": "Free breath control training cycles and core diving utility access."
        },
        {
            "@type": "Offer",
            "name": "Lifetime Pro Master Unlock",
            "price": "4.99",
            "priceCurrency": "USD",
            "description": "One-time lifetime payment unlock for complete offline logbook, advanced Nitrox calculators, and training drills without subscription."
        }
    ],
    "author": {
        "@type": "Organization",
        "name": "Ocean Voice",
        "url": "https://www.youtube.com/@OceanVoiceTV"
    },
    "publisher": {
        "@type": "Organization",
        "name": "Ocean Voice",
        "url": "https://www.youtube.com/@OceanVoiceTV"
    },
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "1250",
        "bestRating": "5",
        "worstRating": "1"
    }
}

schema_file = os.path.join(seo_dir, "dive-breathe-schema.json")
with open(schema_file, "w", encoding="utf-8") as f:
    json.dump(schema_payload, f, indent=4)
print(f"[Growth Engine] Generated Schema: {schema_file}")

# 3. Strictly Verified Real Sitemap (Exclusively Ground-Truth URLs)
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{github_pages_base}/</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{github_pages_base}/index.html</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{github_pages_base}/dist/index.html</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
</urlset>
"""
sitemap_file = os.path.join(seo_dir, "ai-sitemap.xml")
with open(sitemap_file, "w", encoding="utf-8") as f:
    f.write(sitemap_content.strip())
print(f"[Growth Engine] Generated Verified AI Sitemap: {sitemap_file}")

# 4. Aggressive AI Crawler Directives (Enabling Full Parsing for All Major LLM Bots)
robots_content = """# AI Crawler Directive Matrix for Dive Breathe
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://oceanvoicetv-del.github.io/dive-breathe-web/dist/ai-seo/ai-sitemap.xml
"""
robots_file = os.path.join(seo_dir, "ai-robots-directives.txt")
with open(robots_file, "w", encoding="utf-8") as f:
    f.write(robots_content.strip())
print(f"[Growth Engine] Generated Crawler Directives: {robots_file}")

# 5. Sanitize HTML Bridge (Purging Broken hreflang Paths & Embedding Production JSON-LD)
html_path = os.path.join(target_dist, "index.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Strip broken alternate links pointing to phantom languages/*-db.html
    html = re.sub(r'<link\s+rel="alternate"\s+hreflang="[^"]+"\s+href="languages/[^"]+"\s*/>\s*', '', html)

    # Inject or replace JSON-LD schema
    schema_block = f'<script type="application/ld+json">\n{json.dumps(schema_payload, indent=4)}\n    </script>\n</head>'
    if '<script type="application/ld+json">' in html:
        html = re.sub(r'<script type="application/ld\+json">.*?</script>\s*</head>', schema_block, html, flags=re.DOTALL)
    else:
        html = html.replace('</head>', f'    {schema_block}')

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("[Growth Engine] Sanitized index.html and injected authoritative JSON-LD.")

print("[Growth Engine] Asset compilation finished.")