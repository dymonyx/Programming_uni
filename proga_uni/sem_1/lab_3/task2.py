a, b, c = map(float, input("введите три числа: ").split())
if a >= b:
    if a <= c:
        maxx = c
    else:
        maxx = a

else:
    if a >= c:
        maxx = b
    else:
        maxx = c


print(maxx)