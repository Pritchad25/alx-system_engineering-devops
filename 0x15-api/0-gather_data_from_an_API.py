#!/usr/bin/python3
"""
This Python script uses a REST API, for a given employee ID,
 and returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url + "users/{}".format(user_id))
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    if res.status_code != 200:
        print("User not found")
        exit(1)

    emp_name = res.json().get("name")

    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(completed), len(todos)))
    for todo in completed:
        print("\t " + todo.get("title"))
