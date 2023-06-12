# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# calculate the mean for both min and max temperatures
max_temps = [d['tmax'] for d in summer_months]
min_temps = [d['tmin'] for d in summer_months]
print(max_mean := statistics.mean(max_temps))
print(min_mean := statistics.mean(min_temps))

# calculate the median values for min and max temperatures
print(statistics.median(max_temps))
print(statistics.median(min_temps))

# use the standard deviation function to find outlier temperatures
upper_outlier = max_mean + statistics.stdev(max_temps) * 2
lower_outlier = min_mean - statistics.stdev(min_temps) * 2
print(upper_outlier)
print(lower_outlier)

max_outliers = [t for t in max_temps if t >= upper_outlier] 
min_outliers = [t for t in min_temps if t <= lower_outlier] 
print("Upper outliers", max_outliers)
print("Lower outliers", min_outliers)
