import multiprocessing

class Multiprocess(object):

    def __init__(self, config, news_id, news_sources):
        self.config = config
        self.news_id = news_id
        self.news_urls_list = news_sources[news_id]
        self.processes = {}

    def get_processes(self):
        return self.processes

    def print_processes(self):
        for process_name, process_obj in self.processes:
            print(process_name, process_obj)

    def setup_processes(self, func):
        """
        func: Function to run (a.k.a; should be scraping for A SINGLE url)
        """
        # Create process per url
        try:
            for i, news_url in enumerate(self.news_urls_list):
                self.processes["{0}_{1}".format(self.news_id, i)] = \
                    multiprocessing.Process(target=func, args=(news_url,))
        except:
            raise Exception("Error: unable to start process")

    def kickoff_processes(self):
        for process_id in self.processes:
            process = self.processes[process_id]
            process.start()

        for process_id in self.processes:
            process = self.processes[process_id]
            process.join()

    