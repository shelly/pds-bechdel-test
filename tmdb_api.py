import requests, time, csv  
import pandas as pd 

api_key = ''
base_tmdb_url = 'https://api.themoviedb.org/3'

data = pd.read_csv('movie_data.csv', dtype=object, names=['Title', 'IMDB_ID', 'Year', 'Bechdel_Rating'])
output_file = open('movie_data_with_tmdb.csv', 'w')

def imdb_to_tmdb(imdb_id): 
	path = '/find/tt' + str(imdb_id)
	
	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key, 
															'external_source': 'imdb_id'})
	
	if r.status_code is requests.codes.ok:
		parsed = r.json()
		if 'movie_results' in parsed and len(parsed['movie_results']) > 0:
			movie = parsed['movie_results'][0]
			if 'id' in movie:
				return movie['id']

def cast_crew_female(tmdb_id): 
	first_billed_is_female = 0
	director_is_female = 0  
	path = '/movie/{0}/credits'.format(tmdb_id)

	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key})

	if r.status_code is requests.codes.ok:
		parsed = r.json()
		
		if 'cast' in parsed and len(parsed['cast']) > 0:
			first_billed = parsed['cast'][0]
			first_billed_is_female = int('gender' in first_billed and first_billed['gender'] is 1)
		
		if 'crew' in parsed:
			find_female_dirs = lambda obj: ('job' in obj 
											and 'gender' in obj 
											and obj['job'] == 'Director' 
											and obj['gender'] is 1
											) 
			female_directors = list(filter(find_female_dirs, parsed['crew']))
			director_is_female = int(len(female_directors) > 0)
	
	return (first_billed_is_female, director_is_female)

for index, movie in data.iterrows():
	tmdb_id = imdb_to_tmdb(movie['IMDB_ID'])
	time.sleep(0.3)
	if tmdb_id:
		(first_billed, director) = cast_crew_female(tmdb_id)
		time.sleep(0.3)

		row = ','.join([movie['Title'], 
					    movie['IMDB_ID'], 
					    movie['Year'], 
					    movie['Bechdel_Rating'], 
					    str(first_billed), 
					    str(director)]
					   )

		output_file.write('{0}\n'.format(row))

output_file.close()
