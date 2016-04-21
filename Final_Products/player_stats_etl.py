import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='skt522', db='mysql')
cur = conn.cursor()
cur.execute("USE TeamCT")

file = open("stats_info.txt", "r")
player_stats = []
for line in file:
    line = line.split(";")
    lname = line[1]
    fname = line[2]
    line[17] = line[17][:-1]
    cur.execute("SELECT * FROM Player_Bio_Info WHERE lname = %s AND fname = %s", (lname, fname))
    if cur.rowcount:
        statID = cur.fetchone()
        statID = list(statID)
        statID = statID[0]
        line.append(str(statID))
        player_stats.append(line)
print(player_stats)
for player in player_stats:
    cur.execute("INSERT INTO Player_Stats (stats_id, lname, fname, season, team, PPG, APG, RPG, SPG, BPG, TOs, FG_percent, FGM, 3P_percent, 3PM, FT_percent, FTM, min_per_game, player_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (player[0], player[1], player[2], player[3], player[4], player[5], player[6], player[7], player[8], player[9], player[10], player[11], player[12], player[13], player[14], player[15], player[16], player[17], player[18]))
    cur.connection.commit()

cur.close()
conn.close()