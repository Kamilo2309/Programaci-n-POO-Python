#************************* CLASE HIJA *******************************
from vehiculo import Vehiculo

class Vehiculo_furgoneta(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    # Polimorfismo: se sobrescriben metodos del padre
    def aceleracion_frenado(self):
        return f"La furgoneta {self._modelo} acelera de forma moderada y frena con suavidad"

    def sistema_direccion(self):
        return "La furgoneta tiene direccion asistida para manejar con comodidad"

    def tipo_seguridad(self):
        return f"La furgoneta tiene cinturones para sus {self._capacidad_pasajeros} pasajeros"