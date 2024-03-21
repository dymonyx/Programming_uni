def solve_ur(a, b, c):
    discr = b**2 - 4*a*c
    if discr < 0:
        return (f'Корней уравнения нет. Дискриминант отрицателен.')
    elif discr == 0:
        x1 =( b+discr**0.5)/(2*a)
        return(f'Корень равен: {x1}')
    else:
        x1 = (b + discr**0.5)/(2*a)
        x2 = (-b + discr**0.5)/(2*a)
        return(f'Первый корень равен: {x1}, Второй корень равен: {x2}')



a, b, c = map(float, input('введите коэффициенты квадратного уравнения (через пробел): ').split())
print(solve_ur(a, b, c))

