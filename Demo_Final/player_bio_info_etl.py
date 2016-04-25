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

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='skt522', db='mysql')
cur = conn.cursor()
cur.execute("CREATE DATABASE TeamCT")
cur.execute("USE TeamCT")
cur.execute("CREATE TABLE Player_Bio_Info (player_id INT NOT NULL, lname VARCHAR(30) NOT NULL, fname VARCHAR(30) NOT NULL, position VARCHAR(20), height VARCHAR(20), weight INT, DOB VARCHAR(20), college VARCHAR(50), CONSTRAINT pk_Player_Bio_Info PRIMARY KEY (player_id));")

cur.execute("CREATE TABLE Salary (salary_id INT NOT NULL, lname VARCHAR(30) NOT NULL, fname VARCHAR(30) NOT NULL, season VARCHAR(10) NOT NULL, salary INT, player_id INT NOT NULL, CONSTRAINT pk_Salary PRIMARY KEY (salary_id), CONSTRAINT fk_Salary FOREIGN KEY (player_id) REFERENCES Player_Bio_Info(player_id));")

cur.execute("CREATE TABLE Player_Stats (stats_id INT NOT NULL, lname VARCHAR(30) NOT NULL, fname VARCHAR(30) NOT NULL, season VARCHAR(10) NOT NULL, team VARCHAR(30), PPG LONG, APG LONG, RPG LONG, SPG LONG, BPG LONG, TOs LONG, FG_percent LONG, FGM LONG, 3P_percent LONG, 3PM LONG, FT_percent LONG, FTM LONG, min_per_game LONG, player_id INT NOT NULL, CONSTRAINT pk_Player_Stats PRIMARY KEY (stats_id), CONSTRAINT fk_Player_Stats FOREIGN KEY (player_id) REFERENCES Player_Bio_Info(player_id));")

cur.execute("CREATE TABLE Shoe_Endorsement (endorsement_id INT NOT NULL, lname VARCHAR(30) NOT NULL, fname VARCHAR(30) NOT NULL, shoe_brand VARCHAR(30), shoe_model VARCHAR(50), player_id INT NOT NULL, CONSTRAINT pk_Shoe_Endorsement PRIMARY KEY (endorsement_id), CONSTRAINT fk_Shoe_Endorsement FOREIGN KEY (player_id) REFERENCES Player_Bio_Info(player_id));")


for player in players:
    cur.execute("INSERT INTO Player_Bio_Info (player_id, lname, fname, position, height, weight, DOB, college) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (player[0], player[1], player[2], player[3], player[4], int(player[5]), player[6], player[7]))
    cur.connection.commit()

cur.close()
conn.close()