# Example file for Advanced Python: Hands On by Joe Marini
# Solution file for programming challenge

import json
from functools import reduce

# Challenge: using the reduce() function, return the most "miserable" day
# in the data set as calculated by a combination of heat, rain, and wind.
#
# To calculate a "misery score", use the following formula:
# score = (average wind speed + (precipitation * 10) + (max temp * 0.8)) / 3


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

def misery_score(day):
    wind = 0 if day['awnd'] is None else day['awnd']
    temp = day['tmax'] * 0.8
    rain = day['prcp'] * 10

    score = (temp + rain + wind) / 3
    return score

def day_rank(acc, elem):
    return acc if misery_score(acc) >= misery_score(elem) else elem

result = reduce(day_rank, weatherdata)
print(f"{result['date']} with data: {result['tmax']}, {result['prcp']}, {result['awnd']}")
