class Country:
    def __init__(self, capital="", population=1):
        self._capital = capital
        if self.right_value_population(population):
            self._population = population

    def set_Population(self, population):
        if self.right_value_population(population):
            self._population = population

    def get_Population(self):
        return self._population

    def get_Capital(self):
        return self._capital

    def right_value_population(self, population):
        return population > 0


    def get_info(self):
        print(self.get_Capital(), end=",")
        print(self.get_Population())


class Russia(Country):
    def __init__(self):
        super().__init__(self)
        self._capital = "Moscow"

class Canada(Country):
    def __init__(self):
        super().__init__(self)
        self._capital = "Ottawa"

class Germany(Country):
    def __init__(self):
        super().__init__(self)
        self._capital = "Berlin"


russia = Russia()
canada = Canada()
germany = Germany()
russia.set_Population(146_447_424)
canada.set_Population(40_000_000)
germany.set_Population(84_607_016)
russia.get_info()
canada.get_info()
germany.get_info()
