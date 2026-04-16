def rent():
    try:
        name=input('\nEnter your name:')
        c2='y'
        while c2=='y':
            import mysql.connector
            mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='bikerentalservice')
            cur=mydb.cursor()
            print('\n1.Rent a bike using Bike no:')
            print('2.Rent a bike using Name:')
            print('3.Return')
            q=int(input('\nEnter your choice:'))
            
            
            if q==1:  #1
                q1=int(input('\nEnter Bike no:'))
                hr=int(input('\nFor how many hours do you want to rent your bike:'))
                a='select * from bike where B_no=%s'
                search=(q1,)
                cur.execute(a,search)
                count=0
                for (B_no,Bike,Class,Cost_per_hr,Availability) in cur:
                    print('\n\nBIKE FOUND')
                    print('\nBike No     :\t',B_no)
                    print('Bike        :\t',Bike)
                    print('Class       :\t',Class)
                    print('Availability:\t',Availability)
                    print('Total Cost  :\t rs',Cost_per_hr*hr)
                    count+=1
                    c2=input("\npress 'y' to continue:")
                    if c2!='y':
                        print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
                if count==0:
                    print('\nBike No. not found')
                    c2=input("\npress 'y' to continue:")
                    if c2!='y':
                        print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
            elif q==2:#2
                hr=int(input('\nFor how many hours do you want to rent your bike:'))
                q1=int(input('\nEnter Bike Name:'))
                a='select * from bike where Bike=q1'
                
                cur.execute(a)
                count=0
                for (B_no,Bike,Class,Cost_per_hr,Availability) in cur:
                    print('\n\nBIKE FOUND')
                    print('\nBike No     :\t',B_no)
                    print('Bike        :\t',Bike)
                    print('Class       :\t',Class)
                    print('Availability:\t',Availability)
                    print('Total Cost  :\t rs',Cost_per_hr*hr)
                    count+=1
                    c2=input("\npress 'y' to continue:")
                    if c2!='y':
                        print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
                if count==0:
                    print('\nBike not found')
                    c2=input("\npress 'y' to continue:")
                    if c2!='y':
                        print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
            elif q==3:#3                                                                         #3.
                return menu()       
            else:     #4                                                                          #4.
                print('\nERROR:wrong input')
                c2=input("\npress 'y' to continue:")
                if c2!='y':
                    print('\n\n\t\t\t\t\t\t\t\t\tTHANK YOU FOR JOINING US\n')
    except:
        print('\nERROR:unexpected error found')
            
rent()
    

 
