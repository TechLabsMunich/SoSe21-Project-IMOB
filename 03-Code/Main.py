import functions as f

#GETTING THE X AND Y PART:

data_path = '../01-Data/sample_data'
id_path = "../01-Data/new data's IDs.xlsx"
target_variable = 'Ruhepuls'

X, y = f.create_X_y(data_path, id_path, target_variable)
print(X)
print(y)


#MACHINE LEARNING PART:
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from sktime.classification.compose import ColumnEnsembleClassifier
from sktime.classification.dictionary_based import BOSSEnsemble
from sktime.classification.interval_based import TimeSeriesForestClassifier
# from sktime.classification.shapelet_based import MrSEQLClassifier
from sktime.datasets import load_basic_motions
from sktime.transformations.panel.compose import ColumnConcatenator

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

#  multivariate input data
print(X_train.head())

# multi-class target variable
print(np.unique(y_train))

#time series concatenation
steps = [
    ("concatenate", ColumnConcatenator()),
    ("classify", TimeSeriesForestClassifier(n_estimators=100)),
]
clf = Pipeline(steps)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

#column ensambling

# clf = ColumnEnsembleClassifier(
#     estimators=[
#         ("TSF0", TimeSeriesForestClassifier(n_estimators=100), [0]),
#         ("BOSSEnsemble3", BOSSEnsemble(max_ensemble_size=5), [3]),
#     ]
# )
# clf.fit(X_train, y_train)
# clf.score(X_test, y_test)