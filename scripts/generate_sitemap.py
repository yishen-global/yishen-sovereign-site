import json, os
from datetime import datetime

DOMAIN = "https://yishenglobal.net/"
OUTPUT = "public/sitemap.xml"
LEDGER = "public/assets/data/sku-database.json"

today = datetime.utcnow().strftime("%Y-%m-%d")

nodes = []

# ROOT
nodes.append({"loc": DOMAIN, "priority": "1.0"})

# STATIC HTML
if os.path.exists("public"):
    for f in os.listdir("public"):
        if f.endswith(".html"):
            nodes.append({"loc": DOMAIN + f, "priority": "0.8"})

# DYNAMIC SKU PAGES
if os.path.exists(LEDGER):
    with open(LEDGER, "r", encoding="utf-8") as f:
        data = json.load(f)
        for sku in data.get("products", []):
            sid = sku.get("id")
            if sid:
                nodes.append({"loc": f"{DOMAIN}technical-passport.html?id={sid}", "priority": "0.7"})

xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for n in nodes:
    xml.append("<url>")
    xml.append(f"<loc>{n['loc']}</loc>")
    xml.append(f"<lastmod>{today}</lastmod>")
    xml.append("<changefreq>weekly</changefreq>")
    xml.append(f"<priority>{n['priority']}</priority>")
    xml.append("</url>")

xml.append("</urlset>")

os.makedirs("public", exist_ok=True)
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(xml))

print("AUTO SEO SITEMAP ENGINE ONLINE")
