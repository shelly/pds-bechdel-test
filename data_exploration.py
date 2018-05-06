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

def passing_over_budget():
	# Buckets of $10 million 
	budgets = movies['Budget'][movies['Budget'] > 0]
	map_to_bud = budgets.apply(lambda year: int(year) // 10000000 * 10000000)
	ind = list(range(0, 210000000, 10000000))

	y_data = [0]*len(ind)
	for i in range(len(ind)):
		if (ind[i] == 200000000):
			y_data[i] = (map_to_bud[map_to_bud >= ind[i]]).shape[0]
		else:
			y_data[i] = (map_to_bud[map_to_bud == ind[i]]).shape[0]

	bar_width = 0.5
	plt.bar(range(len(ind)), y_data, width=bar_width)
	plt.xticks(range(len(ind)), tuple(map(lambda x: x // 10000000, ind)))
	plt.show()
