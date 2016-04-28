import pymysql
import json
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import webbrowser

result = open("player_info_result.txt", 'w')

teams = [1610612738, 1610612751, 1610612752, 1610612755, 1610612761, 1610612741, 1610612739, 1610612765, 1610612754, 1610612749, 1610612737, 1610612766, 1610612748, 1610612753, 1610612764, 1610612743, 1610612750, 1610612760, 1610612757, 1610612762, 1610612744, 1610612746, 1610612747, 1610612756, 1610612758, 1610612742, 1610612745, 1610612763, 1610612740, 1610612759]
playerID = 1
bioInfo = []
player = []

for year in ["2013-14","2014-15", "2015-16"]:
    # use this if error 400
    # WARNING: will open 30+ tabs
    #for team in teams:
    #webbrowser.open("http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=" + year + "&TeamID=" + str(team))

    for team in teams:
        print(team)
        response = requests.get("http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=" + year + "&TeamID=" + str(team))
        response.raise_for_status()
        response = response.json()
        entireSet = response['resultSets'][0]['rowSet']
        playerPos = []
        playerHeight = []
        playerWeight = []
        playerDOB = []
        playerCollege = []
        fullNameList = []
        firstLastSet = []
        lnameList = []
        fnameList = []
        for eachSet in entireSet:
            fullName = eachSet[3]
            if fullName != "Nene":
                position = eachSet[5]
                height = eachSet[6]
                weight = eachSet[7]
                dateOfBirth = eachSet[8]
                college = eachSet[11]
                fullNameList.append(fullName)
                firstLastSet = fullName.split(" ", 1)
                fname = firstLastSet[0]
                lname = firstLastSet[1]
                fnameList.append(fname)
                lnameList.append(lname)
                player = [str(lname), str(fname), str(position), str(height), str(weight), str(dateOfBirth), str(college)]
                bioInfo.append(player)
            else:
                position = eachSet[5]
                height = eachSet[6]
                weight = eachSet[7]
                dateOfBirth = eachSet[8]
                college = eachSet[11]
                fullNameList.append(fullName)
                fnameList.append(fullName)
                lnameList.append("Hilario")
                player = ["Hilario", str(fullName), str(position), str(height), str(weight), str(dateOfBirth), str(college)]
                bioInfo.append(player)
print(bioInfo)
for player in bioInfo:
    insert_player = player[0] + ";" + player[1] + ";" + player[2] + ";" + player[3] + ";" + player[4] + ";" + player[5] + ";" + player[6] + "\n"
    result.write(insert_player)
#print(bioInfo)
print(len(bioInfo))

