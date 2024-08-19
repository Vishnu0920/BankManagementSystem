from tkinter import *
import os
from tkinter import messagebox as msg
import mysql.connector as mydb
from mysql.connector import Error
import math

###ESTABLISHING CONNECTION DATABASE
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

finally:

    if mycon.is_connected():
        cur.close()
        mycon.close()
        print('MySQL connection is closed')





def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1000x500")
 
    global username
    global password
    global email
    global contact_no
    global dob
    
    global username_entry
    global password_entry
    global email_entry
    global contact_no_entry
    global dob_entry

    username = StringVar()
    password = StringVar()
    email=StringVar()
    contact_no=StringVar()
    dob=StringVar()
 
    Label(register_screen, text="Please enter details below", bg="red").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen,textvariable=username)
    username_entry.pack()

    contactnumber_lable = Label(register_screen, text="contact number * ")
    contactnumber_lable.pack()
    contactnumber_entry = Entry(register_screen,textvariable=contact_no)
    contactnumber_entry.pack()

    dateofbirth_lable = Label(register_screen, text="Date of birth(YYYY-MM-DD ) * ")
    dateofbirth_lable.pack()
    dateofbirth_entry = Entry(register_screen,textvariable=dob)
    dateofbirth_entry.pack()

    emailid_lable = Label(register_screen, text="Email Id * ")
    emailid_lable.pack()
    emailid_entry = Entry(register_screen,textvariable=email)
    emailid_entry.pack()


    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack() 




 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("3000x2500")

    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
    
    global username1
    global password1
    username1 = username.get()
    password1 = password.get()
    contact_no_info=contact_no.get()
    email_info=email.get()
    dob_info=dob.get()


    if str(contact_no_info).isdigit()==True:

        if len(str(contact_no_info))==10:

            dob_list=dob_info.split('-')
            print(dob_list)

            if int(dob_list[1]) in range(1,13) and int(dob_list[2]) in range(1,32):
 
                mycon=mydb.connect(user='root',host='localhost',password='a1s2d3f$',database='banking')
                cur=mycon.cursor()

                sql=(
               "INSERT INTO User_Details(NAME, CONTACT_NO, DOB, EMAIL, password)"
               "VALUES (%s, %s, %s, %s, %s)"
                )
                data = (username1,contact_no_info,dob_info,email_info,password1)
                cur.execute(sql,data)
                mycon.commit()

                sql="SELECT Account_No FROM User_Details WHERE NAME=%s AND Password=%s"
                data=(username1,password1)
                cur.execute(sql,data)

                global ifsc1
                ifsc1=''
                ifsc1=str(cur.fetchall()[0][0])
                mgprint="""Registration Successful
                    Your Account Number is :"""+str(ifsc1)
                
                msg.showinfo('Registration Successful',mgprint)
                menu()


            else:
                msg.showinfo('Invalid DOB','Please Enter a valid Date of Birth')

        else:

            msg.showinfo('Invalid Mobile No','Please Enter a valid Mobile Number')

    else:

        msg.showinfo('Invalid Mobile No','Please enter only digits for Mobile No')





 
# Implementing event on login button 
 
def login_verify():

    global username1
    global  password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    mycon=mydb.connect(user='root',host='localhost',password='a1s2d3f$',database='banking')
    cur=mycon.cursor()
    
    cur.execute("SELECT name FROM user_details")
    Name_List = [row[0] for row in cur.fetchall()]
    print(Name_List)

    
    

    cur.execute("SELECT password FROM user_details")
    Password_List = [row[0] for row in cur.fetchall()]
    print(Password_List)

    if username1 in Name_List:

        if password1 in Password_List :
            menu()

        else:
           password_not_recognised() 

    else:
        user_not_found()
        
        
    
    
        
 

# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Login Unsuccessful!!")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Login Unsuccessful!!")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()



 
# Designing Main(first) window
def deposit():
    
    global am1
    global deposit_screen

    deposit_screen = Toplevel(main_screen)
    deposit_screen.title("deposit")
    deposit_screen.geometry("3000x2500")
    Label(deposit_screen, text="Please enter Amount to be deposited").pack()
    Label(deposit_screen, text="").pack()

    amount_lable = Label(deposit_screen, text="Amount * ")
    amount_lable.pack()
    am1 = Entry(deposit_screen)
    am1.pack()

  
    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="deposit", width=10, height=1, bg="red", command = save_deposit).pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen,text="GO HOME", height="2", width="10",fg='black',bg='orange', command=main_menu).pack()
    Label(deposit_screen,text="").pack()




def main_menu():
    deposit_screen.destroy()



def withdraw():

    global withdraw_screen
    global am1

    withdraw_screen = Toplevel(main_screen)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry("3000x2500")
    Label(withdraw_screen, text="Please enter Amount to be withdrawn").pack()
    Label(withdraw_screen, text="").pack()

    amount_lable = Label(withdraw_screen, text="Amount * ")
    amount_lable.pack()
    am1 = Entry(withdraw_screen)
    am1.pack()

    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="withdraw", width=10, height=1, bg="red", command = save_withdraw).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen,text="GO HOME", height="2", width="10",fg='black',bg='orange', command=main_menu1).pack()
    Label(withdraw_screen,text="").pack()



#FUNCTION TO SAVE DETAILS TO DATABASE
def save_deposit():

    con=mydb.connect(db='banking',user='root',passwd='a1s2d3f$',host='localhost')
    cur=con.cursor()
    amount=int(am1.get())


    sql="SELECT Account_No FROM User_Details WHERE NAME=%s AND PASSWORD=%s"
    data=(username1,password1)
    cur.execute(sql,data)
    ifsc=str(cur.fetchall()[0][0])
    print(ifsc)

    i="UPDATE User_Details SET BALANCE=BALANCE+%s WHERE Account_No=%s"
    data=(amount,ifsc)
    cur.execute(i,data)
    con.commit()

    
	    
    msg.showinfo('Information','Record Saved')
    am1.delete(0,'end')

    
    con.close()



def save_withdraw():

    con=mydb.connect(db='banking',user='root',passwd='a1s2d3f$',host='localhost')
    cur=con.cursor()

    amount=int(am1.get())

    sql="SELECT Account_No FROM User_Details WHERE NAME=%s AND PASSWORD=%s"
    data=(username1,password1)
    cur.execute(sql,data)
    ifsc=str(cur.fetchall()[0][0])
    print(ifsc)

    sql='SELECT Balance FROM User_Details WHERE Account_No=%s'
    data=(int(ifsc),)
    cur.execute(sql,data)
##    print(cur.fetchall()[0][0])
    balance1=int(cur.fetchall()[0][0])

    if balance1>=amount:
    
        i="UPDATE User_Details SET BALANCE=BALANCE-%s WHERE Account_No=%s"
        data=(amount,ifsc)
        cur.execute(i,data)
        con.commit()
   
        msg.showinfo('Information','Record Saved')
        am1.delete(0,'end')
        con.close()

    else:
        msg.showinfo("Low Balance Alert","You do not have enough money in your account")



def main_menu1():
    withdraw_screen.destroy()
    
def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.title("menu")
    menu_screen.geometry("3000x2500")
    Label(menu_screen,text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(menu_screen,text="").pack()    
    Button(menu_screen,text="Deposit", height="2", width="30",fg='black',bg='violet', command=deposit).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Withdraw", height="2", width="30",fg='black',bg='orange', command=withdraw).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Balance", height="2", width="30",fg='black',bg='orange', command=balance).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Logout", height="2", width="10",fg='black',bg='orange', command=logout2).pack()
    Label(menu_screen,text="").pack()




def logout2():
    menu_screen.destroy()




def balance():
    global balance_screen

    mycon=mydb.connect(user='root',host='localhost',password='a1s2d3f$',database='banking')
    cur=mycon.cursor()

    sql="SELECT Account_No FROM user_details WHERE password=%s and name=%s"
    data=(password1,username1)
    cur.execute(sql,data)
    
    ifsc=cur.fetchall()[0][0]
    print(ifsc)
    
    sql="SELECT BALANCE FROM user_details WHERE Account_No=%s"
    data=(ifsc,)
    cur.execute(sql,data)

    global balance
    balance=StringVar()
    
    balance.set(str(cur.fetchall()[0][0]))
    
    print(balance)


    balance_screen=Toplevel(main_screen)		
    balance_screen.title("Balance enquiry")
    balance_screen.geometry("300x250")
    Label(balance_screen, text="Balance left in your account(In Rupees): ").pack()
    Label(balance_screen, textvariable=balance).pack()
    
  
 



def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50",fg='black',bg='green' ,font=("Arial Bold", 10)  ,command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="50",fg='black',bg='blue',font=("Arial Bold", 10), command=register).pack()
    Label(text="").pack()

    main_screen.mainloop()
 
 
main_account_screen()
