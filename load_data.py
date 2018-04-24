import pandas as pd 

# Necessary to get matplotlib to import correctly.
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing

data = pd.read_csv('movie_data.csv', 
					dtype=object, 
					names=['Title', 'IMDB_ID', 'Year', 'Bechdel_Rating']
				  )
print(data.shape)
print(data.head())
print(data.tail())

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing
# First_Billed: 1 = female, 0 = non-female
# Director: 1 = at least one female, 0 = no females 

data_with_tmdb = pd.read_csv('movie_data_with_tmdb.csv', 
					dtype=object, 
					names=['Title', 
						   'IMDB_ID', 
						   'Year', 
						   'Bechdel_Rating', 
						   'First_Billed', 
						   'Director'
						  ]
				  )
print(data_with_tmdb.shape)
print(data_with_tmdb.head())
print(data_with_tmdb.tail())

