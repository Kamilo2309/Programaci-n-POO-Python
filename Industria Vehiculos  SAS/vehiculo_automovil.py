# ************ Clase Hija *******************
from vehiculo import Vehiculo

class Vehiculo_automovil(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    # Polimorfismo: se sobrescriben metodos del padre
    def aceleracion_frenado(self):
        return f"El automovil {self._modelo} acelera rapido y tiene frenos deportivos"

    def sistema_direccion(self):
        return "El automovil tiene direccion electrica, agil y precisa"

    def tipo_seguridad(self):
        return "El automovil tiene airbags frontales y laterales"