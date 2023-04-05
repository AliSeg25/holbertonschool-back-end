#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # On va chercher l'utilisateur et sa todo
    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_dict = response_url.json()
    employee_name = response_dict.get("username")

    response_url = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    response_dict = response_url.json()


    tasks = []
    for task in response_dict:
        tasks.append([employee_id, employee_name, task['completed'], task['title']])

    # Exportation des résultats au format CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)