import random

highst = [random.randint(50, 220) for _ in range(0, 20)]
highst.sort(reverse=True)

new_peop = input('Введите рост нового человека (для завершение нажмите Q): ')
while new_peop != 'Все построены':
    if 0 < int(new_peop) < 250:
        new_peop = int(new_peop)
        highst.append(new_peop)
        highst.sort(reverse=True)
        print(highst, highst.index(new_peop))
        new_peop = input('Введите рост нового человека (для завершение нажмите Q): ')
    else:
        print('По-моему это не рост человека.')
        new_peop = input('Введите рост нового человека (для завершение нажмите Q): ')

print(highst)

