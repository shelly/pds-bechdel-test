import requests, csv 

response = requests.get('http://bechdeltest.com/api/v1/getAllMovies')
parsed = response.json()

output_file = open('movie_data.csv', 'w')

for movie in parsed:
	if movie['title'] and movie['imdbid'] and movie['year'] and movie['rating']:
		title = movie['title'].replace(',', '')
		row = ','.join([title, movie['imdbid'], movie['year'], movie['rating']])
		output_file.write('{0}\n'.format(row))

output_file.close()
