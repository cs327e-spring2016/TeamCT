import pymysql

def unique_items(players):
    insert_set = []
    name_set = set()
    for item in players:
        if item[0]+" "+item[1] not in name_set:
            name_set.add(item[0]+" "+item[1])
            insert_set.append(item)
    return insert_set

file = open("player_info.txt", "r")
players = []
for line in file:
    line = line.split(";")
    line[6] = line[6][:-1]
    players.append(line)
print(len(players))
players = unique_items(players)
players = sorted(players)
player_id = 1
for player in players:
    player.reverse()
    player.append(player_id)
    player.reverse()
    player_id += 1
print(players)

# once player array is cleaned up, add to MySQL database 'TeamCT'

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xx', db='mysql')
cur = conn.cursor()
cur.execute("USE TeamCT")

for player in players:
    cur.execute("INSERT INTO Player_Bio_Info (player_id, lname, fname, position, height, weight, DOB, college) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (player[0], player[1], player[2], player[3], player[4], int(player[5]), player[6], player[7]))
    cur.connection.commit()

cur.close()
conn.close()