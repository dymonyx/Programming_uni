class Progression:
    def __init__(self, a, d, n):
        self.first_a = a
        self.d = d
        self.n = n
    def geometry_progression(self):
        new_b = self.first_a * self.d ** (self.n - 1)
        return new_b

    def arifmath_progression(self):
        new_a = self.first_a + self.d*(self.n - 1)
        return new_a


def start_work():
    numb = int(input("1 - арифм, 2 - геометр. : "))
    a = int(input("первый член: "))
    d = int(input("разность/коэффициент: "))
    n = int(input("номер нужного члена: "))
    prog = Progression(a, d, n)
    if numb == 1:
        print(prog.arifmath_progression())
    if numb == 2:
        print(prog.geometry_progression())


start_work()
