import argparse
from models.user import User


from rich.console import Console
from models.task import Task

from models.project import Project
from utils.storage import (
    load_users,
    save_users,
    load_projects,
    save_projects,
    load_tasks,
    save_tasks,
)

console = Console()


def list_users():
    """Display all users."""

    users = load_users()

    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    console.print("[bold green]Users[/bold green]")

    for user in users:
        console.print(
            f"- {user['id']}: {user['name']} ({user['email']})"
        )

def list_projects():
    """Display all projects."""

    projects = load_projects()

    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    console.print("[bold blue]Projects[/bold blue]")

    for project in projects:
        console.print(
            f"- {project['id']}: {project['title']}"
            f"(Due:  {project['due_date']})"

        )
        
def add_user(name, email):
    """Add a new user."""

    users = load_users()

    for user in users:
        if user["email"] == email:
            console.print("[red]A user with this email already exists.[/red]")
            return

    new_user = User(name, email)
    users.append(new_user.to_dict())

    save_users(users)

    console.print(f"[green]User '{name}' added successfully![/green]")            

def add_project(user_name, title, description, due_date):
    """Add a new project to an existing user."""

    users = load_users()
    projects= load_projects()

    user_exists = False

    for user in users:
        if user["name"].lower() == user_name.lower():
            user_exists = True
            break
    if not user_exists:
        console.print(f"[red]User '{user_name}' not found.[/red]")
        return
    project = Project(title, description, due_date)


    project_data = project.to_dict()
    project_data["user"] = user_name

    projects.append(project_data)
    save_projects(projects)

    console.print(
        f"[green]Project '{title}' added successfully![/green]"
    )

def add_task(project_title, title, assigned_to):
    """Add a task to an existing project."""

    projects = load_projects()
    tasks = load_tasks()

    project_exists = False


    for project in projects:
        if project["title"].lower() == project_title.lower():
            project_exists = True
            break
    if not project_exists:
            console.print(f"[red]Project '{project_title}' not found.[/red]")
            return
        
    task = Task(title, assigned_to)

    task_data = task.to_dict()
    task_data["project"] = project_title

    tasks.append(task_data)

    save_tasks(tasks)

    console.print(
            f"[green]Task '{title}' added successfully![/green]"
        )
def list_tasks():
    """Display all tasks."""
    tasks = load_tasks()

    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    console.print("[bold cyan]Tasks[/bold cyan]")

    for task in tasks:
        console.print(
            f"- {task['id']}: {task['title']} "
            f"[{task['status']}] "
            f"(Project: {task['project']}, Assigned to: {task['assigned_to']})"
        )

def complete_task(task_title):
    """Mark a task as completed."""

    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["title"].lower() == task_title.lower():
            task["status"] = "Completed"
            found = True
            break
    if not found:
        console.print(f"[red]Task '{task_title}' not found.[/red]")
        return
    save_tasks(tasks)

    console.print(
        f"[green]Task '{task_title}' marked as Completed![/green]"
    )  
def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "list-users",
        help="Display all users"
    )
    subparsers.add_parser(
        "list-projects",
        help="Display all projects"
    )
    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Add a new user"
    )
    add_user_parser.add_argument(
        "--name",
        required=True,
        help="User's name"
    )
    add_user_parser.add_argument(
        "--email",
        required=True,
        help="User's email"
    )
    subparsers.add_parser(
        "list-tasks",
        help="Display all tasks"
    )
    


    

    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Add a new project"
    )

    add_project_parser.add_argument(
        "--user",
        required=True,
        help="Owner of the project"
    )
    add_project_parser.add_argument(
        "--title",
        required=True,
        help="Project title"
    )
    add_project_parser.add_argument(
        "--description",
        required=True,
        help="Project description"
    )
    add_project_parser.add_argument(
        "--due-date",
        required=True,
        help="Project due date"
    )

    add_task_parser = subparsers.add_parser(
        "add-task",
        help="Add a task to a project"
    )

    add_task_parser.add_argument(
        "--project",
        required=True,
        help="Project title"
    )
    add_task_parser.add_argument(
        "--title",
        required=True,
        help="Task title"
    )
    add_task_parser.add_argument(
        "--assigned-to",
        required=True,
        help="Person assigned to the task"
    )
    complete_task_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as completed"
    )
    complete_task_parser.add_argument(
        "--title",
        required=True,
        help="Task title"
    )
    
    args = parser.parse_args()

    if args.command == "list-users":
        list_users()
    elif args.command == "list-projects":
        list_projects()
    elif args.command =="list-tasks":
        list_tasks()    
    elif args.command == "add-task":
        add_task(
            args.project,
            args.title,
            args.assigned_to
        )
    elif args.command == "complete-task":
        complete_task(args.title)            

    elif args.command =="add-user":
        add_user(args.name, args.email)
    elif args.command == "add-project":
        add_project(
            args.user,
            args.title,
            args.description,
            args.due_date
        )        
    else:
        parser.print_help()


if __name__ == "__main__":
    main()