#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress
"""

import csv
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


def write_to_file(obj):
    """Writer user todos data to csv file"""
    user = obj["user"]
    todos = obj["todos"]

    with open(f"{user['id']}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([f'{user["id"]}',
                             f'{user["name"]}', f'{todo["completed"]}',
                             f'{todo["title"]}'])


if __name__ == "__main__":
    _, id = sys.argv
    obj = get_user_todos(id)
    write_to_file(obj)
