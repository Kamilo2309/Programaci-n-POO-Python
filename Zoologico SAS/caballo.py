# *************** CLASE HIJA *******************
from animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    # Polimorfismo: se sobrescriben metodos del padre
    def moverse(self):
        return f"El caballo {self._nombre} galopa con sus 4 patas"

    def comunicacion(self):
        return f"El caballo {self._nombre} relincha para comunicarse"

    def reproduccion(self):
        return f"El caballo {self._nombre} se reproduce de forma sexual mediante la fecundación interna"