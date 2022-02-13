# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    result = {}
    for line in open(f):
        #list of data in format ['Toy Story (1995)', '4.0']
        data = line.split('|')[0:]
        data = data[:-1]
        if data[0] in result.keys():
            result[data[0]].append(float(data[1]))
        else:
            result[data[0]] = [float(data[1])]
    return(result)
    
# 1.2
def read_movie_genre(f):
    result = {}
    for line in open(f):
        line = line.rstrip()
        data = line.split('|')[0:]
        result[data[2]] = data[0]
    return(result)
    
# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    result = {}
    for k, v in d.items():
        result[v] = result.get(v, []) + [k]
    return result

# 2.2
def calculate_average_rating(d):
    avg_result = {}
    for key, value in d.items():
        avg_result[key] = sum(value)/float(len(value))
    return avg_result

# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    
    sorted_avg = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    items = sorted_avg.items()
    topn = list(items)[:n]
    #convert list to dict
    dict_top_n = dict(topn)
    
    del sorted_avg
    del items

    return dict_top_n

# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW

    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW

    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW

    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW


# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW

    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW

    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW


# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading

    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py
main()
