class Color:
    def __init__(self, color):
        self._color = color

# geters y seters
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

