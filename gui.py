import todoapp_func as func
import PySimpleGUI as sg
import time

sg.theme('LightGreen7')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', size=10)
list_box = sg.Listbox(values=func.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit', size=10)

window = sg.Window('lolo To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%d.%m.%Y,  %H:%M'))
    print(event, values)
    match event:
        case 'Add':
            todos = func.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            func.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = func.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                func.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('No todo selected', title='Error', font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = func.get_todos()
                todos.remove(todo_to_complete)
                func.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('No todo selected', title='Error', font=('Helvetica', 20))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
