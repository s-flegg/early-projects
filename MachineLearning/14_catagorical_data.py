# representing sting data numerically

import pandas as pd
from sklearn import linear_model

cars = pd.read_csv("data.csv")
print(cars.to_string())

# create a column for each category, with 1 or 0
# called One Hot Encode
ohe_cars = pd.get_dummies(cars["Car"])
print("\n")
print(ohe_cars.to_string())

# select variables
X = pd.concat([cars[["Volume", "Weight"]], ohe_cars], axis=1)
y = cars["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)

# predict the CO2 emission of a Volvo where the weight is 2300kg,
# and the volume is 1300cm3:
predictedCO2 = regr.predict(
    [[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
)
print(predictedCO2)

# -------------------------------------
# can have 1 less column than categories by using true and false
colors = pd.DataFrame({"color": ["blue", "red", "green"]})
dummies = pd.get_dummies(colors, drop_first=True)
dummies["color"] = colors["color"]

print(dummies)
