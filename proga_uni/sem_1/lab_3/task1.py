import math
a, b = map(float, input("введите числа для задания диапазона: ").split())
if a > b:
    a, b = b, a
elif a == b:
    print('диапазон задан неверно')
arr = []
for i in range(math.floor(a) + 1, math.ceil(b)):
    if i % 2 != 0:
        arr.append(i)

print(*arr)