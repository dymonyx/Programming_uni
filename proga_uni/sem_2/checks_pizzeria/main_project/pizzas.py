import asyncio
from abc import ABC, abstractmethod
from exceptions import CheeseException, DoughException


# возможно сюда нужно будет импортировать исключения

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
        print(f"the following ingredients have been added: {', '.join(self._products)}.")

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
