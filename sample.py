from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

# Loading IRIS dataset from scikit-learn object into iris variable.
iris = datasets.load_iris()

# Prints the type/type object of iris
print('type(iris)' )
print(type(iris))
print()
# <class 'sklearn.datasets.base.Bunch'>

# prints the dictionary keys of iris data
print('iris.keys()')
print(iris.keys())
print()

# prints the type/type object of given attributes
print('type(iris.data), type(iris.target)')
print(type(iris.data), type(iris.target))
print()

# prints the no of rows and columns in the dataset
print('iris.data.shape')
print(iris.data.shape)
print()

# prints the target set of the data
print('iris.target_names')
print(iris.target_names)
print()

# Load iris training dataset
X = iris.data

# Load iris target set
Y = iris.target

# Convert datasets' type into dataframe
df = pd.DataFrame(X, columns=iris.feature_names)

# Print the first five tuples of dataframe.
print(df.head())