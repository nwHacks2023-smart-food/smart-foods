from bs4 import BeautifulSoup
import requests
import random

USER_INPUT = ["apples", "lemons", "cup noodles"]

ran_list  = ["228.39.248.80", "116.132.147.250", "178.172.154.68", "139.64.230.154", "207.157.75.236"]
random_IP = random.choice(ran_list)

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + random_IP + ' Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

class saveOnFoodsCollector():
    def __init__(self, user_input: list):
        self.choices = user_input 
        self.item_info = {}

    def scrap_save_on_foods(self):
        for item in self.choices:
            search = "https://www.saveonfoods.com/sm/pickup/rsid/1982/results?q=" + item
            page = requests.get(search, headers=HEADERS)
            soup = BeautifulSoup(page.content, "html.parser")
            self.return_item_info(item, soup)
        return self.item_info

    def return_item_info(self, item, soup):
        products = [product.decode_contents().strip() for 
                product in soup.find_all("div", {"class": "sc-hKFyIo bdDYJz"})]
        prices = [price.decode_contents().strip() for 
                  price in soup.find_all("span", {"class": "ProductCardPrice--ogjs72"})]
        links = [link.get("href") for 
                 link in soup.find_all("a", {"class": "ProductCardHiddenLink--1rjraab bWuEcw"})]
        min_price = 10000
        
        for i in range(0, len(products)):
            name = products[i][:products[i].index("<span")]
            price = prices[i][1:]
            link = links[i]
            try:
                end_index = price.index('/')
                price = price[:end_index]
                price = float(price)
            except:
                end_index = price.index(" ")
                price = price[:end_index]
                price = float(price)
            
            try:
                if price < float(min_price):
                    min_price = price
                    dict_to_add = {
                        "name": name,
                        "price": price,
                        "link": link
                    }
                    self.item_info[item] = dict_to_add
            except ValueError:
                if price < float(min_price):
                    min_price = price
                    dict_to_add = {
                        "name": name,
                        "price": price,
                        "link": link
                    }
                    self.item_info[item] = dict_to_add
