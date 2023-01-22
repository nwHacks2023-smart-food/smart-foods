from bs4 import BeautifulSoup
from random import choice
import requests


ran_list  = ["175.253.118.191", "120.182.24.204", "13.217.229.181", "158.6.11.214", "188.173.32.94"]

random_IP = choice(ran_list)

HEADERS = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + random_IP +  ' Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}

class Walmartscraper():
    def __init__(self, user_input: list):
        self.choices = user_input 
        self.item_info = {}


    def scraper_walmart(self):
        for item in self.choices:
            search = "https://www.walmart.ca/search?q=" + item + "&c=10019"
            page = requests.get(search, headers=HEADERS)
            soup = BeautifulSoup(page.content, "html.parser")
            self.return_item_info(item, soup)
        return self.item_info

    def return_item_info(self, item, soup):
        products = [product.text for 
        product in soup.find_all("p", attrs={"data-automation": "css-1p4va6y eudvd6x0"})]
        prices = [price.text for 
            price in soup.find_all("p", attrs={"data-automation": "css-1p4va6y eudvd6x0"})]
        links = [link.get("href") for 
            link in soup.find_all("a", attrs={"class": "css-mfluef e1m8uw911"})]
        min_price = 100000

        print(soup.find_all("p", attrs={"data-automation": "css-1p4va6y eudvd6x0"}))

        products = [title.text for title in products]
        price = [(price.text) for price in prices]
        links = [ "https://www.walmart.ca"+ link["href"] for link in links]

        


        min_price = 10000
        index = smallest_index(products, prices, links)
        for i in range(0, index):
            name = products[i]
            price = prices[i]
            link = links[i]

            if price < min_price:
                dict_to_add = {
                    "name": name,
                    "price": price,
                    "link": link
                }
                self.item_info[item] = dict_to_add


def smallest_index(titles, prices, index):
    indexm = 0
    lst = [len(titles), len(prices), len(index)]

    for i in range(0,3):
        if (lst[i] < lst[indexm]):
            indexm = i
    
    return lst[indexm]

# TODO: Add links
# TODO: Add budgeting mechanism