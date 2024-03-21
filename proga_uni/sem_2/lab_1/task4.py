class Car:
    def __init__(self, color="", type="", year=None):
        self.color = color
        self.type = type
        self.year = year
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print("Автомобиль заведен.")
        else:
            print("Автомобиль уже заведен.")

    def stop_engine(self):
        if self.engine:
            self.engine = False
            print("Автомобиль заглушен.")
        else:
            print("Автомобиль уже заглушён.")

    def change_year(self, new_year):
        if 1886 <= new_year <= 2024:
            self.year = new_year

    def change_type(self, new_type):
        self.type = new_type

    def change_color(self, new_color):
        self.color = new_color

    def get_info(self):
        print(self.__dict__)

def start_work():
    color = input("введите цвет: ")
    type = input("введите тип: ")
    year = int(input("введите год: "))
    car = Car(color, type, year)
    while True:
        action = input('''какой метод хотите использовать? 1 - запуск двигателя, 
        2 - отключение двигателя, 3 - присвоение года выпуска, 4 - присвоение типа, 
        5 - присвоение цвета, 6 - отображение всей инфы (для выхода Q): ''')
        if action == "Q":
            break
        if action == "1":
            car.start_engine()
        elif action == "2":
            car.stop_engine()
        elif action == "3":
            new_year = int(input("введите год: "))
            car.change_year(new_year)
        elif action == "4":
            new_color = input("введите тип: ")
            car.change_type(new_color)
        elif action == "5":
            new_color = input("введите цвет: ")
            car.change_color(new_color)
        else:
            car.get_info()

start_work()