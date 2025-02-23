import os

class Producto:
    # Clase que representa un producto con atributos ID, nombre, cantidad y precio
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(producto_str):
        # Convierte una línea de texto en un objeto Producto
        try:
            id_producto, nombre, cantidad, precio = producto_str.strip().split(',')
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            print("Error al convertir los datos del producto. Verifique el formato del archivo.")
            return None

class Inventario:
    # Clase que maneja una lista de productos y proporciona métodos para gestionarlos
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        # Guarda la lista de productos en un archivo con manejo de excepciones
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        # Carga los productos desde un archivo si existe, manejando excepciones
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r") as f:
                    self.productos = [Producto.from_string(linea) for linea in f if linea.strip()]
                self.productos = [p for p in self.productos if p is not None]  # Filtrar productos inválidos
            except FileNotFoundError:
                print("El archivo de inventario no se encontró, se creará uno nuevo.")
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
        else:
            # Si el archivo no existe, se crea automáticamente
            with open(self.ARCHIVO_INVENTARIO, "w") as f:
                pass

    def agregar_producto(self, producto):
        # Agrega un producto al inventario y lo guarda en archivo con manejo de duplicados
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario por su ID y actualiza el archivo
        if any(p.id_producto == id_producto for p in self.productos):
            self.productos = [p for p in self.productos if p.id_producto != id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto específico por su ID
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre, permitiendo coincidencias parciales
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
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
            try:
                id_producto = input("ID del producto: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: Entrada inválida, ingrese valores correctos.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
