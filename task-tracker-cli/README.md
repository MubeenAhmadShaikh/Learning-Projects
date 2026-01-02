# Task Tracker CLI App

A **Command-Line Task Tracker** built in Python. This app allows you to manage tasks directly from your terminal, storing all task data in a JSON file.

---

## Features

- Add, update, and delete tasks
- Mark tasks as **todo**, **in-progress**, or **done**
- List all tasks or filter tasks by status
- Tasks are stored in a **JSON file** (`tasks.json`) in the current directory
- Handles errors and edge cases gracefully

---

## Requirements

- Python 3.x
- No external libraries required

---

## Installation

1. Clone the repository or download the `task-app.py` file.
2. Ensure Python 3 is installed on your system.
3. Navigate to the project directory in your terminal.

---

## Usage

The app is run from the **command line** using **positional arguments** and subcommands.

### Run the app:

```bash
python task-app.py <command> [options]
```

### 1. Create a Task

```bash
python task-app.py create_task --id <task_id> --description "<task_description>" --status <status>
```
 - id → Integer ID for the task (required)
 - description → Description of the task 
 - status → One of todo, in-progress, done (default: todo)

#### Example:

```bash
- python task-app.py create_task --id 1 --description "Create a task tracker CLI app using Python" --status todo
- python task-app.py create_task --id 2 --description "Create web app using Python" --status done
```

### 2. Update a Task

```bash
python task-app.py update_task --id <task_id> --description "<new_description>" --status <new_status>
```
 - Updates the task description and/or status 
 - Updates the updatedAt timestamp automatically

#### Example:

```bash
python task-app.py update_task --id 1 --description "Updated description" --status done
```

### 3. Delete a Task

```bash
python task-app.py delete_task --id <task_id>
```

 - Deletes the task with given --id 

#### Example:

```bash
python task-app.py delete_task --id 1
```
**Note:** If no tasks exist, the app will notify you gracefully.

### 4. List Tasks

```bash
python task-app.py list_task [--status <status>]
```
 - Lists all tasks if no status is provided 
 - Lists tasks filtered by todo, in-progress, or done if --status is used

#### Example:

```bash
# List all tasks
python task-app.py list_task

# List tasks with status "in-progress"
python task-app.py list_task --status in-progress

# List tasks with status "todo"
python task-app.py list_task --status todo
```

#### Output Example:

```bash
# List all tasks
ID: 1, Description: Create a task tracker CLI app using Python, Status: todo, Created At: 2026-01-03T12:00:00, Updated At:
ID: 2, Description: Create web app using Python, Status: done, Created At: 2026-01-03T12:05:00, Updated At:
```