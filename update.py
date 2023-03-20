import datetime

import pandas as pd
import streamlit as st
from database import *


def update1():
    result = view_all_user_data()
    df = pd.DataFrame(result, columns=['User_ID', 'FName' , 'LName' , 'DOB' , 'Age', 'Gender', 'Address' , 'Email_ID'])
    with st.expander("Current Users"):
        st.dataframe(df)
    list_of_users = [i[0] for i in view_only_user_id()]
    selected_user = st.selectbox("Users to Edit", list_of_users)
    selected_result = get_user(selected_user)
    if selected_result:
        user_id  = selected_result[0][0]
        FName = selected_result[0][1]
        LName = selected_result[0][2]
        DOB = selected_result[0][3]
        Age  = selected_result[0][4]
        Gender = selected_result[0][5]
        Address = selected_result[0][6]
        Email_ID = selected_result[0][7]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_User_id = st.text_input("User_ID:",user_id)
            new_FName  = st.text_input("FName:",FName)
            new_LName = st.text_input("LName:",LName)
            new_DOB = st.date_input("DOB",DOB)
        with col2:
            new_Age = st.text_input("Age",Age)
            new_Gender = st.text_input("Gender",Gender)
            new_Address = st.text_input("Address :",Address)
            new_Email_ID = st.text_input("Email_ID : ",Email_ID)
        if st.button("Update User"):
            edit_user_data(new_User_id, new_FName , new_LName , new_DOB , new_Age, new_Gender, new_Address, new_Email_ID, user_id)
            st.success("Successfully updated details of {}".format(user_id))

    result2 = view_all_user_data()
    df2 = pd.DataFrame(result2, columns=['User_ID', 'FName' , 'LName' , 'DOB' , 'Age', 'Gender', 'Address' , 'Email_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update2():
    result = view_all_author_data()
    df = pd.DataFrame(result, columns=['Author ID', 'firstName', 'lastName', 'EmailID' , 'Gender', 'Country'])
    with st.expander("Current Authors"):
        st.dataframe(df)
    list_of_athrs = [i[0] for i in view_only_a_id()]
    selected_athr = st.selectbox("Authors to Edit", list_of_athrs)
    selected_result = get_author(selected_athr)
    if selected_result:
        A_ID  = selected_result[0][0]
        firstName = selected_result[0][1]
        lastName = selected_result[0][2]
        EmailID = selected_result[0][3]
        Gender  = selected_result[0][4]
        Country = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_A_ID = st.text_input("Author ID:",A_ID)
            new_firstName = st.text_input("First Name :",firstName)
            new_lastName = st.text_input("Last Name :",lastName)
        with col2:
            new_EmailID = st.text_input("Email ID :",EmailID)
            new_Gender = st.selectbox("Gender",['M','F','NA'])
            new_Country = st.text_input("Country : ",Country)
        if st.button("Update Author"):
            edit_author_data(new_A_ID, new_firstName, new_lastName, new_EmailID, new_Gender,new_Country, A_ID)
            st.success("Successfully updated details of {}".format(A_ID))

    result2 = view_all_author_data()
    df2 = pd.DataFrame(result2, columns=['Author ID', 'firstName', 'lastName', 'EmailID' , 'Gender', 'Country'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update3():
    result = view_all_books_data()
    df = pd.DataFrame(result, columns=['BookID','Title','Price','Genre','Publisher','Published_Date','A_ID','Availability'])
    with st.expander("Current Books"):
        st.dataframe(df)
    list_of_books = [i[0] for i in view_only_book_id()]
    selected_book = st.selectbox("Books to Edit", list_of_books)
    selected_result = get_book(selected_book)
    if selected_result:
        Book_ID = selected_result[0][0]
        Title = selected_result[0][1]
        Genre = selected_result[0][2]
        Price = selected_result[0][3]
        Publisher  = selected_result[0][4]
        Published_Date = selected_result[0][5]
        A_ID = selected_result[0][6]
        Availability = selected_result[0][7]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Book_ID = st.text_input("Book ID:",Book_ID)
            new_Title = st.text_input("Title : ",Title)
            new_Price = st.text_input("Price : ",Price)
            new_Genre = st.text_input("Genre : ",Genre)
        with col2:
            new_Publisher = st.text_input("Publisher : ",Publisher)
            new_Published_Date = st.text_input("Published_Date : ",Published_Date)
            new_A_ID = st.text_input("A_ID:",A_ID)
            new_Availabilty = st.text_input("Availabilty : ",Availability)
        if st.button("Update Book"):
            edit_book_data(new_Book_ID,new_Title,new_Price,new_Genre,new_Publisher,new_Published_Date,new_A_ID,new_Availabilty,Book_ID)
            st.success("Successfully updated details of {}".format(Book_ID))

    result2 = view_all_books_data()
    df2 = pd.DataFrame(result2, columns=['BookID','Title','Price','Genre','Publisher','Published_Date','A_ID','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update4():
    result = view_all_orders_data()
    df = pd.DataFrame(result, columns=['Order_ID','Order_Time','Order_Date'])
    with st.expander("Current Orders"):
        st.dataframe(df)
    list_of_orders = [i[0] for i in view_only_orders_id()]
    selected_order = st.selectbox("Orders to Edit", list_of_orders)
    selected_result = get_order(selected_order)
    if selected_result:
        Order_ID = selected_result[0][0]
        Order_Time = selected_result[0][1]
        Order_Date = selected_result[0][2]

        # Layout of Create
        new_Order_ID = st.text_input("Order ID:",Order_ID)
        new_Order_Time = st.text_input("Order Time : ",Order_Time)
        new_Order_Date = st.text_input("Ordered Date : ",Order_Date)
        if st.button("Update Order"):
            edit_orders_data(new_Order_ID,new_Order_Time,new_Order_Date,Order_ID)
            st.success("Successfully updated details of {}".format(Order_ID))

    result2 = view_all_orders_data()
    df2 = pd.DataFrame(result2, columns=['OrderID', 'Order_Time','Ordered_Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update5():
    result = view_all_payment_data()
    df = pd.DataFrame(result, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("Current Payment"):
        st.dataframe(df)
    list_of_payment = [i[0] for i in view_only_payment_id()]
    selected_order = st.selectbox("Payment Details to Edit", list_of_payment)
    selected_result = get_payment(selected_order)
    if selected_result:
        P_id = selected_result[0][0]
        Amount = selected_result[0][1]
        BankName = selected_result[0][2]
        Card_No = selected_result[0][3]
        Order_ID = selected_result[0][4]

        # Layout of Create

        col1,col2 = st.columns(2)
        with col1:
            new_P_id = st.text_input("Payment ID:",P_id)
            new_Amount = st.text_input("Amount  : ",Amount)
            new_BankName = st.text_input("Bank Name : ",BankName)
        with col2:
            new_Card_No = st.text_input("Card Number : ",Card_No)
            new_Order_ID = st.text_input("Order_ID : ",Order_ID)
        if st.button("Update Payment Details"):
            edit_payment_data(new_P_id,new_Amount,new_BankName,new_Card_No,new_Order_ID,P_id)
            st.success("Successfully updated details of {}".format(P_id))

    result2 = view_all_payment_data()
    df2 = pd.DataFrame(result2, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        

        

        

        

    


