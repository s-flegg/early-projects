import numpy
from scipy import stats

example_data = [95, 85, 75, 88, 64, 133, 122, 76, 45, 89, 88, 99, 89, 87]

# mean, median, mode
mean = numpy.mean(example_data)
median = numpy.median(example_data)
mode = stats.mode(example_data)

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))
print("\n")

# standard deviation, variance
std = numpy.std(example_data)
# variance is std^2
var = numpy.var(example_data)

print("Standard deviation: " + str(std))
print("Variance: " + str(var))
print("\n")

# percentiles
# 75th percentile means 75% is less than or equal to the value
percentile_75 = numpy.percentile(example_data, 75)
percentile_50 = numpy.percentile(example_data, 50)
percentile_25 = numpy.percentile(example_data, 25)

print("75th percentile: " + str(percentile_75))
print("50th percentile: " + str(percentile_50))
print("25th percentile: " + str(percentile_25))
print("\n")
