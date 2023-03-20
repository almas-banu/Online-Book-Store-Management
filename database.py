# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PES1UG20CS535_Project"
)
c = mydb.cursor()

'''
def create_table1():
    c.execute('CREATE TABLE IF NOT EXISTS User(user_id TEXT, FName TEXT, LName TEXT, DOB TEXT,'
               'Adress TEXT, Email_ID TEXT)')
    
def create_table2():
    c.execute('CREATE TABLE IF NOT EXISTS Author(A_ID TEXT, firstName TEXT, lastName TEXT, EmailID TEXT,Year TEXT)')

def create_table3():
    c.execute('CREATE TABLE IF NOT EXISTS Book(BookID TEXT,Title TEXT,Genre TEXT,Price TEXT,Publisher TEXT,Published_Date TEXT)')

def create_table4():
    c.execute('CREATE TABLE IF NOT EXISTS Orders(OrderID TEXT,No_Of_Books TEXT, Order_Time TEXT)')

def create_table5():
    c.execute('CREATE TABLE IF NOT EXISTS Payment(PID TEXT,Amount TEXT,BankName TEXT)')

def create_table6():
    c.execute('CREATE TABLE IF NOT EXISTS Stocks(BookName TEXT,Availability TEXT)')

'''
def add_user_data(User_ID, FName , LName , DOB , Age, Gender, Address , Email_ID):
    c.execute('INSERT INTO USER(User_ID, FName , LName , DOB , Age, Gender, Address , Email_ID) VALUES (%s,%s,%s,'
              '%s,%s,%s,%s,%s)',
              (User_ID, FName , LName , DOB , Age, Gender, Address , Email_ID))
    mydb.commit()
    
def add_author_data(A_ID, firstName, lastName, EmailID ,Gender,Country):
    c.execute('INSERT INTO Author(A_ID, firstName, lastName, EmailID ,Gender,Country) VALUES (%s,%s,%s,%s,%s,%s)',
              (A_ID, firstName, lastName, EmailID ,Gender,Country))
    mydb.commit()
    
def add_book_data(Book_ID,Title,Price,Genre,Publisher,Published_Date,A_ID,Availabilty):
    c.execute('INSERT INTO Books(Book_ID,Title,Price,Genre,Publisher,Published_Date,A_ID,Availabilty) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (Book_ID,Title,Price,Genre,Publisher,Published_Date,A_ID,Availabilty))
    mydb.commit()

def add_orders_data(Order_ID,Order_Time,Order_Date):
    c.execute('INSERT INTO Orders(Order_ID,Order_Time,Order_Date) VALUES (%s,%s,%s)',
              (Order_ID,Order_Time,Order_Date))
    mydb.commit()
    
def add_payment_data(P_id,Amount,BankName,Card_No,Order_ID):
    c.execute('INSERT INTO Payment(P_id,Amount,BankName,Card_No,Order_ID) VALUES (%s,%s,%s,%s,%s)',
              (P_id,Amount,BankName,Card_No,Order_ID))
    mydb.commit()
    
def add_buys_places_data(User_ID,Book_ID,Order_ID,No_Of_Books):
    c.execute('INSERT INTO Buys_Places(User_ID,Book_ID,Order_ID,No_Of_Books) VALUES (%s,%s,%s,%s)',
              (User_ID,Book_ID,Order_ID,No_Of_Books))
    mydb.commit()

def view_all_user_data():
    c.execute('SELECT * FROM USER')
    data = c.fetchall()
    return data

def view_all_author_data():
    c.execute('SELECT * FROM AUTHOR')
    data = c.fetchall()
    return data

def view_all_books_data():
    c.execute('SELECT * FROM BOOKS')
    data = c.fetchall()
    return data

def view_all_orders_data():
    c.execute('SELECT * FROM ORDERS')
    data = c.fetchall()
    return data

def view_all_payment_data():
    c.execute('SELECT * FROM PAYMENT')
    data = c.fetchall()
    return data

def view_all_buys_places_data():
    c.execute('SELECT * FROM Buys_Places')
    data = c.fetchall()
    return data

def view_only_user_id():
    c.execute('SELECT user_id FROM USER')
    data = c.fetchall()
    return data

def view_only_a_id():
    c.execute('SELECT a_id FROM AUTHOR')
    data = c.fetchall()
    return data

def view_only_book_id():
    c.execute('SELECT book_id FROM BOOKS')
    data = c.fetchall()
    return data

def view_only_orders_id():
    c.execute('SELECT Order_ID FROM ORDERS')
    data = c.fetchall()
    return data

def view_only_payment_id():
    c.execute('SELECT p_id FROM PAYMENT')
    data = c.fetchall()
    return data

def get_user(User_ID):
    c.execute('SELECT * FROM USER WHERE User_ID="{}"'.format(User_ID))
    data = c.fetchall()
    return data

def get_author(A_ID):
    c.execute('SELECT * FROM AUTHOR WHERE A_ID="{}"'.format(A_ID))
    data = c.fetchall()
    return data

def get_book(Book_ID):
    c.execute('SELECT * FROM BOOKS WHERE Book_ID="{}"'.format(Book_ID))
    data = c.fetchall()
    return data

def get_order(Order_ID):
    c.execute('SELECT * FROM ORDERS WHERE Order_ID="{}"'.format(Order_ID))
    data = c.fetchall()
    return data

def get_payment(P_ID):
    c.execute('SELECT * FROM PAYMENT WHERE P_ID = "{}"'.format(P_ID))
    data = c.fetchall()
    return data


def edit_user_data(new_User_ID, new_FName , new_LName , new_DOB , new_Age, new_Gender, new_Address , new_Email_ID, User_ID):
    c.execute("UPDATE USER SET User_ID=%s, FName=%s , LName=%s , DOB=%s , Age=%s, Gender=%s, Address=%s , Email_ID=%s WHERE User_ID=%s", (new_User_ID, new_FName, new_LName , new_DOB , new_Age, new_Gender, new_Address, new_Email_ID,User_ID))
    mydb.commit()
    
def edit_author_data(new_A_ID, new_firstName, new_lastName, new_EmailID ,new_Gender,new_Country,A_ID):
    c.execute("UPDATE AUTHOR SET A_ID=%s, firstName=%s, lastName=%s, Email_ID=%s ,Gender=%s,Country=%s WHERE A_ID=%s", (new_A_ID, new_firstName, new_lastName, new_EmailID ,new_Gender,new_Country,A_ID))
    mydb.commit()

def edit_book_data(new_Book_ID,new_Title,new_Price,new_Genre,new_Publisher,new_Published_Date,new_A_ID,new_Availabilty,Book_ID):
    c.execute("UPDATE BOOKS SET Book_ID=%s,Title=%s,Price=%s,Genre=%s,Publisher=%s,Published_Date=%s,A_ID=%s,Availabilty=%s WHERE Book_ID=%s", (new_Book_ID,new_Title,new_Price,new_Genre,new_Publisher,new_Published_Date,new_A_ID,new_Availabilty,Book_ID))
    mydb.commit()
    
def edit_orders_data(new_Order_ID,new_Order_Time,new_Order_Date,Order_ID):
    c.execute("UPDATE ORDERS SET Order_ID=%s,Order_Time=%s,Order_Date=%s WHERE Order_ID=%s", (new_Order_ID,new_Order_Time,new_Order_Date,Order_ID))
    mydb.commit()
    
def edit_payment_data(new_P_id,new_Amount,new_BankName,new_Card_No,new_Order_ID,P_id):
    c.execute("UPDATE PAYMENT SET P_id=%s,Amount=%s,BankName=%s,Card_No=%s,Order_ID=%s WHERE P_ID=%s", (new_P_id,new_Amount,new_BankName,new_Card_No,new_Order_ID,P_id))
    mydb.commit()
    
    
def delete_user_data(user_id):
    c.execute('DELETE FROM USER WHERE user_id="{}"'.format(user_id))
    mydb.commit()
    
def delete_author_data(A_id):
    c.execute('DELETE FROM AUTHOR WHERE A_id="{}"'.format(A_id))
    mydb.commit()

def delete_book_data(Book_ID):
    c.execute('DELETE FROM BOOKS WHERE BookID="{}"'.format(Book_ID))
    mydb.commit()
    
def delete_orders_data(Order_ID):
    c.execute('DELETE FROM ORDERS WHERE Order_ID="{}"'.format(Order_ID))
    mydb.commit()

def delete_payment_data(P_id):
    c.execute('DELETE FROM PAYMENT WHERE P_ID="{}"'.format(P_id))
    mydb.commit()
    



def join1():
    c.execute('SELECT DISTINCT Fname AS Name From User NATURAL JOIN Buys_Places WHERE User.User_ID = Buys_Places.User_ID')
    data = c.fetchall()
    return data

def join2():
    c.execute("UPDATE Payment as p INNER JOIN Buys_Places as bp ON p.Order_ID = bp.Order_ID INNER JOIN Books as b ON bp.Book_ID = b.Book_ID SET p.Amount = b.Price * bp.No_Of_Books")
    mydb.commit()

def join3():
    c.execute("SELECT Distinct User_ID,FName,LName,DOB,Gender,Address,Email_ID From User as u NATURAL JOIN Buys_Places as bp WHERE u.User_ID = bp.User_ID and Gender = 'F'")
    data = c.fetchall()
    return data

def join4():
    c.execute("SELECT DISTINCT Fname,Lname FROM User as u INNER JOIN Searches_For as s ON u.User_ID = s.User_ID INNER JOIN Books as b ON s.Book_ID = b.Book_ID and b.price > 400")
    data = c.fetchall()
    return data

def aggr():
    c.execute("SELECT A_ID,firstName,lastName,Count(Books.A_ID) AS No_of_Books From Books NATURAL JOIN Author GROUP BY Books.A_ID")
    data = c.fetchall()
    return data

def set():
    c.execute("SELECT User_ID,FName,LName FROM User as u NATURAL JOIN Searches_For as s WHERE (u.Gender = 'M') EXCEPT SELECT User_ID,FName,LName FROM User as u NATURAL JOIN Searches_For as s WHERE (u.Gender = 'M' and u.Gender = 'F')")
    data = c.fetchall()
    return data

def proc():
    c.execute("CALL Calculate_Age()")
    mydb.commit()
    
def view():
    c.execute("SELECT * FROM User_Max_Books WHERE Number_of_books_bought = (SELECT MAX(Number_of_books_bought) from User_Max_Books)")
    data = c.fetchall()
    return data

