import asyncio
from datetime import datetime
from database_ORM import engine, Orders
import numpy as np
from GUI import PizzaApp  # Импортируем функцию для запуска GUI
from sqlalchemy.orm import sessionmaker
from order import Order
from pizzas import PizzaPepperoni, PizzaBarbeque, PizzaSeafood
from tkinter import Tk
from threading import Thread

Session = sessionmaker(bind=engine)
session = Session()

class Terminal:
    def __init__(self, menu=['PizzaPepperoni', 'PizzaBarbeque', 'PizzaSeafood']):
        self._menu = menu

    def get_menu(self):
        return ','.join(self._menu)

    def start_work(self, name, order_details):
        order = Order(name)
        order_list = []

        for detail in order_details:
            action = detail['action']
            size = detail['size']
            ingredients_to_change = detail['ingredients']

            name_pizza = f'{action}_{len(order.order_list) + 1}_' + size
            pizza = self.create_pizza(action, name_pizza, size)

            if ingredients_to_change:
                self.change_ingredients(pizza, ingredients_to_change)

            order.order_list.append(pizza)

        if len(order.order_list) != 0:

            final_price = order.get_price()
            pizzas = [str(pizza) for pizza in order.order_list]
            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
            new_order = Orders(
                name=order.name,
                price=final_price,
                order_description=', '.join(pizzas),
                date=current_datetime_str
            )
            session = Session()
            session.add(new_order)  # Добавляем объект Order в сессию
            session.commit()  # Фиксируем изменения в базе данных
            session.close()

            asyncio.run(self.prepare_order(order.order_list))
        else:
            print('Order is empty.')

    def create_pizza(self, action, name_pizza, size):
        if action == "PizzaPepperoni":
            return PizzaPepperoni(name_pizza, size)
        elif action == "PizzaBarbeque":
            return PizzaBarbeque(name_pizza, size)
        else:
            return PizzaSeafood(name_pizza, size)

    def change_ingredients(self, pizza, ingredients_to_change):
        now_ingredients = np.copy(pizza.ingredients)
        new_ingredients = pizza.ingredients

        try:
            for ingredient in ingredients_to_change:
                if ingredient in now_ingredients:
                    new_ingredients.remove(ingredient)
            pizza.ingredients = new_ingredients
        except Exception as e:
            pizza.ingredients = now_ingredients
            print(e)

    async def prepare_order(self, pizzas):
        async def prepare_pizza(pizza):
            await pizza.prepare()
            await pizza.bake()
            await pizza.cut()
        tasks = [asyncio.create_task(prepare_pizza(pizza)) for pizza in pizzas]
        await asyncio.gather(*tasks)

def on_order(name, order_details):
    terminal = Terminal()
    terminal_thread = Thread(target=terminal.start_work, args=(name, order_details))
    terminal_thread.start()
    terminal_thread.join()

if __name__ == '__main__':
    # Setup database session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Launch GUI
    tk = Tk()
    app = PizzaApp(tk, on_order)
    tk.mainloop()

    # Display all orders


    session.close()
