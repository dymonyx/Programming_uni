class Soda:

    def __init__(self, add_product):
        self.add = add_product
    def show_my_drink(self):
        if self.add != "Q":
            print(f"Газировка и {self.add}")
        else:
            print("Обычная газировка")
def start_work():
    add_product = input("Если хотите добавить что-то к лимонаду, напишите название, иначе введите Q: ")
    drink = Soda(add_product)
    drink.show_my_drink()

start_work()