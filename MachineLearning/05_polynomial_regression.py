import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# amke polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# specify how the line will display, start and stop are x values
myline = numpy.linspace(1, 22, 100)

# r2 is r squared, and is the polynomial version of r
print(r2_score(y, mymodel(x)))

# predict values same as with linear
speed = mymodel(17)
print(speed)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
