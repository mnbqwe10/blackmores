from __future__ import division
from time import strftime
import sqlite3
import argparse
from bs4 import BeautifulSoup
import urllib.request

__author__ = "qulong627@gmail.com"
__version__ = "1.1"
# product name
__pn__ = "blackmores"

# -------------------------------------------------------------------------------------------
# Project Path
project_path = "F:\QL\{}\\".format(__pn__)
db_browser_path = 'C:\\Program Files\\DB Browser for SQLite\\DB Browser for SQLite.exe'
# Database Settings
sqlite_file = project_path + "{}-product{}.sqlite".format(__pn__, __version__)
his_price_tb = "'datetime' INTEGER NOT NULL PRIMARY KEY UNIQUE, 'price' REAL "

au_url_list = ["https://www.chemistwarehouse.com.au/Shop-OnLine/513/Blackmores?size=120",
               "https://www.chemistwarehouse.com.au/Shop-Online/513/Blackmores?size=120&page=2"]
# nz_url = "http://www.healthpost.co.nz/brands/swisse?limit=all"

# -------------------------------------------------------------------------------------------


def get_au(au_url):
    prod_list = []
    prod_html = urllib.request.urlopen(au_url).read()
    print("Getting data from: " + au_url)
    print("......\n")
    soup = BeautifulSoup(prod_html, "lxml")
    print("Analyzing......\n")
    products = soup.find_all('a', class_='product-container')
    print("Total {} items found!".format(str(len(products))))
    for product in products:
        title_list = product['title'].split(' ')
        index = len(title_list)
        for word in reversed(title_list):
            if word.isdigit():
                index = title_list.index(word)
                break
        name = " ".join(title_list[2:index])
        size = " ".join(title_list[index:index+2])
        url = "http://www.chemistwarehouse.com.au/" + product['href']
        price = float(product.find('span', class_='Price').get_text()[1:])
        id = int(product.find('div', id=True)['id'].split('-')[1])
        print({'id': id, 'name': name, 'size': size, 'price': price})
        prod_list.append({'id': id, 'name': name, 'size': size, 'url': url, 'price': price})
    print("----------------------------------------------------------------------------------------")
    return prod_list


class sqlitedb():

    def __init__(self, sqlite_file):
        self.connection = sqlite3.connect(sqlite_file)
        self.cursor = self.connection.cursor()

    def new_table(self, table_name, table_column):
        # self.cursor.execute('DROP TABLE IF EXISTS "{tn}"'.format(tn=table_name))
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS "{tn}" ({cn})'.format(tn=table_name, cn=table_column))
        self._commit()

    def _commit(self):
        self.connection.commit()

    def close(self):
        self._commit()
        self.connection.close()

    def insert(self, table_name, datetime, price):
        tv = str(datetime)+","+str(price)
        self.cursor.execute(
            'INSERT OR REPLACE INTO "{tn}" VALUES ( {tv} )'.format(tn=table_name, tv=tv))
        self._commit()

    def add_item(self, table_name, value):
        row_value = '{id},"{nm}","{sz}","{ul}",{pr}'.format(id=value['id'],
                                                            nm=value['name'],
                                                            sz=value['size'],
                                                            ul=value['url'],
                                                            pr=value['price'])
        self.cursor.execute('insert or replace into {tn} values ({vs})'.format(tn=table_name,vs=row_value))
        self._commit()

    def read_table(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        return self.cursor.fetchall()

    def read_product_info(self, productID):
        self.cursor.execute("SELECT * FROM productinfo WHERE productID={}".format(productID))
        return self.cursor.fetchall()

    def read_lowest_price(self, productID):
        self.cursor.execute(
            'SELECT * FROM "{id}" WHERE datetime=(SELECT MAX(datetime) FROM "{id}" WHERE price=(SELECT MIN(price) FROM "{id}" WHERE price > 0))'.format(
                id=productID))
        return self.cursor.fetchall()


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-o", "--opendb", help="Open database", action="store_true")
    parser.add_argument("--latest", help="Read latest price", action="store_true")
    parser.add_argument("--lowest", help="Read lowest price", action="store_true")
    args = parser.parse_args()

    # Open database
    if args.opendb:
        import subprocess
        subprocess.call([db_browser_path, sqlite_file])

    # Read latest price
    elif args.latest:
        modify_db = sqlitedb(sqlite_file)
        rows = modify_db.read_table("productinfo")
        for row in rows:
            print("{},  {},  {}".format(str(row[0]), str(row[3]), row[1]))
        modify_db.close()

    # Read lowest price
    elif args.lowest:
        modify_db = sqlitedb(sqlite_file)
        rows = modify_db.read_table("productinfo")
        for row in rows:
            print(row[0:2])
            lowest_record = modify_db.read_lowest_price(row[0])
            print(lowest_record[0][1:])
        modify_db.close()

    # Collect price
    # else:
    if True:
        timestamp = strftime("%Y%m%d%H%M%S")
        print(timestamp)
        db = sqlitedb(sqlite_file)
        au_list = []
        for au_url in au_url_list:
            au_list = au_list + get_au(au_url)
        for item in au_list:
            db.new_table('au_'+str(item['id']), his_price_tb)
            db.insert('au_'+str(item['id']), int(timestamp), item['price'])
        for item in au_list:
            db.add_item('product_au', item)

        print("*****************************************************************")
        print("Database is updated!!!")
        print(timestamp + "is collected successfully!!!")
