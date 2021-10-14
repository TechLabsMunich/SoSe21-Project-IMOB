import functions as f

#GETTING THE X AND Y PART:

data_path = '../01-Data/sample_data'
id_path = "../01-Data/new data's IDs.xlsx"
target_variable = 'Geschlecht m=0,w=1'

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

from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

#  multivariate input data
print(X_train.head())

# multi-class target variable
print(np.unique(y_train))

#time series concatenation
steps = [
    ("concatenate", ColumnConcatenator()),
    ("classify", TimeSeriesForestClassifier(n_estimators=100, n_jobs=-1)),
]
model = Pipeline(steps)
parameters = {'n_estimators':(10,50,100,200), 'criterion':('gini', 'entropy'), 'max_depth':(5, 10, 50)}
clf = GridSearchCV(model, parameters, scoring='f1')
clf.fit(X_train, y_train)
best_params = clf.get_params()
print(best_params)
score = clf.score(X_test, y_test)
y_pred = clf.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred, average='micro').ravel()
# precision = tp/(tp+fp)
precision = precision_score(y_test, y_pred, average='micro')
recall = recall_score(y_test, y_pred, average='micro')
#ballanced f-score
# f_1 = 2*(precision*recall)/(precision+recall)
f_1 = f1_score(y_test, y_pred, average='micro')

print(f'f1 score: {f_1}')






