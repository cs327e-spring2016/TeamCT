import pymysql
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

seasons = ["2013-14", "2014-15", "2015-16"]
playerID = 1
databaseList = []

for i in seasons:

  response = urlopen("http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=" + i +"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=")
  string = response.read().decode("utf-8")
  responseJson = json.loads(string)

  entireSet = responseJson['resultSets'][0]['rowSet']
  print(entireSet)

  # loop to get all stats lists
  fullNameList = []
  lnameList = []
  fnameList = []
  teamList = []
  PPGList = []
  APGList = []
  RPGList = []
  SPGList = []
  BPGList = []
  TOsList = []
  FGMList = []
  FGPList = []
  ThreePMList = []
  ThreePPList = []
  FTMList = []
  FTPList = []
  minList = []

  for set in entireSet:
    fullName = set[1]
    fullNameList.append(fullName)
    firstAndLast = fullName.split()
    fname = firstAndLast[0]
    lname = firstAndLast[-1]
    fnameList.append(fname)
    lnameList.append(lname)

    team = set[3]
    teamList.append(team)

    points = set[29]
    PPGList.append(points)

    assists = set[22]
    APGList.append(assists)

    rebounds = set[21]
    RPGList.append(rebounds)

    steals = set[24]
    SPGList.append(steals)

    blocks = set[25]
    BPGList.append(blocks)

    turnovers = set[23]
    TOsList.append(turnovers)

    FGM = set[11]
    FGMList.append(FGM)

    FGP = set[13]
    FGPList.append(FGP)

    ThreePM = set[14]
    ThreePMList.append(ThreePM)

    ThreePP = set[16]
    ThreePPList.append(ThreePP)

    FTM = set[17]
    FTMList.append(FTM)

    FTP = set[19]
    FTPList.append(FTP)

    minutes = set[10]
    minList.append(minutes)

  print(lnameList)
  print(fnameList)
  print(PPGList)
  print(APGList)
  print(RPGList)
  print(SPGList)
  print(BPGList)
  print(TOsList)
  print(FGMList)
  print(FGPList)
  print(ThreePMList)
  print(ThreePPList)
  print(FTMList)
  print(FTPList)
  print(minList)

  # now, create rows in database in our format
  counter = 1	# also a counter
  maxCount = len(entireSet)	# number of rows from NBA stat website
  seasonID = i # need to figure how to distinguish data from website



  #for loops gets all players + stats, ordered by first name however
  while counter <= maxCount:

    playerRow = []
    #playerRow.append(playerID)
    playerRow.append(lnameList[counter-1])
    playerRow.append(fnameList[counter-1])
    playerRow.append(seasonID)
    playerRow.append(teamList[counter-1])
    playerRow.append(PPGList[counter-1])
    playerRow.append(APGList[counter-1])
    playerRow.append(RPGList[counter-1])
    playerRow.append(SPGList[counter-1])
    playerRow.append(BPGList[counter-1])
    playerRow.append(TOsList[counter-1])
    playerRow.append(FGMList[counter-1])
    playerRow.append(FGPList[counter-1])
    playerRow.append(ThreePMList[counter-1])
    playerRow.append(ThreePPList[counter-1])
    playerRow.append(FTMList[counter-1])
    playerRow.append(FTPList[counter-1])
    playerRow.append(minList[counter-1])

    databaseList.append(playerRow)

    counter = counter + 1	# increment counter & move onto next player

  # once databaseList is created, sort by last names




databaseList.sort(key=lambda x: x[0])
 # reset playerID to 1
counter = 1
while counter <= len(databaseList):
  databaseList[playerID-1].insert(0,playerID)
  counter = counter + 1
  playerID = playerID + 1
for list in databaseList:
  print(list)


# once playerRow is created, add to MySQL database 'TeamCT'
  
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyz', db='mysql')
cur = conn.cursor()
cur.execute("USE TeamCT")

for num in range(len(databaseList)):  # loop to add each playerRow into Player_Bio_Info table
  cur.execute("INSERT INTO Player_Bio_Info (player_id, lname, fname, season, team, PPG, APG, RPG, SPG, BPG, TOs, FG_Percent, FGM, 3P_Percent, 3PM, FT_Percent, FTM, min_per_game) VALUES (databaseList[num-1][0], databaseList[num-1][1], databaseList[num-1][2], databaseList[num-1][3], databaseList[num-1][4], databaseList[num-1][5], databaseList[num-1][6], databaseList[num-1][7], databaseList[num-1][8], databaseList[num-1][9], databaseList[num-1][10], databaseList[num-1][11], databaseList[num-1][12], databaseList[num-1][13], databaseList[num-1][14], databaseList[num-1][15], databaseList[num-1][16], databaseList[num-1][-1])
  cur.connection.commit()
  
  print(cur.fetchone())
  
#cur.execute("SELECT * FROM pages WHERE id=1")
#print(cur.fetchone())
cur.close()
conn.close()