def pprint_tmdb(m, m_r, p, y):
    print(f"Year is: {y}")
    print(f"Page is: {p +1}")
    print(f"There are {len(m[y])} movies in movies dict for {y}")
    print(f"Here is an example from movies_running:")
    slice_m_r = []
    for index in m_r[0:2]:
        slice_m_r.append((dict(index)))
    slice_m_r = dict
    for k,v in m_r.items:
        pprint.pprint(k,v)
    print()