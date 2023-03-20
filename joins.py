import pandas as pd
import streamlit as st
from database import *
from create import *

def query(inp):
    if (inp == ""):
        st.error("Please Enter the Query")
    else:
        c.execute(inp)
        data = c.fetchall()
        st.write(data)
        
def j1():
    result = join1()
    df = pd.DataFrame(result, columns=['FName'])
    with st.sidebar.expander("View all Users who has bought atleast 1 book"):
        st.dataframe(df)

def j2():
    res = join2()
    result = view_all_payment_data()
    df = pd.DataFrame(result, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("Payment Data With Updated Data"):
        st.dataframe(df)
        
def j3():
    result = join3()
    df = pd.DataFrame(result,columns=['User_ID','FName','LName','DOB','Gender','Address','Email_ID'])
    with st.expander("Retrieve all the female users who has bought atleast 1 book"):
        st.dataframe(df)
        
def j4():
    result = join4()
    df = pd.DataFrame(result,columns=['FName','LName'])
    with st.sidebar.expander("Retrieve first and last name of users who have searched a book with price > 400"):
        st.dataframe(df)
        
def agg1():
    result = aggr()
    df = pd.DataFrame(result,columns=['Author_ID','firstName','lastName','Number_Of_Books'])
    with st.expander("Find the number of books written by each author."):
        st.dataframe(df)
        
def set1():
    result = set()
    df = pd.DataFrame(result,columns=['User_ID','FName','LName'])
    with st.sidebar.expander("The details of only male users who have searched for books"):
        st.dataframe(df)
        
def p1():
    proc()
    result = view_all_user_data()
    df2 = pd.DataFrame(result,columns=['User ID', 'FName' , 'LName' , 'DOB' ,'Age','Gender','Address' , 'Email_ID'])
    with st.expander("Updating the Age column in User Table using a stored procedure"):
        st.dataframe(df2)
        
def view1():
    result = view()
    df = pd.DataFrame(result,columns=['User_ID','FName','LName','DOB','Gender','Address','Email_ID','Book_ID','Order_ID','Number_of_books_bought'])
    with st.expander("Retrieve the user who bought maximum number of books.Also the display the details of books bought by  user"):
        st.dataframe(df)
    

def trig():
    result = view_all_buys_places_data()
    df = pd.DataFrame(result, columns=['User_ID','Book_ID','Order_ID','No_Of_Books'])
    with st.expander("Current Buys_Places Data"):
        st.dataframe(df)
    result1 = view_all_books_data()
    df = pd.DataFrame(result1, columns=['BookID','Title','Price','Genre','Publisher','Published_Date','A_ID','Availability'])
    with st.expander("View all Books"):
        st.dataframe(df)
    create6()
    viw = view_all_buys_places_data()
    df = pd.DataFrame(viw, columns=['User_ID','Book_ID','Order_ID','No_Of_Books'])
    with st.expander("Updated Buys_Places Data"):
        st.dataframe(df)
    viw1 = view_all_books_data()
    df = pd.DataFrame(viw1, columns=['BookID','Title','Price','Genre','Publisher','Published_Date','A_ID','Availability'])
    with st.expander("View all Books after updating Availability"):
        st.dataframe(df)
    
        