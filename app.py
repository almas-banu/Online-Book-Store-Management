
#import mysql.connector

#mydb = mysql.connector.connect(
#    host="localhost",
#    user="root",
#   password=""
#)
#c = mydb.cursor()

#c.execute("use PES1UG20CS535_Project")


import streamlit as st

from create import *
from database import *
from delete import *
from read import *
from joins import *
from update import *



def main():
    st.set_page_config(page_title="Kindle", page_icon='📚')
    st.markdown(f'<h1 style=color:#D30B60 ;font-size:40px;border-radius:2%;text-align:center">Online BookStore Management App</h1>', unsafe_allow_html=True)
    menu = ["Main","Read","Insert","Delete","Update"," "]
    
    choice = st.sidebar.selectbox("Menu", menu)
     
    if choice == "Main":
        desc()
        inp = st.text_input("Enter MySQL Query:")
        query(inp)
    if choice == " ":
        pass
    if choice == "Read":
        read1()
            
    if choice == "Insert":
        menu = ["User","Author","Books","Orders","Payment"]
        ch1 = st.selectbox("Menu",menu)
        if ch1 == "User":
            create1()
        elif ch1 == "Author":
            create2()
        elif ch1 == "Books":
            create3()
        elif ch1 == "Orders":
            create4()
        elif ch1 == "Payment":
            create5()
    
    if choice == "Delete":
        menu = ["User","Author","Books","Orders","Payment"]
        ch1 = st.selectbox("Menu",menu)
        if ch1 == "User":
            delete1()
        elif ch1 == "Author":
            delete2()
        elif ch1 == "Books":
            delete3()
        elif ch1 == "Orders":
            delete4()
        elif ch1 == "Payment":
            delete5()
            
    if choice == "Update":
        menu = ["User","Author","Books","Orders","Payment"]
        ch1 = st.selectbox("Menu",menu)
        if ch1 == "User":
            update1()
        elif ch1 == "Author":
            update2()
        elif ch1 == "Books":
            update3()
        elif ch1 == "Orders":
            update4()
        elif ch1 == "Payment":
            update5()

    menu2 = ["Atleast 1 book","Male Users","Price > 400"]
    ch = st.sidebar.selectbox("Operations",menu2)
    
    if ch == "Atleast 1 book":
        j1()
    elif ch == "Male Users":
        set1()
    elif ch == "Price > 400":
        j4()
        
    menu3 = [" ","Aggregation","Join2","Join3","Procedure","View","Trigger"]
    dh = st.sidebar.selectbox("Operations",menu3)
    
    if dh == " ":
        pass
    elif dh == "Aggregation":
        agg1()
    elif dh == "Join2":
        j2()
    elif dh == "Join3":
        j3()
    elif dh == "Procedure":
        p1()
    elif dh == "View":
        view1()
    elif dh == "Trigger":
        trig()
    
if __name__ == '__main__':
    main()


