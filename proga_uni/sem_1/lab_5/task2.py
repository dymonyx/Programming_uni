import math

def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True
def square(fig, data, length):
    if length == 1:
        r = int(data)
        sq = math.pi * r**2
    elif length == 2:
        a, b = map(int, data.split())
        sq = a*b
    else:
        a, b, c = map(int, data.split())
        if max(a, b, c) > a + c + b - max(a, b, c):
            return("нет такого треугольника")
        else:
            p = (a+b+c)/2
            sq = (p*(p-a)*(p-b)*(p-c))**0.5
    return sq



if __name__ == '__main__':
    fig = input('введите фигуру: (треугольник - 1, круг - 2, прямоугольник - 3): ')
    while fig != 'Q':
        length = 0
        data = 0
        if all([a in '123' for a in fig]):
            if int(fig) == 1:
                data = input('введите три стороны треугольника через пробел: ')
                if all([isNumber(s) for s in list(data.split())]):
                    length = len(list(map(float, data.split())))
                    if length != 3:
                        print('надо было ввести три стороны')
                else:
                    print('вы ввели не числа')
            elif int(fig) == 2:
                data = input("введите радиус круга: ")
                if all([isNumber(s) for s in list(data.split())]):
                    length = len(list(map(float, data.split())))
                    if length != 1:
                        print('надо было ввести 1 радиус')
                else:
                    print('вы ввели не числа')
            elif int(fig) == 3:
                data = input("введите стороны прямоугольника: ")
                if all([isNumber(s) for s in list(data.split())]):
                    length = len(list(map(float, data.split())))
                    if length != 2:
                        print('надо было ввести две стороны')
                else:
                    print('вы ввели не числа')

            if length != 0 and data != 0:
                if all([x > 0 for x in list(map(float, data.split()))]):
                    squ = square(fig, data, length)
                    if squ == 0:
                        print('таких параметров быть не может')
                    else:
                        print('площадь равна:', squ)
                else:
                    print("все параметры должны быть положительны")
        else:
            print('вы ввели некорректное число')
        fig = input('введите фигуру: (треугольник - 1, круг - 2, прямоугольник - 3): ')
