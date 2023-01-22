from amazon_scraping import amazonScraper
from saveonfoods import saveOnFoodsCollector
from walmart_scraping import Walmartscraper

USER_INPUT = ["apple", "lemons", "bananas"]


# amazon_options = amazonScraper(USER_INPUT)
# saveonfoods_options = saveOnFoodsCollector(USER_INPUT)
walmart_options = Walmartscraper(USER_INPUT)

# print(amazon_options.scrap_amazon())
# print(saveonfoods_options.scrap_save_on_foods())
print(walmart_options.scraper_walmart())