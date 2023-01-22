from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from nutrition_checker import nutritionChecker
from saveonfoods import saveOnFoodsCollector
from amazon_scraping import amazonScraper

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["20.104.64.188"],
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str

class ItemList(BaseModel):
    items: List[Item]

@app.get('/api/nutrition')
def products(food:str):
    nu = nutritionChecker([food])
    result = nu.search_for_nutrition()
    return result

@app.post('/api/items')
def post_to_items(body: dict):
    items:ItemList = body["items"]
    sof = saveOnFoodsCollector(items)
    amazon = amazonScraper(items)
    result_sof = sof.scrap_save_on_foods()
    result_amazon = amazon.scrap_amazon()
    return  {'amazon':result_amazon,'saveonfood':result_sof}
