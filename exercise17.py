# 17: Decode A Web Page
# Use the BeautifulSoup and requests Python packages to print out a list of
# all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
title = soup.findAll('p', class_="indicate-hover")
news_titles = [title.text for title in title]

COUNT = len(news_titles) - 6

for i in range(1, COUNT):
    print(f'{i}. {news_titles[i]}')
