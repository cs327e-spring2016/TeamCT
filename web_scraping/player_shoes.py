import pymysql
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re


### DONT FORGET TO CHANGE PERSONAL PASSWORD PER USER ###
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Skater123', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE TeamCT")

row_array = []
brands = {"361":1, "adidas":4, "and1":1, "anta":1, "brandblack":1, "jordan":4, "k1x":1, "li-ning":1, "nike":16, "peak":1, "reebok":1, "spalding":1, "under-armour":1}

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
                    name = name.split()
                    if(len(name) != 1):
                        name = name[0] + " " + name [1]
                    row_player.append(name)
                elif(idx == 5):
                    name = col.find("a").text
                    row_player.append("Nike")
                    row_player.append(name)
                    row_array.append(row_player)
                idx+=1
print(row_array)