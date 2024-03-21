class Student:
    def __init__(self, name="Radomir", age=18, groupNumber=1213):
        self.__name = name
        self.__age = age
        self.__groupNumber = groupNumber

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_groupNumber(self, groupNumber):
        self.__groupNumber = groupNumber

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_groupNumber(self):
        return self.__groupNumber

    def get_info(self):
        print(self.get_name(), end=",")
        print(self.get_age(), end=",")
        print(self.get_groupNumber())



student_1 = Student("Arseniy", 20, 1111)
student_2 = Student("Alexey", 17, 2934)
student_3 = Student("Maria", 18, 3954)
student_4 = Student("Yulia", 18, 3121)
student_5 = Student("Evgeniy", 19, 3249)

student_1.get_info(), student_2.get_info(), student_3.get_info(), student_4.get_info(), student_5.get_info()