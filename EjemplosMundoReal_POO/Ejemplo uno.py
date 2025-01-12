#sistema de reservas para un hotel
# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            return f"Habitación {self.numero} reservada con éxito."
        return f"Habitación {self.numero} no está disponible."

    def liberar(self):
        """Marca la habitación como disponible."""
        if not self.disponible:
            self.disponible = True
            return f"Habitación {self.numero} liberada con éxito."
        return f"Habitación {self.numero} ya está disponible."

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} - {estado}"


# Clase que representa el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al sistema."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones y su estado."""
        for habitacion in self.habitaciones:
            print(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        """Busca habitaciones disponibles por tipo."""
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and habitacion.disponible:
                return habitacion
        return None


# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaReservas()

    # Agregando habitaciones
    sistema.agregar_habitacion(Habitacion(101, "Simple", 50))
    sistema.agregar_habitacion(Habitacion(102, "Doble", 75))
    sistema.agregar_habitacion(Habitacion(103, "Suite", 150))

    print("Habitaciones iniciales:")
    sistema.mostrar_habitaciones()

    # Reservar una habitación
    habitacion = sistema.buscar_habitacion_disponible("Doble")
    if habitacion:
        print(habitacion.reservar())
    else:
        print("No hay habitaciones disponibles de este tipo.")

    print("\nHabitaciones después de la reserva:")
    sistema.mostrar_habitaciones()
