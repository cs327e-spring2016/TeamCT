from prettytable import PrettyTable
from tabulate import tabulate
import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup


### DONT FORGET TO CHANGE PASSWORD ###
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyz', db='mysql')
cur = conn.cursor()
cur.execute("USE TeamCT")


# Main Menu
##############
ans = True
while ans:
  #print("Note: input 'quit' if you would like to return to the Main Menu. \n")
  mainMenu = str(input("Choose one of the following menu options(#): \n 1) Colleges \n 2) Salaries \n 3) Player Lookup \n 4) Teams \n 5) Shoe Endorsements \n 6) Basketball Stats \n 7) Player Analysis \n"))
  
  if mainMenu == "1":
    print("College")
    # INSERT collegeMenu code here
    
    # College Menu
    ##############
    ansCollege = True
    while ansCollege:
      
      print("This lookup will find all NBA players who have played at a specified college. \n")
      
      result = []	# filler for error loop
      while result == []:
        college = str(input("Name of college: "))
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = '" + college + "'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "position".ljust(20) + "height".ljust(20) + "weight".ljust(20) + "DOB".ljust(20))
        print("----------------------------------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, pos, ht, wt, birth = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])
          print(last.ljust(20) + first.ljust(20) + pos.ljust(20) + ht.ljust(20) + wt.ljust(20) + birth.ljust(20))
        
      ansCollege = False 
    ans = False
       
  elif mainMenu == "2":
    print("Salaries")

    # Salary Menu
    #################
    ansSalary = True
    while ansSalary:
      seasonsMenu = str(input("Select the number of a season: \n 1) 2013-14 \n 2) 2014-15 \n 3) 2015-16 \n"))
      
      if seasonsMenu == "1":
        print("2013-14")
        salaryMenu = str(input("Choose one of the following numbers to select all NBA players making salary in that range during the 2013-14 season: \n 1) More than $20M \n 2) Between $10M and $20M \n 3) Between $5M and $10M \n 4) Between $1M and $5M \n 5) Less than $1M \n"))

        if salaryMenu == "1":
          print("More Than $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND salary > 20000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "2":
          print("Between $10M and $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary >= 10000000 AND salary <= 20000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "3":
          print("Between $5M and $10M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary >= 5000000 AND salary <= 10000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "4":
          print("Between $1M and $5M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary >= 1000000 AND salary <= 5000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "5":
          print("Less than $1M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND salary < 1000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu != "":  
          print("Not Valid Choice, Please Try Again \n")
        
        ansSalary = False
      elif seasonsMenu == "2":
        print("2014-15")
        salaryMenu = str(input("Choose one of the following numbers to select all NBA players making salary in that range during the 2013-14 season: \n 1) More than $20M \n 2) Between $10M and $20M \n 3) Between $5M and $10M \n 4) Between $1M and $5M \n 5) Less than $1M \n"))

        if salaryMenu == "1":
          print("More Than $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND salary > 20000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "2":
          print("Between $10M and $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary >= 10000000 AND salary <= 20000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "3":
          print("Between $5M and $10M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary >= 5000000 AND salary <= 10000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "4":
          print("Between $1M and $5M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary >= 1000000 AND salary <= 5000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "5":
          print("Less than $1M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND salary < 1000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu != "":  
          print("Not Valid Choice, Please Try Again \n")

        ansSalary = False
        
      elif seasonsMenu == "3":
        print("2015-16")
        salaryMenu = str(input("Choose one of the following numbers to select all NBA players making salary in that range during the 2013-14 season: \n 1) More than $20M \n 2) Between $10M and $20M \n 3) Between $5M and $10M \n 4) Between $1M and $5M \n 5) Less than $1M \n"))

        if salaryMenu == "1":
          print("More Than $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND salary > 20000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "2":
          print("Between $10M and $20M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary >= 10000000 AND salary <= 20000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "3":
          print("Between $5M and $10M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary >= 5000000 AND salary <= 10000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "4":
          print("Between $1M and $5M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary >= 1000000 AND salary <= 5000000)")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu == "5":
          print("Less than $1M")
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND salary < 1000000")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "salary".ljust(20))
          print("------------------------------------------------")
          # table items
          for row in resultList:
            last, first, sal = row[0], row[1], str(row[-1])
            print(last.ljust(20) + first.ljust(20) + sal.ljust(20))
          ansSalary = False
        elif salaryMenu != "":  
          print("Not Valid Choice, Please Try Again \n")

        ansSalary = False
        
      elif seasonsMenu == "":
        print("Please Choose a Valid Season \n")
      
  
          
    ans = False  

  elif mainMenu == "3":
    print("Player Lookup")
    
    # Player Lookup Menu
    ##############
    ansLookup = True
    while ansLookup:
      print("This lookup will find the basketball stats of a desired player in a specific season. \n ")
      lastName = str(input("Last Name: "))
      firstName = str(input("First Name: ")) 
      query = "SELECT * FROM Player_Stats WHERE lname LIKE '%" + lastName + "%' AND fname LIKE '%" + firstName + "%'"
      cur.execute(query)
      cur.connection.commit()
      result = cur.fetchall()
      result = list(result)
      resultList = [list(elem) for elem in result]
      #header
      print("lname".ljust(20) + "fname".ljust(20) + "season".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
      print("-------------------------------------------------------------------------------------------------------")
      for row in resultList:
        last, first, season, ppg, apg, rpg, spg, bpg, to, minutes = str(row[1]), str(row[2]), str(row[3]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[-2])
        print(last.ljust(20) + first.ljust(20) + season.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
      ansLookup = False
    ans = False
    
  elif mainMenu == "4":
    print("Teams")
    
    ## Teams Menu
    #############
    ansTeams = True
    while ansTeams:
      seasonsMenu = str(input("Select the number of a season: \n 1) 2013-14 \n 2) 2014-15 \n 3) 2015-16 \n"))
      
      if seasonsMenu == "1":
        print("2013-14")
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2013-14 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n 6) Cleveland Cavaliers \n 7) Dallas Mavericks \n 8) Denver Nuggets \n 9) Detroit Pistons \n 10) Golden State Warriors \n 11) Houston Rockets \n 12) Indiana Pacers \n 13) Los Angeles Clippers \n 14) Los Angeles Lakers \n 15) Memphis Grizzlies \n 16) Miami Heat \n 17) Milwaukee Bucks \n 18) Minnesota Timberwolves \n 19) New Orleans Pelicans \n 20) New York Knicks \n 21) Oklahoma City Thunder \n 22) Orlando Magic \n 23) Philadelphia 76ers \n 24) Phoenix Suns \n 25) Portland Trail Blazers \n 26) Sacramento Kings \n 27) San Antonio Spurs \n 28) Toronto Raptors \n 29) Utah Jazz \n 30) Washington Wizards"))
        
        if teamsMenu == "1":
          print("2013-14 Atlanta Hawks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'ATL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "2":
          print("2013-14 Boston Celtics")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'BOS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False       
           
        elif teamsMenu == "3":
          print("2013-14 Brooklyn (New Jersey) Nets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'BKN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "4":
          print("2013-14 Charlotte Hornets (Bobcats)")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'CHA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))      
          ansTeams = False
          
        elif teamsMenu == "5":
          print("2013-14 Chicago Bulls")  
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'CHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))    
          ansTeams = False
        
        if teamsMenu == "6":
          print("2013-14 Cleveland Cavaliers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'CLE'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "7":
          print("2013-14 Dallas Mavericks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'DAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "8":
          print("2013-14 Denver Nuggets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'DEN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "9":
          print("2013-14 Detroit Pistons")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'DET'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "10":
          print("2013-14 Golden State Warriors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'GSW'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False  
        
        if teamsMenu == "11":
          print("2013-14 Houston Rockets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'HOU'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "12":
          print("2013-14 Indiana Pacers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'IND'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "13":
          print("2013-14 Los Angeles Clippers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'LAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "14":
          print("2013-14 Los Angeles Lakers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'LAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "15":
          print("2013-14 Memphis Grizzlies")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'MEM'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "16":
          print("2013-14 Miami Heat")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'MIA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "17":
          print("2013-14 Milwaukee Bucks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'MIL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "18":
          print("2013-14 Minnesota Timberwolves")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'MIN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "19":
          print("2013-14 New Orleans Pelicans")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'NOP'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "20":
          print("2013-14 New York Knicks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'NYK'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "21":
          print("2013-14 Oklahoma City Thunder")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'OKC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "22":
          print("2013-14 Orlando Magic")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'ORL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "23":
          print("2013-14 Philadelphia 76ers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'PHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "24":
          print("2013-14 Phoenix Suns")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'PHX'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "25":
          print("2013-14 Portland Trail Blazers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'POR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "26":
          print("2013-14 Sacramento Kings")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'SAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "27":
          print("2013-14 San Antonio Spurs")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'SAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "28":
          print("2013-14 Toronto Raptors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'TOR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "29":
          print("2013-14 Utah Jazz")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'UTA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "30":
          print("2013-14 Washington Wizards")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2013-14' AND team = 'WAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False
        
        
      if seasonsMenu == "2":
        print("2014-15")
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2014-15 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n 6) Cleveland Cavaliers \n 7) Dallas Mavericks \n 8) Denver Nuggets \n 9) Detroit Pistons \n 10) Golden State Warriors \n 11) Houston Rockets \n 12) Indiana Pacers \n 13) Los Angeles Clippers \n 14) Los Angeles Lakers \n 15) Memphis Grizzlies \n 16) Miami Heat \n 17) Milwaukee Bucks \n 18) Minnesota Timberwolves \n 19) New Orleans Pelicans \n 20) New York Knicks \n 21) Oklahoma City Thunder \n 22) Orlando Magic \n 23) Philadelphia 76ers \n 24) Phoenix Suns \n 25) Portland Trail Blazers \n 26) Sacramento Kings \n 27) San Antonio Spurs \n 28) Toronto Raptors \n 29) Utah Jazz \n 30) Washington Wizards"))
        
        if teamsMenu == "1":
          print("2014-15 Atlanta Hawks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'ATL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "2":
          print("2014-15 Boston Celtics")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'BOS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False       
           
        elif teamsMenu == "3":
          print("2014-15 Brooklyn (New Jersey) Nets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'BKN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "4":
          print("2014-15 Charlotte Hornets (Bobcats)")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'CHA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))      
          ansTeams = False
          
        elif teamsMenu == "5":
          print("2014-15 Chicago Bulls")  
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'CHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))    
          ansTeams = False
        
        if teamsMenu == "6":
          print("2014-15 Cleveland Cavaliers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'CLE'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "7":
          print("2014-15 Dallas Mavericks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'DAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "8":
          print("2014-15 Denver Nuggets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'DEN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "9":
          print("2014-15 Detroit Pistons")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'DET'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "10":
          print("2014-15 Golden State Warriors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'GSW'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False  
        
        if teamsMenu == "11":
          print("2014-15 Houston Rockets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'HOU'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "12":
          print("2014-15 Indiana Pacers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'IND'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "13":
          print("2014-15 Los Angeles Clippers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'LAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "14":
          print("2014-15 Los Angeles Lakers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'LAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "15":
          print("2014-15 Memphis Grizzlies")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'MEM'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "16":
          print("2014-15 Miami Heat")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'MIA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "17":
          print("2014-15 Milwaukee Bucks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'MIL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "18":
          print("2014-15 Minnesota Timberwolves")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'MIN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "19":
          print("2014-15 New Orleans Pelicans")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'NOP'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "20":
          print("2014-15 New York Knicks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'NYK'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "21":
          print("2014-15 Oklahoma City Thunder")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'OKC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "22":
          print("2014-15 Orlando Magic")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'ORL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "23":
          print("2014-15 Philadelphia 76ers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'PHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "24":
          print("2014-15 Phoenix Suns")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'PHX'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "25":
          print("2014-15 Portland Trail Blazers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'POR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "26":
          print("2014-15 Sacramento Kings")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'SAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "27":
          print("2014-15 San Antonio Spurs")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'SAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "28":
          print("2014-15 Toronto Raptors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'TOR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "29":
          print("2014-15 Utah Jazz")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'UTA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "30":
          print("2014-15 Washington Wizards")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2014-15' AND team = 'WAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False  
        
      if seasonsMenu == "3":
        print("2015-16")
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2015-16 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n 6) Cleveland Cavaliers \n 7) Dallas Mavericks \n 8) Denver Nuggets \n 9) Detroit Pistons \n 10) Golden State Warriors \n 11) Houston Rockets \n 12) Indiana Pacers \n 13) Los Angeles Clippers \n 14) Los Angeles Lakers \n 15) Memphis Grizzlies \n 16) Miami Heat \n 17) Milwaukee Bucks \n 18) Minnesota Timberwolves \n 19) New Orleans Pelicans \n 20) New York Knicks \n 21) Oklahoma City Thunder \n 22) Orlando Magic \n 23) Philadelphia 76ers \n 24) Phoenix Suns \n 25) Portland Trail Blazers \n 26) Sacramento Kings \n 27) San Antonio Spurs \n 28) Toronto Raptors \n 29) Utah Jazz \n 30) Washington Wizards"))
        
        if teamsMenu == "1":
          print("2015-16 Atlanta Hawks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'ATL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "2":
          print("2015-16 Boston Celtics")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'BOS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False       
           
        elif teamsMenu == "3":
          print("2015-16 Brooklyn (New Jersey) Nets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'BKN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "4":
          print("2015-16 Charlotte Hornets (Bobcats)")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'CHA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))      
          ansTeams = False
          
        elif teamsMenu == "5":
          print("2015-16 Chicago Bulls")  
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'CHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))    
          ansTeams = False
        
        if teamsMenu == "6":
          print("2015-16 Cleveland Cavaliers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'CLE'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "7":
          print("2015-16 Dallas Mavericks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'DAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "8":
          print("2015-16 Denver Nuggets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'DEN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "9":
          print("2015-16 Detroit Pistons")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'DET'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "10":
          print("2015-16 Golden State Warriors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'GSW'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False  
        
        if teamsMenu == "11":
          print("2015-16 Houston Rockets")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'HOU'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "12":
          print("2015-16 Indiana Pacers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'IND'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "13":
          print("2015-16 Los Angeles Clippers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'LAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "14":
          print("2015-16 Los Angeles Lakers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'LAL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "15":
          print("2015-16 Memphis Grizzlies")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'MEM'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "16":
          print("2015-16 Miami Heat")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'MIA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "17":
          print("2015-16 Milwaukee Bucks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'MIL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "18":
          print("2015-16 Minnesota Timberwolves")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'MIN'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "19":
          print("2015-16 New Orleans Pelicans")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'NOP'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "20":
          print("2015-16 New York Knicks")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'NYK'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "21":
          print("2015-16 Oklahoma City Thunder")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'OKC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "22":
          print("2015-16 Orlando Magic")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'ORL'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "23":
          print("2015-16 Philadelphia 76ers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'PHI'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "24":
          print("2015-16 Phoenix Suns")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'PHX'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "25":
          print("2015-16 Portland Trail Blazers")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'POR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "26":
          print("2015-16 Sacramento Kings")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'SAC'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "27":
          print("2015-16 San Antonio Spurs")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'SAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "28":
          print("2015-16 Toronto Raptors")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'TOR'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
        
        if teamsMenu == "29":
          print("2015-16 Utah Jazz")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'UTA'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        if teamsMenu == "30":
          print("2015-16 Washington Wizards")
          cur.execute("SELECT lname, fname, PPG, APG, RPG, SPG, BPG, TOs, min_per_game FROM Player_Stats WHERE season = '2015-16' AND team = 'WAS'")
          cur.connection.commit()
          result = cur.fetchall()
          # next two lines make tuples of tuples into lists of lists
          result = list(result)
          resultList = [list(elem) for elem in result]
          #header
          print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
          print("----------------------------------------------------------------------------------")
          # table items
          for row in resultList:
            last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])
            print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
          ansTeams = False
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False
      
      elif seasonsMenu == "":
        print("Please Choose a Valid Season \n")
        
    ans = False       
  
  elif mainMenu == "5":
    print("Shoe Endorsements")
    
    ## Shoes Menu
    ###############
    ansShoe = True
    while ansShoe:
      shoeMenu = str(input("Choose one of the following shoe brands: \n 1) Nike \n 2) Jordan \n 3) Adidas \n 4) Under Armour \n 5) K1X \n 6) Li-Ning \n 7) Brandblack \n 8) Reebok \n 9) Anta \n 10) And1 \n 11) Peak \n 12) Spalding \n"))
    
      if shoeMenu == "1":
        print("Nike")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'nike'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "2":
        print("Jordan")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'jordan'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "3":
        print("Adidas")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'adidas'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "4":
        print("Under Armour")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'under-armour'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "5":
        print("K1X")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'K1X'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20)) 
        ansShoe = False
      elif shoeMenu == "6":
        print("Li-Ning")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'li-ning'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "7":
        print("Brandblack")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'brandblack'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "8":
        print("Reebok")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'reebok'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "9":
        print("Anta")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'anta'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "10":
        print("And1")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'and1'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "11":
        print("Peak")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'peak'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "12":
        print("Spadling")
        cur.execute("SELECT lname, fname, shoe_model FROM Shoe_Endorsement WHERE shoe_brand = 'spalding'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("lname".ljust(20) + "fname".ljust(20) + "shoe_model".ljust(20))
        print("---------------------------------------------------------------------------")
        for row in resultList:
          last, first, model = str(row[0]), str(row[1]), str(row[2])
          print(last.ljust(20) + first.ljust(20) + model.ljust(20))
        ansShoe = False
      elif shoeMenu == "":
        print("Please choose a valid shoe brand \n")
        
    ans = False
   
 
 
  elif mainMenu =="6":
    print("Basketball Stats")
    
    ## Basketball Stats Menu
    ########################
    ansStats = True
    while ansStats:
      print("This search will find specified player(s) with at least a specified PPG, APG, RPG, SPG, and/or RPG at a certain minimum salary. \nCan input '0' to specify any amount for that specific stat. \n")
      season = str(input("Which season (2013-14, 2014-15, 2015-16): "))
      points = str(input("PPG Greater Than or Equal To: "))
      assists = str(input("APG Greater Than or Equal To: "))
      rebounds = str(input("RPG Greater Than or Equal To: "))
      steals = str(input("SPG Greater Than or Equal To: "))
      blocks = str(input("BPG Greater Than or Equal To: "))
      three = str(input("3PM Greater Than or Equal To: "))
      sal = str(input("Minimum Salary: "))
      cur.execute("SELECT ps.lname, ps.fname, ps.season, ps.PPG, ps.APG, ps.RPG, ps.SPG, ps.BPG, ps.3PM, s.salary FROM Player_Stats ps INNER JOIN Player_Bio_Info pb USING (player_id) INNER JOIN Salary s USING (player_id) WHERE ps.PPG >= " + points + " AND ps.APG >= " + assists + " AND ps.RPG >= " + rebounds + " AND ps.SPG >= " + steals + " AND ps.BPG >= " + blocks + " AND s.salary >= " + sal + " AND ps.season = '" + season + "' AND s.season = '" + season + "' AND ps.3PM >= '" + three + "'")
      cur.connection.commit()
      result = cur.fetchall()
      result = list(result)
      resultList = [list(elem) for elem in result]
      print("lname".ljust(20) + "fname".ljust(20) + "season".ljust(20) + "PPG".ljust(20) + "APG".ljust(20) + "RPG".ljust(20) + "SPG".ljust(20) + "BPG".ljust(20) + "3PM".ljust(20) + "salary".ljust(20))
      print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      for row in resultList:
        #print(row)
        last, first, yr, ppg, apg, rpg, spg, bpg, thr, s = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9])
        print(last.ljust(20) + first.ljust(20) + yr.ljust(20) + ppg.ljust(20) + apg.ljust(20) + rpg.ljust(20) + spg.ljust(20) + bpg.ljust(20) + thr.ljust(20) + s.ljust(20))
      
      ansStats = False  
    ans = False
      
      
  elif mainMenu == "7":
    print("Player Analysis")
    
    ## Player Analysis
    ##################
    print("This menu will allow the user to input a number that will search the top X number of players based upon Team CT's algorithm. \n")
    
    ansAnalysis = True
    while ansAnalysis:
      seasonsMenu = str(input("Select the number of a season: \n 1) 2013-14 \n 2) 2014-15 \n 3) 2015-16 \n"))
      
      if seasonsMenu == "1":
        print("2013-14 Top Players")
        qty = str(input("How many records would you like the query to return: "))
        cur.execute("select lname, fname, season, team, (PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48 as GRADE from player_stats WHERE season = '2013-14' order by GRADE desc limit " + qty + "")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "season".ljust(20) + "team".ljust(20) + "GRADE".ljust(20))
        print("-----------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, seas, team, grade = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])
          print(last.ljust(20) + first.ljust(20) + seas.ljust(20) + team.ljust(20) + grade.ljust(20))
      
        # average grade for season
        cur.execute("select season, avg((PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48) as AVG_GRADE from player_stats where season = '2013-14'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("\n")
        print("season".ljust(20) + "grade".ljust(20))
        print("--------------------------------------------")
        for row in resultList:
          seas, grade = str(row[0]), str(row[1])
          print(seas.ljust(20) + grade.ljust(20))
        ansAnalysis = False
      
      elif seasonsMenu == "2":
        print("2014-15 Top Players")
        qty = str(input("How many records would you like the query to return: "))
        cur.execute("select lname, fname, season, team, (PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48 as GRADE from player_stats WHERE season = '2014-15' order by GRADE desc limit " + qty + "")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "season".ljust(20) + "team".ljust(20) + "GRADE".ljust(20))
        print("-----------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, seas, team, grade = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])
          print(last.ljust(20) + first.ljust(20) + seas.ljust(20) + team.ljust(20) + grade.ljust(20))
          
        # average grade for season
        cur.execute("select season, avg((PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48) as AVG_GRADE from player_stats where season = '2014-15'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("\n")
        print("season".ljust(20) + "grade".ljust(20))
        print("--------------------------------------------")
        for row in resultList:
          seas, grade = str(row[0]), str(row[1])
          print(seas.ljust(20) + grade.ljust(20))
          
        ansAnalysis = False
      
      elif seasonsMenu == "3":
        print("2015-16 Top Players")
        qty = str(input("How many records would you like the query to return: "))
        cur.execute("select lname, fname, season, team, (PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48 as GRADE from player_stats WHERE season = '2015-16' order by GRADE desc limit " + qty + "")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "season".ljust(20) + "team".ljust(20) + "GRADE".ljust(20))
        print("-----------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, seas, team, grade = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])
          print(last.ljust(20) + first.ljust(20) + seas.ljust(20) + team.ljust(20) + grade.ljust(20))
          
        # average grade for season
        cur.execute("select season, avg((PPG + APG + RPG + 2*SPG + 2*BPG - 2*TOs + 2.5*3PM + 0.33*FTM)*min_per_game/48) as AVG_GRADE from player_stats where season = '2015-16'")
        cur.connection.commit()
        result = cur.fetchall()
        result = list(result)
        resultList = [list(elem) for elem in result]
        print("\n")
        print("season".ljust(20) + "grade".ljust(20))
        print("--------------------------------------------")
        for row in resultList:
          seas, grade = str(row[0]), str(row[1])
          print(seas.ljust(20) + grade.ljust(20))
          
        ansAnalysis = False
        
      elif seasonsMenu == "":
        print("Please Choose a Valid Season \n")  
  
    ans = False
      
  elif mainMenu == "":
    print("Please Choose a Valid Menu Option \n")
    
    
    

 
  
cur.close()
conn.close()