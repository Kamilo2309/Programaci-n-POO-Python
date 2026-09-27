from animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)