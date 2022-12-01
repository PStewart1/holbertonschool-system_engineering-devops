#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
dumps todo info into csv file """
import requests
import sys
import json


if __name__ == "__main__":
    eid = sys.argv[1]
    name_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid).json()
    name = name_response['username']
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todo_dic = {}
    todos = []
    for v in response:
        todo = {"task": v['title'], "completed": v['completed'],
                "username": name}
        todos.append(todo)
    todo_dic.update({2: todos})
    file = eid + ".json"
    with open(file, 'w') as f:
        json.dump(todo_dic, f)
