# Clase base
class Ave:
    def volar(self):
        print("Algunas aves pueden volar.")  # Método genérico

# Clase hija que sobrescribe el comportamiento del método volar
class Pinguino(Ave):
    def volar(self):
        print("Los pingüinos no pueden volar.")  # Implementación específica

# Uso del polimorfismo
aves = [Ave(), Pinguino()]  # Lista de objetos que comparten la misma base
for ave in aves:
    ave.volar()  # Llama al método correspondiente dependiendo del tipo del objeto