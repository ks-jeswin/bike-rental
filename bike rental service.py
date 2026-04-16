#Making a table for bikes and their availability
import mysql.connector
import random
mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='BikeRentalService')
cur=mydb.cursor()
cur.execute("create table if not exists Bike (B_no int(3)primary key,Bike varchar(50),Class varchar(50),Cost_per_hr int(5),Availability varchar(50));")
cur.execute("create table if not exists Customer (C_no int(3)primary key,Name varchar(50),Hour int(5),Total_Cost int(10));")            
a1="insert into bike values(%s,%s,%s,%s,%s)"
T1list=[(11,'Harley Davidson Street 750','Cruiser',random.randrange(500,1000,100),'AVAILABLE'),
        (22,'Triumph StreetMaster','Cruiser',random.randrange(500,1000,100),'AVAILABLE'),
        (33,'BMW S1000R','Sports',random.randrange(500,1000,100),'AVAILABLE'),
        (44,'Triumph ThunderBird','Cruiser',random.randrange(500,1000,100),'AVAILABLE'),
        (55,'Kawasaki Ninja Zx14R','Sports',random.randrange(500,1000,100),'AVAILABLE'),
        (66,'Ducati Multistrada','Offroad',random.randrange(500,1000,100),'AVAILABLE'),
        (77,'KTM RC390','Sports',random.randrange(500,1000,100),'AVAILABLE'),
        (88,'Yamaha Tracer 900','Offroad',random.randrange(500,1000,100),'AVAILABLE'),
        (99,'RE Himalayan','Offroad',random.randrange(500,1000,100),'AVAILABLE'),]
cur.executemany(a1,T1list)
mydb.commit()

#Starting Main Menu


def menu():
    c='y'
    while c=='y':
        print("\n1. Show Bikes")
        print("2. Rent a Bike")
        print('3. EXIT')
        choice=int(input('\nEnter your choice:'))
        if choice==1:
            show_menu()
            break
        elif choice==2:
            rent()
        elif choice==3:
            print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
            break
        else:
            print('\nERROR:wrong input')
            c=input("\nPRESS 'y' TO CONTINUE:")
            if c!='y':
                print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')


#Show bikes Menu

                
def show_menu():
    c1='y'
    while c1=='y':
        print("\n\n1.Show All Details")
        print("2.Show Available Bikes")
        print("3.Show Bike Types")
        print("4.RETURN")
        b=int(input("\nEnter your choice:"))
        if b==1:
            allbikes()
            c1=input("\npress 'y' to continue:")
            if c1!='y':
                return menu()
        elif b==2:
            availablebikes()
            c1=input("\npress 'y' to continue:")
            if c1!='y':
                return menu()
        elif b==3:
            typebikes()
            c1=input("\npress 'y' to continue:")####
            if c1!='y':
                return menu()
        elif b==4:
            return menu()
        else:
            print('\nERROR:wrong input')
            c1=input("\npress 'y' to continue:")
            if c1!='y':
                print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
        
    
def allbikes():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='bikerentalservice')
        cur=mydb.cursor()
        a='select * from bike;'
        cur.execute(a)
        result=cur.fetchall()
        for i in result:
            print(i)
    except:
        print('ERROR:unexpected error found')


def availablebikes():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='bikerentalservice')
        cur=mydb.cursor()
        a='select * from bike where availability="available";'
        cur.execute(a)
        result=cur.fetchall()
        for i in result:
            print(i)
    except:
        print('ERROR:unexpected error found')


def typebikes():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='bikerentalservice')
    cur=mydb.cursor()
    c2='y'
    while c2=='y':
        print("\n1.Sports")
        print("2.Cruiser")
        print("3.ADV")
        print('4.RETURN')
        b1=int(input('\nEnter your choice:'))
        if b1==1:
            try:    
                a='select * from bike where class="Sports";'
                cur.execute(a)
                result=cur.fetchall()
                for i in result:
                    print(i)
            except:
                print('ERROR:unexpected error found')
        elif b1==2:
            try:    
                a='select * from bike where class="Cruiser";'
                cur.execute(a)
                result=cur.fetchall()
                for i in result:
                    print(i)
            except:
                print('ERROR:unexpected error found')
        elif b1==3:
            try:    
                a='select * from bike where class="Offroad";'
                cur.execute(a)
                result=cur.fetchall()
                for i in result:
                    print(i)
            except:
                print('ERROR:unexpected error found')
        elif b1==4:
            return menu()
        else:
            print('ERROR:wrong input')
            c2=input("press 'y' to continue:")
            if c2!='y':
                print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
        cont=input("\npress 'y' to continue:")
        if cont!='y':
            return menu()


menu()
