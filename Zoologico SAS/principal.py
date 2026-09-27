# ***************** CODIGO PRINCIPAL ***************
from caballo import Caballo
from cocodrilo import Cocodrilo
from escarabajo import Escarabajo
from pato import Pato
from pez import Pez

# Se crean los objetos
caballo = Caballo("Spirit", 5, "la pradera", "herbivora", "grande", "cafe")
cocodrilo = Cocodrilo("Coco", 20, "rios y pantanos", "carnivora", "grande", "verde oscuro")
escarabajo = Escarabajo("Rino", 1, "la selva", "herbivora", "pequeño", "cafe rojizo")
pato = Pato("Donald", 3, "lagos y lagunas", "omnivora", "mediano", "verde y cafe")
pez = Pez("Nemo", 2, "arrecifes de coral", "omnivora", "pequeño", "amarillo y azul")

# ************ GET Y SET *******************
print("--- Get y Set ---")
print("Nombre del caballo:", caballo.get_nombre())
print("Edad del caballo:", caballo.get_edad())
caballo.set_edad(6)
print("Nueva edad del caballo:", caballo.get_edad())
caballo.set_edad(-1)

print("Habitat del pato:", pato.get_habitat())
pato.set_habitat("el parque del zoologico")
print("Nuevo habitat del pato:", pato.get_habitat())

print("Dieta del cocodrilo:", cocodrilo.get_dieta())
print("Color del pez:", pez.get_color())
print("Tamano del escarabajo:", escarabajo.get_tamano())

# ************ METODOS HEREDADOS *******************
print("\n--- Metodos heredados ---")
print(caballo.alimentarse())
print(cocodrilo.adaptacion())
print(pez.instintos())
print(escarabajo.interaccion_social())
print(pato.adaptacion())

# ************ POLIMORFISMO *******************
animales = [caballo, cocodrilo, pez, escarabajo, pato]

for animal in animales:
    print(f"\n--- {animal.get_nombre()} ---")
    print(animal.moverse())
    print(animal.comunicacion())
    print(animal.reproduccion())