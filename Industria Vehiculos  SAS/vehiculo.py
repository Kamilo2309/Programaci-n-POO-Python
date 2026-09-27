# ************ Clase padre *******************
class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self._modelo = modelo
        self._color = color
        self._motor = motor
        self._numero_puertas = numero_puertas
        self._capacidad_pasajeros = capacidad_pasajeros
        self._tipo_combustible = tipo_combustible
    # ************ GET Y SET ******************
    # Modelo
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, nuevo_valor):
        self._modelo = nuevo_valor

    # Color
    def get_color(self):
        return self._color

    def set_color(self, nuevo_valor):
        self._color = nuevo_valor

    # Motor
    def get_motor(self):
        return self._motor

    def set_motor(self, nuevo_valor):
        self._motor = nuevo_valor

    # Numero Puertas
    def get_numeroPuertas(self):
        return self._numero_puertas

    def set_numeroPuertas(self, nuevo_valor):
        self._numero_puertas = nuevo_valor

    # Capacidad Pasajeros
    def get_capacidadPasajeros(self):
        return self._capacidad_pasajeros

    def set_capacidadPasajeros(self, nuevo_valor):
        self._capacidadPasajeros = nuevo_valor

    # Tipo Combustible
    def get_tipoCombustible(self):
        return self._tipo_combustible

    def set_tipoCombustible(self, nuevo_valor):
        self._tipo_combustible = nuevo_valor

    # ************* Metodos ***************
    def arranque(self):
        return f"El vehiculo {self._modelo} enciende su motor {self._motor}"

    def apagado(self):
        return f"El vehiculo {self._modelo} apaga su motor {self._motor}"

    def aceleracion_frenado(self):
        return f"El vehiculo {self._modelo} acelera con motor a {self._tipo_combustible} y frena con el pedal"

    def sistema_direccion(self):
        return f"El {self._modelo} vehiculo gira con el volante"

    def climatizacion(self):
        return f"El vehiculo {self._modelo} enciende el aire acondicionado"

    def tipo_seguridad(self):
        return f"El vehiculo {self._modelo} tiene cinturones para {self._capacidad_pasajeros} pasajeros"

    def luces(self):
        return f"El vehiculo {self._modelo} enciende las luces delanteras y traseras"

    def sistema_ventanas(self):
        return f"El vehiculo {self._modelo} sube y baja las ventanas de sus {self._numero_puertas} puertas"

    def sistema_espejo(self):
        return f"El vehiculo {self._modelo} ajusta los espejos retrovisores"