class Dog:
    def __init__(self, name="безымянный", age=0):
        self._name = name
        if self.right_age(age):
            self._age = age

    def right_age(self, age):
        return 20 >= age >= 0

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if self.right_age(age):
            self._age = age

    def get_age(self, age):
        return self._age

    def get_name(self):
        return self._name

    def get_voice(self):
        return self._voice

    def get_method(self):
        return self._method


class ToyTerier(Dog):
    _voice = "gav"
    def active(self):
        print("sitting_at_home")


class Spaniel(Dog):
    _voice = "tyaf"
    _method = "hunting"


class GermanySheepdog(Dog):
    _voice = "rrr"
    _method = "defensing"

josh = ToyTerier("Josh", 6)
josh.active()
ann = ToyTerier("Ann", 2)
bibi = Spaniel("Bibi", 3)
milka = Spaniel("Milka", 16)
malysh = GermanySheepdog("Malysh", 8)
ded = GermanySheepdog("Ded", 13)