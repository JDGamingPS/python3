cadena = 'jorge'

for letra in cadena:
    print(letra)
# else:
#     print('fin ciclo')

for letra in 'holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break #<- rompe la itracion al encontrar lo que queremos

print('numeros naturales')
for i in range(10):
    if i % 2 == 0:
        print(f'Valor: {i}')

print('Continue')
for i in range(6):
    if i % 2 != 0:
        continue # continuara con la siguiente, en este caso tomara los pares
    print(f'Valor: {i}')
