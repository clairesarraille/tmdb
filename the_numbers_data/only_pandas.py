import pandas as pd

df = pd.read_html(
    'https://www.the-numbers.com/box-office-star-records/domestic/yearly-acting/highest-grossing-2021-stars')

print(df)
