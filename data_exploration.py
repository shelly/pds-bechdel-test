# Necessary to get matplotlib to import correctly.
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np 

from load_data import get_movies, get_people

movies = get_movies()
# people = get_people().set_index('TMDB_ID')

def passing_over_year():
	map_to_decades = movies['Year'].apply(lambda year: year // 10 * 10)
	ind = list(map_to_decades.unique())
	y_data = [[0]*len(ind) for label in range(0, 4)]

	for i in range(len(ind)):
		for label in range(0, 4):
			bucket = ind[i]
			y_data[label][i] = 100*(movies[
			(map_to_decades == bucket) & (movies[
			'Bechdel_Rating'] == label)].shape[0]) / (movies[map_to_decades == bucket].shape[0])

	bar_width = 10
	line_width = 1
	edge_color = 'black'
	ind = ind[3:]
	for li in range(len(y_data)):
		y_data[li] = y_data[li][3:]

	p0 = plt.bar(ind, y_data[3], width=bar_width, edgecolor=edge_color, linewidth=line_width, color='green')
	p1 = plt.bar(ind, y_data[2], width=bar_width, edgecolor=edge_color, linewidth=line_width, bottom=y_data[3], color='yellow')
	p2 = plt.bar(ind, y_data[1], width=bar_width, edgecolor=edge_color, linewidth=line_width, bottom=list(map(lambda x, y: x + y, y_data[3], y_data[2])), color='orange')
	p3 = plt.bar(ind, y_data[0], width=bar_width, edgecolor=edge_color, linewidth=line_width, bottom=list(map(lambda x, y, z: x + y + z, y_data[3], y_data[2], y_data[1])), color='red')

	plt.legend((p0[0], p1[0], p2[0], p3[0]), ('0', '1', '2', '3'))
	plt.title("Bechdel Test Scores by Year")
	plt.xlabel("Decade")
	plt.ylabel("Percent of Movies")

	plt.show()

def passing_over_genre():
	map_to_genres = movies['Genres'].apply(lambda genres: [genre['name'] for genre in genres])
	ind = ['Western', 'TV Movie', 'Family', 'Comedy', 
			  'Action', 'Crime', 'Horror', 'Animation', 
			  'Thriller', 'Adventure', 'Fantasy', 'War', 
			  'Science Fiction', 'Drama', 'Documentary', 
			  'History', 'Mystery', 'Romance', 'Music'] 
	y_data = [[0]*len(ind) for label in range(0, 4)]

	for i in range(len(ind)):
		for label in range(0, 4):
			bucket = ind[i]
			y_data[label][i] = 100*(movies[
			(map_to_genres.apply(lambda genres: bucket in genres)) & (movies[
			'Bechdel_Rating'] == label)].shape[0]) / (movies[map_to_genres.apply(lambda genres: bucket in genres)].shape[0])

	line_width = 1
	edge_color = 'black'

	p0 = plt.bar(ind, y_data[3], edgecolor=edge_color, linewidth=line_width, color='green')
	p1 = plt.bar(ind, y_data[2], edgecolor=edge_color, linewidth=line_width, bottom=y_data[3], color='yellow')
	p2 = plt.bar(ind, y_data[1], edgecolor=edge_color, linewidth=line_width, bottom=list(map(lambda x, y: x + y, y_data[3], y_data[2])), color='orange')
	p3 = plt.bar(ind, y_data[0], edgecolor=edge_color, linewidth=line_width, bottom=list(map(lambda x, y, z: x + y + z, y_data[3], y_data[2], y_data[1])), color='red')

	plt.legend((p0[0], p1[0], p2[0], p3[0]), ('0', '1', '2', '3'))
	plt.title("Bechdel Test Scores by Genre")
	plt.xticks(rotation=90)
	plt.xlabel("Genre")
	plt.ylabel("Percent of Movies")

	plt.show()

passing_over_genre()
