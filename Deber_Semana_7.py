# Clase Persona que utiliza constructores y destructores
class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor: Se activa cuando se crea una instancia de la clase.
        Inicializa los atributos 'nombre' y 'edad'.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Constructor llamado: Se ha creado a {self.nombre}, de {self.edad} años.")

    def saludar(self):
        """Método para que la persona salude."""
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """
        Destructor: Se activa cuando el objeto es eliminado o el programa termina.
        Realiza la limpieza necesaria.
        """
        print(f"Destructor llamado: {self.nombre} ha sido eliminado.")

# Código principal
if __name__ == "__main__":
    # Creación de una instancia de Persona
    persona1 = Persona("Marcos", 25)
    persona1.saludar()

    # Creación de otra instancia de Persona
    persona2 = Persona("Lucas", 30)
    persona2.saludar()

    # Eliminación explícita de los objetos
    del persona1
    del persona2

    print("Fin del programa.")