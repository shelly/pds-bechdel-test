from load_data import get_movies
from load_data import get_people
from sklearn.svm import SVC
import pandas as pd
import numpy as np

movie_data = get_movies()
movie_by_id = movie_data.set_index('TMDB_ID')
people_data = get_people()
people_data = people_data.set_index('TMDB_ID')

# Returns Revenue/Budget ratio
def get_rev_budget_ratio():
	rev = movie_data['Revenue']
	budget = movie_data['Budget']
	return np.divide(rev, budget)

# Returns 0/1 indicating whether or not there was a female director
def get_female_directing():
	crews = movie_data['Crew']
	fem_dir = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		for mem in crew:
			if (mem['department'] == 'Directing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					person_info = people_data.loc[person_id]
					person_gender = person_info['Gender']
					if (person_gender):
						fem_dir[ind] = 1
		ind += 1
	return fem_dir

# Returns fraction of females in directing crew
def get_female_directing_score():
	crews = movie_data['Crew']
	scores = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		directors = 0
		fem_dir = 0
		for mem in crew:
			if (mem['department'] == 'Directing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					directors += 1
					person_info = people_data.loc[person_id]
					person_gender = person_info['Gender']
					if (person_gender):
						fem_dir += 1
		if (directors == 0):
			scores[ind] = 0
		else:
			scores[ind] = fem_dir/directors
		ind += 1
	return scores

# Returns 0/1 indicating whether or not there was a female in the cast
def get_female_cast():
	casts = movie_data['Cast']
	fem_cast = np.zeros(casts.shape)
	ids = people_data.index
	ind = 0
	for cast in casts:
		for mem in cast:
			person_id = int(mem['id'])
			if (person_id in ids):
				person_info = people_data.loc[person_id]
				person_gender = person_info['Gender']
				if (person_gender):
					fem_cast[ind] = 1
		ind += 1
	return fem_cast

# Returns fraction of females in directing cast
def get_female_cast_score():
	casts = movie_data['Cast']
	scores = np.zeros(casts.shape)
	ids = people_data.index
	ind = 0
	for cast in casts:
		num_cast = 0
		num_fem = 0
		for mem in cast:
			person_id = int(mem['id'])
			if (person_id in ids):
				num_cast += 1
				person_info = people_data.loc[person_id]
				person_gender = person_info['Gender']
				if (person_gender):
					num_fem += 1
		if (num_cast == 0):
			scores[ind] = 0
		else:
			scores[ind] = num_fem/num_cast
		ind += 1
	return scores

# Returns 0/1 indicating whether or not there was a female writer
def get_female_writing():
	crews = movie_data['Crew']
	fem_writ = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		for mem in crew:
			if (mem['department'] == 'Writing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					person_info = people_data.loc[person_id]
					person_gender = person_info['Gender']
					if (person_gender):
						fem_writ[ind] = 1
		ind += 1
	return fem_writ

# Returns fraction of females in writing crew
def get_female_writing_score():
	crews = movie_data['Crew']
	scores = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		writers = 0
		fem_writ = 0
		for mem in crew:
			if (mem['department'] == 'Writing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					writers += 1
					person_info = people_data.loc[person_id]
					person_gender = person_info['Gender']
					if (person_gender):
						fem_writ += 1
		if (writers == 0):
			scores[ind] = 0
		else:
			scores[ind] = fem_writ/writers
		ind += 1
	return scores

# Returns fraction of recommendations that pass Bechdel Test
def recs_passing_score():
	pass

# Returns average Bechdel Test score of the recommendations
def recs_passing_avg_score():
	recs = movie_data['Recommendations']
	for rec in recs:
		for movie_id in rec:
			print(movie_by_id.loc[movie_id])
	return 0

# print(get_rev_budget_ratio())
# print(get_female_directing())
# print(get_female_directing_score())
# print(get_female_cast())
# print(get_female_cast_score())
# print(get_female_writing())
# print(get_female_writing_score())
# print(recs_passing())
# print(recs_passing_score())
print(recs_passing_avg_score())




