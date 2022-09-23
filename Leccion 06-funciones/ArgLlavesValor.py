# argumentos variables llaves valor **args es diccionario
#listar diccionario los argumentos que resive son de diccionario

def listarTerminos(**llavesValores):
    for llave, valor in llavesValores.items():
        print(f'{llave}: {valor}')

# el key o clave no lleva '', pero si el valor debe llevar ''
listarTerminos(IDE='Integreted Development Environment',
               PK='Primary key')
