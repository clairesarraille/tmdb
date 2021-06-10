# Set environment before running this script with: conda activate learn-env

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from tmdbv3api import TMDb, Discover, Movie
import os
from math import ceil

# Load classes from tmdbv3api - a python library for The Movie Database (TMDb) API
tmdb = TMDb()
discover = Discover()
movie = Movie()

# Call TMDb api key using previously set environment variable in learn-env
priv_api_key = os.environ.get('TMDB_PRIVATE_API_KEY')
tmdb.api_key = priv_api_key

# Query discover/movie data: https://developers.themoviedb.org/3/discover/movie-discover
N_YEAR_RANGE = range(2000, 2020)  # Grab 2000-2019 data, inclusive
N_RESULT = 100  # Enter number of results desired for each year
N_RESULT_PAGE = 20  # Discover() class returns 20 results per page
# Num pages = Num results / num results per page, rounded UP using math.ceil
N_PAGES = ceil(N_RESULT / N_RESULT_PAGE)

ids = {}  # Instantiate empty dictionary to store movie ids
for year in N_YEAR_RANGE:  # Iterate through years 2000-2019 inclusive
    # Keys are integers for each year, and value is list of ids for that year
    ids[year] = []

    for page in range(0, N_PAGES):
        # For N_PAGES, create list movies_running, querying results by year, page, & sort revenue desc
        movies_running = discover.discover_movies({
            'sort_by': 'revenue.desc',
            'primary_release_year': str(year),
            # API is 1 indexed - so we grab pages 1 to N_PAGES inclusive
            'page': str(page + 1)
        })
        # .extend used rather than .append in order to extend our list by >1 items at once
        ids[year].extend([index['id'] for index in movies_running])

# print(
    # f" Current key is key {year} and current value for that key is the list: {ids[year]} ")
