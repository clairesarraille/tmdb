def boolean_df(item_lists, unique_items):
    # Instantiate Boolean Dictionary:
    bool_dict = {}
    # Loop through all the tags
    for i, item in enumerate(unique_items):
        # Apply boolean mask that returns a True-False list of whether a tag is in a taglist
        bool_dict[item] = item_lists.apply(lambda x: item in x)
    # Return the results as a dataframe
    return pd.DataFrame(bool_dict)
