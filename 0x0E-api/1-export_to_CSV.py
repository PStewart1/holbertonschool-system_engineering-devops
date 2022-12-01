#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
returns information about his/her TODO list progress. """
import requests
import sys
import csv


if __name__ == "__main__":
    eid = sys.argv[1]
    name_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid).json()
    name = name_response['username']
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todos = []
    for v in response:
        todo = [eid, name, v['completed'], v['title']]
        todos.append(todo)
    file = eid + ".csv"
    with open(file, 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=1)
        my_writer.writerows(todos)
