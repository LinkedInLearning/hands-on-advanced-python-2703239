# Example file for Advanced Python: Hands On by Joe Marini
# Solution file for programming challenge

# Challenge: using the weather data set, write code to transform each
# weather data point from a dictionary into a tuple value that contains
# the date string and a string that is one of "cold", "warm", "hot" based
# upon the average temperature for that day. Return the newly created
# list of tuples as the result.
# "cold" day: average temp <= 60
# "warm" day: average temp between 60 and 80
# "hot" day: average temp >= 80
#
# Example: 
# This weather record:               Becomes this tuple:
# {
#     "date": "2017-01-01",          ("2017-01-01", "cold")
#     "tmin": 41,
#     "tmax": 50,
#     "prcp": 0.54,
#     "snow": 0.0,
#     "snwd": 0.0,
#     "awnd": 6.49
# }

import json

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# create a new list that transforms each element in the weather data
def average_temp_to_desc(day_data):
    avg_temp = (day_data['tmin'] + day_data['tmax']) /2
    desc = ""
    if avg_temp <= 60:
        desc = "cold"
    elif avg_temp > 60 and avg_temp < 80:
        desc = "warm"
    else:
        desc = "hot"
    return (day_data['date'], desc)
    
newdata = list(map(average_temp_to_desc, weatherdata))
print(len(weatherdata), len(newdata))
print(newdata)
