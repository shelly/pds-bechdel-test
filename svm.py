from load_data import get_movies
import feature_engineering as fe 
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
import pandas as pd
import numpy as np

df = get_movies()

df['Female_Director'] = fe.get_female_directing()
df['Female_Writer'] = fe.get_female_writing()
df['First_Billed_Female'] = fe.first_billed_female()

features = ['Year', 'Popularity', 'Female_Director', 'Female_Writer', 'First_Billed_Female']

df = df.dropna()
df['Bechdel_Rating'] = (df['Bechdel_Rating'] == 3).astype(int)
train = df.sample(frac=0.8, random_state = 200)
test = df.drop(train.index)

X_train = train[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_train = pd.to_numeric(train['Bechdel_Rating'], errors='coerce').astype(float)

X_test = test[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_test = pd.to_numeric(test['Bechdel_Rating'], errors='coerce').astype(float)


# X_train = X_train.reshape(X_train.shape[0], 1)
# X_test = X_test.reshape(X_test.shape[0], 1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

clf = BernoulliNB()
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Percent of test set that pass: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
