#************************* CLASE HIJA *******************************
from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("vidrio", capacidad, forma, diseno, tapa, grabados)

    # Polimorfismo: se sobrescriben metodos del padre
    def transporte(self):
        return "La botella de vidrio es fragil, se debe transportar con cuidado"

    def compatibilidad(self):
        return "Compatible con bebidas calientes y frias"

    def reutilizacion(self):
        return "La botella de vidrio se puede lavar y reutilizar muchas veces"