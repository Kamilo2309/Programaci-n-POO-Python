#************************* CLASE HIJA *******************************
from botella import Botella

class BotellaPlastico(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("plastico", capacidad, forma, diseno, tapa, grabados)

    # Polimorfismo: se sobrescriben metodos del padre
    def transporte(self):
        return "La botella de plastico es liviana y facil de transportar"

    def compatibilidad(self):
        return "Compatible solo con bebidas frias"

    def reutilizacion(self):
        return "La botella de plastico se recomienda reciclar"