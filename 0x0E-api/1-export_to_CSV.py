#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
dumps todo info into csv file """
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
        todo = [eid, name, v.get('completed'), v.get('title')]
        todos.append(todo)
    file = eid + ".csv"
    with open(file, 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=1)
        my_writer.writerows(todos)
