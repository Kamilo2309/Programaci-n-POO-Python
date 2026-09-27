# *************** CLASE HIJA *******************
from animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    # Polimorfismo: se sobrescriben metodos del padre
    def moverse(self):
        return f" El pato {self._nombre} se mueve principalmente caminando, nadando y volando gracias a sus adaptaciones físicas"

    def comunicacion(self):
        return f"El pato {self._nombre} se comunica principalmente mediante sonidos, lenguaje corporal y rituales visuales."

    def reproduccion(self):
        return f"El pato {self._nombre} se reproduce de forma sexual mediante fecundación interna, y se destaca por ser una de las pocas especies de aves en las que los machos cuentan con un órgano reproductor definido para la cópula"