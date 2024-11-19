import matplotlib.pyplot as plt
import numpy

# uniform data
# min value, max value, no. of entries
data = numpy.random.uniform(0.0, 5.0, 1000)

one, two, three, four, five = 0, 0, 0, 0, 0
for i in range(len(data)):
    if data[i] <= 1:
        one += 1
    elif data[i] <= 2:
        two += 1
    elif data[i] <= 3:
        three += 1
    elif data[i] <= 4:
        four += 1
    else:
        five += 1
print(one)
print(two)
print(three)
print(four)
print(five)

# histogram
# data, no. of bars
plt.hist(data, 5)
plt.show()

plt.hist(data, 100)
plt.show()

# normal distribution
# mean value, standard deviation, no. of entries
data = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(data, 100)
plt.show()

