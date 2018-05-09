from load_data import get_movies
import feature_engineering as fe 
from sklearn.svm import SVC
import pandas as pd
import numpy as np

df = get_movies()

def has_first_billed_female_cond_prob(): 
	female = fe.first_billed_female()
	bechdel_rating = df['Bechdel_Rating']

	female_0 = np.equal(female, np.zeros(female.shape[0]))
	female_1 = np.equal(female, np.ones(female.shape[0]))

	bechdel_pass = bechdel_rating == 3
	print("P(pass | have first billed female):", 
		sum(np.multiply(female_1, bechdel_pass)) / sum(female_1))
	print("P(pass | don't have first billed female)", 
		sum(np.multiply(female_0, bechdel_pass)) / sum(female_0))

def has_female_dir_cond_prob(): 
	female_dirs = fe.get_female_directing()
	bechdel_rating = df['Bechdel_Rating']

	female_dirs_0 = np.equal(female_dirs, np.zeros(female_dirs.shape[0]))
	female_dirs_1 = np.equal(female_dirs, np.ones(female_dirs.shape[0]))

	bechdel_pass = bechdel_rating == 3
	print("P(pass | have female dir):", 
		sum(np.multiply(female_dirs_1, bechdel_pass)) / sum(female_dirs_1))
	print("P(pass | don't have female dir)", 
		sum(np.multiply(female_dirs_0, bechdel_pass)) / sum(female_dirs_0))

def female_dir_score_cond_prob(): 
	female_dirs = fe.get_female_directing_score()
	bechdel_rating = df['Bechdel_Rating']

	female_dirs_0 = female_dirs < 0.5
	female_dirs_1 = female_dirs >= 0.5

	bechdel_pass = bechdel_rating == 3
	print("P(pass | < 50 percent female dirs):", 
		sum(np.multiply(female_dirs_1, bechdel_pass)) / sum(female_dirs_1))
	print("P(pass | >= 50 percent female dirs)", 
		sum(np.multiply(female_dirs_0, bechdel_pass)) / sum(female_dirs_0))

def female_cast_cond_prob():
	female_cast = fe.get_female_cast()
	bechdel_rating = df['Bechdel_Rating']

	female_cast_0 = np.equal(female_cast, np.zeros(female_cast.shape[0]))
	female_cast_1 = np.equal(female_cast, np.ones(female_cast.shape[0]))

	bechdel_pass = bechdel_rating == 3
	print("P(pass | have female cast in first 3):", 
		sum(np.multiply(female_cast_1, bechdel_pass)) / sum(female_cast_1))
	print("P(pass | don't have female cast in first 3)", 
		sum(np.multiply(female_cast_0, bechdel_pass)) / sum(female_cast_0))
	print("Number of movies with no females: ", 
		sum(female_cast_0), " / ", sum(female_cast_0) + sum(female_cast_1))

def female_cast_score_cond_prob(): 
	female_cast = fe.get_female_cast_score()
	bechdel_rating = df['Bechdel_Rating']

	female_cast_0 = female_cast < 0.5
	female_cast_1 = female_cast >= 0.5

	bechdel_pass = bechdel_rating == 3
	print("P(pass | < 50 percent female cast):", 
		sum(np.multiply(female_cast_1, bechdel_pass)) / sum(female_cast_1))
	print("P(pass | >= 50 percent female cast)", 
		sum(np.multiply(female_cast_0, bechdel_pass)) / sum(female_cast_0))

def female_writing_cond_prob():
	female_writing = fe.get_female_writing()
	bechdel_rating = df['Bechdel_Rating']

	female_writing_0 = np.equal(female_writing, np.zeros(female_writing.shape[0]))
	female_writing_1 = np.equal(female_writing, np.ones(female_writing.shape[0]))

	bechdel_pass = bechdel_rating == 3
	print("P(pass | have female writer):", 
		sum(np.multiply(female_writing_1, bechdel_pass)) / sum(female_writing_1))
	print("P(pass | don't have female writer)", 
		sum(np.multiply(female_writing_0, bechdel_pass)) / sum(female_writing_0))
	print("Number of movies with no female writer: ", 
		sum(female_writing_0), " / ", sum(female_writing_0) + sum(female_writing_1))

def female_cast_score_cond_prob(): 
	female_writing = fe.get_female_writing_score()
	bechdel_rating = df['Bechdel_Rating']

	female_writing_0 = female_writing < 0.5
	female_writing_1 = female_writing >= 0.5

	bechdel_pass = bechdel_rating == 3
	print("P(pass | >= 50 percent female writing):", 
		sum(np.multiply(female_writing_1, bechdel_pass)) / sum(female_writing_1))
	print("P(pass | < 50 percent female writing)", 
		sum(np.multiply(female_writing_0, bechdel_pass)) / sum(female_writing_0))
	print("Number of movies with no female writer: ", 
		sum(female_writing_0), " / ", sum(female_writing_0) + sum(female_writing_1))


def avg_rec_cond_prob(): 
	rec_avg = fe.recs_passing_avg_score()
	bechdel_rating = df['Bechdel_Rating']

	rec_under_thresh = rec_avg < 1
	rec_over_thresh = rec_avg >= 2

	bechdel_pass = bechdel_rating == 3
	bechdel_fail = bechdel_rating < 3
	print("P(fail | average score of recs is under threshold):", 
		sum(np.multiply(rec_under_thresh, bechdel_fail)) / sum(rec_under_thresh))
	print("P(pass | average score of recs is over threshold)", 
		sum(np.multiply(rec_over_thresh, bechdel_pass)) / sum(rec_over_thresh))

avg_rec_cond_prob()

def avg_bechdel_cast_score_cond_prob(): 
	cast_avg = fe.ave_bechdel_cast_score()
	bechdel_rating = df['Bechdel_Rating']

	cast_under_thresh = cast_avg < 1
	cast_over_thresh = cast_avg >= 2

	bechdel_pass = bechdel_rating == 3
	bechdel_fail = bechdel_rating < 3
	print("P(fail | average score of cast is under threshold):", 
		sum(np.multiply(cast_under_thresh, bechdel_fail)) / sum(cast_under_thresh))
	print("P(pass | average score of cast is over threshold)", 
		sum(np.multiply(cast_over_thresh, bechdel_pass)) / sum(cast_over_thresh))

def avg_bechdel_dir_score_cond_prob(): 
	dir_avg = fe.ave_bechdel_dir_score()
	bechdel_rating = df['Bechdel_Rating']

	dir_under_thresh = dir_avg < 1
	dir_over_thresh = dir_avg >= 2

	bechdel_pass = bechdel_rating == 3
	bechdel_fail = bechdel_rating < 3
	print("P(fail | average score of directors is under threshold):", 
		sum(np.multiply(dir_under_thresh, bechdel_fail)) / sum(dir_under_thresh))
	print("P(pass | average score of directors is over threshold)", 
		sum(np.multiply(dir_over_thresh, bechdel_pass)) / sum(dir_over_thresh))

def avg_dir_age_cond_prob(): 
	cast_avg = fe.average_age_of_cast()
	bechdel_rating = df['Bechdel_Rating']

	cast_under_thresh = cast_avg < 40
	cast_over_thresh = cast_avg >= 40

	bechdel_pass = bechdel_rating == 3
	bechdel_fail = bechdel_rating < 3
	print("P(fail | average age of cast is under threshold):", 
		sum(np.multiply(cast_under_thresh, bechdel_fail)) / sum(cast_under_thresh))
	print("P(pass | average age of cast is over threshold)", 
		sum(np.multiply(cast_over_thresh, bechdel_pass)) / sum(cast_over_thresh))

def genre_cond_prob():
	genres = fe.genres_one_hot()

	bechdel_rating = df['Bechdel_Rating']
	bechdel_pass = bechdel_rating == 3
	bechdel_fail = bechdel_rating < 3

	for genre in genres:
		in_genre = genres[genre]
		print("P(pass | {0}): {1:.2f}".format(
			genre, 
			sum(np.multiply(in_genre, bechdel_pass)) / sum(in_genre)) 
			)

