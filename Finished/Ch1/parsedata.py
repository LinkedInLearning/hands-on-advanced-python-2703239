# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# make sure the data loaded correctly by printing the length of the dataset
print(len(weatherdata))
# let's also take a look at the first item in the data
pprint.pp(weatherdata[0])

# How many days of data do we have for each year?
years = {}
for d in weatherdata:
    key = d['date'][0:4]
    if key in years:
        years[key] += 1
    else:
        years[key] = 1

pprint.pp(years, width=5)
