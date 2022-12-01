#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    eid = sys.argv[1]
    name_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid).json()
    name = name_response['name']
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todos = []
    total = len(response)
    done = 0
    for v in response:
        if v['completed'] is True:
            done += 1
            todos.append(v['title'])
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for i in todos:
        print("\t {}".format(i))
