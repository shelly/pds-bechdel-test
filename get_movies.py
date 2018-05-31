import requests, time  
import pandas as pd 

api_key = 'API_KEY' 
base_tmdb_url = 'http://api.themoviedb.org/3'

bechdel_data = pd.read_csv('bechdel_test_data.csv', dtype=object, names=['Title', 
	'IMDB_ID', 'Year', 'Bechdel_Rating'])
df = pd.DataFrame(columns=['Title', 
						   'IMDB_ID', 
						   'Year', 
						   'Bechdel_Rating', 
						   'TMDB_ID',
						   'Budget', 
						   'Overview',
						   'Popularity',
						   'Revenue',
						   'Genres',
						   'Cast',
						   'Crew',
						   'Recommendations',
						  ])

#Movie /find/ -> TMDB ID 
def imdb_to_tmdb(imdb_id): 
	path = '/find/tt' + str(imdb_id)
	
	r = requests.get(base_tmdb_url + path, 
		params = {'api_key': api_key,'external_source': 'imdb_id'})
	
	if r.status_code is requests.codes.ok:
		parsed = r.json()
		if 'movie_results' in parsed and len(parsed['movie_results']) > 0:
			movie = parsed['movie_results'][0]
			if 'id' in movie:
				return movie['id']

# GetDetails
	# Budget
	# Overview 
	# Popularity 
	# Revenue 
	# Genres: List [{id: , name: }]
def get_details(tmdb_id): 
	path = '/movie/{0}'.format(tmdb_id)

	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key})

	if r.status_code is requests.codes.ok:
		parsed = r.json()
		return (parsed['title'],
			    parsed['budget'], 
			    parsed['overview'], 
			    parsed['popularity'],
			    parsed['revenue'],
			    parsed['genres']) 

# GetCredits
	# Cast: List[{id: , order: }]
	# Crew: List[{id: , job: , department: }]
def get_credits(tmdb_id): 
	cast = list()
	crew = list() 
	path = '/movie/{0}/credits'.format(tmdb_id)

	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key})

	if r.status_code is requests.codes.ok:
		parsed = r.json()
		
		if 'cast' in parsed:
			cast_obj = parsed['cast']
			cast = list(map(lambda person: {'id': person['id'], 
											'order': person['order'],
											'character': person['character'],
											}, cast_obj))
		
		if 'crew' in parsed:
			crew_obj = parsed['crew']
			crew = list(map(lambda person: {'id': person['id'], 
											'department': person['department'], 
											'job': person['job'],
											}, crew_obj))
	
	return (cast, crew)

# GetRecommendations
	# recommendations: List [id]
def get_recommendations(tmdb_id): 
	recommendations = list()
	path = '/movie/{0}/recommendations'.format(tmdb_id)

	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key})

	if r.status_code is requests.codes.ok:
		parsed = r.json() 
		if 'results' in parsed:
			recommendations = [rec['id'] for rec in parsed['results']][:5]

	return recommendations 


for index, movie in bechdel_data.iterrows():
	tmdb_id = imdb_to_tmdb(movie['IMDB_ID'])
	time.sleep(0.3)
	if tmdb_id:
		(title, budget, overview, popularity, revenue, genres) = get_details(tmdb_id)
		time.sleep(0.3)
		(cast, crew) = get_credits(tmdb_id)
		time.sleep(0.3)
		recommendations = get_recommendations(tmdb_id)
		time.sleep(0.3)

		df.loc[index] = [title, 
	    movie['IMDB_ID'], 
	    movie['Year'], 
	    movie['Bechdel_Rating'],
	    tmdb_id,
	    budget,
	    overview,
	    popularity,
	    revenue,
	    genres, 
	    cast,
	    crew, 
	    recommendations]

df.to_csv('movies.csv')
