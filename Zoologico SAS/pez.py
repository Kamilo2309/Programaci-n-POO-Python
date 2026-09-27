# *************** CLASE HIJA *******************
from animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    # Polimorfismo: se sobrescriben metodos del padre
    def moverse(self):
        return f" El pez {self._nombre} se mueve principalmente ondulando su cuerpo y batiendo la cola, utilizando sus aletas para dirigir el rumbo y equilibrarse"

    def comunicacion(self):
        return f"El pez {self._nombre} se comunican principalmente mediante sonidos, señales químicas y lenguaje visual"

    def reproduccion(self):
        return f"El pez {self._nombre} se reproduce principalmente de forma sexual mediante fecundación externa"