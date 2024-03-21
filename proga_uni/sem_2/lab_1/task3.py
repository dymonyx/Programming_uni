class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        if self.b == 0:
            print("нельзя делить на ноль")
        else:
            print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


def start_work():
    operation = int(input("какое действие необходимо? (1 - сложение, 2 - умножение, 3 - деление, 4 - вычитание): "))
    a, b = int(input("первое число: ")), int(input("второе число: "))
    operations = Math(a, b)
    if operation == 1:
        operations.addition()
    elif operation == 2:
        operations.multiplication()
    elif operation == 3:
        operations.division()
    else:
        operations.subtraction()


start_work()
