import pprint


# Pretty-Print preview of discover.discover_movies data
def print_sample_tmdb(m, m_r, p, y):
    print(f"Year is: {y}")
    print(f"Page is: {p +1}")
    print(f"There are {len(m[y])} movies in movies dict for {y}")
    print(f"Here is an example from movies_running:")
    for index in m_r[0:1]:
        pprint.pprint(dict(index))
    print()
