from load_data import get_movies, get_people
import pandas as pd
import numpy as np
from functools import reduce 
from collections import defaultdict 

movie_data = get_movies()
movie_by_id = movie_data.set_index('TMDB_ID')
people_data = get_people()
people_data = people_data.set_index('TMDB_ID')

def person_bechdel_score():
	cast_to_scores = defaultdict(int)
	cast_to_num_movies = defaultdict(int)
	for movie_tmdb_id in movie_data.index:
		cast = movie_data.loc[movie_tmdb_id]['Cast']
		for mem in cast:
			person_id = int(mem['id'])
			cast_to_scores[person_id] += movie_data.loc[movie_tmdb_id]['Bechdel_Rating']
			cast_to_num_movies[person_id] += 1
	
	print("Created dictionaries.")
	best_score = 0
	best_id = 0
	for person in cast_to_num_movies:
		if cast_to_num_movies[person] > 2:
			if (cast_to_scores[person] / cast_to_num_movies[person]) > best_score:
				best_score = (cast_to_scores[person] / cast_to_num_movies[person])
				best_id = person

	print(best_score, people_data.loc[best_id, 'Name'])

person_bechdel_score()

