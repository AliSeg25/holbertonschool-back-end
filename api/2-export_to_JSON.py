#!/usr/bin/python3
"""
Using what you did in the task #0,
 extend your Python script to export data in the JSON format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # On va chercher l'utilisateur et sa todo
    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_dict = response_url.json()
    employee_name = response_dict.get("username")

    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    response_dict = response_url.json()

    tasks = []
    for task in response_dict:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = employee_name
        tasks.append(task_dict)

    # Exportation des résultats au format JSON
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as f:
        json.dump({employee_id: tasks}, f)