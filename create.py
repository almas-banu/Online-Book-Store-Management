import streamlit as st
from database import *

def desc():
    st.info("A Online Book Store Management is a project that manages and stores books information electronically according to user/customer needs. The system helps both user and library admin to keep a constant track of all the books available in the store. It allows both the admin and the user to search for the desired book.")
def create1():
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input("User_ID:")
        FName  = st.text_input("FName:")
        LName = st.text_input("LName:")
        DOB = st.date_input("DOB")
    with col2:
        Age = st.text_input("Age")
        Gender = st.selectbox("Gender",['M','F','NA'])
        Address = st.text_input("Address :")
        Email_ID = st.text_input("Email_ID : ")
    if st.button("Add User"):
        add_user_data(user_id , FName, LName, DOB,Age,Gender,Address , Email_ID)
        st.success("Successfully added User: {}".format(user_id))
        
def create2():
    col1, col2 = st.columns(2)
    with col1:
        A_ID = st.text_input("Author ID:")
        firstName = st.text_input("First Name :")
        lastName = st.text_input("Last Name :")
    with col2:
        EmailID = st.text_input("Email ID :")
        Gender = st.selectbox("Gender",['M','F','NA'])
        Country = st.text_input("Country : ")
    if st.button("Add Author"):
        add_author_data(A_ID, firstName, lastName, EmailID ,Gender,Country)
        st.success("Successfully Added Author : {}".format(A_ID))
        
def create3():
    col1, col2 = st.columns(2)
    with col1:
        Book_ID = st.text_input("Book ID:")
        Title = st.text_input("Title : ")
        Price = st.text_input("Price : ")
        Genre = st.text_input("Genre : ")
    with col2:
        Publisher = st.text_input("Publisher : ")
        Published_Date = st.text_input("Published_Date : ")
        A_ID = st.text_input("Author ID")
        Availabilty = st.text_input("Availabilty")
    if st.button("Add Book"):
        add_book_data(Book_ID,Title,Price,Genre,Publisher,Published_Date,A_ID,Availabilty)
        st.success("Successfully Added Book : {}".format(Book_ID))

def create4():
    Order_ID = st.text_input("Order ID:")
    Order_Time = st.text_input("Ordered Time : ")
    Order_Date = st.text_input("Ordered Date : ")
    if st.button("Add Order"):
        add_orders_data(Order_ID,Order_Time,Order_Date)
        st.success("Successfully Added Order : {}".format(Order_ID))
    
def create5():
    col1, col2 = st.columns(2)
    with col1:
        P_id = st.text_input("Payment ID:")
        Amount = st.text_input("Amount  : ")
        BankName = st.text_input("Bank Name : ")
    with col2:
        Card_No = st.text_input("Card Number : ")
        Order_ID = st.text_input("Order ID : ")
    if st.button("Add Payment"):
        add_payment_data(P_id,Amount,BankName,Card_No,Order_ID)
        st.success("Successfully Added Payment : {}".format(P_id))
        
def create6():
    User_ID = st.text_input("User ID : ")
    Book_ID = st.text_input("Book_ID : ")
    Order_ID = st.text_input("Order_ID : ")
    No_Of_Books = st.text_input("No Of Books : ")
    if st.button("Add Buys_Places"):
        add_buys_places_data(User_ID,Book_ID,Order_ID,No_Of_Books)
        st.success("Successfully Added Buys_Places : {}".format(User_ID))
    
        
        

        

        
    
    
    
    
    
    
    
    
    
    