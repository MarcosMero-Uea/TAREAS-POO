import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        """
        Constructor de la clase. Configura la ventana principal y los elementos de la GUI.
        """
        self.root = root
        self.root.title("Aplicación GUI Básica")  # Título de la ventana
        self.root.geometry("500x350")  # Dimensiones de la ventana
        self.root.configure(bg="lightgray")  # Color de fondo

        # Encabezado
        self.header = tk.Label(self.root, text="Aplicación GUI básica", font=("Arial", 16, "bold"), bg="green", fg="white")
        self.header.pack(fill=tk.X)  # Se expande horizontalmente

        # Contenedor principal
        self.frame = tk.Frame(self.root, bg="lightgray")
        self.frame.pack(pady=10)

        # Etiqueta y campo de texto para ingresar datos
        self.etiqueta = tk.Label(self.frame, text="Agrega tu nombre", font=("Arial", 12, "bold"), bg="lightgray")
        self.etiqueta.grid(row=0, column=0, padx=10, pady=5)
        
        self.entrada = tk.Entry(self.frame, width=30)  # Campo de entrada de texto
        self.entrada.grid(row=0, column=1, padx=10, pady=5)

        # Botón para seleccionar todos los elementos de la lista
        self.btn_seleccionar_todo = tk.Button(self.frame, text="Seleccionar todo", command=self.seleccionar_todo, relief="solid", borderwidth=2)
        self.btn_seleccionar_todo.grid(row=1, column=0, padx=10, pady=5)

        # Botón para agregar datos a la lista
        self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_dato, relief="solid", borderwidth=2)
        self.btn_agregar.grid(row=1, column=1, padx=10, pady=5)

        # Lista donde se almacenan los datos ingresados
        self.lista = tk.Listbox(self.root, selectmode=tk.MULTIPLE)  # Permite seleccionar múltiples elementos
        self.lista.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

        # Botón para limpiar la selección en la lista
        self.btn_limpiar = tk.Button(self.root, text="Limpiar selección", command=self.limpiar_lista, relief="solid", borderwidth=2)
        self.btn_limpiar.pack(pady=5)

    def agregar_dato(self):
        """
        Agrega un dato ingresado en el campo de entrada a la lista.
        Si el campo está vacío, muestra una advertencia.
        """
        dato = self.entrada.get()
        if dato:
            self.lista.insert(tk.END, dato)  # Agrega el dato al final de la lista
            self.entrada.delete(0, tk.END)  # Borra el campo de entrada después de agregar
        else:
            messagebox.showwarning("Advertencia", "Ingrese un dato válido.")

    def limpiar_lista(self):
        """
        Elimina los elementos seleccionados en la lista.
        Si no hay elementos seleccionados, muestra un mensaje de error.
        """
        seleccion = self.lista.curselection()  # Obtiene los índices de los elementos seleccionados
        if seleccion:
            for index in reversed(seleccion):  # Se eliminan en orden inverso para evitar errores de índice
                self.lista.delete(index)
        else:
            messagebox.showerror("Error", "Seleccione un dato.")

    def seleccionar_todo(self):
        """
        Selecciona todos los elementos de la lista.
        """
        self.lista.select_set(0, tk.END)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = AplicacionGUI(root)  # Instanciar la aplicación
    root.mainloop()  # Ejecutar el bucle principal de Tkinter