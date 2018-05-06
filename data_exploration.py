# Necessary to get matplotlib to import correctly.
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np 

from load_data import get_movies, get_people

movies = get_movies()
people = get_people().set_index('TMDB_ID')

def passing_over_year():
	map_to_decades = movies['Year'].apply(lambda year: year // 10 * 10)
	ind = map_to_decades.unique()
	y_data = [[0]*len(ind) for label in range(0, 4)]

	for i in range(len(ind)):
		for label in range(0, 4):
			bucket = ind[i]
			y_data[label][i] = movies[
			(map_to_decades == bucket) & (movies[
			'Bechdel_Rating'] == label)].shape[0]

	bar_width = 10
	p0 = plt.bar(ind, y_data[0], width=bar_width, color='red')
	p1 = plt.bar(ind, y_data[1], width=bar_width, bottom=y_data[0], color='orange')
	p2 = plt.bar(ind, y_data[2], width=bar_width, bottom=list(map(lambda x, y: x + y, y_data[0], y_data[1])), color='yellow')
	p3 = plt.bar(ind, y_data[3], width=bar_width, bottom=list(map(lambda x, y, z: x + y + z, y_data[0], y_data[1], y_data[2])), color='green')

	plt.legend((p0[0], p1[0], p2[0], p3[0]), ('0', '1', '2', '3'))

	plt.show()

passing_over_year()
