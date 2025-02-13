class Producto:
    # Clase que representa un producto con atributos ID, nombre, cantidad y precio
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"

class Inventario:
    # Clase que maneja una lista de productos y proporciona métodos para gestionarlos
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto al inventario, asegurándose de que el ID sea único
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario por su ID
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto específico por su ID
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre, permitiendo coincidencias parciales
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        for p in resultados:
            print(p)
        if not resultados:
            print("No se encontraron productos.")

    def mostrar_productos(self):
        # Muestra todos los productos en el inventario
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("Inventario vacío.")

def menu():
    # Función que muestra un menú interactivo para gestionar el inventario
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo producto al inventario
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            # Opción para eliminar un producto del inventario por ID
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Opción para actualizar la cantidad o el precio de un producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Opción para buscar productos por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Opción para mostrar todos los productos en el inventario
            inventario.mostrar_productos()

        elif opcion == "6":
            # Opción para salir del programa
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
