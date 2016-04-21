import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup

### DONT FORGET TO CHANGE PASSWORD ###
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyz', db='mysql')
cur = conn.cursor()
cur.execute("USE TeamCT")

'''
ans = True
while ans:
  collegeMenu = str(input("Choose one of the following numbers to select all NBA players from that college: \n 1) Texas \n 2) Duke \n 3) UNC \n 4) Kansas \n 5) UCLA \n"))

  if collegeMenu == "1":
    print("Texas")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Texas";
    cur.connection.commit()
    ans = False
  elif collegeMenu == "2":
    print("Duke")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Duke";
    cur.connection.commit()
    ans = False
  elif collegeMenu == "3":
    print("UNC")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "UNC";
    cur.connection.commit()
    ans = False
  elif collegeMenu == "4":
    print("Kansas")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "Kansas";
    cur.connection.commit()
    ans = False
  elif collegeMenu == "5":
    print("UCLA")
    cur.execute("SELECT * FROM Player_Bio_Info WHERE college = "UCLA";
    cur.connection.commit()
    ans = False
  elif collegeMenu != "":  
    print("Not Valid Choice, Please Try Again")
'''  
ans = True
while ans:
  salaryMenu = str(input("Choose one of the following numbers to select all NBA players making salary in that range during the 2013-14 season: \n 1) More than $20M \n 2) Between $10M and $20M \n 3) Between $5M and $10M \n 4) Between $1M and $5M \n 5) Less than $1M \n"))

  if salaryMenu == "1":
    print("More Than $20M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE salary > 20000000")
    cur.connection.commit()
    print(cur.fetchall())
    ans = False
  elif salaryMenu == "2":
    print("Between $10M and $20M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season_id = '2013-14' AND (salary > 10000000 AND salary <= 20000000)")
    cur.connection.commit()
    ans = False
  elif salaryMenu == "3":
    print("Between $5M and $10M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season_id = '2013-14' AND (salary > 5000000 AND salary <= 10000000)")
    cur.connection.commit()
    ans = False
  elif salaryMenu == "4":
    print("Between $1M and $5M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season_id = '2013-14' AND (salary > 1000000 AND salary <= 5000000)")
    cur.connection.commit()
    ans = False
  elif salaryMenu == "5":
    print("Less than $1M")
    cur.execute("SELECT lname, fname, salary FROM Salary WHERE season_id = '2013-14' AND  salary <= 1000000)")
    cur.connection.commit()
    ans = False
  elif collegeMenu != "":  
    print("Not Valid Choice, Please Try Again")


cur.close()
conn.close()