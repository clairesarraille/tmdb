import pandas as pd
import requests
from bs4 import BeautifulSoup

# Ping server and store html in variable "html_doc"
URL = 'https://www.the-numbers.com/box-office-star-records/domestic/yearly-acting/highest-grossing-2021-stars'
html_doc = requests.get(URL)

# Parse html_doc using BeautifulSoup and html5lib
soup = BeautifulSoup(html_doc.content, 'html5lib')

# with open("/Users/clairesarraille/git-repos/Flatiron-School/module01/additional_courses/beautiful_soup/output.txt", "w") as text_file:
# print(soup.prettify(), file=text_file)

# Find the first <b> tag after the string 'Complete List'
textmatch = soup.find('b', text='Complete List')
# Find the first <table> tag after our textmatch object and store in bs4 tag object, table
table = textmatch.findNext('table')

# Transform tag object, table, into formatted Unicode string, each tag on its own line, using .prettify()
# Read this nicely formatted Unicode string using pd.read_html, and store in a list, dfs
dfs = pd.read_html(table.prettify())

# Turn list into dataframe:
df = pd.DataFrame(dfs[0])

print(df.head())
print(type(df))
