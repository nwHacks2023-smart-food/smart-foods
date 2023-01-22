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
        # Slicing to last element to stop before serving size
        under_mask = np.where(total_nutrients.iloc[:-1] < self.nutrition_dv.iloc[:-1], True, False)
        under_nutrients = total_nutrients[:-1].loc[under_mask].index.tolist()
        under_nutrients = [str(i).replace("_", " ") for i in under_nutrients]

        over_mask = np.where(total_nutrients.iloc[:-1] > self.nutrition_dv.iloc[:-1], True, False)
        over_nutrients = total_nutrients[:-1].loc[over_mask].index.tolist()
        over_nutrients = [str(i).replace("_", " ") for i in over_nutrients]


        under_return_message = None
        over_return_message = None

        if len(under_nutrients) > 0:
            under_nutrients = ", and ".join(under_nutrients)
            under_return_message = f"You could use more {under_nutrients} in your diet!"
        if len(over_nutrients) > 0:
            over_nutrients = ", ".join(over_nutrients)
            over_return_message = f"You have a bit too much {over_nutrients} in your diet!"



        if (under_return_message and over_return_message is not None): 
            return(f"{under_return_message}\n + {over_return_message}")
        elif under_return_message is not None:
            return(under_return_message)
        else:
            return(over_return_message)


test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
test_rater = nutritionRater("Man", 3, test.search_for_nutrition())

# TODO: Sum numpy arrays together to compare against dict value (based on i)
# TODO: create individual numpy array for each item???
# TODO: Consider how to scale values based on period chosen 