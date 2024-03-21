def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def calculator(data, operation):
    a, b = map(float, data.split())
    if operation == '+':
        ans = a+b
    elif operation == "-":
        ans = a-b
    elif operation == '*':
        ans = a*b
    else:
        ans = a/b
    return round(ans, 2)






if __name__ == "__main__":
    data = input('введите два числа: ')
    while data != 'Q':
        if all([isNumber(s) for s in list(data.split())]):
            if len(list(data.split())) == 2:
                operation = input('введите оператор(-, +, *, /): ')
                if operation in '-+*/':
                    if operation != '/':
                        print(calculator(data, operation))
                    else:
                        if list(data.split())[1] != '0':
                            print(calculator(data, operation))
                        else:
                            print('делить на ноль нельзя')
                else:
                    print('такой операции в калькуляторе нет =)')
            else:
                print('числа должно быть 2')
        else:
            print('вы ввели не числа')
        data = input('введите два числа: ')