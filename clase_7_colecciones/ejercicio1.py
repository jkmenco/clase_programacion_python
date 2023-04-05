# Operaciones de conjuntos con listas

'''
Escriba un programa que tenga dos listas y que, acontinuacion,
cree las siguientes listas (en las que no debe haber repeticiones):

    > Lista de palabras que aparecen en las 2 listas
    > Lista de palabras que aparecen en la primera pero no en la segunda
    > Lista de palabras que aparecen en segunda pero no en la primera
    > Lista de palabras que aparecen en ambas listas
'''



print()
list1 = [1,2,3,4,5,8,10]
list2 = [2,4,6,7,8,9,11]
print('Tenemos 2 listas: ')
print(f"lista 1: {list1}\nLista 2: {list2}")
print()
# eliminacion de elementos duplicados
a = set(list1)
b = set(list2)

igualdad = a | b
diferencia1 = a - b
diferencia2 = b - a
interceccion = a & b

lista1 = list(igualdad)
lista2 = list(diferencia1)
lista3 = list(diferencia2)
lista4 = list(interceccion)
# list2 = list(set(list2))


print(f'Esta es la lista de datos que aparecen en las 2 listas\n{lista1}')
print()
print(f'Esta es la lista de datos que aparecen en la primera pero no en la segunda\n{lista2}')
print()
print(f'Esta es la lista de datos que aparecen en la segunda pero no en la primera\n{lista3}')
print()
print(f'Esta es la lista de datos que aparecen en ambas listas\n{lista4}')
print()