#!/usr/bin/python3
"""script uses a public api, returns information
about todo list progressfor all users. """
import json
import requests


if __name__ == "__main__":
    user_list = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    users = {}
    for v in user_list:
        users.update({v.get('id'): v.get('username')})

    json_dic = {}
    todo_list = []
    user_id = 1
    for v in todos:
        if v.get('userId') > user_id:
            json_dic.update({user_id: todo_list})
            user_id = v.get('userId')
            todo_list = []
        todo = {"username": users.get(v.get('userId')), "task": v.get('title'),
                "completed": v.get('completed')}
        todo_list.append(todo)
    json_dic.update({user_id: todo_list})

    with open("todo_all_employees.json", 'w') as f:
        json.dump(json_dic, f)
