import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys 

from src.Multiprocess import Multiprocess

class TwitterScraper(Multiprocess):
    def __init__(self, config, news_id, news_sources):
        super().__init__(config, news_id, news_sources)
        self.config = config
        self.twitter_username = self.config["twitter_username"]
        self.news_id = news_id
        self.news_urls_list = news_sources[self.news_id]
        
    def scrape(self, news_url):
        # browser = webdriver.Chrome()
        # for url in self.twitter_urls:
        #     browser.get(url.format(twitter_username))

        # time.sleep(1)
        # elem = browser.find_element_by_tag_name("body")

        # twitter_elm = browser.find_elements_by_css_selector(".r-thb0q2")

        # for _ in range(2):
        #     elem.send_keys(Keys.PAGE_DOWN)
        #     time.sleep(0.2)

        # twitter_elm = browser.find_elements_by_css_selector(".r-thb0q2")

        # for post in twitter_elm:
        #     print(post.text)
        print("Twitter scrape")

