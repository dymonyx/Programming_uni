import random
def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


numb = input("введите число: ")
if isNumber(numb):
    numb = float(numb)
    array = [random.randint(1, 50) for _ in range(0, 20)]
    comprasion = []
    for x in array:
        if x > numb:
            comprasion.append("High")
        elif x == numb:
            comprasion.append("Equal")
        else:
            comprasion.append('Low')

    print(array, comprasion, sep="\n")

    s = 'Эля, Ян, Исак, Исакий, Исидор, Иустин, Казимир, Каллимах, Каллиник, Каллиопий, Каллист, Кондратий, Конон, Конрад, Константин, Корней, Корнелий, Корнил, Корнилий, Ксенофонт, Кузьма, Куприян, Лавр, Лаврентий, Ладимир, Лазарь, Ларион, Лев, Леон, Леонард, Леонид, Леонтий, Леопольд, Логвин, Мавродий, Май, Макар, Макарий, Македон, Македоний, Максим, Максимиан, Юля, Андрей, Катя, Денис, Арнольд, Паша, Сергей, Анатолий'
    names = list(s.split(", "))
    names_a, names_other = [], []
    for x in names:
        names_a.append(x) if x[0] in 'АБВГДЕЁЖЗИЙК' else names_other.append(x)

    print(names, names_a, names_other, sep="\n")
else:
    print("Вы ввели не число")

