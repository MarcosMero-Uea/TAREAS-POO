class CuentaBancaria:
    def __init__(self, titular, saldo):
        # Atributos privados: solo accesibles dentro de la clase
        self.__titular = titular
        self.__saldo = saldo

    # Método público para depositar dinero
    def depositar(self, monto):
        self.__saldo += monto

    # Método público para retirar dinero, con una validación
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente.")

    # Método público para consultar el saldo
    def obtener_saldo(self):
        return self.__saldo

# Uso de la encapsulación
cuenta = CuentaBancaria("Juan", 500)  # Crear una cuenta con saldo inicial de 500
cuenta.depositar(200)  # Depositar 200
print(f"Saldo: {cuenta.obtener_saldo()}")  # Consultar el saldo actual
cuenta.retirar(1000)  # Intentar retirar más del saldo disponible (mensaje de error)