import pymysql
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re


### DONT FORGET TO CHANGE PERSONAL PASSWORD PER USER ###
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Skater123', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE TeamCT")

# row_array stores all the data to be inputted
# brands stores the key(brand) => value(pages)
row_array = []
brands = {"361":1, "adidas":4, "and1":1, "anta":1, "brandblack":1, "jordan":4, "k1x":1, "li-ning":1, "nike":16, "peak":1, "reebok":1, "spalding":1, "under-armour":1}

# execute
for brand in brands:
    for pageNumber in range(1, brands[brand]+1):
        print("http://www.nbashoesdb.com/en/search/players/brand/" +brand+ "/page/" + str(pageNumber))
        html = Request("http://www.nbashoesdb.com/en/search/players/brand/" +brand+ "/page/" + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        bsObj = BeautifulSoup(urlopen(html).read(), 'html.parser')
        table = bsObj.find('table')
        for row in table.find_all('tr'):
            idx = 0
            row_player = []
            for col in row.find_all('td'):
                if(idx == 1):
                    name = col.find("a").text
                    name = name.replace("\\", "")
                    name = name.split()
                    if(len(name) != 1):
                        row_player.append(name[1])
                        row_player.append(name[0])
                    elif(name == "Nene"):
                        row_player.append("Hilario")
                        row_player.append("Nene")
                elif(idx == 5):
                    name = col.find("a").text
                    row_player.append(brand)
                    row_player.append(name)
                    row_array.append(row_player)
                idx+=1

#results
print(row_array)
print(str(len(row_array)) + "total records")

# now, insert each row (array) into table 'shoe_endorsement'
e_id = 1
for entry in row_array:
    # get player id
    cur.execute("SELECT * FROM Player_Bio_Info WHERE lname = %s AND fname = %s", (entry[0], entry[1]))
    if cur.rowcount:
        playerID = cur.fetchone()
        playerID = list(playerID)
        playerID = playerID[0]
        cur.execute("INSERT INTO shoe_endorsement (endorsement_id, lname, fname, shoe_brand, shoe_model, player_id) VALUES (%s,%s,%s,%s,%s,%s)", (e_id, entry[0], entry[1], entry[2], entry[3], playerID))
        cur.connection.commit()
        e_id+=1
    else:
        print("Missing player_id: " + entry[1] + " " + entry[0])
print(e_id)
cur.close()
conn.close()