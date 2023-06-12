# Example file for Advanced Python: Hands On by Joe Marini
# Using the random package

import json
import random

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

def select_days(year, month):
    # concatenate the year and month to one string
    yearmonth = year + "-" + month

    def yearmonthfilter(day):
        if yearmonth in day['date']:
            return True
        return False

    # use that string to filter the weather data
    yearmonthdata = list(filter(yearmonthfilter, weatherdata))
    # use the random.sample method to select 5 days
    datalist = random.sample(yearmonthdata, k=5)

    # return the list
    return datalist

result = select_days("2020", "12")
print(result)
