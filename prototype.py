

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
        print("3.Offroad")
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
