# Function to pretty-print results of discover.discover_movies
import pprint


def pprint_tmdb(m, m_r, p, y):  # Pretty-Print preview of discover.discover_movies data
    print(f"Year is: {y}")
    print(f"Page is: {p +1}")
    print(f"There are {len(m[y])} movies in movies dict for {y}")
    print(f"Here are two examples from movies_running:")
    for index in m_r[0:2]:
        pprint.pprint(dict(index))
    print()

    # Check to see if all movies have all the same fields:


def check_keys(expected_keys, list_of_dict):
    bool_list = []
    for index in range(0, len(list_of_dict)):
        if expected_keys != list_of_dict[index.keys()]:
            bool_list.append(f"has different keys at index {index}")
    return bool_list


check_keys(movies[2019][0].keys(), movies[2019])
