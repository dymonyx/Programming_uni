from abc import ABC, abstractmethod
from threading import Thread
from sqlalchemy import *
import numpy
import asyncio
from sqlalchemy.orm import *
from datetime import datetime

class Pizza(ABC):
    def __init__(self, name='', size='', dough='', sauce='', ingredients=['cheese']):
        self._name = name
        self._size = size
        self._dough = dough
        self._sauce = sauce
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size in ['30cm', '35cm', '40cm']:
            self._size = new_size
        else:
            raise ValueError('Incorrect size of pizza. Correct values are 30cm, 35cm, 40cm.')

    def _check_size(self, new_size):
        if new_size in ['30cm', '35cm', '40cm']:
            return new_size
        else:
            raise ValueError('Incorrect size of pizza. Correct values are 30cm, 35cm, 40cm.')

    @property
    def dough(self):
        return self._dough

    @dough.setter
    def dough(self, new_dough):
        if new_dough in ['yeast', 'yeast-free', 'whole-grain']:
            self._dough = new_dough
        else:
            raise DoughException('Incorrect dough. Correct values are yeast, yeast-free, whole-grain.')

    @property
    def sauce(self):
        return self._sauce

    @sauce.setter
    def sauce(self, new_sauce):
        self._sauce = new_sauce

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, new_ingredients):
        if 'cheese' in new_ingredients:
            self._ingredients = new_ingredients
        else:
            raise CheeseException('Cheese have to be in ingredient list for pizza.')

    def __str__(self):
        return self._name

    async def prepare(self):
        await asyncio.sleep(3)
        print(f'kneaded {self._dough} dough.')
        await asyncio.sleep(1)
        print(f'{self._sauce} sauce is added.')
        await asyncio.sleep(2)
        print(f"the following ingredients have been added: {','.join(self._products)}.")

    @abstractmethod
    def bake(self):
        pass

    async def cut(self):
        await asyncio.sleep(3)
        print(f'{self._name} is cut.')


class PackingDeliveryMixin:

    async def pack(self):
        await asyncio.sleep(3)
        print(f'{self._name} is packed.')

    async def deliver(self):
        await asyncio.sleep(3)
        print(f'{self._name} is delivering.')


class PizzaPepperoni(Pizza, PackingDeliveryMixin):
    def __init__(self, name='Pepperoni', size='', dough='yeast', sauce='tomato',
                 products=['cheese', 'pepperoni', 'italian_herbs']):
        super().__init__(name, size, dough, sauce, products)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    async def bake(self):
        print(f'{self._name} will be baked in 20 minutes.')
        await asyncio.sleep(1)
        print(f'{self._name} is baked.')


class PizzaBarbeque(Pizza, PackingDeliveryMixin):
    def __init__(self, name='Barbeque', size='', dough='yeast-free', sauce='tomato',
                 products=['cheese', 'sauce barbeque', 'bacon', 'tomatoes', 'eggplant', 'champignons', 'sweet onions',
                           'pickles', 'parsley']):
        super().__init__(name, size, dough, sauce, products)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    async def bake(self):
        print(f'{self._name} will be baked in 25 minutes.')
        await asyncio.sleep(2)
        print(f'{self._name} is baked.')


class PizzaSeafood(Pizza):
    def __init__(self, name='Seafood', size='', dough='whole-grain', sauce='cream',
                 products=['cheese', 'calamari', 'shrimp', 'mussels', 'octopus', 'tomatoes', 'red pepper']):
        super().__init__(name, size, dough, sauce, products)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    async def bake(self):
        print(f'{self._name} will be baked in 30 minutes.')
        await asyncio.sleep(3)
        print(f'{self._name} is baked.')


class CheeseException(BaseException):
    """Класс исключения при отсутствии сыра в пицце"""


class DoughException(BaseException):
    """Класс исключения для несуществующих видов пицц"""


def countdown(func):
    import time
    def wrapped(*args, **kwargs):  # зачем??
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to ordering is {round(end - start, 2)}sec.")

    return wrapped


class CorrectNumb(Exception):
    pass


class NotExistProduct(Exception):
    """Класс исключения для добавления несуществующего товара"""


class OrderIsNotEmpty(Exception):
    pass


def counting(order_list):
    if len(order_list) != 0:
        raise OrderIsNotEmpty
    else:
        return

engine = create_engine('sqlite:///myDBase.db')

meta = MetaData()

orders_table = Table('orders', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', String),
    Column('order_description', String),
    Column('date', String)
)

meta.create_all(engine)

class Terminal:
    def __init__(self, menu=['PizzaPepperoni', 'PizzaBarbeque', 'PizzaSeafood']):
        self._menu = menu

    def get_menu(self):
        return ','.join(self._menu)

    @countdown
    def start_work(self):
        name = input('What is your name? ')
        print(*self._menu)
        action = input('What would you like to order? ')
        while True:
            try:
                if action not in ['PizzaPepperoni', 'PizzaBarbeque', 'PizzaSeafood', "Q"]:
                    raise NotExistProduct("Вы добавили несуществующий товар")
            except NotExistProduct as e:
                print(e)
                action = input('What would you like to order? ')
            else:
                break
        order = Order(name)
        pizzas_ordering = []
        while action != 'Q':
            size = ''
            while True:
                new_size = input("What size would you like to order? (30cm, 35cm, 40cm) ")
                try:
                    if new_size in ['30cm', '35cm', '40cm']:
                        size = new_size
                        break
                    else:
                        raise ValueError('Incorrect size of pizza. Correct values are 30cm, 35cm, 40cm.')
                except ValueError as e:
                    print(e)
            try:
                counting(order.order_list)
            except OrderIsNotEmpty:
                amount_pizzas = len(order.order_list)
            else:
                amount_pizzas = 0
            name_pizza = f'{action}_{amount_pizzas + 1}_' + size
            if action == "PizzaPepperoni":
                pizzas_ordering.append(PizzaPepperoni(name_pizza, size))
            elif action == "PizzaBarbeque":
                pizzas_ordering.append(PizzaBarbeque(name_pizza, size))
            else:
                pizzas_ordering.append(PizzaSeafood(name_pizza, size))
            ans_products = input("Would you like to change some ingredients? (Y/N) ")
            if ans_products == 'Y':
                now_ingredients = numpy.copy(pizzas_ordering[amount_pizzas].ingredients)
                new_ingredients = pizzas_ordering[amount_pizzas].ingredients
                del_ingredients = list(input(
                    f'Now there are {pizzas_ordering[amount_pizzas].ingredients} products. Choose one or some ingredients to change with " ," ').split(
                    ' ,'))
                while True:
                    while True:
                        if del_ingredients == ["Q"]:
                            break
                        if all([ingredient in now_ingredients for ingredient in del_ingredients]):
                            break
                        else:
                            print(
                                f'Incorrect ingredients. Now there are {pizzas_ordering[amount_pizzas].ingredients} products. Choose one or some ingredients to change with " ," ')
                            del_ingredients = list(input(
                                f'Now there are {pizzas_ordering[amount_pizzas].ingredients} products. Choose one or some ingredients to change with " ," ').split(
                                ' ,'))
                    if del_ingredients == ["Q"]:
                        pizzas_ordering[amount_pizzas].ingredients = now_ingredients
                        break
                    try:
                        for i in del_ingredients:
                            new_ingredients.remove(i)
                        pizzas_ordering[amount_pizzas].ingredients = new_ingredients
                    except CheeseException as e:
                        pizzas_ordering[amount_pizzas].ingredients = now_ingredients
                        new_ingredients = numpy.copy(now_ingredients).tolist()
                        print(e)
                        del_ingredients = list(input(
                            f'Now there are {pizzas_ordering[amount_pizzas].ingredients} products. Choose one or some ingredients to change with " ," ').split(
                            ' ,'))
                    else:
                        break
            order.order_list.append(pizzas_ordering[amount_pizzas])
            action = input('Do you want to add more pizzas? (Y/N): ')
            if action == 'Y':
                print(*self._menu)
                action = input('What would you like to order? ')
            else:
                break
        if len(order.order_list) != 0:
            answer = input('Do you confirm your order? yes/no: ')
            if answer == 'yes':
                final_price = order.get_price()
                pizzas = [str(pizza) for pizza in order._order_list]
                print(f"Your order contains: {' ,'.join(pizzas)} and final price is {final_price}")
                print('Thanks for ordering! See you next time!')
                current_datetime = datetime.now()
                # Преобразование текущей даты и времени в строку
                current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                new_order = {'name': name, 'price': final_price, 'order_description': ' ,'.join(pizzas), 'date': current_datetime_str}
                session.execute(orders_table.insert(), new_order)
                session.commit()

                async def preparing_pizza(pizza):
                    await pizza.prepare()
                    await pizza.bake()
                    await pizza.cut()
                async def doing_order():
                    pizzas = order.order_list
                    tasks = [asyncio.create_task(preparing_pizza(pizza)) for pizza in pizzas]
                    await asyncio.gather(*tasks)


                asyncio.run(doing_order())
                print('Your order is ready!')
            else:
                print('See you next time!')
        else:
            print('See you next time!')
        del order


class Order:
    def __init__(self, name, order_list=[]):
        self._name = name
        self._order_list = order_list

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, new_order_list):
        self._order_list = new_order_list

    # как это обернуть в try так чтобы я могла использовать значения final_price и pizzas - SOLVE: убрать этот декоратор к черту, заменить на простую обработку исключений

    def get_price(self):
        prices = {'PizzaPepperoni': 10, 'PizzaBarbeque': 13, 'PizzaSeafood': 15}
        final_price = 0
        for pizza in self._order_list:
            if 'Pepperoni' in str(pizza):
                price = 10
            elif 'Barbeque' in str(pizza):
                price = 13
            else:
                price = 15
            if "30cm" in str(pizza):
                final_price += price
            elif '35cm' in str(pizza):
                final_price += int(price * 1.3)
            else:
                final_price += int(price * 1.5)
        return final_price


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()

    terminal = Terminal()
    # ВТОРОЙ ТЕРМИНАЛ - вторичный поток
    terminal1 = Thread(target=terminal.start_work())
#    terminal2 = Thread(target=terminal.start_work())
    terminal1.start()
#    terminal2.start()
    terminal1.join()
#    terminal2.join()

    orders = session.execute(orders_table.select()).fetchall()
    for order in orders:
        print(f'name: {order.name}, price: {order.price}, order_contained: {order.order_description}, date: {order.date}')

    session.close()

# если не первый атрибут пустой, то сначала видимо заполняется он (эт про ошибку с size)
# сеттер с property вызывается видимо как обычный атрибут (а в чем смысл??????  )
