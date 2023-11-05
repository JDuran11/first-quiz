################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.

# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!


combination_elements = [
    
    {   "combinacion": ["lead", "mercury"],
        "estados": {"boil": ["hot lead and mercury", "gold"],
                    "freeze": ["cold lead and mercury","frozen lead and mercury"],
                    "room temperature": "lead and mercury"}
    },
    {
        "combinacion": ["water", "air"],
        "estados": {"boil": ["warm water", "steam"],
                    "freeze": ["cold water", "snow"],
                    "room temperature": "water" }
    },
    {
        "combinacion": ["cheese", "dough", "tomato"],
        "estados": {"boil": ["pizza", "borned pizza"],
                    "freeze": ["cold cheese, dough and tomato", "frozen cheese, dough and tomato"],
                    "room temperature": "cheese, dough and tomato" }
    }
]



class Oven:
    def __init__(self):
        self.ingredients = []
        self.output = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self, temperature):
        
        for diccionario in combination_elements:
            
            if self.ingredients == diccionario["combinacion"]:

                if temperature >= -5:
                    self.output = diccionario["estados"]["freeze"][0]
                    return self.output
                
                self.output = diccionario["estados"]["freeze"][1]
                return self.output
                

    def boil(self, temperature):
        
        for diccionario in combination_elements:
            
            if self.ingredients == diccionario["combinacion"]:

                if temperature <= 1000:
                    self.output = diccionario["estados"]["boil"][0]
                    return self.output
                
                self.output = diccionario["estados"]["boil"][1]
                return self.output
  

    def wait(self):
        
        for diccionario in combination_elements:
            
            if self.ingredients == diccionario["combinacion"]:

                self.output = diccionario["estados"]["room temperature"]
                return self.output

    def get_output(self):
        return self.output


def make_oven():
    return Oven()



def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze(temperature)
    elif temperature >= 100:
        oven.boil(temperature)
    else:
        oven.wait()

    return oven.get_output()