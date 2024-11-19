import pandas
from sklearn import linear_model

df = pandas.read_csv("Large Data Set CARS.csv")
df.fillna(0, inplace=False)

ohe_make = pandas.get_dummies(df["Make"])
ohe_region = pandas.get_dummies(df["GovRegion"])

variables = [
    "PropulsionTypeId",
    "BodyTypeId",
    "KeeperTitleId",
    "EngineSize",
    "YearRegistered",
    "Mass",
    "CO2",
    "CO",
    "NOX",
    "part",
    "hc",
]

y_option = int(
    input(
        "What would you like to predict?"
        + "\n"
        + "1) Make "
        + "\n"
        + "2) PropulsionTypeId"
        + "\n"
        + "3) BodyTypeId "
        + "\n"
        + "4) GovRegion"
        + "\n"
        + "5) KeeperTitleId"
        + "\n"
        + "6) EngineSize "
        + "\n"
        + "7) YearRegistered"
        + "\n"
        + "8) Mass"
        + "\n"
        + "9) CO2"
        + "\n"
        + "10) CO \n11) NOX\n12) part\n13) hc"
        + "\n: "
    )
)

y = variables[y_option]
prediction_data = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

if y_option == 1:
    X = pandas.concat([df[variables], ohe_region], axis=1)
    for i in range(11):
        print(variables[i])
        prediction_data[i] = input("Known " + variables[i] + ": ")
    prediction_data[11] = input("Known GovRegion: ")
elif y_option == 4:
    X = pandas.concat([df[variables], ohe_make], axis=1)
    for i in range(11):
        prediction_data[i] = input("Known " + variables[i] + ": ")
    prediction_data[11] = input("Known Make: ")
else:
    temp = variables
    variables.remove(variables[y_option])
    X = pandas.concat([df[variables], ohe_make, ohe_region], axis=1)
    for i in range(10):
        prediction_data[i] = input("Known " + variables[i] + ": ")
        prediction_data[10] = input("Known Make: ")
        prediction_data[11] = input("Known GovRegion: ")
    variables = temp

print(prediction_data)
print(X)
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

prediction = regr.predict(prediction_data)
print(prediction_data)
print(prediction)
