# objetos = ['juan', 'karla', 'Ricardo', 'Maria', 0, 100, True] #<- en una lista puede tener tod tipo de objetos

nombres = ['juan', 'Karla', 'Ricardo', 'Maria', 'luis']

print(nombres)
# acceder a los elementos de  una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de forma de forma inverda, lo hacemos con numeros negativos
print(nombres[-1])
print(nombres[-2])
# imprimir un rango
print(nombres[0:2])  # sin incluir el indice apartir del indice2
# IR del inicio de la lista al indice 3 (el 3 no se incluye para adelante)
print(nombres[:3])
# Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# preguntar el largo de una lista
print(len(nombres))
#agregar un elemento
nombres.append('Lorenzo')
print(nombres)
#insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
#remueve el ultimo valor agregado y lo retorna
nombres.pop()
print(nombres)
#eliminar un indice
del nombres[0]
print(nombres)
#limpiar la lista
nombres.clear()
print(nombres)
#borrar la lista por completo (de la memoria)
del nombres
print(nombres)
