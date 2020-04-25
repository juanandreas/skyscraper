import uuid
import _thread
import time
import yaml



class NewsAgent(object):

    def __init__(self, config, news_type):
        self.config = config
        self.agent_id = news_type[0]
        self.news_sites = news_type[1]

    # Define a function for the thread
    def run_scrape(self, news_site, thread_name, delay):
        while True:
            print("Agent:{0} scrape skirrt skirrt on {1}".format(thread_name, news_site))
            time.sleep(delay)

    def run_agent(self):
        # Create thread per news url
        try:
            for news_site in self.news_sites:
                _thread.start_new_thread(self.run_scrape, (news_site, str(uuid.uuid4()), 8,))
        except:
            raise Exception("Error: unable to start thread")

        while 1:
            pass

def main(config, news_types):
    agents = {}
    for news_data in news_types:
        agents[news_data[0]] = NewsAgent(config, news_data)

    for agent in agents:
        agents[agent].run_agent()

if __name__ == '__main__':
    conf = yaml.load(open("conf/prod/conf.yaml", 'r').read(), Loader=yaml.Loader)
    finance_news = yaml.load(open("news_sites/finance_news.yaml", 'r').read(), Loader=yaml.Loader)
    yahoo_finance_sites = finance_news["news_sites"]["yahoo_finance_sites"]
    news_types = [("yahoo_finance", yahoo_finance_sites)]
    main(conf, news_types)

