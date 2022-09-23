# diccionarios (clave, valor) no existen indices, se usa las keys o llaves
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Programacion orientada a objetos',
    'DBMS': 'Database Management System'
}

print(diccionario)
# largo
print(len(diccionario))

# acceder a un elemento (key); se acceden por las llaves
print(diccionario['IDE'])
# otra forma de acceder a los elementos
print(diccionario.get('OOP'))
# modificando los elementos
diccionario['IDE'] = 'Programacion java'
print(diccionario)

# recorrer los elementos del diccionario
for clave, valor in diccionario.items():  # <- diccionario.items() recuperamos clave y el valor
    print(clave, valor)

for clave in diccionario.keys():  # <- recuperando las llaves
    print(clave)

for valor in diccionario.values(): #<- recuperando los valores
    print(valor)

# coprobar la existencia de un elemento
print('IDE' in diccionario) #<- debemos respetar las mayusulas y minusculas

#agregar u elemento
diccionario['PK'] = 'clave primaria'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar el diccionario
diccionario.clear()
print(diccionario)

# borrar de la memoria el diccionario
del diccionario
print(diccionario)