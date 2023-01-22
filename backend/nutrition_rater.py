from nutrition_dict import nutrition_dict
from nutrition_checker import nutritionChecker
import pandas as pd 

class nutritionRater():
    def __init__(self, gender, days, nutrient_values: dict):
        self.gender = gender
        self.days = int(days)
        self.nutrition_info = nutrient_values

        self.compare_nutrients()

    def compare_nutrients(self):
        # Set index to determine which value in nutrition_dict to use
        if self.gender == "Male":
            i = 0
        else:
            i = 1

        # Creates series that contains nutriton info of first item
        total_nutrients = pd.Series(self.nutrition_info[next(iter(self.nutrition_info))])

        # Loops through item names in chosen items, converting nutrient info to series
        # Adds item series to total info series
        for item in self.nutrition_info:
            if item == next(iter(self.nutrition_info)):
                # Skips first item 
                pass
            item_series = pd.Series(self.nutrition_info[item])
            total_nutrients = total_nutrients.add(item_series, fill_value=0)
        
        print(total_nutrients)
        # Divides series by number of days in budget
        total_nutrients = total_nutrients / self.days
        print(total_nutrients)
            

test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
test_rater = nutritionRater("Male", 3, test.search_for_nutrition())

# TODO: Sum numpy arrays together to compare against dict value (based on i)
# TODO: create individual numpy array for each item???
# TODO: Consider how to scale values based on period chosen 