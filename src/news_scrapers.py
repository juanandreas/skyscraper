import uuid
import _thread
import time
import yaml



class NewsScraper(object):

    def __init__(self, config, news_type):
        self.config = config
        self.agent_id = news_type[0]
        self.news_sites = news_type[1]

    # Define a function for the thread
    # Maybe override this function per news source (i.e. twitter, citron, etc) css selector will be different
    # Chrome extension: SelectorGadget
    def run_scrape(self, news_site, thread_name, delay):
        while True:
            print("Agent:{0} scrape skirrt skirrt on {1}".format(thread_name, news_site))
            time.sleep(delay)

    def run_threads(self):
        # Create thread per news_url
        try:
            for news_site in self.news_sites:
                _thread.start_new_thread(self.run_scrape, (news_site, str(uuid.uuid4()), 8,))
        except:
            raise Exception("Error: unable to start thread")

        while 1:
            pass

def main(config, news_sources):
    """
    news_sources = [
        ("news_id", [news_urls_list]), 
        ("news_id", [news_urls_list]), 
        ...
    ]
    """
    scrapers = {}
    for news_id, news_urls_list in news_types:
        # build Scraper for each news_id
        scrapers[news_id] = NewsScraper(config, news_urls_list)

    for scraper in scrapers:
        scrapers[scraper].run_threads()

if __name__ == '__main__':
    conf = yaml.load(open("conf/prod/conf.yaml", 'r').read(), Loader=yaml.Loader)
    
    finance_news = yaml.load(open("news_urls/yahoo_finance.yaml", 'r').read(), Loader=yaml.Loader)
    yahoo_finance_sites = finance_news["news_sites"]["yahoo_finance_sites"]
    
    news_sources = [
        ("yahoo_finance", yahoo_finance_sites)
        ]
    main(conf, news_sources)

