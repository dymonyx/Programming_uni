def get_degree_first(num, degree): # вычисляем степень через встроенную функцию
    return (pow(num, degree))

def get_degree_second(num, degree): # вычисляем степень рекурсивно
    if degree < 0:
        result = 1 / (num * get_degree_second(num, -degree - 1))
    if degree == 0:
        return 1
    if degree > 0:
        result = num * get_degree_second(num, degree - 1)
    return result


if __name__ == "__main__":
    num = float(input("Введите число: "))
    degree = int(input("Введите степень: "))
    print(get_degree_first(num, degree))
    print(get_degree_second(num, degree))