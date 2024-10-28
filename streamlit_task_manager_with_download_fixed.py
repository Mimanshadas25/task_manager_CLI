
#import required libraries
import streamlit as st

# File where tasks will be stored
TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task = line.strip()  
                tasks.append(task)
    except FileNotFoundError:
        pass  # return an empty task list if file not found
    return tasks

def save_tasks(tasks):
    # Save tasks to the tasks file without completion status.
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task_description):
    tasks = load_tasks()
    tasks.append(task_description)
    save_tasks(tasks)

# Streamlit App
st.title("Task Manager")

st.header("Add a new task")
task_description = st.text_input("Task Description")

if st.button("Add Task"):
    if task_description:
        add_task(task_description)
        st.success(f"Task '{task_description}' added successfully!")
    else:
        st.warning("Please enter a task description.")

# Display Tasks
st.header("Current Tasks")
tasks = load_tasks()
if tasks:
    for task in tasks:
        st.write(f"- {task}")
else:
    st.info("No tasks available.")

# Download Tasks
st.header("Download Tasks")
st.download_button(
    label="Download tasks as text file",
    data=open(TASKS_FILE, "rb").read(),
    file_name="tasks.txt",
    mime="text/plain"
)
