day_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31]
def new_year(day, month):
    if month in ['1', '3', '5', '7', '8', '10', '12']:
        if 0 < day < 32:
            days = 0
            for i in range(0, int(month)-1):
                days += day_months[i]
            res = 365 - (days + day) + 1
        else:
            return 'Неверно введён день.'
    elif month in ['2']:
        if 0 < day < 29:
            days = 0
            for i in range(0, int(month)-1):
                days += day_months[i]
            res = 365 - (days + day) + 1
        else:
            return 'Неверно введён день.'

    elif month in ['4', '6', '9', '11']:
        if 0 < day < 31:
            days = 0
            for i in range(0, int(month)-1):
                days += day_months[i]
            res = 365 - (days + day) + 1
        else:
            return 'Неверно введён день.'
    else:
        return 'Неверно введён месяц.'
    if 9 < res < 21:
        return (f'До нового года осталось {res} дней.')
    elif str(res)[-1] == '1':
        return (f'До нового года остался {res} день.')
    elif str(res)[-1] in '234':
        return (f'До нового года осталось {res} дня.')
    elif str(res)[-1] in '567890':
        return (f'До нового года осталось {res} дней.')

day = int(input('введите день: '))
month = input('введите месяц: ')
print(new_year(day, month))