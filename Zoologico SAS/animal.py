#******************* CLASE PADRE ***********************
class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._dieta = dieta
        self._tamano = tamano
        self._color = color

    # ************ GET Y SET ***************
    # Nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    # Edad
    def get_edad(self):
        return self._edad

    def set_edad(self, nuevo_valor):
        if (nuevo_valor >= 0):
            self._edad = nuevo_valor
        else:
            print(f"La edad no puede ser negativa")

    # Habitat
    def get_habitat(self):
        return self._habitat

    def set_habitat(self, nuevo_valor):
        self._habitat = nuevo_valor

    # Dieta
    def get_dieta(self):
        return self._dieta

    def set_dieta(self, nuevo_valor):
        self._dieta = nuevo_valor

    # Tamaño
    def get_tamano(self):
        return self._tamano

    def set_tamano(self, nuevo_valor):
        self._tamano = nuevo_valor

    # Color
    def get_color(self):
        return self._color

    def set_color(self, nuevo_valor):
        self._color = nuevo_valor

    # ************ METODOS ***************
    def moverse(self):
        return f"El animal {self._nombre} se mueve por su habitat: {self._habitat}"

    def comunicacion(self):
        return f"El animal {self._nombre} se comunica con otros de su especie"

    def reproduccion(self):
        return f"El animal {self._nombre} se reproduce para tener crias"

    def alimentarse(self):
        return f"El animal {self._nombre} se alimenta con una dieta {self._dieta}"

    def adaptacion(self):
        return f"El animal {self._nombre} esta adaptado para vivir en {self._habitat}"

    def instintos(self):
        return f"El animal {self._nombre} huye o se defiende cuando siente peligro"

    def descanso(self):
        return f"El animal {self._nombre} descansa para recuperar energia"

    def sueno(self):
        return f"El animal {self._nombre} duerme"

    def interaccion_social(self):
        return f"El animal {self._nombre} se relaciona con otros animales"