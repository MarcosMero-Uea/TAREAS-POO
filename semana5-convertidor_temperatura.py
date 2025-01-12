# convertidor_temperatura.py
"""
Este programa permite convertir temperaturas entre Celsius, Fahrenheit y Kelvin.
El usuario puede elegir la escala de origen y destino, e ingresar el valor de la temperatura.
"""

def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    """Convierte Celsius a Kelvin."""
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def kelvin_a_celsius(kelvin):
    """Convierte Kelvin a Celsius."""
    return kelvin - 273.15

def convertir_temperatura():
    """Gestiona la conversión de temperaturas según la selección del usuario."""
    print("Bienvenido al Convertidor de Temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Kelvin a Celsius")

    opcion = int(input("Seleccione una opción (1-4): "))
    temperatura = float(input("Ingrese el valor de la temperatura a convertir: "))

    if opcion == 1:
        print(f"{temperatura} °C son {celsius_a_fahrenheit(temperatura):.2f} °F")
    elif opcion == 2:
        print(f"{temperatura} °C son {celsius_a_kelvin(temperatura):.2f} K")
    elif opcion == 3:
        print(f"{temperatura} °F son {fahrenheit_a_celsius(temperatura):.2f} °C")
    elif opcion == 4:
        print(f"{temperatura} K son {kelvin_a_celsius(temperatura):.2f} °C")
    else:
        print("Opción no válida.")

# Llamada principal
if __name__ == "__main__":
    convertir_temperatura()
