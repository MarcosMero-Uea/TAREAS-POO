# Programa en Python para calcular el promedio semanal del clima usando programación tradicional

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas de cada día de la semana.
    Retorna una lista con las temperaturas.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    """
    Recibe una lista de temperaturas y calcula el promedio.
    """
    suma = sum(temperaturas)  # Suma todas las temperaturas
    promedio = suma / len(temperaturas)  # Divide entre la cantidad de días
    return promedio

# Función principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA ===")
    temperaturas = ingresar_temperaturas()  # Entrada de datos
    promedio = calcular_promedio(temperaturas)  # Cálculo del promedio
    print(f"\nEl promedio semanal del clima es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()