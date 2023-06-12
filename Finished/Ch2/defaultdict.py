# Example file for Advanced Python: Hands On by Joe Marini
# Count items using a default dictionary

import json
import pprint
from collections import defaultdict

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# The defaultdict collection provides a cleaner way of initializing key values
# Count the number of data points for each year we have data
years = defaultdict(int)
for d in weatherdata:
    key = d['date'][0:4]
    years[key] += 1
pprint.pp(years)

# defaultdict can use more complex objects, like lists
years_months = defaultdict(list)
# create a dictionary with year-month keys and lists for each day in the month
for d in weatherdata:
    key = d['date'][0:7]
    years_months[key].append(d)
print(len(years_months))

# What were the coldest and warmest days of each month?
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])

# loop over the keys of the dictionary and find each warmest and coldest day
for year_month, daylist in years_months.items():
    print(f"Warmest day in {year_month}: {warmest_day(daylist)}")
    print(f"Coldest day in {year_month}: {coldest_day(daylist)}")
