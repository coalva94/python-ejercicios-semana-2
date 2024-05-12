"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva./*
"""

print('*** Pizzeria Napolitana ***')
print(f'''Tenemos las siguientes pizzas:
1: Pizza vegetariana
2: Pizza no vegetariana ''')
tipo = input('Escriba el número del tipo de pizza que desee pedir: ')
if tipo == '1':
    print('Los ingredientes de la pizza vegetariana son: \n1: Pimiento \n2: Toffu')
    ingrediente = input('Escoja el número del ingrediente que desea: ')
    print('Ha obtenido una pizza vegetariana con mozarella, tomate y ',end='')
    if ingrediente == '1':
        print('Pimiento')
    else:
        print('Toffu')
else:
    print('Los ingredientes de la pizza no vegetariana son: \n1: Peperoni \n2: Jamón \n3: Salmón')
    ingredientes = input('Escoja el número del ingrediente que desea: ')
    print('Ha obtenido una pizza no vegetariana con mozarella, tomate y ', end = '')
    if ingredientes == '1':
        print('Peperoni')
    elif ingredientes =='2':
        print('Jamón')
    else:
        print('Salmón')
