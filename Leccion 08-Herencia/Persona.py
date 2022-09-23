class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # def mostrar(self):
    #     print(f"persona: {self.nombre} {self.edad}")

    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

    # getters and seterss
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'persona: {super().__str__()}, [Sueldo: {self.sueldo}] '

    # def mostrarSueldo(self):
    #     super().mostrar()
    #     print(f'sueldo: {self.sueldo}')



empleado1 = Empleado('Carlos', 20, 15000)
