# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily


# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)


# TODO: what was the warmest weekend day in the dataset?


# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
# coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
# coldest_date = date.fromisoformat(coldest_day['date'])
# print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days
