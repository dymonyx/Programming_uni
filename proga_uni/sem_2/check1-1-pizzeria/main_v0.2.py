from abc import ABC, abstractmethod
from threading import Thread
from sqlalchemy import *
import sqlite3

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
            raise CheeseException('Cheese have to be in ingredient list for pizza. Please add cheese.')

    def __str__(self):
        return self._name

    def prepare(self):
        print(f'kneaded {self._dough} dough.')
        print(f'{self._sauce} id added.')
        print(f"the following ingredients have been added: {','.join(self._products)}.")

    @abstractmethod
    def bake(self):
        pass

    def cut(self):
        return f'{self._name} is cut.'


class PackingDeliveryMixin:

    def pack(self):
        return f'{self._name} is packed.'

    def deliver(self):
        return f'{self._name} is delivering.'


class PizzaPepperoni(Pizza, PackingDeliveryMixin):
    def __init__(self, name='Pepperoni', size='', dough='yeast', sauce='tomato',
                 products=['cheese', 'pepperoni', 'italian_herbs']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    def bake(self):
        return f'{self._name} will be baked in 20 minutes.'


class PizzaBarbeque(Pizza, PackingDeliveryMixin):
    def __init__(self, name='Barbeque', size='', dough='yeast-free', sauce='tomato',
                 products=['cheese', 'sauce barbeque', 'bacon', 'tomatoes', 'eggplant', 'champignons', 'sweet onions',
                           'pickles', 'parsley']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    def bake(self):
        return f'{self._name} will be baked in 25 minutes.'


class PizzaSeafood(Pizza):
    def __init__(self, name='Seafood', size='', dough='whole-grain', sauce='cream',
                 products=['cheese', 'calamari', 'shrimp', 'mussels', 'octopus', 'tomatoes', 'red pepper']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products

    def bake(self):
        return f'{self._name} will be baked in 30 minutes.'


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


def checking_that_arg_is(predicate, error_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if predicate(result):
                raise ValueError(error_message)
            return result

        return wrapper

    return decorator


def greater_than(value):
    def predicate(arg):
        return arg > value

    return predicate


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
        while action != 'Q':
            size = input("What size would you like to order? (30cm, 35cm, 40cm) ")
            if action == 'PizzaPepperoni':
                try:
                    counting(order.order_list)
                except OrderIsNotEmpty:
                    pepperoni_pizzas = len([pizza for pizza in order.order_list if 'PizzaPepperoni' in str(pizza)])
                else:
                    pepperoni_pizzas = 0
                order.order_list.append(PizzaPepperoni(f"PizzaPepperoni_{pepperoni_pizzas + 1}_" + size, size))
            if action == 'PizzaBarbeque':
                try:
                    counting(order.order_list)
                except OrderIsNotEmpty:
                    barbeque_pizzas = len([pizza for pizza in order.order_list if 'PizzaBarbeque' in str(pizza)])
                else:
                    barbeque_pizzas = 0
                order.order_list.append(PizzaBarbeque(f"PizzaBarbeque_{barbeque_pizzas + 1}_" + size, size))
            if action == 'PizzaSeafood':
                try:
                    counting(order.order_list)
                except OrderIsNotEmpty:
                    seafood_pizzas = len([pizza for pizza in order.order_list if "PizzaSeafood" in str(pizza)])
                else:
                    seafood_pizzas = 0
                order.order_list.append(PizzaSeafood(f"PizzaSeafood_{seafood_pizzas + 1}_" + size, size))
            action = input('Do you want to add more pizzas? yes/no: ')
            if action == 'yes':
                print(*self._menu)
                action = input('What would you like to order? ')
            else:
                break
        if len(order.order_list) != 0:
            answer = input('Do you confirm your order? yes/no: ')
            if answer == 'yes':
                order.get_price()
                print('Thanks for ordering! See you next time!')
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
    @checking_that_arg_is(greater_than(40), "You are ordered too much..Please take a new order.")
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
        pizzas = [str(pizza) for pizza in self._order_list]
        print(f"Your order contains: {','.join(pizzas)} and final price is {final_price}")
        return final_price




if __name__ == '__main__':
    terminal = Terminal()
    #ВТОРОЙ ТЕРМИНАЛ
    thread1 = Thread(target=terminal.start_work())
    thread2 = Thread(target=terminal.start_work())
    thread1.start()
    thread2.start()
"""для асинхронной многопоточности нужно реализовать использование стадий приготовления,
например, пока печется одна пицца из заказа можно начать готовить другую
"""
