class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        if eng not in self.tr.keys():
            self.tr[eng] = list(rus)
        else:
            words = self.tr.get(eng)
            if rus not in words:
                words.append(rus)
                self.tr[eng] = words

    def remove(self, eng):
        # здесь продолжайте метод remove
        del self.tr[eng]

    def translate(self, eng):
        # здесь продолжайте метод translate
        return self.tr[eng]


# здесь создавайте объект класса Translator
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
tr.translate("go")

