import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(df.head())

