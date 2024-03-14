from Personaa import Persona

class Profesion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sueldo_total = 0
        self.cantidad_personas = 0

    def agregar_persona(self, sueldo):
        self.sueldo_total += sueldo
        self.cantidad_personas += 1

def obtener_porcentaje(total, cantidad):
    if total == 0:
        return 0
    return (cantidad / total) * 100