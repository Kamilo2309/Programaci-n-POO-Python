class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados
        
    def Contener_Liquidos(self):
        print("Se Contiene el liquido")
    
    def facilitar_El_Vertido(self):
        print("Facilitado")

    def Cierre_Hermetico(self):
        print("No")
    
    def Transporte(self):
        print("Si")

    def Manejo(self):
        print("Aceptable")
    
    def Compatibilidad(self):
        print("Nulo")
        
    def Reutilizacion(self):
        print("Reutilizado")
        
    def Transparencia(self):
        print("Opaco")