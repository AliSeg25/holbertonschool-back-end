#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # On va chercher l'utilisateur et sa todo
    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_dict = response_url.json()
    employee_name = response_dict.get("name")

    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    response_dict = response_url.json()

    # On va compter le nombre de tâches faites et finies
    count, total = 0, 0
    completed_tasks = []
    for task in response_dict:
        total += 1
        if task['completed'] is True:
            count += 1
            completed_tasks.append(task['title'])

    # Affichage des résultats
    print("Employee {} is done with tasks({}/{}):".format(employee_name, count, total))
    for task in completed_tasks:
        print("\t " + task)
