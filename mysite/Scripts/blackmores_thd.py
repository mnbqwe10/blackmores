from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()


import threading
from hist_price.crawler.crawler import BlackmoresCrawler


class BlackmoresThread(threading.Thread):

    def __init__(self):
        # super(BlackmoresThread, self).__init__()
        threading.Thread.__init__(self)
        self.crawler = BlackmoresCrawler()
        # self.crawler.feed('http://www.verkkokauppa.com/')

    def run(self):
        self.crawler.get_product_detail('https://www.chemistwarehouse.com.au/Shop-OnLine/513/Blackmores?size=120')


def main():
    crawling = BlackmoresThread()
    crawling.start()

if __name__ == '__main__':
    main()
