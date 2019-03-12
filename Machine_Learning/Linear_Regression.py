import statsmodels.api as sm
from sklearn import datasets, linear_model
import numpy as np
import pandas as pd

# Load the data and put it into pandas
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# look at the description of it
print(data.DESCR)

# lets make a simple model without constants
X = df["sepal width (cm)"]
Y = df["petal length (cm)"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)
model.summary()

# Add constant to the model
X = sm.add_constant(X)

# Add more variables to the model
X = df[["sepal width (cm)", "sepal length (cm)"]]
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)
model.summary()

# lets use sklearn now
target = pd.DataFrame(data.target, columns=["petal length (cm)"])
lm = linear_model.LinearRegression()
model = lm.fit(X, Y)
predictions = lm.predict(X)
print(predictions)[0:5]

# Get the r squared value
lm.score(X, Y)
lm.coef_
lm.intercept_
