#imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
def numeroDes(numero):
    if numero >= 1:
        print(numero)
        numeroDes(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor incorrecto...')


numeroDes(0)