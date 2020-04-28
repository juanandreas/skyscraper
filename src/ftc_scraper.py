# import requests
from bs4 import BeautifulSoup as BeautifulSoup
from pprint import pprint
from src.Multiprocess import Multiprocess

class FTCScraper(Multiprocess):
    
    def __init__(self, config, news_id, news_sources):
        super().__init__(config, news_id, news_sources)
        self.news_id = news_id
        self.news_urls_list = news_sources[self.news_id]
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    
    def scrape(self, news_url):
        page = requests.get(self.urls[0], headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        titles = []
        for item in soup.select('.views-row a'):
            titles.append(item.contents[0])
        return titles
        print("FTC scrape")
            