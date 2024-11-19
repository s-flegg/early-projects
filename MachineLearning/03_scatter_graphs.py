import numpy
import matplotlib.pyplot as plt

data_x = numpy.random.normal(5.0, 1.0, 1000)
data_y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(data_x, data_y)
plt.show()
