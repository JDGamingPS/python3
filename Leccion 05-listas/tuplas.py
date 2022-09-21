# una lista es modificable
#una tupla no se puede modificar los elemtos (inmutable)
#defibnir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
#saber el largo
print(len(frutas))
print(frutas)
#acceder a un elemento en particular
print(frutas[0])
# navegacion inversa
print(frutas[-1]) # accede al ultimo elemento
# acceder a un rango de valores
print(frutas[0:1]) # va hasta antes del 1 o inidice indicado
# si la tupla tiene un elemento se debe colar una coma ejemplo: tupla('naranja',)

# recorrer elementos en tupla
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla; convertir la tupla a lista
#frutas[0] = 'Pera'
frutaList = list(frutas)
frutaList[0] = 'Pera'
frutas = tuple(frutaList)
print('\n', frutas)
#borrar la tupla de la memoria
del frutas
