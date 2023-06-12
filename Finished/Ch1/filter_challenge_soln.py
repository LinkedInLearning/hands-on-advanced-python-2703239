# Example file for Advanced Python: Hands On by Joe Marini
# Solution file for programming challenge

# Challenge: using the weather data set, write code to use the filter()
# function to create a list of all the "cold, rainy, windy" days as
# define by precipitation (either rain or snow) > 0.7in, the average temp
# for the day being below 45deg F, and average wind > 10.0 mph

import json

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

def is_cold_windy_rainy_day(d):
    avg_temp = (d['tmax'] + d['tmin']) / 2
    total_prcp = d['snow'] + d['prcp']
    if avg_temp < 45 and total_prcp > 0.7 and d['awnd'] >= 10.0:
        return True
    return False

blustery_days = list(filter(is_cold_windy_rainy_day, weatherdata))
print(f"{len(blustery_days)} cold, windy, rainy days")
print(blustery_days)
