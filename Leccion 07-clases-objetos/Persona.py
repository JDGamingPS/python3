class Persona:
    # def __init__(self, nombre, apellido, edad, *tupla, **diccionario):
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # se utiliza "_" para encapzular los atributos
        self._apellido = apellido
        self._edad = edad
        # self.tupla = tupla
        # self.diccionario = diccionario

# <======= GETERS y SETERS =======>
    @property
    #con property ya no es necesario poner "()" para llamar al get "nombre"
    def nombre(self):
        #print('Llamando el metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        #print('Llamando el metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

# es obligatorio el self en funciiones de instancia
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

    def __del__(self):
        print(f'Persona: {self.nombre} {self.apellido}')

# persona1 = Persona('juan', 'Perez', '35', 'medicina', 'cirugia', m='manzana', p='pera')
# # print(f'Objeto Persona 2: {persona1.nombre} {persona1.apellido} {persona1.edad}')
# persona1.mostrarDetalle()
# # Persona.mostrarDetalle(persona1) #<- otra forma de referenciar
#
# # añadir un nuevo atributo
# persona1.telefono = 2245484  # <- se puede añadir un atributo que no este definid dentro de la clase pero esolo es externo no se comparte el atributo añadido al vuelo
# print(persona1.telefono)

if __name__ == '__main__':

    persona2 = Persona('Jaqueline', 'Machaca', 22)
    #print(persona2.nombre)
    persona2.nombre = 'Jorge Daniel'
    print(persona2.nombre)
    persona2.apellido = 'Lara'
    print(persona2.apellido)
    persona2.edad = 30
    print(persona2.edad)
    # print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
    #persona2.mostrarDetalle()
