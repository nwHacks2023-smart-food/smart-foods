from bs4 import BeautifulSoup
from random import choice
import requests

USER_INPUT = ["apples", "banana", "oranges"]
ran_list  = ["228.39.248.80", "116.132.147.250", "178.172.154.68", "139.64.230.154", "207.157.75.236"]

random_IP = choice(ran_list)

HEADERS = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + random_IP +  ' Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}

class amazonScraper():
    def __init__(self, user_input: list):
        self.choices = user_input
        self.prices = {}

        self.amazonCollector(self.choices)

    def amazonCollector(self, choices):
        for item in choices:
            search = "https://www.amazon.ca/s?k=" + item + "&i=grocery&s=review-rank"
            page = requests.get(search, headers=HEADERS)
            soup = BeautifulSoup(page.content, "lxml")

            titles = soup.find_all("span", attrs={"class": 'a-size-base-plus a-color-base a-text-normal'})
            price_whole = str(soup.find_("span", attrs={"class": 'a-price-whole'})).decode_contents().strip()
            price_decimal = str(soup.find("span", attrs={"class": 'a-price-fraction'})).decode_contents().strip()
            min_price = 100000
            
            # for title in titles[:6]:
            #     price_whole = str(soup.find_all("span", attrs={"class": 'a-price-whole'}))[28:30]
            #     price_decimal = str(soup.find_all("span", attrs={"class": 'a-price-fraction'}))[31:33]

            #     if price_whole[1] == '<':
            #         price_whole = price_whole[0]
            #     elif price_decimal[1] == '<':
            #         price_decimal = price_decimal[0]
            #     price = float(price_whole + "." + price_decimal)

            #     if price < min_price:
            #         min_price = price
            
        #     self.prices[item] = [title_value, price]
        # return self.prices

            print(price_decimal)

scraper = amazonScraper(["apple","banana","oranges"])

# TODO: Add links
# TODO: Add budgeting mechanism