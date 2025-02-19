import requests
from bs4 import BeautifulSoup

#2. Sending Request

headers = {'User-Agent': 'Mozilla/5.0'} #without this you will get 403. Most of thes sites need a browser info in the header to prevent attacjs from bots
r = requests.get('http://www.goodreads.com', headers=headers)
print(r.status_code)  # status code 200 defines Success - OK

#4. Parsing the data

book_soup = BeautifulSoup(r.content, 'html.parser')
categories=book_soup.find_all('a',attrs={'class':'gr-hyperlink'})
print(categories)

"""
<h3>5. Oragnizing the data</h3>
<ul><li> We only need the categories, rest of the data is useless</li>
    <li> Each category have hyperlink to respective genres
"""

txt_categories=[]
for tag in categories:
    if 'genres' in tag.get('href'):
        txt_categories.append(tag.string)

for category in txt_categories:
    print(category)







