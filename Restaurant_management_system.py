# CONNECT DATABASE

import mysql.connector as a
# passwd = str(input('Entre Database password: '))
con = a.connect(host="localhost",user="root",password='something88')


# SELECT OR CREATE DATABASE

c = con.cursor()
c.execute('show databases')
dl = c.fetchall()
dl2 = []
for i in dl:
    dl2.append(i[0])
if 'restaurants' in dl2:
    c.execute('use restaurants')
else:
    c.execute('create database restaurants')
    c.execute('use restaurants')
    c.execute('create table Dish (Dish varchar(30), Cost integer, Cook varchar(50), DishID varchar(20))')
    c.execute('create table Orders (DishIDs varchar(100), Cost integer, Date varchar(20), Customer varchar(50), UID varchar(20))')
    c.execute('create table Cook (Name varchar(50), UID varchar(20), Dishes varchar(100), Salary integer, DOJ varchar(20))')
    c.execute('create table Salary (Name varchar(50), UID varchar(20), Bank varchar(20), Month varchar(20), Salary integer, Days integer, Net integer)')
    c.execute('create table Expenditure (Type varchar(100), Cost integer, Date varchar(20))')
    con.commit()

# SYSTEM PASSWORD LOGIN

def signin():
    print('\n')
    print('--------->>>>>>Welcome to our restaurant<<<<<<----------')
    print('\n')
    p = input('System Password: ')
    if p == 'welcome':
        options()
    else:
        signin()

# DISPLAY OPTIONS

def options():
    print("""
            1. Dishes
            2. Cooks
            3. Salary
            4. Order
            5. Income
            6. Bills
    """)
    choice = input("Select Option: ")
    if choice == '1':
        Dish()
    elif choice == '2':
        Cook()
    elif choice == '3':
        PaySalary()
    elif choice == '4':
        NewOrder()
    elif choice == '5':
        NetIncome()
    elif choice == '6':
        Expenditure()
    else:
        print('Wrong Choice')
        options()

def Dish():
    choice = input("1. Add 2. Remove 3. Display 4. Main Menu\n")
    if choice == '1':
        dn = input("Dish Name : ")
        dc = input("Dish Cost : ")
        Cname()
        cb = input("Cooked By : ")
        did = str(DishID())
        data = (dn,dc,cb,did)
        sql = 'insert into Dish values(%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print('Data Entered Successfully')
    elif choice == '2':
        did = input('Dish ID :')
        data = (did,)
        sql = 'delete from Dish where DishID = %s'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print('Data Updated Successfully')
    elif choice == '3':
        print("\n")
        sql = 'select * from Dish'
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            txt = i[0]
            capi = i[2]
            u = txt.upper()
            ca = capi.capitalize()
            print(f'({i[3]})  {u} - {i[1]}Rs  ({ca})')
        print("\n")
    else:
        options()
    options()




def Cname():
    sql = "select Name , Dishes from Cook"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("--------->>>>>>Available Cooks<<<<<<----------")
    for i in d:
        print(i[0],'---',i[1])
    return




def DishID():
    sql = "select count(*), max(dishid) from dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        if i[0] == 0:
            return(1)
        else:
            return(int(i[1])+1)



def Cook():
    choice = input("1. Add 2. Remove 3. Display 4. Main Menu")
    if choice == "1":
        cn = input("Cook Name : ")
        ci = input("id : ")
        d = input("Dishes : ")
        s = int(input("Salary : "))
        doj = input('Date of joining : Y/M/D : ')
        data = (cn,ci,d,s,doj)
        sql = 'insert into Cook values(%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print('Data Entered Succesfully : ')
    elif choice == '2':
        cn = input('Cook name : ')
        ci = input('Cook ID : ')
        data = (cn,ci)
        sql = 'delete from Cook where Name = %s and UID = %s'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print('Data Updated Successfully')
    elif choice == '3':
        print("\n")
        sql = 'select * from Cook'
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            txt = i[0]
            capi = i[2]
            u = txt.upper()
            ca = capi.capitalize()
            print(f'{u} - {i[1]}  ({ca}) ({i[3]}Rs) {i[4]}')
        print("\n")
    else:
        options()
    options()



def PaySalary():
    sql = "select * from cook"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        txt = i[0]
        capi = i[2]
        u = txt.upper()
        ca = capi.capitalize()
        print(f'{u} - {i[1]}  ({ca}) ({i[3]}Rs) {i[4]}')
        print('---------------------------------------')
    cn = input('Cook name : ')
    ci = input('Cook ID : ')
    ba = input('Bank Account : ')
    mn = input('DATE : Y/M/D : ')
    s = int(input("Salary : "))
    d = int(input("Working days : "))
    if mn[5:7] in ['01','03','05','07','08','10','12']:
        ns = (s/31)*d
    elif mn[5:7] in ['04','06','09','11']:
        ns = (s/30)*d
    else:
        ns = (s/28)*d
    data = (cn,ci,ba,mn,s,d,ns)
    sql = "insert into Salary values(%s,%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Net Salary Paid : ",ns," Rs")
    print('---------------------------------------')
    xy = input("1. Return to Salary      2 Main Menu    : ")
    print('---------------------------------------')
    if xy == '1':
        PaySalary()
    elif xy == '2':
        options()
    else:
        options()

def NewOrder():
    sql = 'select * from Dish'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("NAME ----- COST ----- COOK ----- DISH ID")
    for i in d:
        txt = i[0]
        capi = i[2]
        u = txt.upper()
        ca = capi.capitalize()
        print(f'({i[3]})  {u} - {i[1]}Rs  ({ca})')
    print("\n")
    dil = []
    while True:
        di = input('Select Dish ID { 0 When Done } : ')
        if di == '0':
            break
        else:
            dil.append(di)
    sql = 'select DishID, Cost from Dish'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    dicl = {}
    for i in d:
        dicl[i[0]] = i[1]
    tc = 0
    for i in dil:
        dc = dicl[i]
        tc = tc + dc
    dt = input('Date " Y/M/D : ')
    cn = input('Customer Name : ')
    ca = input('ID : ')
    lis = input('Enter Dish IDs : ')
    data = (lis,tc,dt,cn,ca)
    sql = 'insert into Orders values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    print("Total Amount : ",tc, " Rs")
    print("Data Entered Successfully")
    print('--------------------------------------------')
    xy = input("1. Return to Order      2 Main Menu    : ")
    print('---------------------------------------')
    if xy == '1':
        NewOrder()
    elif xy == '2':
        options()
    else:
        options()
    options()


def NetIncome():
    c = con.cursor()
    t = input('1.All    2.Year    3.Month    4.Date    5.Main Menu : ')
    if t == '1':
        sql = "select Cost from Orders"
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            oi += i[0]
        print(f"Total income from orders {oi}Rs")
    elif t == 2:
        y = input("Entre Year : " )
        sql = "select Cost, Date from Orders"
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            if y in i[1]:
                 oi += i[0]
        print(f"Total income from orders {oi}Rs")
    elif t == 3:
        m = input("Entre YEAR/MONTH no: " )
        sql = "select Cost, Date from Orders"
        c.execute(sql)
        d = c.fetchall()
        oi = 0
        for i in d:
            if m in i[1]:
                 oi += i[0]
        print(f"Total income from orders {oi}Rs")
    elif t == 4:
        date = input("Entre YEAR/MONTH/DAY no: " )
        sql = "select Cost from Orders where Date = '%s"
        data = (date,)
        c.execute(sql,data)
        d = c.fetchall()
        oi = 0
        for i in d:
            oi += i[0]
        print(f"Total income from orders {oi}Rs")
    else:
        options()


def Expenditure():
    choice = input('1.Bill Entry    2.Show Bills    3.Main Menu : ')
    if choice == '1':
        t = input('Type : ')
        c = int(input('Cost : '))
        d = input('Date Y/M/D : ')
        data = (t,c,d)
        sql = 'insert into Expenditure values(%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print('Data entered Successfully')
        options()
    elif choice == '2':
        c = con.cursor()
        t = input('1.All    2.Year    3.Month    4.Date    5.Main Menu : ')
        if t == '1':
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i)
        elif t == 2:
            y = input("Entre Year : " )
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == 3:
            m = input("Entre YEAR/MONTH no: " )
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if m in i[2]:
                    print(i)
        elif t == 4:
            date = input("Entre YEAR/MONTH/DAY no: " )
            sql = "select * from Expenditure"
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if date in i[2]:
                    print(i)
        else:
            options()

options()