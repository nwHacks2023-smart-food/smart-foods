from nutrition_dict import nutrition_dict
from nutrition_checker import nutritionChecker
import numpy as np

class nutritionRater():
    def __init__(self, gender, nutrient_values: dict):
        self.gender = gender
        self.nutrition_info = nutrient_values

        self.compare_nutrients()

    def compare_nutrients(self):
        # Set index to determine which value in nutrition_dict to use
        if self.gender == "Male":
            i = 0
        else:
            i = 1

        # Loops through item names in chosen items, converting nutrient info to a numpy array 
        for item in self.nutrition_info:
            numpy_array = np.array(self.nutrition_info[item])
            print(numpy_array)

test = nutritionChecker(["apple", "orange", "banana", "cup noodle"])
test_rater = nutritionRater("Male", test.search_for_nutrition())

# TODO: Sum numpy arrays together to compare against dict value (based on i)
# TODO: create individual numpy array for each item???
# TODO: Consider how to scale values based on period chosen 