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
# Find the first <table> tag after our textmatch object
table = textmatch.findNext('table')

# Find all "table row" (<tr>) elements and store them in rows object
table_rows = table.find_all('tr')

# For each <tr> element (table row) in table_rows, make list of <td> elements (table data) in table_data.
# Finally, extract text from each td element and store in cell_text.
for tr in table_rows:
    table_data = tr.find_all('td')
    for td in table_data:
        cell_text = td.text
        print("this is a single cell" + cell_text)
