from load_data import get_movies
from load_data import get_people
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from functools import reduce 
from collections import defaultdict 

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
					if (person_gender == 1):
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
					if (person_gender == 1):
						fem_dir += 1
		if (directors != 0):
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
				if (person_gender == 1):
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
				if (person_gender == 1):
					num_fem += 1
		if (num_cast != 0):
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
					if (person_gender == 1):
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
					if (person_gender == 1):
						fem_writ += 1
		if (writers != 0):
			scores[ind] = fem_writ/writers
		ind += 1
	return scores

# Returns average Bechdel Test score of the recommendations
def recs_passing_avg_score():
	recs = movie_data['Recommendations']
	ids = movie_by_id.index
	scores = np.zeros(recs.shape)
	ind = 0
	for rec in recs:
		num_recs = len(rec)
		total = 0
		for movie_id in rec:
			if (movie_id in ids):
				rating = (movie_by_id.loc[movie_id]['Bechdel_Rating'])
				if (isinstance(rating, np.int64)):
					total += rating
		if (num_recs > 0):
			scores[ind] = total / num_recs
		ind += 1
	return scores

# Returns the average age of the directors
def average_age_of_director():
	year = movie_data['Year']
	crews = movie_data['Crew']
	ages = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		total_age = 0
		total_dirs = 0
		for mem in crew:
			if (mem['department'] == 'Directing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					person_info = people_data.loc[person_id]
					birthday = person_info['Birthday']
					if (type(birthday) == str):
						birthyear = int(birthday[:4])
						age = year[ind] - birthyear
						total_dirs += 1
						total_age += age
		if (total_dirs != 0):
			ages[ind] = total_age / total_dirs
		ind += 1
	return ages

# Returns the average age of the cast
def average_age_of_cast():
	year = movie_data['Year']
	casts = movie_data['Cast']
	ages = np.zeros(casts.shape)
	ids = people_data.index
	ind = 0
	for cast in casts:
		total_age = 0
		total_cast = 0
		for mem in cast:
			person_id = int(mem['id'])
			if (person_id in ids):
				person_info = people_data.loc[person_id]
				birthday = person_info['Birthday']
				if (type(birthday) == str):
					birthyear = int(birthday[:4])
					age = year[ind] - birthyear
					total_cast += 1
					total_age += age
		if (total_cast != 0):
			ages[ind] = total_age / total_cast
		ind += 1
	return ages

# Returns one hot enconding of genres
def genres_one_hot(): 
	df = pd.DataFrame() 
	genres = ['Western', 'TV Movie', 'Family', 'Comedy', 
			  'Action', 'Crime', 'Horror', 'Animation', 
			  'Thriller', 'Adventure', 'Fantasy', 'War', 
			  'Science Fiction', 'Drama', 'Documentary', 
			  'History', 'Mystery', 'Romance', 'Music'] 
	genre_names = movie_data['Genres'].apply( lambda li: [genre['name'] for genre in li]) 
	for genre in genres: 
		df[genre] = genre_names.apply(lambda li: int(genre in li)) 
	return df

# Returns average popularity of directors
def ave_pop_directors():
	crews = movie_data['Crew']
	pops = np.zeros(crews.shape)
	ids = people_data.index
	ind = 0
	for crew in crews:
		total_pop = 0
		total_dirs = 0
		for mem in crew:
			if (mem['department'] == 'Directing'):
				person_id = int(mem['id'])
				if (person_id in ids):
					person_info = people_data.loc[person_id]
					pop = person_info['Popularity']
					total_dirs += 1
					total_pop += pop
		if (total_dirs != 0):
			pops[ind] = total_pop / total_dirs
		ind += 1
	return pops

# Returns average popularity of cast
def ave_pop_cast():
	casts = movie_data['Cast']
	pops = np.zeros(casts.shape)
	ids = people_data.index
	ind = 0
	for cast in casts:
		total_pop = 0
		total_casts = 0
		for mem in cast:
			person_id = int(mem['id'])
			if (person_id in ids):
				person_info = people_data.loc[person_id]
				pop = person_info['Popularity']
				total_casts += 1
				total_pop += pop
		if (total_casts != 0):
			pops[ind] = total_pop / total_casts
		ind += 1
	return pops

def first_billed_female():
	casts = movie_data['Cast']
	first_billeds = np.zeros(casts.shape)
	ind = 0
	for cast in casts:
		min_order_fn = lambda p1, p2: p1 if ('order' in p1 
			and 'order' in p2 and p1['order'] < p2['order']) else p2
		first_billed = reduce(min_order_fn, cast, {})
		if len(first_billed) > 0 and int(first_billed['id']) in people_data.index:
			gender = people_data.loc[int(first_billed['id'])]['Gender']
			if gender == 0:
				first_billeds[ind] = np.nan # Not set
			elif gender == 1:
				first_billeds[ind] = 1 # Not set
			elif gender == 2:
				first_billeds[ind] = 0 # Not set
		else:
			first_billeds[ind] = np.nan # Not set
		ind += 1
	return first_billeds 

def generate_cast_to_movies_map():

	cast_to_movies = defaultdict(list)
	for movie_tmdb_id in movie_data.index:
		cast = movie_data.loc[movie_tmdb_id]['Cast']
		for mem in cast:
			person_id = int(mem['id'])
			cast_to_movies[person_id].append(movie_tmdb_id)

	return cast_to_movies

def ave_bechdel_cast_score():
	scores = np.zeros(movie_data.shape[0])
	cast_to_movies = generate_cast_to_movies_map()
	ind = 0
	for movie_tmdb_id in movie_data.index:
		cast = movie_data.loc[movie_tmdb_id]['Cast']
		cast_score = 0
		for mem in cast:
			person_id = int(mem['id'])
			person_movies = cast_to_movies[person_id]
			cast_score += sum(map(lambda movie: movie_data.loc[movie]['Bechdel_Rating'], 
				person_movies))/len(person_movies)
		scores[ind] = (cast_score / len(cast)) if (len(cast) > 0) else np.nan
		ind += 1
	return scores  

def generate_directors_to_movies_map():

	dirs_to_movies = defaultdict(list)
	for movie_tmdb_id in movie_data.index:
		crew = movie_data.loc[movie_tmdb_id]['Crew']
		for mem in crew:
			if (mem['department'] == 'Directing'):
				person_id = int(mem['id'])
				dirs_to_movies[person_id].append(movie_tmdb_id)

	return dirs_to_movies

def ave_bechdel_dir_score():
	scores = np.zeros(movie_data.shape[0])
	dirs_to_movies = generate_directors_to_movies_map()
	ind = 0
	for movie_tmdb_id in movie_data.index:
		crew = movie_data.loc[movie_tmdb_id]['Crew']
		dir_score = 0
		num_dirs = 0
		for mem in crew:
			if (mem['department'] == 'Directing'):
				num_dirs += 1
				person_id = int(mem['id'])
				person_movies = dirs_to_movies[person_id]
				dir_score += sum(map(lambda movie: movie_data.loc[movie]['Bechdel_Rating'], 
					person_movies))/len(person_movies)
		scores[ind] = (dir_score / num_dirs) if (num_dirs > 0) else np.nan
		ind += 1
	return scores  
	