# Example file for Advanced Python: Hands On by Joe Marini

import json
import pprint
import random

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the random module can be used to generate random values
print(random.random())

# choose a random number in a range including both points
print(random.randint(10,20))
# choose a random number in a range excluding end point
print(random.randrange(10,20))

# build a list of the summer days in 2019
def is_summer_day(d):
    summer_months = ["2019-07-", "2019-08-"]
    if any([m in d['date'] for m in summer_months]):
        return True
    return False
summer_2019 = list(filter(is_summer_day, weatherdata))

# choose 5 random days from that summer
random_days = []
for _ in range(5):
    random_days.append(summer_2019[random.randrange(len(summer_2019))])
pprint.pp(random_days)

# what was the windiest of those 5 days?
print(max(random_days, key=lambda d:d['awnd']))
