class Figures:
    def __init__(self, color="white"):
        self._color = color

    def set_color(self, color):
        self._color = color


class Circle(Figures):
    def __init__(self):
        super().__init__(self)
        if size > 0:
            self._size = size

    def set_color(self, color):
        if color not in ["black", "yellow", "red", "green", "blue"]:
            self._color = color

    def get_info(self):
        return self._color, self._size


class Square(Figures):
    def __init__(self, color, size):
        super().__init__(color)
        if size > 0:
            self._size = size

    def set_color(self, color):
        if color not in ["black", "yellow", "red", "green", "blue"]:
            self._color = color

    def get_info(self):
        return self._color, self._size

krug = Circle("magenta",6)
krug.set_color("red")
print(krug.get_info())