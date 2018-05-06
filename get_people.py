import requests, time  
import pandas as pd
import json  

api_key = 'a4a3dc6220c1d494515cbef159badb43'
base_tmdb_url = 'http://api.themoviedb.org/3'

movie_data = pd.read_csv('movies.csv')
df = pd.DataFrame(columns=['TMDB_ID',
						    'Name',
						   'Birthday',
						   'Deathday',
						   'Gender',
						   'Place of Birth',
						   'Popularity',
						  ])

def get_details(tmdb_id): 
	path = '/person/{0}'.format(tmdb_id)

	r = requests.get(base_tmdb_url + path, params = {'api_key': api_key})

	if r.status_code is requests.codes.ok:
		parsed = r.json()
		return (parsed['name'] if 'name' in parsed else '',
			    parsed['birthday'] if 'birthday' in parsed else '', 
			    parsed['deathday'] if 'deathday' in parsed else '', 
			    parsed['gender'] if 'gender' in parsed else 0,
			    parsed['place_of_birth'] if 'place_of_birth' in parsed else '',
			    parsed['popularity'] if 'popularity' in parsed else '')
	else:
		return ('', '', '', '', '', '') 


for index, movie in movie_data.iterrows():
	# I know, I'm judging myself bc of this line of code too 
	cast = eval(movie['Cast'])[:10]
	crew = list(filter(lambda person: person['department'] == 'Writing' or person['department'] == 'Directing', eval(movie['Crew'])))

	people_in_movie = [person['id'] for person in cast + crew]
	for person in people_in_movie: 
		if person not in df.index:
			(name, birth, death, gender, place_of_birth, popularity) = get_details(person)
			time.sleep(0.3)
			df.loc[person] = [person, name, birth, death, gender, place_of_birth, popularity]

df.to_csv('people.csv')
