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
        "availableLanguage": ["ar", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "he", "hi", "hu", "id", "it", "ja", "ko", "ms", "nl", "no", "pl", "pt", "ru", "sk", "sv", "th", "tl", "tr", "vi", "zh"],
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
        
        print(f"Injected 30-Language JSON-LD Schema into: {fname}")

if __name__ == "__main__":
    deploy_dive_breathe_exposure()