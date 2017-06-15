from bs4 import BeautifulSoup
import urllib, time, os, subprocess
from urllib.request import urlopen
# print (soup.find(class_="innings-info-2").text)
old = ""
lst = []
c = 0
while True:
	time.sleep(2)
	redditFile = urlopen('http://www.espncricinfo.com/ci/engine/match/index.html?view=live')
	redditHtml = redditFile.read()
	redditFile.close()
	soup = BeautifulSoup(redditHtml, 'html.parser')
	new = str(soup.find(class_="innings-info-1").text)
	if old[10:12] != new[10:12] and not new in lst:
		subprocess.call(["xdg-open", 'Mu.mp3'])
		print (new[10:])
		old = new 
		lst.insert(c, new)
		c = c+1