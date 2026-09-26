#************************* CODIGO PRINCIPAL *******************************
from botella_vidrio import BotellaVidrio
from botella_plastico import BotellaPlastico

# Se crean los objetos
botella1 = BotellaVidrio(750, "alargada", "clasico", "corcho", "logo en relieve")
botella2 = BotellaPlastico(600, "cilindrica", "moderno", "rosca", "sin grabados")

# Get y Set
print("Material:", botella1.get_material())
print("Capacidad:", botella2.get_capacidad())
botella2.set_capacidad(1000)
print("Nueva capacidad:", botella2.get_capacidad())

# Metodos heredados
print("\n--- Metodos heredados ---")
print(botella1.contener_liquidos())
print(botella1.cierre_hermetico())
print(botella2.manejo())

# Polimorfismo: mismo metodo, distinta respuesta
print("\n--- Botella de vidrio ---")
print(botella1.transporte())
print(botella1.compatibilidad())
print(botella1.reutilizacion())

print("\n--- Botella de plastico ---")
print(botella2.transporte())
print(botella2.compatibilidad())
print(botella2.reutilizacion())
