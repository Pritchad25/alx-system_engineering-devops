#!/usr/bin/python3
"""
This Python script uses REST API, for a given employee ID,
and returns information about his/her TODO list progress.
"""
import csv
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

    data = []
    for todo in todos:
        title = todo.get("title")
        completed = todo.get("completed")
        data.append([user_id, username, completed, title])

    with open("{}.csv".format(user_id), 'w') as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
