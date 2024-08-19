import mysql.connector as mydb
from mysql.connector import Error


try:
    mycon=mydb.connect(user='root',host='localhost',password='a1s2d3f$',database='banking')

    if mycon.is_connected():
        db_info=mycon.get_server_info()
        print('Connected to MySQL Server Version',db_info)
        cur=mycon.cursor()
        cur.execute('select database();')
        record=cur.fetchone()
        print('Youre connected to database:',record)


except Error as e:
    print('Error while connecting to MySQL',e)

##finally:
##
##    if mycon.is_connected():
##        cur.close()
##        mycon.close()
##        print('MySQL connection is closed')



mycon=mydb.connect(user='root',host='localhost',password='a1s2d3f$',database='banking')
cur=mycon.cursor()

cur.execute("SELECT name FROM user_details")
x=cur.fetchall()
print(x)
