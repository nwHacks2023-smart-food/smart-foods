from nutrition_dict import nutrition_dict
from nutrition_checker import nutritionChecker
import pandas as pd 
import numpy as np

class nutritionRater():
    def __init__(self, sex, days, nutrient_values: dict):
        self.sex = sex
        self.days = int(days)
        self.nutrition_info = nutrient_values
        self.nutrition_dv = {}

        self.set_sex_nutrition()
        self.compare_nutrients()

    def set_sex_nutrition(self):
        if self.sex == "Man":
            i = 0
        else:
            i = 1
        self.nutrition_dv = pd.Series({nutrient:value[i] for nutrient, value in nutrition_dict.items()})
       
    def compare_nutrients(self):
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
        
        # Divides series by number of days in budget
        total_nutrients = total_nutrients / self.days
        keys = total_nutrients.index.tolist()
        values = nutrition_dict.keys()
        new_index = dict(zip(keys, values))
        total_nutrients.rename(new_index, inplace=True)        

        # Comparison logic
        print(total_nutrients)
        print(self.nutrition_dv)
        # mask = np.where(total_nutrients < self.nutrition_dv, True, False)
        # print(mask)

test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
test_rater = nutritionRater("Man", 3, test.search_for_nutrition())

# TODO: Sum numpy arrays together to compare against dict value (based on i)
# TODO: create individual numpy array for each item???
# TODO: Consider how to scale values based on period chosen 