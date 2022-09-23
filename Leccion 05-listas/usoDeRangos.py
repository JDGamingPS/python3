#sintaxis de range (inicio<opcional>, fin<requerido>, incremento<opcinal>)

# Ejercicio 1. iterar un rango de 0 a 10 imprimir numeros divisibles entre 3
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11): #<- imprimi 0 a 10, no toca el 11
    if i % 3 == 0:
        print(i)

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimirlos
print('Rango con valores de inicio 2 y fin = 6 (7)')
rango = range(2,7) #<- ira de 2 a 6, no toca el 7
for i in rango:
    print(i)

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
rango = range(3, 11, 2)
for i in rango:
    print(i)






