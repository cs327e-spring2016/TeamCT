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
  mainMenu = str(input("Choose one of the following menu options(#): \n 1) Colleges \n 2) Salaries \n 3) Player Lookup\n")

  if mainMenu == "1":
    print("College")
    # INSERT collegeMenu code here
  elif mainMenu == "2":
    print("Salaries")
    # INSERT salaryMenu code here
  elif mainMenu == "3":
    print("Player Lookup")
    # INSERT lookupMenu code here
  elif mainMenu == "":
    print("Please Choose a Valid Menu Option")



'''
# College Menu
##############
ansCollege = True
while ansCollege:
  collegeMenu = str(input("Choose one of the following numbers to select all NBA players from that college: \n 1) Texas \n 2) Duke \n 3) UNC \n 4) Kansas \n 5) UCLA \n"))

  if collegeMenu == "1":
    print("Texas")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Texas";
    cur.connection.commit()
    ansCollege = False
  elif collegeMenu == "2":
    print("Duke")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Duke";
    cur.connection.commit()
    ansCollege = False
  elif collegeMenu == "3":
    print("UNC")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "UNC";
    cur.connection.commit()
    ans = False
  elif collegeMenu == "4":
    print("Kansas")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Kansas";
    cur.connection.commit()
    ansCollege = False
  elif collegeMenu == "5":
    print("UCLA")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "UCLA";
    cur.connection.commit()
    ansCollege = False
  elif collegeMenu != "":  
    print("Not Valid Choice, Please Try Again")
'''  
# Salary Menu
#################
ansSalary = True
while ansSalary:
  salaryMenu = str(input("Choose one of the following numbers to select all NBA players making salary in that range during the 2013-14 season: \n 1) More than $20M \n 2) Between $10M and $20M \n 3) Between $5M and $10M \n 4) Between $1M and $5M \n 5) Less than $1M \n"))

  if salaryMenu == "1":
    print("More Than $20M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE salary > 20000000")
    cur.connection.commit()
    result = cur.fetchall()
    
    '''
    x = PrettyTable(["lname", "fname", "salary"])
    x.set_padding_width(1) # One space between column edges and contents (default) 
    for item in result:
      x.add_row(list(item))
    print(x)
    '''
    
    ansSalary = False
  elif salaryMenu == "2":
    print("Between $10M and $20M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 10000000 AND salary <= 20000000)")
    cur.connection.commit()
    ansSalary = False
  elif salaryMenu == "3":
    print("Between $5M and $10M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 5000000 AND salary <= 10000000)")
    cur.connection.commit()
    ansSalary = False
  elif salaryMenu == "4":
    print("Between $1M and $5M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND (salary > 1000000 AND salary <= 5000000)")
    cur.connection.commit()
    ansSalary = False
  elif salaryMenu == "5":
    print("Less than $1M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season = '2013-14' AND  salary <= 1000000)")
    cur.connection.commit()
    ansSalary = False
  elif salaryMenu != "":  
    print("Not Valid Choice, Please Try Again")

# Player Lookup Menu
##############
ansLookup = True
while ansLookup:
  print("This lookup will find the basketball stats of a desired player in a specific season.")
  lastName = str(input("Last Name: ")
  firstName = str(input("First Name: ")
  years = str(input("Which season: ")  
  
  #....
  #....
  
cur.close()
conn.close()