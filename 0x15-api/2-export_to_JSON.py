#!/usr/bin/python3
"""
This Python script uses a REST API, for a given employee ID,
and returns information about his/her TODO list progress.
"""
import json
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

    username = res.json().get("username")

    data = {user_id: []}
    for todo in todos:
        title = todo.get("title")
        completed = todo.get("completed")
        data[user_id].append({
            "task": title,
            "completed": completed,
            "username": username
            })

    with open("{}.json".format(user_id), 'w') as json_f:
        json.dump(data, json_f)
