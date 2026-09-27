# *************** CLASE HIJA *******************
from animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    # Polimorfismo: se sobrescriben metodos del padre
    def moverse(self):
        return f" El cocodrilo {self._nombre} se desplaza de manera diferente según esté en el agua o en la tierra, utilizando su cola y sus patas de forma adaptada a cada entorno"

    def comunicacion(self):
        return f"El cocodrilo {self._nombre} se comunica mediante sonidos, vibraciones bajo el agua, posturas corporales, olores y el tacto"

    def reproduccion(self):
        return f"El cocodrilo {self._nombre} se reproduce de forma sexual, tienen fecundación interna y son ovíparos (ponen huevos)"