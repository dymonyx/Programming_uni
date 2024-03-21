steps = int(input("введите число ступенек от 1 до 9: "))
if not (1 <= steps <= 9):
    print("число вне диапазона. лестницы не будет")

else:
    for i in range(1, steps+1):
        for j in range(1, i+1):
            if j == i:
                print(j)
                break
            print(j, end = "")



