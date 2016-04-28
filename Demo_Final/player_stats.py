import pymysql
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

result = open("stats_info_result.txt", "w")

seasons = ["2013-14", "2014-15", "2015-16"]
databaseList = []

for i in seasons:
  print("http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=" + i +"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=")
  response = urlopen("http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=" + i +"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=")
  string = response.read().decode("utf-8")
  responseJson = json.loads(string)

  entireSet = responseJson['resultSets'][0]['rowSet']
  #print(entireSet)

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

    FGM = set[10]
    FGMList.append(FGM)

    FGP = set[12]
    FGPList.append(FGP)

    ThreePM = set[13]
    ThreePMList.append(ThreePM)

    ThreePP = set[15]
    ThreePPList.append(ThreePP)

    FTM = set[16]
    FTMList.append(FTM)

    FTP = set[18]
    FTPList.append(FTP)

    minutes = set[9]
    minList.append(minutes)

#  print(lnameList)
#  print(fnameList)
#  print(PPGList)
#  print(APGList)
#  print(RPGList)
#  print(SPGList)
#  print(BPGList)
#  print(TOsList)
#  print(FGMList)
#  print(FGPList)
#  print(ThreePMList)
#  print(ThreePPList)
#  print(FTMList)
#  print(FTPList)
#  print(minList)

  # now, create rows in database in our format
  counter = 1	# also a counter
  maxCount = len(entireSet)	# number of rows from NBA stat website
  seasonID = i # need to figure how to distinguish data from website



  #for loops gets all players + stats, ordered by first name however
  while counter <= maxCount:
    playerRow = []
    playerRow.append(str(lnameList[counter-1]))
    playerRow.append(str(fnameList[counter-1]))
    playerRow.append(str(seasonID))
    playerRow.append(str(teamList[counter-1]))
    playerRow.append(str(PPGList[counter-1]))
    playerRow.append(str(APGList[counter-1]))
    playerRow.append(str(RPGList[counter-1]))
    playerRow.append(str(SPGList[counter-1]))
    playerRow.append(str(BPGList[counter-1]))
    playerRow.append(str(TOsList[counter-1]))
    playerRow.append(str(round(FGPList[counter-1] * 100,1)))
    playerRow.append(str(FGMList[counter-1]))
    playerRow.append(str(round(ThreePPList[counter-1] * 100,1)))
    playerRow.append(str(ThreePMList[counter-1]))
    playerRow.append(str(round(FTPList[counter-1] * 100,1)))
    playerRow.append(str(FTMList[counter-1]))
    playerRow.append(str(minList[counter-1]))

    databaseList.append(playerRow)

    counter = counter + 1	# increment counter & move onto next player

  # once databaseList is created, sort by last names
print(databaseList)
for stat in databaseList:
    insert_stat = stat[0] + ";" + stat[1] + ";" + stat[2] + ";" + stat[3] + ";" + stat[4] + ";" + stat[5] + ";" + stat[6] + ";" + stat[7] + ";" + stat[8] + ";" + stat[9] + ";" + stat[10] + ";" + stat[11] + ";" + stat[12] + ";" + stat[13] + ";" + stat[14] + ";" + stat[15] + ";" + stat[16] + "\n"
    result.write(insert_stat)
