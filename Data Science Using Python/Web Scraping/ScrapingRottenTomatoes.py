
"""
Refer these videos:

https://www.youtube.com/watch?v=xjA1HjvmoMY

"""

import requests
import csv #to store the data
import pandas as pd #For storing data
import matplotlib.pyplot as plt #For Visualisation
from bs4 import BeautifulSoup

#sending request

headers = {'User-Agent': 'Mozilla/5.0'} #without this you will get 403. Most of thes sites need a browser info in the header to prevent attacjs from bots
response=requests.get('https://www.rottentomatoes.com/browse/movies_in_theaters/sort:top_box_office', headers=headers)
print(response.status_code)# status code 200 defines Success - OK

#Creating BeautifulSoup object and parsing the table
soup=BeautifulSoup(response.content,'html.parser')

#print(soup.prettify())

#print(soup.find('div'))

#print(soup.find_all('div'))

movie_name = soup.find_all('span', class_='p--small')
#print(movie_name)
print(movie_name[1].text.strip())

criticsScore = soup.find_all('rt-text',attrs={'slot':'criticsScore'})
print(criticsScore[1].text.strip())

audienceScore = soup.find_all('rt-text',attrs={'slot':'audienceScore'})
print(audienceScore[1].text.strip())

L = min(len(movie_name), len(criticsScore), len(audienceScore))

arrMovieName= []
arrCriticsScore = []
arrAudienceScore = []
for i in range(L):
    arrMovieName.append(movie_name[i].text.strip())
    arrCriticsScore.append(criticsScore[i].text.strip())
    arrAudienceScore.append(audienceScore[i].text.strip())

#7. Storing the data

movie=pd.DataFrame({'Name':arrMovieName,'CriticsScore':arrCriticsScore,'AudienceScore':arrAudienceScore})
print(movie.head())
print(movie.shape)

### 8. Visualizing Data

#Critics reviews of movies
plt.barh(movie.Name,movie.CriticsScore)
plt.xlabel('CriticsScore', rotation=90)
plt.ylabel('Movies',rotation=90)
plt.show()

#Audience score of movies

plt.barh(movie.Name,movie.AudienceScore)
plt.xlabel('AudienceScore', rotation=90)
plt.ylabel('Movies',rotation=90)
plt.show()









