import pandas as pd
import streamlit as st
from database import *


def delete1():
    result = view_all_user_data()
    df = pd.DataFrame(result, columns=['User ID', 'FName' , 'LName' , 'DOB' ,'Age','Gender','Address' , 'Email_ID'])
    with st.expander("Current User Data"):
        st.dataframe(df)

    list_of_users = [i[0] for i in view_only_user_id()]
    selected_user = st.selectbox("User to Delete", list_of_users)
    st.warning("Do you want to delete {}?".format(selected_user))
    if st.button("Delete User"):
        delete_user_data(selected_user)
        st.success("User {} has been deleted successfully".format(selected_user))
    new_result = view_all_user_data()
    df2 = pd.DataFrame(new_result, columns=['User ID', 'FName' , 'LName' , 'DOB' ,'Age','Gender','Address' , 'Email_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def delete2():
    result = view_all_author_data()
    df = pd.DataFrame(result, columns=['Author ID', 'firstName', 'lastName', 'EmailID' , 'Gender', 'Country'])
    with st.expander("View all Authors"):
        st.dataframe(df)

    list_of_athrs = [i[0] for i in view_only_a_id()]
    selected_athr = st.selectbox("Author to Delete", list_of_athrs)
    st.warning("Do you want to delete {}?".format(selected_athr))
    if st.button("Delete Author"):
        delete_author_data(selected_athr)
        st.success("Author has been deleted successfully")
    new_result = view_all_author_data()
    df2 = pd.DataFrame(new_result, columns=['Author ID', 'firstName', 'lastName', 'EmailID' , 'Gender', 'Country'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def delete3():
    result = view_all_books_data()
    df = pd.DataFrame(result, columns=['BookID','Title','Price','Genre','Publisher','Published_Year','A_ID','Availability'])
    with st.expander("View all Books"):
        st.dataframe(df)

    list_of_books = [i[0] for i in view_only_book_id()]
    selected_book = st.selectbox("Book to Delete", list_of_books)
    st.warning("Do you want to delete {}?".format(selected_book))
    if st.button("Delete Author"):
        delete_book_data(selected_book)
        st.success("Book has been deleted successfully")
    new_result = view_all_books_data()
    df2 = pd.DataFrame(new_result,  columns=['BookID','Title','Price','Genre','Publisher','Published_Year','A_ID','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def delete4():
    result = view_all_orders_data()
    df = pd.DataFrame(result, columns=['OrderID','Order_Time','Order_Date'])
    with st.expander("View all Orders"):
        st.dataframe(df)

    list_of_orders = [i[0] for i in view_only_orders_id()]
    selected_order = st.selectbox("Order to Delete", list_of_orders)
    st.warning("Do you want to delete {}?".format(selected_order))
    if st.button("Delete Order"):
        delete_orders_data(selected_order)
        st.success("Order has been deleted successfully")
    new_result = view_all_orders_data()
    df2 = pd.DataFrame(new_result, columns=['OrderID','Order_Time','Order_Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def delete5():
    result = view_all_payment_data()
    df = pd.DataFrame(result, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("View all Payment"):
        st.dataframe(df)

    list_of_payment = [i[0] for i in view_only_payment_id()]
    selected_payment = st.selectbox("Payment Detail to be deleted", list_of_payment)
    st.warning("Do you want to delete {}?".format(selected_payment))
    if st.button("Delete Payment"):
        delete_payment_data(selected_payment)
        st.success("Payment has been deleted successfully")
    new_result = view_all_payment_data()
    df2 = pd.DataFrame(new_result, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        


        

        
