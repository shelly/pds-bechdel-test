import pandas as pd 

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing
def get_bechdel_data(): 
	return pd.read_csv('bechdel_test_data.csv', 
					dtype=object, 
					names=['Title', 'IMDB_ID', 'Year', 'Bechdel_Rating']
				  )

# 'Title', 
# 'IMDB_ID', 
# 'Year', 
# 'Bechdel_Rating', 
# 'TMDB_ID',
# 'Budget', 
# 'Overview',
# 'Popularity',
# 'Revenue',
# 'Genres',
# 'Cast',
# 'Crew',
# 'Recommendations',
def get_movies():
	df = pd.read_csv('movies.csv')

	# I know 
	df['Genres'] = df['Genres'].apply(eval)
	df['Cast'] = df['Cast'].apply(eval)
	df['Crew'] = df['Crew'].apply(eval)
	df['Recommendations'] = df['Recommendations'].apply(eval)

	return df 

# 'TMDB_ID',
# 'Name',
# 'Birthday',
# 'Deathday',
# 'Gender',
# 'Place of Birth',
# 'Popularity',
def get_people():
	return pd.read_csv('people.csv')

