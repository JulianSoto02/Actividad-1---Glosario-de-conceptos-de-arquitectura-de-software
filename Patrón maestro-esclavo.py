import threading
import queue
import time
import random

class Tarea:
    def __init__(self, id, duracion):
        self.id = id
        self.duracion = duracion

    def ejecutar(self):
        print(f"Ejecutando tarea {self.id}")
        time.sleep(self.duracion)
        print(f"Tarea {self.id} completada")

class Esclavo(threading.Thread):
    def __init__(self, id, cola_tareas):
        threading.Thread.__init__(self)
        self.id = id
        self.cola_tareas = cola_tareas

    def run(self):
        while True:
            tarea = self.cola_tareas.get()
            if tarea is None:
                break
            print(f"Esclavo {self.id} procesando tarea {tarea.id}")
            tarea.ejecutar()
            self.cola_tareas.task_done()

class Maestro:
    def __init__(self, num_esclavos):
        self.cola_tareas = queue.Queue()
        self.esclavos = []
        for i in range(num_esclavos):
            esclavo = Esclavo(i, self.cola_tareas)
            self.esclavos.append(esclavo)
            esclavo.start()

    def agregar_tarea(self, tarea):
        self.cola_tareas.put(tarea)

    def esperar_finalizacion(self):
        self.cola_tareas.join()

    def detener_esclavos(self):
        for _ in self.esclavos:
            self.cola_tareas.put(None)
        for esclavo in self.esclavos:
            esclavo.join()

def main():
    maestro = Maestro(num_esclavos=3)

    # Crear algunas tareas
    for i in range(10):
        tarea = Tarea(i, random.randint(1, 3))
        maestro.agregar_tarea(tarea)

    # Esperar a que todas las tareas se completen
    maestro.esperar_finalizacion()

    # Detener los esclavos
    maestro.detener_esclavos()

    print("Todas las tareas han sido completadas")

if __name__ == "__main__":
    main()
