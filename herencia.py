# Clase base que define un método genérico hablar
class Animal:
    def hablar(self):
        pass  # Método vacío que será sobreescrito por las clases hijas

# Clase hija que hereda de Animal e implementa el método hablar
class Perro(Animal):
    def hablar(self):
        return "Guau"

# Otra clase hija que también implementa el método hablar
class Gato(Animal):
    def hablar(self):
        return "Miau"

# Uso de la herencia
animales = [Perro(), Gato()]  # Lista de objetos de diferentes clases hijas
for animal in animales:
    print(animal.hablar())  # Cada objeto utiliza su propia implementación del método hablar