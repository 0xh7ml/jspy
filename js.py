import requests
from bs4 import BeautifulSoup as bs
import sys
from urllib.parse import urljoin
domain=sys.argv[1]
def js(domain):
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    html = session.get(domain).content
    soup = bs(html, "html.parser")
    script_files = []
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            script_url = urljoin(domain, script.attrs.get("src"))
            script_files.append(script_url)
            for js_file in script_files:
                print(js_file)
js(domain)
