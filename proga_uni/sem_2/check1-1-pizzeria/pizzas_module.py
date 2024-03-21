class Pizza:
    def __init__(self, name='', size='', dough='yeast', sauce='', ingredients=['cheese']):
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
            raise ValueError('Incorrect dough. Correct values are yeast, yeast-free, whole-grain.')

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
            raise ValueError('Cheese have to be in ingredient list for pizza. Please add cheese.')

    def __str__(self):
        return self._name

    def prepare(self):
        print(f'kneaded {self._dough} dough.')
        print(f'{self._sauce} id added.')
        print(f"the following ingredients have been added: {','.join(self._products)}.")

    def bake(self):
        return f'{self._name} is baked.'

    def cut(self):
        return f'{self._name} is cut.'

    def pack(self):
        return f'{self._name} is packed.'


class PizzaPepperoni(Pizza):
    def __init__(self, name='Pepperoni', size='', dough='yeast', sauce='tomato',
                 products=['cheese', 'pepperoni', 'italian_herbs']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products


class PizzaBarbeque(Pizza):
    def __init__(self, name='Barbeque', size='', dough='yeast-free', sauce='tomato',
                 products=['cheese', 'sauce barbeque', 'bacon', 'tomatoes', 'eggplant', 'champignons', 'sweet onions',
                           'pickles', 'parsley']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products


class PizzaSeafood(Pizza):
    def __init__(self, name='Seafood', size='', dough='whole-grain', sauce='cream',
                 products=['cheese', 'calamari', 'shrimp', 'mussels', 'octopus', 'tomatoes', 'red pepper']):
        super().__init__(self)
        self._name = name
        self._size = self._check_size(size)
        self._dough = dough
        self._sauce = sauce
        self._products = products