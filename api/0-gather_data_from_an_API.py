#!/usr/bin/python3
"""for a given employee ID, returns information about
    his/her TODO list progress
"""

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
    completed_todos = [todo for todo in todos if todo["completed"]]
    stats = f"{len(completed_todos)}/{len(todos)}"
    print(f"Employee {user['name']} is done with tasks ({stats}):")
    for todo in completed_todos:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    _, id = sys.argv
    get_user_todos(id)
