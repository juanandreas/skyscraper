import requests
from bs4 import BeautifulSoup as BeautifulSoup
from pprint import pprint


class CitronScraper:
    
    def __init__(self):
        self.name = "Citron"
        self.urls = ['https://citronresearch.com/category/2020-reports/']
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    
    def scrape(self):
        page = requests.get(self.urls[0], headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        titles = []
        for item in soup.select('.entry-title a'):
            titles.append(item.contents[0])
        return titles
            
                
