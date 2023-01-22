from bs4 import BeautifulSoup
import requests
import random


ran_list  = ["147.193.158.146",
"34.67.133.244",
"197.209.144.232",
"63.138.171.176",
"47.113.19.170"]
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

            
            index = -1

            for i, c in enumerate(price):
                if not c.isdigit():
                    index = i
                    break

            price = price[:index + 3]

            if price != '':
                price = float(price)

                if price < float(min_price):

                    min_price = price
                    dict_to_add = {
                        "name": name,
                        "price": price,
                        "link": link
                    }
                    self.item_info[item] = dict_to_add
    

