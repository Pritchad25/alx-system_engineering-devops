#!/usr/bin/python3
"""
This Python script uses REST API, for a given employee ID,
and returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url + "users")

    if res.status_code != 200:
        print("not found")
        exit(1)

    tasks = {}
    for user in res.json():
        user_id = user.get("id")
        username = user.get("username")

        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        data = []
        for todo in todos:
            title = todo.get("title")
            completed = todo.get("completed")
            data.append({
                "username": username,
                "task": title,
                "completed": completed
                })
        tasks[user_id] = data

    with open("todo_all_employees.json", 'w') as json_f:
        json.dump(tasks, json_f)
