import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='2003',database='BikeRentalService')
cur=mydb.cursor()
A="delete from bike;"
B='drop table customer;'
cur.execute(A)
mydb.commit()

