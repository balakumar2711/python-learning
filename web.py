import streamlit as st
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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter the new item",
              on_change=add_todo, key='new_todo')


