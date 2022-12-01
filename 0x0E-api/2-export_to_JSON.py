#!/usr/bin/python3
"""script uses a public api, for a given employee ID,
dumps todo info into csv file """


def get_json():
    import csv
    import json
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    toDo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    completedTask = []

    for task in toDo:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completedTask), len(toDo)))
    for task in completedTask:
        print("\t {}".format(task))

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in toDo:
            writer.writerow([int(id), user.get("username"),
                            task.get("completed"), task.get("title")])

    jsonTask = []
    for task in toDo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user.get("username")
        jsonTask.append(task_dict)
    json_dict = {}
    json_dict[id] = jsonTask
    with open("{}.json".format(id), "w") as file:
        json.dump(json_dict, file)


if __name__ == '__main__':
    get_json()
