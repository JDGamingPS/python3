#funciones con argumentos Variables
#*args que se refiere a que son argumentos variables
def listarNombres(*nombres): #<- con * lo convertira como una tupla
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Maria', 'Karla', 'Ernesto')
listarNombres('Laura', 'Carlos')
