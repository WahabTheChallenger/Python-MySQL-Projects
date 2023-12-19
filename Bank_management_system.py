import mysql.connector as mc

mydb = mc.connect(
  host="localhost",
  user="root",
  password="something88",
  database="Bank"
)

def openAccount():
  n = input("Entre name:- ")
  ac = input("Entre account number:- ")
  dob = input("Entre dat of birth:- ")
  ad = input("Entre adress:- ")
  p  = input("Entre phone number:- ")
  ob = int(input("Entre opening balance:- "))
  data1 = (n,ac,dob,ad,p,ob)
  data2 = (n,ac,ob)
  sql1 = "insert into account values(%s,%s,%s,%s,%s,%s)"
  sql2 = "insert into ammount values(%s,%s,%s)"
  c = mydb.cursor()
  c.execute(sql1,data1)
  c.execute(sql2,data2)
  mydb.commit()
  print('\nData Entered Successfully')
  print('---------------------')
  main()
  
def depoAmmount():
  amount = int(input("Entre ammount:- ")) 
  account = input("Entre account number:- ")
  a = "select balance from ammount where acno = %s"
  data = (account,)
  c = mydb.cursor() 
  c.execute(a,data)
  myresult = c.fetchone()
  tom = myresult[0]+ammount
  sql = "update ammount set balance = %s where acno = %s"
  d = (tom,account)
  c.execute(sql,d)
  mydb.commit()
  main()

def withAmmount():
  amount = int(input("Entre ammount:- ")) 
  account = input(input("Entre account number:- "))
  a = "select balance from ammount where acno = %s"
  data = (account,)
  c = mydb.cursor() 
  c.execute(a,data)
  myresult = c.fetchone()
  tom = myresult[0]-ammount
  sql = "update ammount set balance = %s where acno = %s"
  d = (tom,account)
  c.execute(sql,d)
  mydb.commit()
  main()

def displaybalance():
  account = input("Entre Account number:- ")
  a = "select balance from ammount where acno = %s"
  data = (account,)
  c = mydb.cursor()
  c.execute(a,data)
  myresult = c.fetchone()
  print("\nBalance for account : ", account ," is ",myresult[0])
  print('---------------------')
  main()

def displayDetails():
  account = input("Entre account no:- ")
  a = "select * from account where acno = %s"
  data = (account,)
  c = mydb.cursor()
  c.execute(a,data)
  myresult = c.fetchone()
  for i in myresult:
    print('\n',i,end=' ')
    print('---------------------')
  # print(myresult)
  main()

def closeAccount():
  account = input("Entre account no:- ")
  sql1 = " delete from account where acno = %s"
  sql2 = " delete from ammount where acno = %s"
  data = (account,)
  c = mydb.cursor()
  c.execute(sql1,data)
  c.execute(sql2,data)
  mydb.commit()
  print('Data Deleted Successfully')
  main()

def main():
  print('''
  \n  OPEN NEW ACCOUNT          (PRESS 1)
  DEPOSIT AMOUNT            (PRESS 2)
  WITHDRAW AMOUNT           (PRESS 3)
  CHECK TOTAL BALANCE       (PRESS 4)
  DISPLAY ACCOUNT DETAILS   (PRESS 5)
  CLOSE AN ACCOUNT          (PRESS 6)
  ''')
  choice = input("Entre Task No:- ")
  if choice == '1':
    openAccount()
  elif choice =='2':
    depoAmmount()
  elif choice =='3':
    withAmmount()
  elif choice == '4':
    displaybalance()
  elif choice == '5':
    displayDetails()
  elif choice == '6':
    closeAccount()
  else:
    print('You press the wrong number..............')
    main()

def password():
  x = input('Entre the password:- ')
  if x == 'BMS':
    main()
  else:
    print('Wrong password')
    password()
  
password()

