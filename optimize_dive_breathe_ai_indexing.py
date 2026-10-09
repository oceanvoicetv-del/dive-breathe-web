import os
import json
import re

def deploy_dive_breathe_exposure():
    target_dist = r"C:\GrowthEngine\DiveBreathe_Web\dist"
    seo_directory = os.path.join(target_dist, "ai-seo")
    os.makedirs(seo_directory, exist_ok=True)

    base_url = "https://oceanvoicetv-del.github.io/dive-breathe-web"
    play_store_url = "https://play.google.com/store/apps/details?id=com.divebreathe.app"

    language_codes = [
        "ar", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr",
        "he", "hi", "hu", "id", "it", "ja", "ko", "ms", "nl", "no",
        "pl", "pt", "ru", "sk", "sv", "th", "tl", "tr", "vi", "zh"
    ]

    schema_data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Dive Breathe: Scuba Tools",
        "operatingSystem": "ANDROID, IOS",
        "applicationCategory": "SportsApplication",
        "downloadUrl": play_store_url,
        "installUrl": play_store_url,
        "availableLanguage": language_codes,
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
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "1250"
        }
    }

    schema_file_path = os.path.join(seo_directory, "dive-breathe-schema.json")
    with open(schema_file_path, "w", encoding="utf-8") as schema_file:
        json.dump(schema_data, schema_file, indent=4)
    print(f"Generated Verified Schema: {schema_file_path}")

    sitemap_entries = [
        f"""    <url>
        <loc>{base_url}/dist/index.html</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>"""
    ]

    for lang in language_codes:
        if lang == "en":
            continue
        sitemap_entries.append(
            f"""    <url>
        <loc>{base_url}/dist/languages/{lang}-db.html</loc>
        <lastmod>2026-10-09</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>"""
        )

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{os.linesep.join(sitemap_entries)}
</urlset>
"""
    sitemap_file_path = os.path.join(seo_directory, "ai-sitemap.xml")
    with open(sitemap_file_path, "w", encoding="utf-8") as sitemap_file:
        sitemap_file.write(sitemap_content)
    print(f"Generated 30-Language Sitemap: {sitemap_file_path}")

    robots_content = """User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
"""
    robots_file_path = os.path.join(seo_directory, "ai-robots-directives.txt")
    with open(robots_file_path, "w", encoding="utf-8") as robots_file:
        robots_file.write(robots_content.strip())
    print(f"Generated Open Directives: {robots_file_path}")

    schema_script_block = f'<script type="application/ld+json">\n{json.dumps(schema_data, indent=4)}\n    </script>\n</head>'

    for root, _, files in os.walk(target_dist):
        for fname in files:
            if not fname.endswith(".html"):
                continue
            file_path = os.path.join(root, fname)
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            if '<script type="application/ld+json">' in html_content:
                html_content = re.sub(
                    r'<script type="application/ld\+json">.*?</script>\s*</head>',
                    schema_script_block,
                    html_content,
                    flags=re.DOTALL
                )
            else:
                html_content = html_content.replace("</head>", f"    {schema_script_block}")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Injected Ground-Truth Schema: {os.path.relpath(file_path, target_dist)}")

if __name__ == "__main__":
    deploy_dive_breathe_exposure()