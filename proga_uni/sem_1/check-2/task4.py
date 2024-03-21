def check_snils(numb):
    flag = True
    snils = ""
    for i in list(numb.split("-")):
        snils+=i
    main_part = [int(i) for i in snils[:-2]]
    control_part = snils[-2:]
    for x in snils[:-2]: # проверка на не более двух одинаковых чисел
        if x * 3 in snils[:-2]:
            flag = False
    mults = []
    for position, value in enumerate(main_part): # вычисляем сумму
        mults.append(value * (len(main_part) - position))
    sums = sum(mults)
    if sums < 100:
        if int(control_part) != sums:
            flag = False
    if (sums == 100 or sums == 101):
        if control_part != "00":
            flag = False
    if sums > 101:
        sums = sums % 101
    if sums < 100:
        if int(control_part) != sums:
            flag = False
    if sums == 100:
        if control_part != "00":
            flag = False
    return flag


if __name__ == "__main__":
    numb = input("Введите СНИЛС: ")
    #149-709-522-01
    print(check_snils(numb))
