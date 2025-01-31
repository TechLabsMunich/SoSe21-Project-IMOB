import functions as f

#GETTING THE X AND Y PART:

data_path = '../01-Data/sample_data'
id_path = "../01-Data/new data's IDs.xlsx"
target_variable = 'Alter>median'

X, y = f.create_X_y(data_path, id_path, target_variable)


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

from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

from sktime.forecasting.model_selection import ForecastingGridSearchCV

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

#  multivariate input data
# print(X_train.head())

# multi-class target variable
# print(np.unique(y_train))


#time series concatenation
steps = [
    ("concatenate", ColumnConcatenator()),
    ("classify", TimeSeriesForestClassifier(n_estimators=50, n_jobs=-1)),
]
clf = Pipeline(steps)

# clf = GridSearchCV(model, parameters, scoring='f1', n_jobs=-1)
clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)
y_pred = clf.predict(X_test)
#tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
# precision = tp/(tp+fp)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
#ballanced f-score
# f_1 = 2*(precision*recall)/(precision+recall)
f_1 = f1_score(y_test, y_pred)

print(f'f1 score: {f_1}')
print(f'precision: {precision}')
print(f'recall: {recall}')
print(f'score: {score}')







