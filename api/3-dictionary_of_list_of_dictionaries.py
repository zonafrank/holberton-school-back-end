#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress
"""

import sys
import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_users():
    """get all users in db"""
    res = requests.get(f"{BASE_URL}/users")
    return res.json()


def get_user_todos(user_id):
    """for a given employee ID, returns information about
    his/her TODO list progress
    """
    res = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    todos = res.json()
    return todos


def get_all_users_todos():
    result = {}
    users = get_users()
    for user in users:
        todos = get_user_todos(user["id"])
        result[user["id"]] = [
            {"username": user["username"],
             "task": item["title"],
             "completed": item["completed"]
             }
            for item in todos
        ]
    return result


def export_to_json(obj):
    """Writer user todos data to json file"""

    filename = "todo_all_employees.json"
    with open(filename, "w", newline="") as out_file:
        json.dump(obj, out_file)


if __name__ == "__main__":
    obj = get_all_users_todos()
    export_to_json(obj)
