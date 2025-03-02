import json
import os  # Importamos os para manejar rutas del sistema

# Definir la carpeta donde se almacenará el archivo JSON
CARPETA_PROYECTO = "DEBER SEMANA 11"
ARCHIVO_INVENTARIO = os.path.join(CARPETA_PROYECTO, "inventario.json")


class Producto:
    """Clase que representa un producto dentro del inventario."""
    
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un producto con ID, nombre, cantidad y precio."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad de un producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio de un producto."""
        self.precio = nuevo_precio

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario para guardarlo en JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Convierte un diccionario en un objeto Producto."""
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    """Clase que representa el inventario de la tienda, utilizando un diccionario para gestionar productos."""

    def __init__(self):
        """Inicializa el inventario y carga los productos desde un archivo si existe."""
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        if producto.id_producto in self.productos:
            print("⚠️ El producto con este ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("🗑️ Producto eliminado correctamente.")
        else:
            print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o precio de un producto en el inventario."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("✅ Producto actualizado correctamente.")
        else:
            print("⚠️ Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca un producto por su nombre y lo muestra."""
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"🔍 ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio}")
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            print("\n📦 Inventario de la Tienda:")
            for p in self.productos.values():
                print(f"🆔 {p.id_producto} | 📌 {p.nombre} | 📦 {p.cantidad} | 💲 {p.precio}")
        else:
            print("⚠️ El inventario está vacío.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo JSON dentro de la carpeta del proyecto."""
        if not os.path.exists(CARPETA_PROYECTO):
            os.makedirs(CARPETA_PROYECTO)

        with open(ARCHIVO_INVENTARIO, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        print(f"💾 Inventario guardado en '{ARCHIVO_INVENTARIO}'.")

    def cargar_desde_archivo(self):
        """Carga los datos del inventario desde el archivo JSON si existe."""
        if os.path.exists(ARCHIVO_INVENTARIO):
            with open(ARCHIVO_INVENTARIO, "r") as f:
                datos = json.load(f)
                self.productos = {p["id_producto"]: Producto.from_dict(p) for p in datos}
            print(f"📂 Inventario cargado desde '{ARCHIVO_INVENTARIO}'.")
        else:
            print("⚠️ Archivo de inventario no encontrado, iniciando con un inventario vacío.")


def menu():
    """Función que maneja la interfaz de usuario en la consola."""
    inventario = Inventario()

    while True:
        print("\n📋 MENÚ DE GESTIÓN DE INVENTARIO")
        print("1️⃣ Agregar producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto")
        print("5️⃣ Mostrar inventario")
        print("6️⃣ Salir Y guardar")
        opcion = input("👉 Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("🆔 Ingrese el ID del producto: ")
            nombre = input("📌 Ingrese el nombre del producto: ")
            cantidad = int(input("📦 Ingrese la cantidad: "))
            precio = float(input("💲 Ingrese el precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("🆔 Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("🆔 Ingrese el ID del producto a actualizar: ")
            cantidad = input("📦 Ingrese la nueva cantidad (deje en blanco si no quiere cambiarla): ")
            precio = input("💲 Ingrese el nuevo precio (deje en blanco si no quiere cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("🔍 Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida. Inténtelo de nuevo.")


if __name__ == "__main__":
    menu()