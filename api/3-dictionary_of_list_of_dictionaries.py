#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
import requests

def get_all_tasks():
    response_url = requests.get("https://jsonplaceholder.typicode.com/users")
    employees = response_url.json()

    all_tasks = {}
    for employee in employees:
        employee_id = str(employee['id'])
        employee_name = employee['username']
        response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        response_dict = response_url.json()

        tasks = []
        for task in response_dict:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = employee_name
            tasks.append(task_dict)

        all_tasks[employee_id] = tasks

    return all_tasks

if __name__ == "__main__":
    tasks = get_all_tasks()

    # Exportation des résultats au format JSON
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as f:
        json.dump(tasks, f)
