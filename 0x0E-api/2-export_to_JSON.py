#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
dumps todo info into csv file """
import json
import requests
import sys


if __name__ == "__main__":
    eid = sys.argv[1]
    name_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid).json()
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    name = name_response.get("name")
    username = name_response.get('username')
    titles = []
    for v in response:
        if v.get("completed") is True:
            titles.append(v.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(titles), len(response)))
    for i in titles:
        print("\t {}".format(i))

    todos = []
    for v in response:
        todo = {"task": v.get('title'), "completed": v.get('completed'),
                "username": username}
        todos.append(todo)
    todo_dic = {eid: todos}

    with open("{}.json".format(eid), 'w') as f:
        json.dump(todo_dic, f)
