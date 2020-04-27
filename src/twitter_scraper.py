import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

from src.Multiprocess import Multiprocess

class TwitterScraper(Multiprocess):
    def __init__(self, config, urls):
        self.config = config
        self.twitter_username = self.config["twitter_username"]
        self.twitter_urls = urls
        
    def scrape_twitter(self):
        browser = webdriver.Chrome()
        for url in self.twitter_urls:
            browser.get(url.format(twitter_username))

        time.sleep(1)
        elem = browser.find_element_by_tag_name("body")

        twitter_elm = browser.find_elements_by_css_selector(".r-thb0q2")

        for _ in range(2):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

        twitter_elm = browser.find_elements_by_css_selector(".r-thb0q2")

        for post in twitter_elm:
            print(post.text)

