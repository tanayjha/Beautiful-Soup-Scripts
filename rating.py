from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib, time, os, subprocess
from urllib.request import urlopen
user1 = 'tanay24'
url = "http://codeforces.com/contests/with/" + user1
file = urlopen(url)
filehtml = file.read()
file.close()
soup = BeautifulSoup(filehtml, 'html.parser')
t1 = soup.find(class_ = 'tablesorter user-contests-table')
t2 = t1.find('tbody')
t3 = t2.find_all('td')
count = 0
i = 0
ratings1 = []
x1 = []
for alltd in t3:
	count = count + 1
	if count % 7 == 6:
		ratings1.insert(i, int(alltd.text))
		i = i+1
		x1.insert(i, i)
ratings1 = ratings1[::-1]
print (ratings1)

user2 = 'killerrobot'
url = "http://codeforces.com/contests/with/" + user2
file = urlopen(url)
filehtml = file.read()
file.close()
soup = BeautifulSoup(filehtml, 'html.parser')
t1 = soup.find(class_ = 'tablesorter user-contests-table')
t2 = t1.find('tbody')
t3 = t2.find_all('td')
count = 0
i = 0
ratings2 = []
x2 = []
for alltd in t3:
	count = count + 1
	if count % 7 == 6:
		ratings2.insert(i, int(alltd.text))
		i = i+1
		x2.insert(i, i)
ratings2 = ratings2[::-1]
print (ratings2)
plt.plot(x1, ratings1, 'r--', x2, ratings2, 'b--')
plt.axis([0, 50, 1000, 1650])
plt.show()
