from Persona import Persona

print('Creacion objetos'.center(50, '-'))
persona1 = Persona('karla', 'gomez', 30)
persona1.mostrarDetalle()

print('Eliminacion objetos'.center(30,'-'))
del persona1
print(__name__)