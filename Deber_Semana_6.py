# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Atributo privado para demostrar encapsulación

    # Método público para acceder al atributo privado
    def get_edad(self):
        return self.__edad

    # Método público para modificar el atributo privado
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

    # Método genérico
    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.__edad} años."


# Clase derivada (Herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera

    # Sobrescritura de método (Polimorfismo)
    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.get_edad()} años y estudio {self.carrera}."


# Función principal
def main():
    # Instancia de la clase base
    persona = Persona("Carlos", 45)
    print(persona.presentarse())

    # Modificación del atributo privado
    persona.set_edad(50)
    print(persona.presentarse())

    # Instancia de la clase derivada
    estudiante = Estudiante("Ana", 22, "Ingeniería en Sistemas")
    print(estudiante.presentarse())


# Llamada a la función principal
if __name__ == "__main__":
    main()
