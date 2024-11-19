# for comparing different scale variables
# e.g. weight in kg and volume in cm3

# multiple methods
# standardization method
# z is new value, x is the original value, u is the mea, s is the standard deviation
# z = (x - u) / s
# or use python libs
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[["Weight", "Volume"]]

scaledX = scale.fit_transform(X.values)

print(scaledX)

# scale when predicting values
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(scaledX, y.values)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
