
# PARTE 1) Restaurante:


class Restaurante :
    def __init__(self, restaurant_nombre,cocina_tipo):
        self.restaurant_nombre = restaurant_nombre
        self.cocina_tipo = cocina_tipo

def describe_restaurant():
        print (restaurante.restaurant_nombre,restaurante.cocina_tipo)


def abrir_restaurant():
        print('El Restaurante esta abierto')
    
restaurante = Restaurante ("Las Delicias", "Mariscos")

print(restaurante.restaurant_nombre)
print()
print(restaurante.cocina_tipo)

print()
describe_restaurant()
print()
abrir_restaurant()
print()
# PARTE 2) Tres restaurantes:
restaurante1 = Restaurante ("Las Delicias_1", "Pastas")
restaurante2 = Restaurante ("Las Delicias_2", "Vegetales")
restaurante3 = Restaurante ("Las Delicias_3", "Pasteles")

print(restaurante1.restaurant_nombre,restaurante.cocina_tipo)
print(restaurante2.restaurant_nombre,restaurante.cocina_tipo)
print(restaurante3.restaurant_nombre,restaurante.cocina_tipo)
