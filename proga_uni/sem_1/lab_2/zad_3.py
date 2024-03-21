def time_years(year):
    if 0 < int(year) < 13:
        if year in ['12', '1', '2']:
            return('Зима')
        elif year in ['3', '4', '5']:
            return('Весна')
        elif year in ['6', '7', '8']:
            return('Лето')
        elif year in ['9', '10', '11']:
            return('Осень')
    else:
        return('Ошибка. Неверный формат месяца.')

print(time_years(input('введите порядковый номер месяца (от 1 до 12): ')))