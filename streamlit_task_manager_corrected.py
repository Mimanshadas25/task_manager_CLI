
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
        pass  #return an empty task list
    return tasks

def save_tasks(tasks):
    """Save tasks to the tasks file without completion status."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(description):
    """Add a new task with the given description."""
    tasks = load_tasks()
    tasks.append(description)  
    save_tasks(tasks)
    st.session_state["refresh_trigger"] += 1  # Trigger a refresh

def complete_task(task_number):
    """Mark a task as completed by its index (in memory only)."""
    if "completed_tasks" not in st.session_state:
        st.session_state["completed_tasks"] = set()
    st.session_state["completed_tasks"].add(task_number)  # Mark as completed in memory

def delete_task(task_number):
    """Delete a task by its index."""
    tasks = load_tasks()
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
    save_tasks(tasks)
    st.session_state["refresh_trigger"] += 1  # Trigger a refresh

# Streamlit interface
st.title("Task Manager")

# Initialize session state to control refresh and track completed tasks in memory
if "refresh_trigger" not in st.session_state:
    st.session_state["refresh_trigger"] = 0
if "completed_tasks" not in st.session_state:
    st.session_state["completed_tasks"] = set()

# Adding a new task
st.subheader("Add a new task")
task_description = st.text_input("Task Description")
if st.button("Add Task"):
    if task_description:
        add_task(task_description)
        st.success(f'Task added: "{task_description}"')
    else:
        st.error("Please enter a task description.")

# Separate tasks into pending and completed lists
st.subheader("Pending Tasks")
tasks = load_tasks()
if tasks:
    for i, task in enumerate(tasks):
        if i not in st.session_state["completed_tasks"]:  # Only show pending tasks here
            col1, col2, col3 = st.columns([6, 2, 2])
            with col1:
                st.write(f"{i + 1}. {task}")
            with col2:
                if st.button("Complete", key=f"complete_{i}"):
                    complete_task(i)  # Mark as complete in memory only
            with col3:
                if st.button("Delete", key=f"delete_{i}"):
                    delete_task(i)
else:
    st.write("No pending tasks found.")

# Show completed tasks with delete button
st.subheader("Completed Tasks")
completed_task_list = [tasks[i] for i in st.session_state["completed_tasks"] if i < len(tasks)]
if completed_task_list:
    for i, completed_task in enumerate(completed_task_list):
        task_index = list(st.session_state["completed_tasks"])[i]  # Original index in the tasks list
        col1, col2 = st.columns([8, 2])
        with col1:
            st.write(f"~~{completed_task}~~")
        with col2:
            if st.button("Delete", key=f"delete_completed_{task_index}"):
                delete_task(task_index)
else:
    st.write("No completed tasks.")

st.caption("Tasks are saved in tasks.txt and persist between sessions. Completed tasks are in memory and can be deleted.")
