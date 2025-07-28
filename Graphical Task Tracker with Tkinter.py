import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class TaskTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Tracker")
        self.root.geometry("400x400")
        self.tasks = []
        self.load_tasks()
        self.create_widgets()
    
    def create_widgets(self):
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)
        self.task_entry = tk.Entry(entry_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(entry_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT)
        
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)
        self.task_listbox = tk.Listbox(list_frame, width=40, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Remove Task", command=self.remove_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_tasks).pack(side=tk.LEFT, padx=5)
        
        self.update_listbox()
    
    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                self.tasks = [line.strip() for line in file if line.strip()]
    
    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showerror("Error", "Task cannot be empty!")
            return
        if task in self.tasks:
            messagebox.showerror("Error", "Task already exists!")
            return
        self.tasks.append(task)
        self.save_tasks()
        self.update_listbox()
        self.task_entry.delete(0, tk.END)
    
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            if messagebox.askyesno("Confirm", f"Remove: {task}?"):
                del self.tasks[selected_index]
                self.save_tasks()
                self.update_listbox()
        except IndexError:
            messagebox.showerror("Error", "No task selected!")
    
    def clear_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "Task list is already empty!")
            return
        if messagebox.askyesno("Confirm", "Clear ALL tasks?"):
            self.tasks = []
            self.save_tasks()
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTracker(root)
    root.mainloop()