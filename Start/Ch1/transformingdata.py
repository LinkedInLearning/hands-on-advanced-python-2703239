# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    return (f - 32) * 5/9


def ToMM(i):
    return i * 25.4


def ToKPH(s):
    return s * 1.60934


def ToMetric(wd):
    pass

# TODO: Use map() to call ToMetric and convert weatherdata to metric


# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
