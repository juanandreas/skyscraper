import requests
from bs4 import BeautifulSoup as BeautifulSoup
from pprint import pprint
from Multiprocess import Multiprocess
import time

class FTCScraper(Multiprocess):
    
    def __init__(self, config, news_id, news_sources):
        super().__init__(config, news_id, news_sources)
        self.news_id = news_id
        self.news_urls_list = news_sources[self.news_id]
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    
    def scrape(self, news_url):
        page = requests.get(self.news_urls_list[0], headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        titles = []
        for item in soup.select('.views-row a'):
            titles.append(item.contents[0])
        return titles
        


msg = {
    "news_id": "yt1",
    "news_url": "https://youtube.com"
}
# n1.window_notify(msg)

news_sources = {0:["https://www.ftc.gov/news-events/press-releases"]}
config = None
test_scraper = FTCScraper(config, 0, news_sources)
test_cache = test_scraper.scrape(news_sources[0])

while True:
    freshScrape = test_scraper.scrape(news_sources[0])
    if freshScrape != test_cache:
        pprint(freshScrape[0])
    else:
        time.sleep(1)
