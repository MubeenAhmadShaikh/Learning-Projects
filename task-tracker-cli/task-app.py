import argparse
import os
import json
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file, create file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        # Create empty JSON file
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks dictionary to JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

GLOBAL_TASKS = {
}
def add(args):
    tasks = load_tasks()
    task_id = args.id
    now = datetime.now().isoformat()
    tasks.append({
        "id": task_id,
        "description": args.description,
        "status": args.status,
        "createdAt": now,
        "updatedAt": ''
    })
    save_tasks(tasks)
    print(f"Task added with ID {task_id}: {args.description}")

def update(args):
    tasks = load_tasks()
    task_id = args.id
    now = datetime.now().isoformat()
    if len(tasks) == 0:
        print("No tasks exist to update First create one")
        return
    for task in tasks:
        if task['id'] == task_id:
            if args.description:
                task["description"] = args.description
            if args.status:
                task["status"] = args.status
            task["updatedAt"] = now
    save_tasks(tasks)
    print(f"Task updated with ID {task_id}")

def delete(args):
    tasks = load_tasks()
    task_id = args.id
    if len(tasks) == 0:
        print("No tasks exist to delete")
        return
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
    save_tasks(tasks)
    print(f"Task deleted with ID {task_id}")
def list_tasks(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    else:
        if not args.status:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At : {task['createdAt']}, Updated At : {task['updatedAt']}")
        else:
            for task in tasks:
                if task['status'] == args.status:
                    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Updated At : {task['updatedAt']}")
def done(args):
    print(f"Marking task {args.task_id} as done")


parser = argparse.ArgumentParser(description="Welcome to your personal Task Tracker")
subparsers = parser.add_subparsers(dest="command")

# Add
add_parser = subparsers.add_parser("create_task", help="Add a new task")
add_parser.add_argument("--id",type=int, required=True)
add_parser.add_argument("--description")
add_parser.add_argument("--status", choices=["todo","in-progress","done"], default="todo")
add_parser.set_defaults(func=add)

# Update
add_parser = subparsers.add_parser("update_task", help="Update an existing task")
add_parser.add_argument("--id", type=int, required=True)
add_parser.add_argument("--description")
add_parser.add_argument("--status",  choices=["todo","in-progress","done"], default="todo")
add_parser.set_defaults(func=update)


# Delete
add_parser = subparsers.add_parser("delete_task", help="deleting a task")
add_parser.add_argument("--id", type=int, required=True)
add_parser.set_defaults(func=delete)

# List
list_parser = subparsers.add_parser("list_task", help="List all tasks")
list_parser.add_argument("--status", nargs="?")
list_parser.set_defaults(func=list_tasks)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()