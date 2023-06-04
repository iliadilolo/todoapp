import streamlit as st
import todoapp_func as func


todos = func.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    func.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('Hello!')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='', placeholder="Enter a new todo...", on_change=add_todo,
              key='new_todo')

