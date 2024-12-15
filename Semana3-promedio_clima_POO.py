# Programa en Python para calcular el promedio semanal del clima usando Programación Orientada a Objetos (POO)

# Definición de la clase Clima
class Clima:
    def __init__(self):
        """
        Constructor de la clase Clima.
        Inicializa la lista de temperaturas vacía.
        """
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar temperaturas diarias.
        """
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de las temperaturas.
        """
        if len(self.temperaturas) == 0:
            return 0  # Evita la división por cero
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

# Función principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima_semana = Clima()  # Creación de una instancia de la clase Clima
    clima_semana.ingresar_temperaturas()  # Ingreso de datos
    promedio = clima_semana.calcular_promedio()  # Cálculo del promedio
    print(f"\nEl promedio semanal del clima es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()