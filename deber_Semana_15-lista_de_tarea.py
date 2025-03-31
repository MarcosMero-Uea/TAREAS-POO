import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")
        
        self.entrada_tarea = tk.Entry(self.root, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.bind("<Return>", self.agregar_con_enter)
        
        self.btn_agregar = tk.Button(self.root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack()
        
        self.lista_tareas = tk.Listbox(self.root, width=50, height=15)
        self.lista_tareas.pack(pady=10)
        
        self.btn_completar = tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.pack()
        
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack()
    
    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")
    
    def marcar_completada(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(indice)
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(tk.END, f"✔ {tarea}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")
    
    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")
    
    def agregar_con_enter(self, event):
        self.agregar_tarea()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
