# Example file for Advanced Python: Hands On by Joe Marini
# Sort the data in a sequence

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# create a subset of the data for days that had snowfall
dataset = list(filter(lambda d: d['snow'] > 0.0, weatherdata))

# sort the entire data set by how much snowfall there was
# TODO: method 1: use the sorted() function to create a new list


# TODO: method 2: use the sort() function that every list has to sort in-place


# TODO: Sort on multiple fields: first by snowfall, then by average wind speed
