# Goal: My hypothesis is that Avengers: Endgame was the highest grossing film of 2019.
# Examine 2019's highest grossing films and how Avengers compares
# Narrow scope to Domestic (American) films

# import config # to hide TMDB API keys -- do this before making Git repo public
# to format currency on charts axis
import pprint
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import requests  # to make TMDB API calls
import locale  # to format currency as USD
locale.setlocale(locale.LC_ALL, '')


# api_key = config.tmdb_api_key # get TMDB API key from config.py file

response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' +
                        'ce0d91f6c56a9579c2913151aa709c96' + '&primary_release_year=2019&sort_by=revenue.desc')


# Store the data we recieve as a json into a dataframe and then use matplotlib to visualize our data.
highest_revenue = response.json()  # store parsed json response

# uncomment the next line to get a peek at the highest_revenue json structure
# highest_revenue

highest_revenue_films = highest_revenue['results']

# with open("/Users/clairesarraille/git-repos/Flatiron-School/module01/mod01finproj/the_movie_db_data/output.txt", "w") as text_file:
# print(response, file = text_file)


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(highest_revenue_films)
