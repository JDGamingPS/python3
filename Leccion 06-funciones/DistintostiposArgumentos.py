def desplegarNombres(nombres): #<- lista de nombres
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)

desplegarNombres('Jorge')

desplegarNombres([4, 1])

desplegarNombres((10, 11)) #es una tupla, los ints no se pueden iterar

