import os
os.system('cls')


# PARTE 1) Restaurante:
numero_servicio=0
n=0
s=""
class Restaurante:

    def __init__(self, restaurant_nombre,cocina_tipo,numero_servicio=0):
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
print()
print(restaurante1.restaurant_nombre,restaurante.cocina_tipo)
print(restaurante2.restaurant_nombre,restaurante.cocina_tipo)
print(restaurante3.restaurant_nombre,restaurante.cocina_tipo)
print()
# PARTE 3) Número servicio: 
print()
while s!='s':
    print()
    s=str(input('Otro Nombre ( "S"=Finalizar "Enter" = Continuar  :)'))
    s=s.lower()
    if s!="s":
        n= n + 1
        print()
        print("Atendiendo al cliente   :",n)
        numero_servicio=numero_servicio + 1

def set_numero_servicio():
    print("Atendiendo al cliente    :",numero_servicio)

def incrementar_numero_servicio():
    print()
    os.system('cls')
    print(restaurante.restaurant_nombre)
    print("Número de clientes atendidos en el día  :",numero_servicio)


set_numero_servicio()
incrementar_numero_servicio()