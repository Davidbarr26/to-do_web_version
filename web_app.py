"""
Project: PythonProject
program: To-Do Web App
Purpose: Creating a Web version for the to-do App
Revision History:
    Created on December 27th, 2024. By Juan (David) Barrios Rozo
"""

import streamlit as st
import functions

todos = functions.get_todos()

#st.set_page_config(layout="")

def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("TO-DO App")
st.subheader("This is the To-Do web version")
st.write("Welcome to the Web Version of the To-Do app. This app is to increase <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="Enter a to-do: ", placeholder="Add a new to-do here... ",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.write(functions.display_copyright())
