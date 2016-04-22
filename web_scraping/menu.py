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
  mainMenu = str(input("Choose one of the following menu options(#): \n 1) Colleges \n 2) Salaries \n 3) Player Lookup \n 4) Teams \n"))

  if mainMenu == "1":
    print("College")
    # INSERT collegeMenu code here
    
    # College Menu
    ##############
    ansCollege = True
    while ansCollege:
      collegeMenu = str(input("Choose one of the following numbers to select all NBA players from that college: \n 1) Texas \n 2) Duke \n 3) North Carolina \n 4) Kansas \n 5) Kentucky \n"))

      if collegeMenu == "1":
        print("Texas")
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = 'Texas'")
        cur.connection.commit()
        result = cur.fetchall()
        # next two lines make tuples of tuples into lists of lists
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
      elif collegeMenu == "2":
        print("Duke")
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = 'Duke'")
        cur.connection.commit()
        result = cur.fetchall()
        # next two lines make tuples of tuples into lists of lists
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
      elif collegeMenu == "3":
        print("North Carolina")
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = 'North Carolina'")
        cur.connection.commit()
        result = cur.fetchall()
        # next two lines make tuples of tuples into lists of lists
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
      elif collegeMenu == "4":
        print("Kansas")
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = 'Kansas'")
        cur.connection.commit()
        result = cur.fetchall()
        # next two lines make tuples of tuples into lists of lists
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "position".ljust(20) + "height".ljust(20) + "weight".ljust(20) + "DOB".ljust(20))
        print("-----------------------------------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, pos, ht, wt, birth = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])
          print(last.ljust(20) + first.ljust(20) + pos.ljust(20) + ht.ljust(20) + wt.ljust(20) + birth.ljust(20))
        ansCollege = False
      elif collegeMenu == "5":
        print("Kentucky")
        cur.execute("SELECT lname, fname, position, height, weight, DOB FROM Player_Bio_Info WHERE college = 'Kentucky'")
        cur.connection.commit()
        result = cur.fetchall()
        # next two lines make tuples of tuples into lists of lists
        result = list(result)
        resultList = [list(elem) for elem in result]
        #header
        print("lname".ljust(20) + "fname".ljust(20) + "position".ljust(20) + "height".ljust(20) + "weight".ljust(20) + "DOB".ljust(20))
        print("-----------------------------------------------------------------------------------------------------------------")
        # table items
        for row in resultList:
          last, first, pos, ht, wt, birth = str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])
          print(last.ljust(20) + first.ljust(20) + pos.ljust(20) + ht.ljust(20) + wt.ljust(20) + birth.ljust(20))
        ansCollege = False
      elif collegeMenu != "":  
        print("Not Valid Choice, Please Try Again \n")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 10000000 AND salary <= 20000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 5000000 AND salary <= 10000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 1000000 AND salary <= 5000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND salary <= 1000000")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary > 10000000 AND salary <= 20000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary > 5000000 AND salary <= 10000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND (salary > 1000000 AND salary <= 5000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2014-15' AND salary <= 1000000")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary > 10000000 AND salary <= 20000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary > 5000000 AND salary <= 10000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND (salary > 1000000 AND salary <= 5000000)")
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
          cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2015-16' AND salary <= 1000000")
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
      years = str(input("Which season: "))  
      query = "SELECT * FROM Player_Stats WHERE lname = '" + lastName + "' AND fname = '" + firstName + "' AND season = '" + years + "'"
      cur.execute(query)
      cur.connection.commit()
      result = cur.fetchone()
      row = list(result)
      #header
      print("lname".ljust(20) + "fname".ljust(20) + "PPG".ljust(5) + "APG".ljust(5) + "RPG".ljust(5) + "SPG".ljust(5) + "BPG".ljust(5) + "TOs".ljust(5) + "min_per_game".ljust(5))
      print("----------------------------------------------------------------------------------")
      #table row
      last, first, ppg, apg, rpg, spg, bpg, to, minutes = str(row[1]), str(row[2]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[-2])
      print(last.ljust(20) + first.ljust(20) + ppg.ljust(5) + apg.ljust(5) + rpg.ljust(5) + spg.ljust(5) + bpg.ljust(5) + to.ljust(5) + minutes.ljust(5))
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
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2013-14 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n"))
        
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
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False
        
      elif seasonsMenu == "2":
        print("2014-15")
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2013-14 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n"))
        
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
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False
        
      elif seasonsMenu == "3":
        print("2015-16")
        teamsMenu = str(input("Select the number of the team you wish to see all its players for the 2013-14 season: \n 1) Atlanta Hawks \n 2) Boston Celtics \n 3) Brooklyn (New Jersey) Nets \n 4) Charlotte Hornets (Bobcats) \n 5) Chicago Bulls \n"))
        
        if teamsMenu == "1":
          print("2015-16Atlanta Hawks")
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
          
        elif teamsMenu == "":
          print("Please choose an NBA team \n")  
        ansTeams = False
        
      elif seasonsMenu == "":
        print("Please Choose a Valid Season \n")
        
    ans = False       
  
  elif mainMenu == "":
    print("Please Choose a Valid Menu Option \n")
   
  
cur.close()
conn.close()