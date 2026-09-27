# *************** CLASE HIJA *******************
from animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    # Polimorfismo: se sobrescriben metodos del padre
    def moverse(self):
        return f" El escarabajo {self._nombre} se mueve principalmente caminando con sus seis patas, pero la también tiene la capacidad de volar"

    def comunicacion(self):
        return f"El escarabajo {self._nombre} se comunica principalmente a través de la química, el sonido y las vibraciones"

    def reproduccion(self):
        return f"El escarabajo {self._nombre} reproduce sexualmente por fecundación interna, pone huevos y se transforma de larva a adulto mediante metamorfosis completa"