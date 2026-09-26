# ************ Clase padre *******************
class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self._material = material
        self._capacidad = capacidad
        self._forma = forma
        self._diseno = diseno
        self._tapa = tapa
        self._grabados = grabados
        
    # ************ GET Y SET ******************
    # Material
    def get_material(self):
        return self._material

    def set_material(self, valor_nuevo):
        self._material = valor_nuevo
        
    # Capacidad
    def get_capacidad(self):
        return self._capacidad

    def set_capacidad(self, nuevo_valor):
        if nuevo_valor > 0:
            self._capacidad = nuevo_valor
        else:
            print("La capacidad debe ser mayor a 0")

    # Forma
    def get_forma(self):
        return self._forma

    def set_forma(self, valor_nuevo):
        self._forma = valor_nuevo

    # Diseño
    def get_diseno(self):
        return self._diseno

    def set_diseno(self, valor_nuevo):
        self._diseno = valor_nuevo

    # Tapa
    def get_tapa(self):
        return self._tapa

    def set_tapa(self, valor_nuevo):
        self._tapa = valor_nuevo

    # Grabados
    def get_grabados(self):
        return self._grabados

    def set_grabados(self, valor_nuevo):
        self._grabados = valor_nuevo

    # ************* Metodos ***************
    def contener_liquidos(self):
        return f"La botella contiene hasta {self._capacidad} ml de liquido"

    def facilitar_vertido(self):
        return "La botella facilita el vertido del liquido"

    def cierre_hermetico(self):
        return f"La botella se cierra hermeticamente con tapa {self._tapa}"

    def transporte(self):
        return "La botella se puede transportar"

    def manejo(self):
        return f"La botella se maneja por su forma {self._forma}"

    def compatibilidad(self):
        return "Compatible con bebidas"

    def reutilizacion(self):
        return "La botella se puede reutilizar"

    def transparencia(self):
        return "La botella es transparente"