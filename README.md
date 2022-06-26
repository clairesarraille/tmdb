# Analyzing Movie Success using TMDb Data

TMDB_PROJECT.ipynb is the Jupyter Notebook containing all code for this project. In the folder qa_files are the results from the section of the notebook commented "Sanity check there are 3,000 titles in movies dictionary."
I retrieved The Movie Database data from TMDb's API via the [tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api) python library. If you fork this repo, the only variable you will need to change is:

```
priv_api_key = os.environ.get('TMDB_PRIVATE_API_KEY')
tmdb.api_key = priv_api_key
```

I use Anaconda to manage my datascience environment and python packages -- and I followed the direction for hiding an API key [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables).

The analysis with genre and production company were made possible by Max Hilsdorf's wonderful and detailed tutorial on the subject of list values in columns. Please check out his blog post: [Dealing with List Values in Pandas Dataframes](https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173) and Jupyter Notebook [tutorial](https://github.com/MaxHilsdorf/dealing_with_lists_in_pandas).


The appendix folder contains a short script mocking-up a method of scraping [Film Star Data from The Numbers](https://www.the-numbers.com/box-office-star-records/domestic/yearly-acting/highest-grossing-2021-stars).
In the future if I continue to analyze movie data I'd like to further develop this Beautiful Soup scraper to retrieve highest grossing stars data and compare correlations of high profit films, star power, and professional critic reviews.

Attribution: This product uses the TMDb API but is not endorsed or certified by TMDb

![attribution](https://user-images.githubusercontent.com/71570329/121915422-0bf4be80-cce8-11eb-8992-64b37edacef9.png)
