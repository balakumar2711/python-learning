import streamlit as st
from streamlit import session_state

import functions

todos = functions.read_fun() #Reads the text file present

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_fun(todos)

#Here the order in which these are given matters
st.title("My App") #The name of the app
st.subheader("The tasks to be done") #Sub headers if any
st.write("This is to capture my works") #The next level of sub header

for index, todo in enumerate(todos):
    #Here the value of checkbox when printed by session state will be true or false based on the selection so a dynamic variable is added for the key which makes it easy to capture the checkbox and pop it out using the index
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_fun(todos)
        #The below session state updates are required for the program to update the web page in real time
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter the new item",
              on_change=add_todo, key='new_todo')


