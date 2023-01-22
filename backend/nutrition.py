from nutritionix import Nutritionix

APP_ID = "ff35c543"
API_KEY = "cf9016eb2bedc6abe0e9620bd6677599"
REMOTE_USER_ID = 0
NUTRIENTS = [
    "calories",
    "total_fat",
    "saturated_fat",
    "trans_fatty_acid",
    "polyunsaturated_fat",
    "monounsaturated_fat",
    "cholesterol",
    "sodium",
    "total_carbohydrate",
    "fiber",
    "sugars",
    "protein",
    "vitamin_a",
    "vitamin_c",
    "calcium",
    "iron"
]

class NutritionChecker():
    def __init__(self, user_input: list): 
        self.nix = Nutritionix(app_id=APP_ID, api_key=API_KEY)
        self.choices = user_input
        self.nutrition_info = {}
        
        self.search_for_nutrition()

    def search_for_nutrition(self):
        for item in self.choices:
            item_info = self.nix.search(item, results="0:1").json()
            id = item_info["hits"][0]["fields"]["item_id"]
            self.return_nutrition_info(item, id)
            
    def return_nutrition_info(self, item, item_id):
        raw_info = self.nix.item(id=item_id).json()
        nutrient_list = {nutrient:value for nutrient, value in raw_info.items() if nutrient[3:] in NUTRIENTS}
        self.nutrition_info[item] = nutrient_list

test = NutritionChecker(["apple", "orange", "banana"])