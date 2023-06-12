# Example file for Advanced Python: Hands On by Joe Marini

import json
import random
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get the first 30 days in the dataset
month_data = weatherdata[0:30]

# the shuffle() function will randomly shuffle a list in-place
pprint.pp(month_data[0:3])
print("---------------------------")
random.shuffle(month_data)
pprint.pp(month_data[0:3])

# use choice() and choices() to get random items, but beware that
# these functions can produce duplicate results
rnd_day = random.choice(month_data)
pprint.pp(rnd_day)
print("---------------------------")

rnd_days = random.choices(month_data, k=3)
pprint.pp(rnd_days)

# the sample() function will choose random items with no duplicates
rnd_days = random.sample(month_data, k=3)
pprint.pp(rnd_days)
