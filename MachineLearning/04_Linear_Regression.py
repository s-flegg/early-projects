# linear regression is used for predicting the future
# basically the line of best fit

import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# r is the relationship
# -1 to 1
# -1 and 1 = 100% related, 0 = 0% related
slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    """Creates line, y = mx + c"""
    return slope * x + intercept


# run each value of the x array through the func to create the line
mymodel = list(map(myfunc, x))


print(r)

# predict future values with the linear regression line
# this predicts the y value of x value 10
speed = myfunc(10)
print(speed)

plt.scatter(x, y)
# draw the linear regression line
plt.plot(x, mymodel)
plt.show()
