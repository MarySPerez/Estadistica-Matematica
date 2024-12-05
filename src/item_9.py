import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("./src/datos_.csv")
le = LabelEncoder()

data["sex_aux"] = le.fit_transform(data["sex"])
data["smoker_aux"] = le.fit_transform(data["smoker"])
data["region_aux"] = le.fit_transform(data["region"])
data["smoker_bmi"] = data["smoker_aux"] * data["bmi"]

X = data[
    ["age", "sex_aux", "bmi", "children", "smoker_aux", "region_aux", "smoker_bmi"]
]
y = data["expenses"]

model = LinearRegression()

model.fit(X, y)

r_squared = model.score(X, y)
print("Coeficiente de determinación con interacción:", r_squared)