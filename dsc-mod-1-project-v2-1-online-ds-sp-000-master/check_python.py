# Check that it worked:
is_NaN = df_details.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = df_details[row_has_NaN]

rows_with_NaN[['title', 'genres', 'genres_list_str']].iloc[0:3]
