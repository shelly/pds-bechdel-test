import pandas as pd 

# Necessary to get matplotlib to import correctly.
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing

data = pd.read_csv('bechdel_test_data.csv', 
					dtype=object, 
					names=['Title', 'IMDB_ID', 'Year', 'Bechdel_Rating']
				  )
# print(data.shape)
# print(data.head())
# print(data.tail())

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing

def get_all_data():
	return pd.read_csv('movies.csv', 
					dtype=object, 
					names=['Title', 
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
						  ]
				  )

