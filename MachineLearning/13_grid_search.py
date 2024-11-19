# most machine learning has tweak-able params
# e.g. c in logistic regression
# grid search helps pick best value for c

# grid search tries different values then picks the best
# can also do combinations of multiple params

# higher c tells the model to place a greater weight on training data
# default c val is 1

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# first check default params
iris = datasets.load_iris()

X = iris['data']
y = iris['target']

logit = LogisticRegression(max_iter=10000)
logit.fit(X, y)
print(logit.score(X, y))

# have an idea of good values for c for the task
# or trial and error ig

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []

for choice in C:
    logit.set_params(C=choice)
    logit.fit(X, y)
    scores.append(logit.score(X, y))

print(scores)
# increasing c to 1.75 increases accuracy, no improvement past this point
# should really use test/train to check data is accurate
# making a model using only training data can lead to overfitting
