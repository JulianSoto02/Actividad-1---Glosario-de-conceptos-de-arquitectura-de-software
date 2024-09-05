class Pipe:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_func):
        self.filters.append(filter_func)

    def execute(self, data):
        for filter_func in self.filters:
            data = filter_func(data)
        return data

def to_uppercase(data):
    return data.upper()

def remove_spaces(data):
    return data.replace(" ", "")

def add_prefix(data):
    return "Procesado: " + data

# Uso del patrón
if __name__ == "__main__":
    # Crear la tubería
    pipeline = Pipe()

    # Agregar filtros
    pipeline.add_filter(to_uppercase)
    pipeline.add_filter(remove_spaces)
    pipeline.add_filter(add_prefix)

    # Datos de entrada
    input_data = "Hola Mundo"

    # Ejecutar la tubería
    result = pipeline.execute(input_data)

    print(f"Entrada: {input_data}")
    print(f"Salida: {result}")
