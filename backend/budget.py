from amazon_scraping import amazonScraper
from saveonfoods import saveOnFoodsCollector

USER_INPUT = ["apples", "lemons", "bananas"]


amazon_options = amazonScraper(USER_INPUT)
saveonfoods_options = saveOnFoodsCollector(USER_INPUT)
print(amazon_options.scrap_amazon())
print(saveonfoods_options.scrap_save_on_foods())