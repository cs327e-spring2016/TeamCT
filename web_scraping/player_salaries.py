#Player Salaries
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://espn.go.com/nba/salaries/_/year/2016")
bsObj=BeautifulSoup(html.read(), 'html.parser')
for link in bsObj.find_all('td', {'style':'text-align:right;'}):
    print(link.string)