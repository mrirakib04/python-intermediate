import sys
import os
import json

todo_file = "todos.json"


def load_todos():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(todo_file, "w") as f:
        json.dump(todos, f, indent=2)


def add_task(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Task added: {task}")


def list_tasks():
    todos = load_todos()
    print("--- Todo List ---")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "add":
            task = " ".join(sys.argv[2:])
            add_task(task)
        elif cmd == "list":
            list_tasks()
        else:
            print("Usage: python todo_cli.py [add <task> | list]")
