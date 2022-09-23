def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

n = 3
resultado = factorial(5)
print(f'El factorial de {n} es {resultado}')