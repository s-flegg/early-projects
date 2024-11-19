# solves classification problem
# predicts categorical outcomes
# linear regression predicts continuous outcomes

# 2 outcomes = binomial
# more than 2 = multinomial

import numpy
from sklearn import linear_model

# independent variable X
# dependant variable y

# X = size of tumor in mm
# reshape X into a column form a row so LogisticRegression() can work
X = numpy.array(
    [3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]
).reshape(-1, 1)

# y is cancerous, 1 is yes
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

# now can predict based on size
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
print(predicted)

# coefficient is the expected change in log-odds
# of having the outcome per unit change in X.
log_odds = logr.coef_
odds = numpy.exp(log_odds)
print(odds)
# meaning as size of tumor increase by 1mm odds of it being cancerous increases 4x


# util coef and intercept vals to find probability each tumor is cancerous
def logit2prob(logr, x):
    # log y = x log m + log c
    log_odds = logr.coef_ * x + logr.intercept_
    # de log
    odds = numpy.exp(log_odds)
    # odds to probability
    probability = odds / (1 + odds)
    return probability


print("\n")
# probability each tumor is cancerous, decimal
print(logit2prob(logr, X))
