from todoapp_func import get_todos, write_todos
import time

now = time.strftime('%d.%m.%Y,  %H:%M')
print(f'Today is {now}')

while True:
    user_action = input('Hi! I can add, show, edit, complete or exit. Enter command: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}. {item.title()}')

    elif user_action.startswith('edit'):
        try:
            number_str = user_action[5:]
            number = int(number_str)

            todos = get_todos()

            print(todos[number - 1].title())

            new_todo = input('Enter new todo: ')
            todos[number - 1] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Unknown command. Try again.')
            continue

    elif user_action.startswith('complete'):
        try:
            number_str = user_action[9:]
            number = int(number_str)

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f'Todo {todo_to_remove.title()} was completed.'
            print(message)
        except IndexError:
            print('Unknown command. Try again.')
            continue

    elif user_action.startswith('exit'):
        print('Bye!')
        break
    else:
        print('Unknown command. Try again.')
