from load_data import get_all_data
from sklearn.svm import SVC
import pandas as pd
import numpy as np

df = get_all_data()
print(df.shape)

train = df.sample(frac=0.9, random_state = 200)
test = df.drop(train.index)

X_train = pd.to_numeric(train['Revenue'], errors='coerce').fillna(0).astype(np.int64)
y_train = pd.to_numeric(train['Bechdel_Rating'], errors='coerce').fillna(0).astype(np.int64)

X_test = pd.to_numeric(test['Revenue'], errors='coerce').fillna(0).astype(np.int64)
y_test = pd.to_numeric(test['Bechdel_Rating'], errors='coerce').fillna(0).astype(np.int64)


X_train = X_train.reshape(X_train.shape[0], 1)
X_test = X_test.reshape(X_test.shape[0], 1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

print(sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print(sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print(sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print(sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])