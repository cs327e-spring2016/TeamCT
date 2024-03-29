
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
commandList = []

### DONT FORGET TO CHANGE PERSONAL PASSWORD PER USER ###
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyz', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE TeamCT")

salaryID = 1

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
                nameList = []
                nameList.append(name.split())
                last = nameList[-1][-1]
                first = nameList[-1][0]
                # since player_id cannot be NULL, put fillerCount as filler since cannot be NULL or repeating then later update
                array = [salaryID, last, first]
                prevYear = year-1
                array.append(str(prevYear) + "-" + str(year)[2:])
                salaryString = salaryString.replace("$", "")
                salaryString = salaryString.replace(",", "")
                salaryArray = array.append(salaryString)
                name2016Array.append(array)

                print(last, first)
                # get player id
                cur.execute("SELECT * FROM Player_Bio_Info WHERE lname = %s AND fname = %s", (last, first))
                if cur.rowcount:
                    playerID = cur.fetchone()
                    playerID = list(playerID)
                    playerID = playerID[0]


                    # now, insert each row (array) into table 'Salary'
                    if year == 2014:
                        cur.execute("INSERT INTO Salary (salary_id, lname, fname, season, salary, player_id) VALUES (%s,%s,%s,%s,%s,%s)", (salaryID, last, first, "2013-14", int(salaryString), int(playerID)))
                        cur.connection.commit()
                    if year == 2015:
                        cur.execute("INSERT INTO Salary (salary_id, lname, fname, season, salary, player_id) VALUES (%s,%s,%s,%s,%s,%s)", (salaryID, last, first, "2014-15", int(salaryString), int(playerID)))
                        cur.connection.commit()
                    if year == 2016:
                        cur.execute("INSERT INTO Salary (salary_id, lname, fname, season, salary, player_id) VALUES (%s,%s,%s,%s,%s,%s)", (salaryID, last, first, "2015-16", int(salaryString), int(playerID)))
                        cur.connection.commit()

                salaryID = salaryID + 1

print(name2016Array)

# sort name2016Array

cur.close()
conn.close()
