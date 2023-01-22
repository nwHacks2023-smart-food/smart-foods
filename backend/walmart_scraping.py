from bs4 import BeautifulSoup
from random import choice
import requests


ran_list  = ["228.39.248.80", "116.132.147.250", "178.172.154.68", "139.64.230.154", "207.157.75.236"]

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
            search = "https://www.walmart.ca/search?q=apple&" + item + "c=10019"
            page = requests.get(search, headers=HEADERS)
            soup = BeautifulSoup(page.content, "lxml")
            self.return_item_info(item, soup)
        return self.item_info

    def return_item_info(self, item, soup):
        titles = soup.find_all("span", attrs={"data-automation": 'names'})
        prices = soup.find_all("span", attrs={"data-automation": 'a-price-whole'})
        links = soup.find_all("a", href=True)
        min_price = 100000

        titles = [title.text for title in titles]
        price = [(price.text) for price in prices]

        for link in links:
            if "/search/grocery" in link["href"]:
                "https://www.walmart.ca"+ link["href"]
                print(link["href"])

        min_price = 10000
        index = smallest_index(titles, prices, links)
        for i in range(0, index):
            name = titles[i]
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