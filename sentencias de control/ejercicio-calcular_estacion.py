mes = int(input('proporciona mes del año (1-12)'))
estacion = None #<- no contiene nada de valores
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes== 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'otoño'
else:
    estacion = 'mes incorrecto'
print(f'Para el mes {mes} la estaciòn es: {estacion}')
