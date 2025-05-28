import requests
from bs4 import BeautifulSoup
import time

# Define headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# Enhanced search queries for better discovery
SOCIAL_SITES = [
    "facebook.com", "instagram.com", "linkedin.com",
    "telegram.me", "tiktok.com", "twitter.com",
    "youtube.com", "github.com"
]

def bing_search(query):
    results = []
    try:
        url = f"https://www.bing.com/search?q={query}"
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")
        for item in soup.find_all('li', class_='b_algo'):
            link = item.find('a')
            if link and link['href']:
                results.append(link['href'])
    except Exception as e:
        results.append(f"[!] Bing search error: {str(e)}")
    return results

def generate_report(name, results, report_file):
    with open(report_file, 'w') as f:
        f.write("<html><head><title>Hydra OSINT Report</title></head><body>")
        f.write(f"<h2>Hydra OSINT Report for {name}</h2><hr>")
        for engine, links in results.items():
            f.write(f"<h3>{engine.upper()} Results</h3><ul>")
            for link in links:
                f.write(f"<li><a href='{link}' target='_blank'>{link}</a></li>")
            f.write("</ul><br>")
        f.write("</body></html>")
    print(f"\n📄 Report saved as: {report_file}")

def main():
    print("="*59)
    print("🔥 The Hydra Hunter 🔥")
    print("="*59)
    
    name = input("Enter Full Name: ").strip()
    country = input("Enter Country: ").strip()
    hometown = input("Enter Home Town: ").strip()
    custom_filename = input("Enter custom report filename (leave blank for default): ").strip()

    print("\n[!] Initializing search...")

    queries = [
        f'"{name}" "{country}" "{hometown}"',
        f'"{name}" "{hometown}"',
        f'"{name}" "{country}"',
        f'"{name}"'
    ]

    for site in SOCIAL_SITES:
        queries.append(f'"{name}" site:{site}')

    all_results = {"bing": []}

    for query in queries:
        print(f"\n🔍 Bing Searching: {query}")
        all_results["bing"].extend(bing_search(query))
        time.sleep(1.5)

    # Set report filename
    if custom_filename:
        if not custom_filename.endswith(".html"):
            custom_filename += ".html"
        report_file = custom_filename
    else:
        report_file = f"hydra_report_{name.replace(' ', '_')}.html"

    generate_report(name, all_results, report_file)

if __name__ == "__main__":
    main()
