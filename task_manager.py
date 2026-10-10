import json
from pathlib import Path
from datetime import datetime


TASK_FILE = Path(__file__).with_name("tasks.json")

def current_time(): 
    """Return the current time in ISO format."""
    return datetime.now().isoformat()

def load_json(path):
    """Return the list stored in the file, or [] if missing/empty."""
    if not path.exists() or path.stat().st_size == 0:
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, records):
    print(f"Saving to: {Path(path).resolve()}")
    with open(path, "w") as f:
        json.dump(records, f, indent=2)

class Task:
    STATUS = {'todo', 'in_progress', 'done'}
    def __init__(self, description, status="todo", created_at=None, id=None,update_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at or current_time()
        self.updated_at = update_at or current_time()

        if status not in self.STATUS:
            raise ValueError(f"Invalid status: {status}. Must be one of {self.STATUS}")

        self.id = id or self.generate_id()
        self.description = description
        self.status = status
        self.created_at = created_at or current_time()
        self.update_at = update_at or current_time()

    def generate_id(self):
        """Generate a unique ID for the task."""
        tasks = load_json(TASK_FILE)
        if not tasks:
            return 1
        return max(task['id'] for task in tasks) + 1

    def update(self, description=None, status=None):
        """Update the task's description and/or status."""
        if description is not None:
            self.description = description
        if status is not None:
            if status not in self.STATUS:
                raise ValueError(f"Invalid status: {status}. Must be one of {self.STATUS}")
            self.status = status
        self.update_at = current_time()

    def to_dict(self):
        """Return a dictionary representation of the task."""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "update_at": self.update_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            status=data["status"],
            id=data["id"],
            created_at=data["created_at"],
            update_at=data["update_at"],
        )


class TaskManager():

    def __init__(self, task_file=TASK_FILE):
        self.task_file = task_file
        self.tasks = [Task(**task) for task in load_json(task_file)]

    def add_task(self, description):
        """Add a new task with the given description."""
        next_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(description, id=next_id)
        self.tasks.append(task)
        save_json(self.task_file, [task.to_dict() for task in self.tasks])
        print(f"Task created. ID: {task.id}")

    def update_task(self, task_id, description=None, status=None):
        """Update an existing task by ID."""
        task = self.get_task(task_id)
        if task:
            task.update(description, status)
            save_json(self.task_file, [task.to_dict() for task in self.tasks])
            print(f"Task updated. ID: {task.id}")
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def get_task(self, task_id):
        """Retrieve a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        """Return a list of all tasks."""
        return self.tasks

    def remove_task(self, task_id):
        """Remove a task by ID."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            save_json(self.task_file, [task.to_dict() for task in self.tasks])
            print(f"Task deleted. ID: {task.id}")
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    def remove_all_tasks(self):
        """Remove all tasks."""
        self.tasks.clear()
        save_json(self.task_file, [task.to_dict() for task in self.tasks])
        print("All tasks have been deleted.")
