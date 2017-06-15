from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
file = urlopen('http://www.imdb.com/chart/top')
filehtml = file.read()
file.close()
soup = BeautifulSoup(filehtml, 'html.parser')
movies = soup.find_all(class_="titleColumn", limit = 10)
for i in movies:
	print (i.text)