from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
from citron_scraper import CitronScraper
import time
import subprocess

scraper = CitronScraper()
counter = 0
CitronCache = scraper.scrape()

while True:
    freshScrape = scraper.scrape()
    if freshScrape != CitronCache:
        pprint(freshScrape)
    else:
        time.sleep(1)

    