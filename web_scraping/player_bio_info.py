import pymysql
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


response = urlopen("http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2013-14&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=")
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
playerID = 1	# also a counter
maxCount = len(entireSet)	# number of rows from NBA stat website
seasonID = "1516" # need to figure how to distinguish data from website
#for loops gets all players + stats, ordered by first name however
while playerID <= maxCount:

  playerRow = []
  playerRow.append(playerID)
  playerRow.append(lnameList[playerID-1])
  playerRow.append(fnameList[playerID-1])
  playerRow.append(seasonID)
  playerRow.append(teamList[playerID-1])
  playerRow.append(PPGList[playerID-1])
  playerRow.append(APGList[playerID-1])
  playerRow.append(RPGList[playerID-1])
  playerRow.append(SPGList[playerID-1])
  playerRow.append(BPGList[playerID-1])
  playerRow.append(TOsList[playerID-1])
  playerRow.append(FGMList[playerID-1])
  playerRow.append(FGPList[playerID-1])
  playerRow.append(ThreePMList[playerID-1])
  playerRow.append(ThreePPList[playerID-1])
  playerRow.append(FTMList[playerID-1])
  playerRow.append(FTPList[playerID-1])
  playerRow.append(minList[playerID-1])

  print(playerRow)
  # once playerRow is created, add to MySQL database 'TeamCT'

  playerID = playerID + 1	# increment counter & move onto next player




  
#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyz', db='mysql')
#cur = conn.cursor()
#cur.execute("USE TeamCT")
#cur.execute("SELECT * FROM pages WHERE id=1")
#print(cur.fetchone())
#cur.close()
#conn.close()