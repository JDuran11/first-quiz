################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
   # if city == "Quito":
   #    return 22
   # if city == "Sao Paulo":
   #    return 17
   # if city == "San Francisco":
   #    return 16
   cities_temperature = {
      "Quito": 22,
      "Sao Paulo": 17,
      "San Francisco": 16,
      "New York": 14
   }
   return cities_temperature.get(city)

def get_city_weather(city):

#   sky_condition = None

#   if city == "Sao Paulo":
#      sky_condition = "cloudy"
#   elif city == "New York":
#      sky_condition = "rainy"

   day_state = {
      "Quito" : "sunny",
      "Sao Paulo" : "cloudy",
      "San Francisco" : "cloudy",
      "New York" : "rainy" 
   }
   
   day_state = day_state.get(city)
   
   return str(get_city_temperature(city)) + " degrees and " + day_state
  
  
#print(get_city_weather("New York"))