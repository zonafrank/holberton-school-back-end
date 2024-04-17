#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress
"""

import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_user_todos(user_id):
    """for a given employee ID, returns information about
    his/her TODO list progress
    """
    res = requests.get(f"{BASE_URL}/users/{user_id}")
    user = res.json()
    res = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    todos = res.json()
    return {"user": user, "todos": todos}


def export_to_json(obj):
    """Writer user todos data to json file"""
    user = obj["user"]
    todos = obj["todos"]

    result_obj = {}
    result_obj[user["id"]] = [
        {"task": item["title"],
         "completed": item["completed"],
         "username": user["username"]} for item in todos]

    filename = f"{user['id']}.json"
    with open(filename, "w", newline="") as out_file:
        json.dump(result_obj, out_file)


if __name__ == "__main__":
    _, id = sys.argv
    obj = get_user_todos(id)
    export_to_json(obj)
