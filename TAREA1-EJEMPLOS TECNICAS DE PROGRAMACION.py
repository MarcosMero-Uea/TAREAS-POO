from abc import ABC, abstractmethod

# ===========================
# Abstracción
# ===========================
# La abstracción se logra utilizando clases abstractas y métodos abstractos.
# Esto permite definir una estructura que las clases hijas deben implementar.

class Vehiculo(ABC):  # Clase abstracta
    @abstractmethod
    def moverse(self):
        """Método abstracto que obliga a las clases hijas a implementarlo"""
        pass

# ===========================
# Encapsulación
# ===========================
# La encapsulación protege los atributos privados de una clase y permite acceder a ellos mediante métodos.

class Automovil(Vehiculo):
    def __init__(self, marca, ruedas):
        self.__marca = marca  # Atributo privado
        self.__ruedas = ruedas  # Atributo privado

    # Métodos para acceder a los atributos privados (getters y setters)
    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def get_ruedas(self):
        return self.__ruedas

    # Implementación del método abstracto
    def moverse(self):
        return f"El automóvil {self.__marca} se mueve en {self.__ruedas} ruedas."

# ===========================
# Herencia
# ===========================
# La herencia permite que una clase hija herede atributos y métodos de una clase padre.

class Motocicleta(Automovil):  # Hereda de Automovil
    def __init__(self, marca, ruedas, tipo_motor):
        super().__init__(marca, ruedas)  # Llama al constructor de la clase padre
        self.__tipo_motor = tipo_motor  # Atributo adicional para Motocicleta

    # Sobrescritura del método moverse para adaptarlo a Motocicleta
    def moverse(self):
        return f"La motocicleta {self.get_marca()} con motor {self.__tipo_motor} se mueve en {self.get_ruedas()} ruedas."

# ===========================
# Polimorfismo
# ===========================
# El polimorfismo permite usar un mismo método en diferentes clases con comportamientos distintos.

class Bicicleta(Vehiculo):
    def __init__(self, marca, ruedas):
        self.marca = marca
        self.ruedas = ruedas

    # Implementación del método abstracto
    def moverse(self):
        return f"La bicicleta {self.marca} se mueve en {self.ruedas} ruedas."

# ===========================
# Ejecución y Ejemplos
# ===========================

# Creamos instancias de cada clase
automovil = Automovil("Toyota", 4)      # Ejemplo de Encapsulación
motocicleta = Motocicleta("Honda", 2, "1000cc")  # Ejemplo de Herencia
bicicleta = Bicicleta("BMX", 2)         # Ejemplo de Polimorfismo

# Lista de vehículos para demostrar polimorfismo
vehiculos = [automovil, motocicleta, bicicleta]

# Mostrar cómo se mueven los vehículos
for vehiculo in vehiculos:
    print(vehiculo.moverse())

# Demostración de Encapsulación
print("\nDemostración de Encapsulación:")
print(f"Marca del automóvil: {automovil.get_marca()}")
automovil.set_marca("Ford")  # Modificar el atributo privado usando un setter
print(f"Marca del automóvil actualizada: {automovil.get_marca()}")