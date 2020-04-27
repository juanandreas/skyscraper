import threading
import time
import uuid
import yaml

from src.citron_scraper import CitronScraper
from src.twitter_scraper import TwitterScraper

class ScrapersController(object):
    CitronScraper()
    TwitterScraper()

def main(config, news_sources):
    """
    news_sources = [
        ("news_id", [news_urls_list]), 
        ("news_id", [news_urls_list]), 
        ...
    ]
    """
    scrapers = {}
    for news_id, news_urls_list in news_sources:
        build Scraper for each news_id
        scrapers[news_id] = NewsScraper(config, news_urls_list)

    for scraper in scrapers:
        scrapers[scraper].run_threads()

if __name__ == '__main__':
    conf = yaml.load(open("conf/prod/conf.yaml", 'r').read(), Loader=yaml.Loader)
    news_set = yaml.load(open("news_urls/news_urls.yaml", 'r').read(), Loader=yaml.Loader)
    
    news_sources = [(news_id, news_set[news_id]) for news_id in news_set]
    '''
    news_sources = [
        ("yahoo_finance", yahoo_finance_sites),
        ("twitter", twitter_urls_list),
        ....
        ]
    '''
    main(conf, news_sources)

