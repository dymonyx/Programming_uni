def negative_positive(array):
    negative = sorted(list(filter(lambda x: x < 0, array)), reverse=True)  # создаем массив отрицательных значений фильтрацией
    positive = sorted(list(filter(lambda x: x >= 0, array)))  # создаем массив неотрицательных значений фильтрацией
    return negative, positive


if __name__ == "__main__":
    # 35 9 7 6 -4 5 -0.5 -3 5 7 -8 0
    array = list(map(float, input("Введите аргументы: ").split()))
    print(negative_positive(array))
