#Set, el orden no esta presente en el set{}
planetas = {'marte', 'Jupiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento esta presente
print('marte' in planetas)
# agregar mas elemtnos
planetas.add('Tierra')
print(planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
#eliminar elemento, arroja un error en caso de no encontar el key
planetas.remove('Tierra') #<- la llave tierras no se encuentra en el set
print(planetas)
#discard, borrar un elemento, no arroja un error en caso de no encontrarlo
planetas.discard('Jupiter')
print(planetas)
#limpiar set
planetas.clear()
print(planetas)
#borrar de la memoria el set
del planetas