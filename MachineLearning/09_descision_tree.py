# a tree/flow chart
# makes decisions based on past data

import matplotlib.pyplot as plt
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("data2.csv")

print(df)
print("\n")

# change string values into numerical values
d = {"UK": 0, "USA": 1, "N": 2}
df["Nationality"] = df["Nationality"].map(d)
d = {"YES": 1, "NO": 0}
df["Go"] = df["Go"].map(d)

print(df)
print("\n")

# separate feature columns from target columns
features = ["Age", "Experience", "Rank", "Nationality"]

X = df[features]
y = df["Go"]

print(X)
print("\n")
print(y)

# create the decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X.values, y)

# display the tree
tree.plot_tree(dtree, feature_names=features)
plt.show()

# explanation
# Rank <= 6.5 means comedians with rank <= 6.5 follow the True arrow
# gini = 0.497 is the quality of the split
# gini is 0.0 to 0.5, 0.0 means all samples got the same result,
# 0.5 means a perfect split
# samples = 13 is how many comedians are left at this point
# value = [6, 7] means that 6 will get a no and 7 will get a go

# Gini method is a method of splitting the sample
# gini = 1 - (x/n)^2 - (y/n)^2
# where x = no. of positive answers, n is the no. of samples,
# y is the no. of negative answers

# use the decision tree to predict new values
print(dtree.predict([[40, 10, 7, 1]]))

# decision tree isn't 100%, answer will change each run
