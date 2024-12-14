from abc import ABC, abstractmethod

# Clase abstracta que define un método común para todos los vehículos
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        """Método abstracto que debe ser implementado por las clases derivadas."""
        pass

# Clase concreta que hereda de Vehiculo e implementa el método mover
class Carro(Vehiculo):
    def mover(self):
        print("El carro se mueve en 4 ruedas.")

# Otra clase concreta que también implementa el método mover
class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta se mueve en 2 ruedas.")

# Uso de la abstracción: trabajamos con objetos de las clases concretas
vehiculos = [Carro(), Bicicleta()]
for v in vehiculos:
    v.mover()  # Cada objeto ejecuta su propia implementación del método mover