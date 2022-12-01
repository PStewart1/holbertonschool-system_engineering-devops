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
    name = name_response.get("username")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todos = []
    total = len(response)
    done = 0
    for v in response:
        if v.get("completed") is True:
            done += 1
            todos.append(v.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for i in todos:
        print("\t {}".format(i))

    todos_csv = []
    for v in response:
        todo = [eid, name, v.get("completed"), v.get("title")]
        todos_csv.append(todo)
    file = eid + ".csv"
    with open(file, 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=1)
        my_writer.writerows(todos)
