from bs4 import BeautifulSoup
import requests
import shutil
import os

def amazonCollector(name, db):
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/198.88.101.216 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    search = "https://www.amazon.ca/s?k="+ name +"&i=grocery&s=review-rank"

    page = requests.get(search, headers=HEADERS)

    soup = BeautifulSoup(page.content, "lxml")

    taga = soup.find_all("a", href=True)

    
    test_string = "&s=grocery&sr=1-"
    i = 1

    for raw_link in taga:
        if i != 4:
            link = raw_link['href']

            if  test_string + str(i) in link:
                
                search = "https://www.amazon.ca" + link
                page = requests.get(search, headers=HEADERS)

                soup = BeautifulSoup(page.content, "lxml")
                
            
                title = soup.find("span", attrs={"id": 'productTitle'})
            
                price_whole = str(soup.find("span", attrs={"class": 'a-price-whole'}))[28:30]
                price_decimal = str(soup.find("span", attrs={"class": 'a-price-fraction'}))[31:33]

                if price_whole[1] == '<':
                    price_whole = price_whole[0]
                if price_decimal[1] == '<':
                    price_decimal = price_decimal[0]

                price = float(price_whole + "." + price_decimal)

                title_value = title.string

                db[i - 1] = {title_value, price}

                i += 1
        else:
            return db
        
            
            
            
             






        


    




    


db = dict()

db = amazonCollector("milk", db)


print(db)


