
# Task Manager CLI

This is a simple command-line interface (CLI) tool written in Python for managing tasks. The tool allows users to add, view, complete, and delete tasks, with persistence using a text file (`tasks.txt`), so tasks remain available across sessions.


## Features

- **Add a Task**: Add a new task with a description.
- **View Tasks**: List all current tasks.
- **Complete a Task**: Mark a task as completed, which removes it from the list.
- **Delete a Task**: Delete a task by its number.



## Installation
1. Ensure you have Python 3 installed. You can check by running:
   ```bash
   py -3 --version

## Usage
Running the Tool from the Command Line:
1. **Open a terminal** (Command Prompt, PowerShell, or a terminal emulator).
2. **Navigate to the directory where task_manager.py is located.** For example:
   ```bash
   cd path\to\your\script
3. Use the following commands to interact with the tool:

- Add a Task:
  ```bash
  py -3 task_manager.py add "Your task description here"
- View Tasks:
  ```bash
  py -3 task_manager.py list
- Complete a Task
  ```bash
  py -3 task_manager.py complete <task number>

- Delete a task:
  ```bash
  py -3 task_manager.py delete <task number>

## Requirements

- Python 3.x
## Task Manager Streamlit App

This is a simple task manager app built with Streamlit. The app allows users to add, view, mark as complete, and delete tasks. Tasks are stored in a `tasks.txt` file, ensuring they persist between sessions.

## - Features of Streamlit App
**Add a Task**: Users can add a task with a description, which is saved in `tasks.txt`.
- **View Tasks**:
  - **Pending Tasks**: Displays a list of tasks that are yet to be completed.
  - **Completed Tasks**: Shows tasks marked as completed, displayed with strikethrough.
- **Mark as Complete**: Tasks can be marked as completed, moving them to the "Completed Tasks" section.
- **Delete Tasks**: Both pending and completed tasks can be deleted individually, removing them from `tasks.txt`.

## How to Use

1. **Add a Task**: Enter a task description and click "Add Task."
2. **Mark as Complete**: In the "Pending Tasks" section, click "Complete" to move the task to "Completed Tasks."
3. **Delete a Task**:
   - **Pending Tasks**: Click "Delete" next to a task to remove it from the list and `tasks.txt`.
   - **Completed Tasks**: Click "Delete" next to a completed task to remove it from `tasks.txt`.

## Requirements

- **Python 3.7+**
- **Streamlit**: Install Streamlit with the following command:
  ```bash
  pip install streamlit
## How to run the App
1. **Clone the Repository**:
   Clone the repository from GitHub to your local machine by running the following commands in your terminal:

   ```bash
   git clone https://github.com/Mimanshadas25/task_manager_CLI
   cd task_manager_CLI

2. **Install Dependencies: Install the required dependencies by running:**
   ```bash
   pip install -r requirements.txt

3. **Run the App on Command Line: Start the Streamlit app by running:**
   ```bash
   streamlit run streamlit_task_manager.py

