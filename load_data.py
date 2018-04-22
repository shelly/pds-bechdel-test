import pandas as pd 

# Necessary to get matplotlib to import correctly.
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

# Title: Movie title
# IMDB_ID: IMDB ID
# Year: Year the movie was released
# Bechdel_Rating: 0 = no two women, 1 = no talking, 2 = no talking about men, 3 = passing

data = pd.read_csv('movie_data.csv', names=['Title', 'IMDB_ID', 'Year', 'Bechdel_Rating'])
print(data.shape)
print(data.head())
print(data.tail())