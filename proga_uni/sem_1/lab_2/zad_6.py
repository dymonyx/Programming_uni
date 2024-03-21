
def electres(h1, m1, h2, m2):
    if h2 < h1:
        time = (24*60 - h1*60 -m1 + h2*60 + m2)
    else:
        arrive = h2 * 60 + m2
        otpr = h1 * 60 + m1
        time = arrive - otpr
    h = time // 60
    m = time - h * 60
    if h > 10 and m > 10:
        return f'время в пути {h}:{m}'
    elif h < 10 and m > 10:
        return f'время в пути 0{h}:{m}'
    elif h > 10 and m < 10:
        return f'время в пути {h}:0{m}'
    else:
        return f'время в пути 0{h}:0{m}'

h1, m1 = map(int, input('введите время отправления: ').split(':'))
if (-1 < h1 < 24) and (-1 < m1 < 61):
    h2, m2 = map(int, input('введите время прибития: ').split(':'))
    if (-1 < h2 < 24) and (-1 < m2 < 61):
        print(electres(h1, m1, h2, m2))
    else:
        print('неправильно введено время')
else:
    print('неправильно введено время')
