def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

product = list(input("введите продукты, отделите каждый продукт запятой и пробелом: ").split(", "))

cost = list(input("введите цены: ").split())
if len(cost) == len(product):
    if all(isNumber(x) for x in cost):
        cost = list(map(float, cost))
        if all(10**10 > x > 0 for x in cost):
            price = [x * 1.15 for x in cost]
            zip_list = list(zip(product, [round(x, 2) for x in cost], [round(x, 2) for x in price]))
            print(zip_list)
        else:
            print("Цена должна быть положительной!")
    else:
        print("Цена должна быть числом!")

else:
    print("Количество цен и продуктов не совпадает")
