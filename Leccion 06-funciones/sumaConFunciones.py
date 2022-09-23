#return
def sumar(a, b):
    return (a + b)

#resultado = sumar(5, 3)
print(f'Resultado sumar: {sumar(5, 3)}')

#valores por default

def sum(a=0, b=0) -> int: #<- ; -> int : se llama pista, para ver que retornara
    return a+b

res = sum()
print(f'la suma es: {res}')

print(f'la suma con parametros es: {sum(8, 2)}') # <- los argumentos se sobreescriben en los valores por defecto



