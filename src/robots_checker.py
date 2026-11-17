import urllib.error
import urllib.request
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser


USER_AGENT = "Learning/1.0 (personal practice)"

def can_scrape(url: str) -> bool:
    parts = urlparse(url)
    site = f"{parts.scheme}://{parts.netloc}"

    req = urllib.request.Request(f"{site}/robots.txt", headers={"User_agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            lines = resp.read().decode("utf-8").splitlines()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return True
        return False
    except urllib.error.URLError:
        return False
    rp = RobotFileParser()
    rp.parse(lines)
    return rp.can_fetch("*", url)

if __name__ == "__main__":
    print(can_scrape("https://books.toscrape.com/catalogue/page-1.html"))