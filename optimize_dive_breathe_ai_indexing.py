import os
import json
import re

def deploy_dive_breathe_exposure():
    target_dist = r"C:\GrowthEngine\DiveBreathe_Web\dist"
    seo_directory = os.path.join(target_dist, "ai-seo")
    os.makedirs(seo_directory, exist_ok=True)

    schema_data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Dive Breathe: Scuba Tools",
        "operatingSystem": "ANDROID, IOS",
        "applicationCategory": "SportsApplication",
        "offers": [
            {
                "@type": "Offer",
                "name": "Dive Breathe Basic",
                "price": "0.00",
                "priceCurrency": "USD",
                "description": "Limited freemium base access."
            },
            {
                "@type": "Offer",
                "name": "Lifetime Pro Unlock",
                "price": "4.99",
                "priceCurrency": "USD",
                "description": "One-time payment to unlock all premium scuba tools and offline features."
            }
        ],
        "description": "The ultimate scuba tool and digital logbook for beginner and experienced divers featuring breath control training, Nitrox calculations, offline dive logs, and PADI-endorsed safety guidelines. Includes a limited freemium base with a single lifetime unlock.",
        "publisher": {
            "@type": "Organization",
            "name": "Ocean Voice",
            "url": "https://oceanvoice.tv"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "1250"
        }
    }

    schema_file_path = os.path.join(seo_directory, "dive-breathe-schema.json")
    with open(schema_file_path, "w", encoding="utf-8") as schema_file:
        json.dump(schema_data, schema_file, indent=4)

    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://oceanvoice.tv/apps/dive-breathe</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://oceanvoice.tv/apps/dive-breathe/nitrox-calculator</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://oceanvoice.tv/apps/dive-breathe/breath-control-training</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
"""
    sitemap_file_path = os.path.join(seo_directory, "ai-sitemap.xml")
    with open(sitemap_file_path, "w", encoding="utf-8") as sitemap_file:
        sitemap_file.write(sitemap_content)

    robots_content = """User-agent: GPTBot
Allow: /apps/dive-breathe

User-agent: ClaudeBot
Allow: /apps/dive-breathe

User-agent: PerplexityBot
Allow: /apps/dive-breathe

User-agent: Google-Extended
Allow: /apps/dive-breathe
"""
    robots_file_path = os.path.join(seo_directory, "ai-robots-directives.txt")
    with open(robots_file_path, "w", encoding="utf-8") as robots_file:
        robots_file.write(robots_content.strip())

    base_html_path = os.path.join(target_dist, "index.html")
    if not os.path.exists(base_html_path):
        base_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dive Breathe: Scuba Tools</title>
    <meta name="description" content="The ultimate scuba tool and digital logbook featuring breath control training, Nitrox calculations, and offline dive logs.">
</head>
<body style="background-color: #0f172a; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 50px;">
    <h1>Dive Breathe: Scuba Tools</h1>
    <p>Available for iOS and Android.</p>
</body>
</html>"""
        with open(base_html_path, "w", encoding="utf-8") as base_html_file:
            base_html_file.write(base_html_content)

    for fname in os.listdir(target_dist):
        if not fname.endswith(".html"):
            continue
            
        file_path = os.path.join(target_dist, fname)
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        schema_script_block = f'\n    <script type="application/ld+json">\n{json.dumps(schema_data, indent=4)}\n    </script>\n</head>'
        
        if '<script type="application/ld+json">' in html_content:
            html_content = re.sub(r'<script type="application/ld\+json">.*?</script>', schema_script_block.strip() + '\n</head>', html_content, flags=re.DOTALL)
        else:
            html_content = html_content.replace("</head>", schema_script_block)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"Injected JSON-LD Schema into: {fname}")

if __name__ == "__main__":
    deploy_dive_breathe_exposure()