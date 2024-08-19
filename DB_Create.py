import mysql.connector as sqltor


global dbname
global dbuser
global dbpassword

#Change these values as per the mysql details in the machine where it is executed
dbname = "banking"
dbuser = "root"
dbpassword = "a1s2d3f$"

def CreateTable():

    mycon= sqltor.connect(host="localhost",user=dbuser,password=dbpassword)
    cursor = mycon.cursor()
    sql1="USE  BANKING;"
    cursor.execute(sql1)
    mycon.commit()

    
    sql2="CREATE TABLE User_Details(NAME  varchar(50),CONTACT_NO varchar(10), DOB date,EMAIL varchar(50),PASSWORD varchar(50),ACCOUNT_NO int unsigned auto_increment primary key,BALANCE int DEFAULT 0)"
    cursor.execute(sql2)
    mycon.commit()
    print('Table Created Succesfully')

    
   


mycon= sqltor.connect(host="localhost",user=dbuser,password=dbpassword)
print("Creating new DB....")
cursor = mycon.cursor()
cursor.execute("CREATE DATABASE banking")
mycon= sqltor.connect(host="localhost",user=dbuser,password=dbpassword,database=dbname)
print('DB created succesfully')

CreateTable()
    

    


















