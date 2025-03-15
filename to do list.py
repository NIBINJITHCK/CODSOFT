import tkinter as tk
from tkinter import messagebox
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓ " if task["done"] else "• "
        color = "green" if task["done"] else "red"
        task_listbox.insert(tk.END, f"{status}{task['task']}")
        task_listbox.itemconfig(i, {'fg': color})

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        del tasks[index]
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def exit_app():
    root.destroy()

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="lightblue")

task_entry = tk.Entry(root, width=40, bg="yellow", fg="black")
task_entry.pack(pady=10)

task_add_btn = tk.Button(root, text="Add Task", command=add_task, bg="blue", fg="white")
task_add_btn.pack()

task_listbox = tk.Listbox(root, width=50, height=10, bg="white")
task_listbox.pack(pady=10)

mark_done_btn = tk.Button(root, text="Mark Done", command=mark_done, bg="green", fg="white")
mark_done_btn.pack()

delete_task_btn = tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_task_btn.pack()

exit_btn = tk.Button(root, text="Exit", command=exit_app, bg="black", fg="white")
exit_btn.pack()

update_task_list()

root.mainloop()
