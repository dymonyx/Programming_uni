import math

a, b, c = map(int, input('введите стороны треугольника:').split())
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f'площадь треугольника равна {s}')