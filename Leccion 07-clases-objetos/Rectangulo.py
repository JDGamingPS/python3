#Rectangulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rectangulo1 = Rectangulo(5, 6)
print(rectangulo1.area())