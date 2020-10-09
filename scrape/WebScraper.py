import sys
import argparse
import importlib
import json
from storage.Mongo import Mongo


class WebScraper(object):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.storage = Mongo()


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", help="Site")
    args = parser.parse_args()
    if args.site:
        with open(args.site, "r") as jsonfile:
            config = json.load(jsonfile)
    if config:
        for _site in config:
            site = _site.get("module").split(".")
            mod = importlib.import_module(site[0])
            cls = getattr(mod, site[1])
            scraper = cls(_site)
            scraper.scrape()
        



if __name__ == "__main__":
    main(sys.argv[:1])