from crawler import WikiSemanticCrawler


wsc = WikiSemanticCrawler(
    "https://en.wikipedia.org/wiki/Pikachu",
    "https://en.wikipedia.org/wiki/Python_(programming_language)"
)
links = wsc.find_best_path()

print(links)
