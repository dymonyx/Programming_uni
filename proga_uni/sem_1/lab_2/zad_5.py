def calc(num_1, oper, num_2):
    if oper == '/':
        if num_2 == 0:
            return('делить на ноль нельзя.')
        else:
            return(num_1 / num_2)
    elif oper == '//':
        if num_2 == 0:
            return ('делить на ноль нельзя.')
        else:
            return (num_1 // num_2)
    elif oper == '+':
        return (num_1 + num_2)
    elif oper == '*':
        return (num_1 * num_2)
    elif oper == '%':
        return (num_1 % num_2)
    elif oper == '**':
        return (num_1**num_2)
    else:
        return 'Неверно введен оператор'


num_1 = float(input('введите число: '))
oper = input('введите оператор: ')
num_2 = float(input('введите число: '))
print(calc(num_1, oper, num_2))