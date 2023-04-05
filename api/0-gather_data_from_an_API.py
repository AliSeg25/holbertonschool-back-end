#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def Return_employer_todolist(employee_id):
    # On va chercher l'utilisateur et sa todo

    response_dict = requests.get(f"https://jsonplaceholder.typicode.com/users/\
    {employee_id}/todos").json()

    # On va compter le nombre de task fait et fini
    count, total = 0, 0
    completed_tasks = []
    for task in response_dict:
        total += 1
        if task['completed'] is True:
            count += 1
            completed_tasks.append(task['title'])

    employee_name = requests.get(f"https://jsonplaceholder.typicode.com/users/\
    {employee_id}").json().get("name")
    print(f"Employee {employee_name} is done with tasks({count}/{total}):")
    for task in completed_tasks:
        print("\t " + task)
