import pymysql
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


response = urlopen("http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2013-14&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=")
string = response.read().decode("utf-8")
responseJson = json.loads(string)
print(responseJson['resultSets'][0]['rowSet'])


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Skater123', db='mysql')
cur = conn.cursor()
cur.execute("USE teamct")
#cur.execute("SELECT * FROM pages WHERE id=1")
#print(cur.fetchone())
cur.close()
conn.close()