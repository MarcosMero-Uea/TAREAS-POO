class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para almacenar título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para almacenar los libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros Prestados: {[libro.info[0] for libro in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para garantizar unicidad de IDs

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario registrado: {usuario.nombre}")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # Se remueve del catálogo de disponibles
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Se vuelve a agregar al catálogo
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                    return
            print("Libro no encontrado en los préstamos del usuario.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, clave):
        resultados = [libro for libro in self.libros.values() if clave.lower() in libro.info[0].lower() or clave.lower() in libro.info[1].lower() or clave.lower() in libro.categoria.lower()]
        return resultados if resultados else "No se encontraron resultados."

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            return usuario.libros_prestados if usuario.libros_prestados else "No tiene libros prestados."
        else:
            return "Usuario no encontrado."


# Pruebas del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "5678")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Marcos", "001")
usuario2 = Usuario("Ana", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("001", "1234")

# Listar libros prestados
print(biblioteca.listar_libros_prestados("001"))

# Devolver libro
biblioteca.devolver_libro("001", "1234")

# Buscar libros
print(biblioteca.buscar_libro("Novela"))
