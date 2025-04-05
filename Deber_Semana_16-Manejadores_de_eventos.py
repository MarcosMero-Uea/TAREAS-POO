import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=('Arial', 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Vincular eventos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

        # Lista interna para almacenar tareas
        self.tasks = []

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()
        else:
            messagebox.showinfo("Selecciona una tarea", "Primero selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showinfo("Selecciona una tarea", "Primero selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"[✓] {task['text']}" if task["completed"] else task["text"]
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, fg="gray")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
