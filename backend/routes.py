from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import nutrition 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/nutrition')
def products(food:str):
    nu = nutrition.NutritionChecker([food])
    result = nu.search_for_nutrition()
    return {"data":result}