#************************* CODIGO PRINCIPAL *******************************
from vehiculo_automovil import Vehiculo_automovil
from vehiculo_furgoneta import Vehiculo_furgoneta
from vehiculo_camion import Vehiculo_camion

# Se crean los objetos
automovil = Vehiculo_automovil("Z4", "negro", "2.0 turbo", 2, 2, "gasolina")
furgoneta = Vehiculo_furgoneta("Hiace", "blanco", "2.5", 4, 8, "diesel")
camion = Vehiculo_camion("NPR", "blanco", "5.2", 2, 3, "diesel")

# Get y Set
print("--- Get y Set ---")
print("Modelo del automovil:", automovil.get_modelo())
print("Color del automovil:", automovil.get_color())
automovil.set_color("rojo")
print("Nuevo color del automovil:", automovil.get_color())

# Metodos heredados del padre
print("\n--- Metodos heredados ---")
print(automovil.arranque())
print(furgoneta.climatizacion())
print(camion.luces())
print(furgoneta.sistema_ventanas())
print(automovil.sistema_espejo())

# Polimorfismo: mismo metodo, distinta respuesta
print("\n--- Automovil ---")
print(automovil.aceleracion_frenado())
print(automovil.sistema_direccion())
print(automovil.tipo_seguridad())

print("\n--- Furgoneta ---")
print(furgoneta.aceleracion_frenado())
print(furgoneta.sistema_direccion())
print(furgoneta.tipo_seguridad())

print("\n--- Camion ---")
print(camion.aceleracion_frenado())
print(camion.sistema_direccion())
print(camion.tipo_seguridad())

# Se apagan los vehiculos
print("\n--- Apagado ---")
print(automovil.apagado())
print(furgoneta.apagado())
print(camion.apagado())