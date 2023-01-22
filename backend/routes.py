from fastapi import FastAPI
import nutrition 

app = FastAPI()

@app.get('/api/nutrition')
def products(food:str):
    nu = nutrition.NutritionChecker(['apple','banana'])
    result = nu.search_for_nutrition()
    return {"data":result}