#import re
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import datetime
#import random
#import pymysql
#
#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='skt522', db='mysql', charset='utf8')
#cur = conn.cursor()
#cur.execute("USE scraping")
#random.seed(datetime.datetime.now())
#
#def store(title):
#    cur.execute("INSERT INTO pages title VALUES (\"%s\")", title)
#    cur.connection.commit()
#
#def getLinks(articleURL):
#    html = urlopen("http://espn.go.com/nba/salaries/_/year/2016")
#    bsObj=BeautifulSoup(html.read(), 'html.parser')
#    for title in bsObj.find_all('td', {'style':'text-align:right;'}):
#        store(title)
#cur.close()
#conn.close()

#Player Names
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
numPage2016 = 11
numPage2015 = 11
numPage2014 = 10
name = []
name2016Array = []
for year in (2014, 2015, 2016):
    for pageNumber in range(1, numPage2016+1):
        html = urlopen("http://espn.go.com/nba/salaries/_/year/" + str(year) + "/page/" + str(pageNumber))
        bsObj=BeautifulSoup(html.read(), 'html.parser')
        table = bsObj.find('table')
        for row in table.find_all('tr'):
            col = row.find_all('td')
            name = col[1].text
            salary = col[3].text
            index = name.find(",")
            name = name[:index]
            if name != "NAM" or salary != "SALARY":
                array = [name]
                prevYear = year-1
                array.append(str(prevYear) + "-" + str(year)[2:])
                salary = salary.replace("$", "")
                salary = salary.replace(",", "")
                salaryArray = array.append(salary)
                name2016Array.append(array)
print(name2016Array)

#Player Salaries
#import re
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#numPage2016 = 11
#numPage2015 = 11
#numPage2014 = 10
#name2016Array = []
#name2015Array = []
#name2014Array = []
#for i in range(1, numPage2016+1):
#    html = urlopen("http://espn.go.com/nba/salaries/_/year/2016/page/" + str(i))
#    bsObj=BeautifulSoup(html.read(), 'html.parser')
#    table = bsObj.find('table')
#    for row in table.find_all('tr'):
#        col = row.find_all('td')
#        name2016Array = col[3].text
#        #index = name2016Array.find("\n")
#        #name2016Array = name2016Array[:index]
#        if name2016Array != "SALARY":
#            print(name2016Array[1])


#import re
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#html = urlopen("http://espn.go.com/nba/salaries/_/year/2016")
#bsObj=BeautifulSoup(html.read(), 'html.parser')
#for link in bsObj.find_all('td'):
#    if 'href' in link.attrs:
#        print(link.attres['href'])

#import pymysql
#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='skt522', db='mysql')
#cur = conn.cursor()
#cur.execute("USE scraping")
#cur.execute("SELECT * FROM pages")
#print(cur.fetchone())
#cur.close()
#conn.close()