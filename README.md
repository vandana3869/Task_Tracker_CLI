# Task Tracker CLI

A small command-line task tracker written in Python. Tasks are saved locally in
`tasks.json`.

## Requirements

- Python 3.8 or newer

The project uses only Python's standard library; no packages need to be
installed.

## Project URL

[Task Tracker CLI on GitHub](https://github.com/vandana3869/Task_Tracker_CLI)


## Run the application

Open Command Prompt or PowerShell, change to the project directory, and run:

```cmd
cd C:\Users\van13\python\Task_Track_CLI
py main.py
```

If the `py` command is unavailable, use:

```cmd
python main.py
```

## Menu options

When the program starts, choose an option:

1. **Add task** — enter a task description. The application assigns an ID,
   sets the initial status to `todo`, and records creation and update times.
2. **Update task** — enter a task ID, then provide a replacement description
   and/or status. Press Enter to keep a value unchanged.
3. **List tasks** — display all saved tasks.
4. **Delete task** — enter a task ID to remove that task.
5. **Exit** — close the application.

Statuses supported by the `Task` class are `todo`, `in_progress`, and `done`.

## Data storage

The application reads and writes `tasks.json` in the same directory as
`task_manager.py`. It creates the file when you add a task if it does not
already exist. Each task is stored with this structure:

```json
{
  "id": 1,
  "description": "Example task",
  "status": "todo",
  "created_at": "2026-10-11T10:00:00",
  "update_at": "2026-10-11T10:00:00"
}
```

Do not edit the JSON structure or field names unless you also update
`task_manager.py` to match.


 https://github.com/vandana3869/Task_Tracker_CLI
