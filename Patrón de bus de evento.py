from typing import Callable, Dict, List
import time

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable) -> None:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable) -> None:
        if event_type in self._subscribers and callback in self._subscribers[event_type]:
            self._subscribers[event_type].remove(callback)

    def publish(self, event_type: str, data: dict) -> None:
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                callback(data)

# Componentes del sistema
class UserManager:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.event_bus.subscribe("user_registered", self.handle_user_registered)

    def register_user(self, username: str) -> None:
        print(f"Registrando usuario: {username}")
        self.event_bus.publish("user_registered", {"username": username})

    def handle_user_registered(self, data: dict) -> None:
        print(f"UserManager: Nuevo usuario registrado - {data['username']}")

class EmailService:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.event_bus.subscribe("user_registered", self.send_welcome_email)

    def send_welcome_email(self, data: dict) -> None:
        print(f"EmailService: Enviando email de bienvenida a {data['username']}")

class AnalyticsService:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.event_bus.subscribe("user_registered", self.log_user_registration)

    def log_user_registration(self, data: dict) -> None:
        print(f"AnalyticsService: Registrando estadística de nuevo usuario - {data['username']}")

# Uso del sistema
if __name__ == "__main__":
    event_bus = EventBus()

    user_manager = UserManager(event_bus)
    email_service = EmailService(event_bus)
    analytics_service = AnalyticsService(event_bus)

    user_manager.register_user("alice")
    time.sleep(1)  # Simular un poco de tiempo entre registros
    user_manager.register_user("bob")

    # Demostrar la desuscripción
    print("\nDesuscribiendo EmailService del evento user_registered")
    event_bus.unsubscribe("user_registered", email_service.send_welcome_email)

    time.sleep(1)
    user_manager.register_user("charlie")
