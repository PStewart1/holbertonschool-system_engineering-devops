#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
dumps todo info into csv file """
import csv
import requests
import sys


if __name__ == "__main__":
    eid = sys.argv[1]
    name_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid).json()
    username = name_response.get("username")
    name = name_response.get("name")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + eid + "/todos").json()
    todos = []
    total = len(response)
    todos_csv = []
    for v in response:
        todo = [eid, username, v.get("completed"), v.get("title")]
        todos_csv.append(todo)
        if v.get("completed") is True:
            todos.append(v.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todos), total))
    for i in todos:
        print("\t {}".format(i))

    file = eid + ".csv"
    with open(file, 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=1)
        my_writer.writerows(todos_csv)
