import uuid
from bs4 import BeautifulSoup
import urllib.request

from hist_price.models import Item, Brand, PriceHistory

class BlackmoresCrawler(object):

    def __init__(self):
        self.headers = {'user-agent': 'blackmores/1.0'}
        # self.url = 'http://www.blac.com/fi/'
        self.uuid = uuid.uuid4()

    def get_product_detail(self, au_url):
        prod_list = []
        prod_html = urllib.request.urlopen(au_url).read()
        soup = BeautifulSoup(prod_html, "lxml")
        products = soup.find_all('a', class_='product-container')
        brand = Brand.objects.get(pk=2)
        for product in products:
            id = int(product.find('div', id=True)['id'].split('-')[1])
            item, created = Item.objects.get_or_create(brand=brand, pid=id)
            if created:
                title_list = product['title'].split(' ')
                index = len(title_list)
                for word in reversed(title_list):
                    if word.isdigit():
                        index = title_list.index(word)
                        break
                item.name = " ".join(title_list[2:index])
                item.size = " ".join(title_list[index:index + 2])
                item.url = "http://www.chemistwarehouse.com.au/" + product['href']
            price = float(product.find('span', class_='Price').get_text()[1:])
            if price:
                item.update_price(price)
                item.status = Item.OK
            item.save()