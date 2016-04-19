
#Player Names
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
numPage2016 = 11
numPage2015 = 11
numPage2014 = 10
name = []
name2016Array = []

### DONT FORGET TO CHANGE PERSONAL PASSWORD PER USER ###
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='xyz', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE TeamCT")

fillerCount = 1
for year in (2014, 2015, 2016):
    for pageNumber in range(1, numPage2016+1):
        html = urlopen("http://espn.go.com/nba/salaries/_/year/" + str(year) + "/page/" + str(pageNumber))
        bsObj=BeautifulSoup(html.read(), 'html.parser')
        table = bsObj.find('table')
        for row in table.find_all('tr'):
            col = row.find_all('td')
            name = col[1].text
            salaryString = col[3].text
            index = name.find(",")
            name = name[:index]
            if name != "NAM" or salaryString != "SALARY":
                # since player_id cannot be NULL, put fillerCount as filler since cannot be NULL or repeating then later update
                array = [fillerCount, name]
                prevYear = year-1
                array.append(str(prevYear) + "-" + str(year)[2:])
                salaryString = salaryString.replace("$", "")
                salaryString = salaryString.replace(",", "")
                salaryArray = array.append(salaryString)
                name2016Array.append(array)
                
               
                
                # now, insert each row (array) into table 'Salary'
                if year == 2014:
                  cur.execute("INSERT INTO Salary (player_id, full_name, season_id, salary) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")", (fillerCount, name, "2013-14", salaryString))
                  cur.connection.commit()
                if year == 2015:
                  cur.execute("INSERT INTO Salary (player_id, full_name, season_id, salary) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")", (fillerCount, name, "2014-15", salaryString))
                  cur.connection.commit()
                if year == 2016:
                  cur.execute("INSERT INTO Salary (player_id, full_name, season_id, salary) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")", (fillerCount, name, "2015-16", salaryString))
                  cur.connection.commit()
                
                fillerCount = fillerCount + 1
                

print(name2016Array)

cur.close()
conn.close()
