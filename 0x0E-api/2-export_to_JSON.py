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
    name = name_response.get("name")
    username = name_response.get('username')
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todo_dic = {}
    titles = []
    todos = []
    total = len(response)
    done = 0
    for v in response:
        todo = {"task": v.get('title'), "completed": v.get('completed'),
                "username": username}
        todos.append(todo)
        if v.get("completed") is True:
            done += 1
            titles.append(v.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for i in titles:
        print("\t {}".format(i))
    todo_dic.update({2: todos})

    file = eid + ".json"
    with open(file, 'w', newline='') as f:
        json.dump(todo_dic, f)
