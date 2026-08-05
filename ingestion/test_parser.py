from ingestion.wikipedia_parser import WikipediaParser

parser = WikipediaParser(
    "data/raw/enwiki-latest-pages-articles1.xml-p1p41242.bz2"
)

for i, article in enumerate(parser.parse()):

    print("=" * 80)
    print(article["title"])
    print(article["id"])
    print(article["text"][:300])

    if i == 4:
        break