import pandas as pd
import streamlit as st
from database import *


def read1():
    result = view_all_user_data()
    df = pd.DataFrame(result, columns=['User ID', 'FName' , 'LName' , 'DOB' ,'Age','Gender','Address' , 'Email_ID'])
    with st.expander("Users Details"):
        st.dataframe(df)
        
    result2 = view_all_author_data()
    df = pd.DataFrame(result2, columns=['Author ID', 'firstName', 'lastName', 'EmailID' , 'Gender', 'Country'])
    with st.expander("Authors Details"):
        st.dataframe(df)
        
    result3 = view_all_books_data()
    df = pd.DataFrame(result3, columns=['BookID','Title','Price','Genre','Publisher','Published_Date','A_ID','Availability'])
    with st.expander("Books Details"):
        st.dataframe(df)
        
    result4 = view_all_orders_data()
    df = pd.DataFrame(result4, columns=['OrderID','Order_Time','Order_Date'])
    with st.expander("Orders Details"):
        st.dataframe(df)
        
    result5 = view_all_payment_data()
    df = pd.DataFrame(result5, columns=['PID','Amount','BankName','Card_No','Order_ID'])
    with st.expander("Payment Details"):
        st.dataframe(df)
        

        
        

        
