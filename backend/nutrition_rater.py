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
<<<<<<< HEAD
        print(total_nutrients)
            

test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
test_rater = nutritionRater("Male", 3, test.search_for_nutrition())
=======
        
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
>>>>>>> 9f1b0b6d8ecd4e3d739fbd75e4258a9b9b5bfe62

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


# test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
# test_rater = nutritionRater("Man", 3, test.search_for_nutrition())