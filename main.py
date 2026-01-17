import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


#print(load_diabetes()["DESCR"])

X, y = load_diabetes(return_X_y=True, as_frame=True)

mod = KNeighborsRegressor()
mod.fit(X, y)


pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", KNeighborsRegressor(n_neighbors=1))
])

pipe.fit(X, y)
pred = pipe.predict(X)

plt.scatter(pred, y)
plt.show()