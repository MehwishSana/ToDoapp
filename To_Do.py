import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

# Input Field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task List
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Remove Task Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()
