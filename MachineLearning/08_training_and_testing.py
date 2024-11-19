# Train/Test method
# split data 80/20
# 80 to train/ 20 to test
# training means creating the model
# testing means the checking the accuracy

import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

numpy.random.seed(2)

# get a data set

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

# split into train/test
# data for training should be randomly selected
# for testing should be the remaining 20
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# check the training selection is a fair selected (looks like the full set does)
plt.scatter(train_x, train_y)
plt.show()
# same for testing set
plt.scatter(test_x, test_y)
plt.show()

# decide if linear, polynomial or multiple based on how it looks
# then make
model = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
line = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(line, model(line))
plt.show()

# check the relationship is good
print(r2_score(train_y, model(train_x)))

# check the relationship is also good for the testing set
print(r2_score(test_y, model(test_x)))

# the model can now be used to predict values
print(model(5))
