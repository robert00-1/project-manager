import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_users():
    return load_data(USERS_FILE)


def save_users(users):
    save_data(USERS_FILE, users)


def load_projects():
    return load_data(PROJECTS_FILE)


def save_projects(projects):
    save_data(PROJECTS_FILE, projects)


def load_tasks():
    return load_data(TASKS_FILE)


def save_tasks(tasks):
    save_data(TASKS_FILE, tasks)