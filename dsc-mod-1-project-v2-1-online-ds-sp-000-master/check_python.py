df_q3['revenue_millions'] = '$' + (df_q3['revenue'].astype(round(float)/1000000, 2).astype(str) + 'MM'

df['($) millions'] = '$' + (df['Amount'].astype(round(float,2))/1000000).astype(str) + 'MM'
