# for more than 2 variables
import pandas
from sklearn import linear_model

# reading the data file
df = pandas.read_csv("data.csv")

# independent value
X = df[["Weight", "Volume"]]
# dependant value
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

# coefficient
# describes the relationship against an unknown variable
print(regr.coef_)
# if weight increases by then, if volume increases by one then
# co2 emissions increase by
