#************************* CLASE HIJA *******************************
from vehiculo import Vehiculo


class Vehiculo_camion(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)

    # Polimorfismo: se sobrescriben metodos del padre
    def aceleracion_frenado(self):
        return f"El camion {self._modelo} acelera lento y usa frenos de aire por su peso"

    def sistema_direccion(self):
        return "El camion tiene direccion hidraulica para hacer giros amplios"

    def tipo_seguridad(self):
        return "El camion tiene cabina reforzada y proteccion para la carga"