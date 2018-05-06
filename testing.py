from load_data import get_movies
from sklearn.svm import SVC
import pandas as pd
import numpy as np

df = get_movies()

train = df.sample(frac=0.8, random_state = 200).dropna()
test = df.drop(train.index).dropna()

features = ['Revenue', 'Popularity', 'Budget', 'Year']

X_train = train[features].apply(pd.to_numeric,  errors='coerce').astype(np.int64)
y_train = pd.to_numeric(train['Bechdel_Rating'], errors='coerce').astype(np.int64)

X_test = test[features].apply(pd.to_numeric,  errors='coerce').astype(np.int64)
y_test = pd.to_numeric(test['Bechdel_Rating'], errors='coerce').astype(np.int64)


# X_train = X_train.reshape(X_train.shape[0], 1)
# X_test = X_test.reshape(X_test.shape[0], 1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])
