# Set environment before running this script with: conda activate learn-env

# Import datascience libraries:
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Import libraries for fetching and formatting data:
from tmdbv3api import TMDb, Discover, Movie
import os
import pprint

# Import libraries for performing operations:
from math import ceil


# Load classes from tmdbv3api - a python library for The Movie Database (TMDb) API
tmdb = TMDb()
discover = Discover()
movie = Movie()

# Store my API key in my previously set environment variable as a tmdb.api_key string
priv_api_key = os.environ.get('TMDB_PRIVATE_API_KEY')
tmdb.api_key = priv_api_key


def pprint_tmdb(m, m_r, p, y):  # Pretty-Print preview of discover.discover_movies data
    print(f"Year is: {y}")
    print(f"Page is: {p +1}")
    print(f"There are {len(m[y])} movies in movies dict for {y}")
    print(f"Here is an example from movies_running:")
    slice_m_r = []
    for d in m_r[0:1]:
        slice_m_r.append((dict(d))['original_title'])
    for d_2 in slice_m_r:
        pprint.pprint(d_2)


# Define Constants
# Constants are usually defined on a module level and written in all capital letters with underscores separating words
N_YEAR_RANGE = range(2000, 2020)  # grab 2000-2019 data, inclusive
N_RESULT = 100  # Enter number of results desired for each year
N_RESULT_PAGE = 20  # Discover() class returns 20 results per page
# Num pages = Num results / num results per page, rounded UP using math.ceil
N_PAGES = ceil(N_RESULT / N_RESULT_PAGE)

# Instantiate empty dictionary movies to store  outside of the following loops,
# because you want to use movies after loops are finished executing
movies = {}

# Function to grab data from discover.discover_movies:


def return_discover_movies():
    for year in N_YEAR_RANGE:  # iterate through years 2000-2019 inclusive
        # Keys are integers for each year
        # Values will be lists of tmdbv3api objects, converted to dictionaries
        movies[year] = []
        for page in range(0, N_PAGES):
            # For N_PAGES, create list movies_running, querying results by year, page, & sort revenue desc
            # The objects within movies_running 'tmdbv3api.as_obj.AsObj' objects, and will need to be converted to dictionaries later
            movies_running = discover.discover_movies({
                'sort_by': 'revenue.desc',
                'primary_release_year': str(year),
                # API is 1 indexed - so we grab pages 1 to N_PAGES inclusive
                'page': str(page + 1),
                'vote_count.gte': 1
            })
            # .extend used rather than .append in order to extend our list by >1 items at once
            # For each year in our movies dictionary, iterate through 'tmdbv3api.as_obj.AsObj' objects in movies_running, converting each to a dictionary
            # For each year we will have a list of dictionaries, and each dictionary is a set of information for a single movie
            movies[year].extend([dict(tmdb_obj)
                                for tmdb_obj in movies_running])
            # Pretty-Print some examples from movies_running to check data:
            pprint_tmdb(movies, movies_running, page, year)


# Now we have our dictionary movies, with years 2000-2019 inclusive, each with 100 movies in each list from that year
# We didn't need to return movies in the definition of this function, because movies was declared before the function
return_discover_movies()
