def suma(*args):
    res = 0
    for numero in args:
        #res = res + numero
        res += numero
    return res

resultadoSuma = suma(2, 4, 6)
resultadoSuma = suma(2, 4)

print(resultadoSuma)

#mutiplicar
def multiplicar(*args):
    m = 1
    for numero in args:
        #m = m * numero
        m *= numero
    return m

resMultiplicaion = multiplicar(2, 4, 6)
print(resMultiplicaion)