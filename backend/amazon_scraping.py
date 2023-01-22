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
            search = "https://www.amazon.ca/s?k=" + item + "&i=grocery"
            page = requests.get(search, headers=HEADERS)
            soup = BeautifulSoup(page.content, "lxml")

            titles = soup.find_all("span", attrs={"class": 'a-size-base-plus a-color-base a-text-normal'})
            prices_whole = soup.find_all("span", attrs={"class": 'a-price-whole'})
            prices_decimal = soup.find_all("span", attrs={"class": 'a-price-fraction'})
            min_price = 100000

            titles = [title.text for title in titles]
            prices_whole = [(price_whole.text) for price_whole in prices_whole]
            prices_decimal = [(price_decimal.text).strip(".") for price_decimal in prices_decimal]
            prices = [float(prices_whole[i] + prices_decimal[i]) for i in range(0, len(prices_whole))] 

            print(len(titles))
            print(len(prices))     




scraper = amazonScraper(["apple","banana","oranges"])

# TODO: Add links
# TODO: Add budgeting mechanism