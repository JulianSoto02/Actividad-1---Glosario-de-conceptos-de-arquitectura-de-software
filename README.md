# Capa de Lógica de Negocio
class Libro:
    def __init__(self, id, titulo, autor, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

# Capa de Acceso a Datos
class RepositorioLibros:
    def __init__(self):
        self.libros = {}

    def agregar(self, libro):
        self.libros[libro.id] = libro

    def obtener(self, id):
        return self.libros.get(id)

    def listar(self):
        return list(self.libros.values())

# Capa de Lógica de Negocio
class ServicioCatalogo:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def agregar_libro(self, libro):
        self.repositorio.agregar(libro)

    def buscar_libro(self, id):
        return self.repositorio.obtener(id)

    def listar_libros(self):
        return self.repositorio.listar()

    def prestar_libro(self, id):
        libro = self.buscar_libro(id)
        if libro:
            return libro.prestar()
        return False

# Capa de Aplicación
class ControladorLibros:
    def __init__(self, servicio_catalogo):
        self.servicio_catalogo = servicio_catalogo

    def crear_libro(self, titulo, autor, isbn):
        id = len(self.servicio_catalogo.listar_libros()) + 1
        nuevo_libro = Libro(id, titulo, autor, isbn)
        self.servicio_catalogo.agregar_libro(nuevo_libro)
        return nuevo_libro

    def obtener_libro(self, id):
        return self.servicio_catalogo.buscar_libro(id)

    def listar_libros(self):
        return self.servicio_catalogo.listar_libros()

    def prestar_libro(self, id):
        return self.servicio_catalogo.prestar_libro(id)

# Simulación de uso
if __name__ == "__main__":
    repositorio = RepositorioLibros()
    servicio_catalogo = ServicioCatalogo(repositorio)
    controlador = ControladorLibros(servicio_catalogo)

    # Crear algunos libros
    libro1 = controlador.crear_libro("Don Quijote", "Miguel de Cervantes", "9788424112912")
    libro2 = controlador.crear_libro("Cien años de soledad", "Gabriel García Márquez", "9780307474728")

    # Listar libros
    print("Libros en el catálogo:")
    for libro in controlador.listar_libros():
        print(f"{libro.titulo} por {libro.autor}")

    # Prestar un libro
    id_libro = 1
    if controlador.prestar_libro(id_libro):
        print(f"Libro con ID {id_libro} prestado exitosamente")
    else:
        print(f"No se pudo prestar el libro con ID {id_libro}")

    # Intentar prestar el mismo libro de nuevo
    if controlador.prestar_libro(id_libro):
        print(f"Libro con ID {id_libro} prestado exitosamente")
    else:
        print(f"No se pudo prestar el libro con ID {id_libro} porque ya está prestado")
