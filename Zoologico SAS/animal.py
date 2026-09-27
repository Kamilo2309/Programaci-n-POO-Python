#******************* CLASE PADRE ***********************
class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._dieta = dieta
        self._tamano = tamano
        self._color = color

    # ************ SET Y GET ***************
    # Nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    # Edad