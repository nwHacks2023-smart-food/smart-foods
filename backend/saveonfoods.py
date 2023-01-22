from bs4 import BeautifulSoup
import requests
import random


def saveOnFoodsCollector(name, db, random_IP):
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + random_IP +  ' Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    search = "https://www.saveonfoods.com/sm/pickup/rsid/1982/results?q="+ name

    page = requests.get(search, headers=HEADERS)

    soup = BeautifulSoup(page.content, "html.parser")

    names = soup.find_all("div", {"class": "sc-hKFyIo bdDYJz"})
    prices_raw = soup.find_all("span", {"class": "ProductCardPrice--ogjs72 jwvBiZ"})
    links_raw = soup.find_all("a", {"class": "ProductCardHiddenLink--1rjraab bWuEcw"})
    name_lst = []

    
    for name in names:
        name_str = str(name.decode_contents().strip())
        name_str = name_str[ : name_str.index("<span ")]

        print(name_str)

    for price in prices_raw:
        price = str(price.decode_contents().strip())

        print(price)
    

    for links in links_raw:
        print(links.get("href"))

    

db = dict()
ran_list  = ["228.39.248.80", "116.132.147.250", "178.172.154.68", "139.64.230.154", "207.157.75.236"]

random_IP = random.choice(ran_list)

saveOnFoodsCollector("water", db, random_IP)


print(db)