
import os
import json

global todos_file

todos_file = 'todos.json'

def get_todos():
    if os.path.exists(todos_file):
        with open('todos.json','rb') as file:
            try:
                return json.load(file)
            except:
                return []
    else:
        return []


def create_todo(newTodo):

    print("RUNNING CREATAE TDODO")
    print(todos_file)

    todos = get_todos()

    todos.append(newTodo)

    with open('todos.json','w') as file:
        json.dump(todos, file)

    return newTodo