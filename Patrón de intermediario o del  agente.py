from abc import ABC, abstractmethod

# Interfaz del Mediador
class ChatMediator(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje: str, usuario: 'Usuario') -> None:
        pass

# Implementación concreta del Mediador
class ChatRoom(ChatMediator):
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario: 'Usuario') -> None:
        self.usuarios.append(usuario)

    def enviar_mensaje(self, mensaje: str, emisor: 'Usuario') -> None:
        for usuario in self.usuarios:
            if usuario != emisor:
                usuario.recibir(mensaje)

# Clase base para los usuarios
class Usuario:
    def __init__(self, nombre: str, mediador: ChatMediator):
        self.nombre = nombre
        self.mediador = mediador

    def enviar(self, mensaje: str) -> None:
        print(f"{self.nombre} envía: {mensaje}")
        self.mediador.enviar_mensaje(mensaje, self)

    def recibir(self, mensaje: str) -> None:
        print(f"{self.nombre} recibe: {mensaje}")

# Tipos específicos de usuarios
class UsuarioRegular(Usuario):
    pass

class UsuarioAdmin(Usuario):
    def anunciar(self, anuncio: str) -> None:
        print(f"ANUNCIO de {self.nombre}: {anuncio}")
        self.mediador.enviar_mensaje(f"ANUNCIO: {anuncio}", self)

# Ejemplo de uso
if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = UsuarioRegular("Alice", chat_room)
    bob = UsuarioRegular("Bob", chat_room)
    charlie = UsuarioRegular("Charlie", chat_room)
    admin = UsuarioAdmin("Admin", chat_room)

    chat_room.agregar_usuario(alice)
    chat_room.agregar_usuario(bob)
    chat_room.agregar_usuario(charlie)
    chat_room.agregar_usuario(admin)

    alice.enviar("Hola a todos!")
    bob.enviar("Hola Alice, ¿cómo estás?")
    charlie.enviar("¡Hola chicos!")
    admin.anunciar("La reunión comienza en 5 minutos.")
