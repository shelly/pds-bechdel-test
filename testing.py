from load_data import get_movies
import feature_engineering as fe 

from sklearn.svm import SVC
from sklearn import tree
from sklearn import mixture
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

df = get_movies()

df['Rev_Budget'] = fe.get_rev_budget_ratio()
df['Female_Dir'] = fe.get_female_directing()
df['Female_Dir_Score'] = fe.get_female_directing_score()
df['Female_Cast'] = fe.get_female_cast()
df['Female_Cast_Score'] = fe.get_female_cast_score()
df['Female_Writing'] = fe.get_female_writing()
df['Female_Writing_Score'] = fe.get_female_writing_score()
df['Rec_Bechdel']= fe.recs_passing_avg_score()
df['Dir_Age'] = fe.average_age_of_director()
df['Cast_Age'] = fe.average_age_of_cast()
df['Dir_Pop'] = fe.ave_pop_directors()
df['Cast_Pop'] = fe.ave_pop_cast()
df['First_Billed_Female'] = fe.first_billed_female()

print("How many NaNs")

print('Rev_Budget: ', sum(np.isnan(df['Rev_Budget'])))
print('Female_Dir: ', sum(np.isnan(df['Female_Dir'] == np.nan)))
print('Female_Dir_Score: ', sum(np.isnan(df['Female_Dir_Score'])))
print('Female_Cast: ', sum(np.isnan(df['Female_Cast'])))
print('Female_Cast_Score: ', sum(np.isnan(df['Female_Cast_Score'])))
print('Female_Writing: ', sum(np.isnan(df['Female_Writing'])))
print('Female_Writing_Score: ', sum(np.isnan(df['Female_Writing_Score'])))
print('Rec_Bechdel: ', sum(np.isnan(df['Rec_Bechdel'])))
print('Cast_Age: ', sum(np.isnan(df['Cast_Age'])))
print('Dir_Age: ', sum(np.isnan(df['Dir_Age'])))
print('Cast_Pop: ', sum(np.isnan(df['Cast_Pop'])))
print('Dir_Pop: ', sum(np.isnan(df['Dir_Pop'])))
print('First_Billed_Female: ', sum(np.isnan(df['First_Billed_Female'])))

print("START MODELLING")

features = ['Female_Dir_Score',
			'Female_Writing',
			'First_Billed_Female'
			]

df = df.dropna()

train = df.sample(frac=0.9, random_state = 200)
test = df.drop(train.index)

X_train = train[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_train = pd.to_numeric(train['Bechdel_Rating'], errors='coerce').astype(float)
y_train_bin = pd.to_numeric((train['Bechdel_Rating'] == 3), errors='coerce').astype(float)

X_test = test[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_test = pd.to_numeric(test['Bechdel_Rating'], errors='coerce').astype(float)
y_test_bin = pd.to_numeric((test['Bechdel_Rating'] == 3), errors='coerce').astype(float)

#### SVM ######
print("SVM")

print("SVM rbf kernel")
clf = SVC(kernel='rbf')
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")

print("SVM linear kernel")
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")

print("SVM linear kernel; binary")
clf = SVC(kernel='linear')
clf.fit(X_train, y_train_bin)
print("Training accuracy: ", clf.score(X_train, y_train_bin))
print("Testing accuracy: ", clf.score(X_test, y_test_bin))

print("Zero: ", sum(y_test_bin == np.zeros(y_test_bin.shape[0]))/y_test_bin.shape[0])
print("One: ", sum(y_test_bin == np.ones(y_test_bin.shape[0]))/y_test_bin.shape[0])
print("Two: ", sum(y_test_bin == (2*np.ones(y_test_bin.shape[0])))/y_test_bin.shape[0])
print("Three: ", sum(y_test_bin == (3*np.ones(y_test_bin.shape[0])))/y_test_bin.shape[0])

print("#################")

##### Decision Tree #######
print("Decision Tree")

print("DT Max Depth 4")
clf = tree.DecisionTreeClassifier(max_depth=4)
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")

print("DT Max Depth 3")
clf = tree.DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")

print("DT Max Depth 4; binary")
clf = tree.DecisionTreeClassifier(max_depth=4)
clf.fit(X_train, y_train_bin)
print("Training accuracy: ", clf.score(X_train, y_train_bin))
print("Testing accuracy: ", clf.score(X_test, y_test_bin))

print("Zero: ", sum(y_test_bin == np.zeros(y_test_bin.shape[0]))/y_test_bin.shape[0])
print("One: ", sum(y_test_bin == np.ones(y_test_bin.shape[0]))/y_test_bin.shape[0])
print("Two: ", sum(y_test_bin == (2*np.ones(y_test_bin.shape[0])))/y_test_bin.shape[0])
print("Three: ", sum(y_test_bin == (3*np.ones(y_test_bin.shape[0])))/y_test_bin.shape[0])

print("#################")

##### GMM #######
print("GMM")

clf = mixture.GMM(n_components=4)
clf.fit(X_train)
print("GMM score")
print(clf.score_samples(X_test))

print("#################")

##### Naive Bayes #######
print("Gaussian Naive Bayes")

clf = GaussianNB()
clf.fit(X_train, y_train)

print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")

print("Multinomial Bayes")

clf = MultinomialNB()
clf.fit(X_train, y_train)

print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])

print("#################")
