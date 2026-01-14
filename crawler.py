from bs4 import BeautifulSoup
import requests


class WikiSemanticCrawler:
    def __init__(self, start: str, end: str) -> None:
        self.start = start
        self.end = end

    def _href_filter(self, link: str) -> bool:
        return (
            link
            and link.startswith("/wiki/")
            and ":" not in link
            and "#" not in link
            and link != "/wiki/Main_Page"
        )

    def find_best_path(self):
        html = requests.get(
            self.start,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"
            },
            timeout=10,
        ).content.decode("utf-8")

        bs = BeautifulSoup(html, features="html.parser")
        tags = set(bs.find_all("a", href=self._href_filter))

        links = []
        for tag in tags:
            link = "https://en.wikipedia.org" + tag["href"]
            links.append(link)

        return links
