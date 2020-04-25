from bs4 import BeautifulSoup

class BSS(object):
    def __init__(self):
        self.soup = None

    def setupSoup(self, html_doc, parser_type):
        self.soup = BeautifulSoup(html_doc, parser_type)
