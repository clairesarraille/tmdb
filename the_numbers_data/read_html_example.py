import pandas as pd

df = pd.read_html(
    'http://www.basketball-reference.com/boxscores/200112100LAC.html')[0]  # or [1], [2]
print(df)
