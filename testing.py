from load_data import get_movies
import feature_engineering as fe 
from sklearn.svm import SVC
import pandas as pd
import numpy as np

df = get_movies()

# df['Rev_Budget'] = fe.get_rev_budget_ratio()
df['Female_Dir_Score'] = fe.get_female_directing_score()
df['Female_Cast_Score'] = fe.get_female_cast_score()
df['Dir_Age'] = fe.average_age_of_director()
df['Female_Writing'] = fe.get_female_writing()
df['Dir_Pop'] = fe.ave_pop_directors()
df['Cast_Pop'] = fe.ave_pop_cast()

features = ['Female_Dir_Score',
			'Female_Cast_Score',
			'Dir_Age',
			'Female_Writing',
			'Dir_Pop',
			'Cast_Pop',
			]

df = df.dropna()
train = df.sample(frac=0.8, random_state = 200)
test = df.drop(train.index)

X_train = train[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_train = pd.to_numeric(train['Bechdel_Rating'], errors='coerce').astype(float)

X_test = test[features].apply(pd.to_numeric,  errors='coerce').astype(float)
y_test = pd.to_numeric(test['Bechdel_Rating'], errors='coerce').astype(float)


# X_train = X_train.reshape(X_train.shape[0], 1)
# X_test = X_test.reshape(X_test.shape[0], 1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

clf = SVC(kernel='rbf')
clf.fit(X_train, y_train)
print("Training accuracy: ", clf.score(X_train, y_train))
print("Testing accuracy: ", clf.score(X_test, y_test))

print("Zero: ", sum(y_test == np.zeros(y_test.shape[0]))/y_test.shape[0])
print("One: ", sum(y_test == np.ones(y_test.shape[0]))/y_test.shape[0])
print("Two: ", sum(y_test == (2*np.ones(y_test.shape[0])))/y_test.shape[0])
print("Three: ", sum(y_test == (3*np.ones(y_test.shape[0])))/y_test.shape[0])
