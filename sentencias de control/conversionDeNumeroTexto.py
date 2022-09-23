numero = int(input('Programacion un valor enre 1 y 3'))


if numero == 1:
    numeroText = 'numero uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'número tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Numero proporcionado: {numero} - {numeroTexto}')