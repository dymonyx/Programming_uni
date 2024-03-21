def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def equation(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return('корней нет')
    else:
        first_x = (-b + d**0.5)/(2*a)
        second_x = (-b - d**0.5) / (2 * a)
        return(first_x, second_x)






if __name__ == '__main__':
    data = input('введите коэффициенты кв.уравнения через пробел: ')
    while data != 'Q':
        if all([isNumber(s) for s in data.split()]):
            a, b, c = map(float, data.split())
            print(f'Корни квадратного уравнения: {equation(a, b, c)}')
        else:
            print('вы должны были ввести числа')
        data = input('введите коэффициенты кв.уравнения через пробел: ')