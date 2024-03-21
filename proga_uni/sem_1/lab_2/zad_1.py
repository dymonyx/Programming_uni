sex = input('введите пол человека (ж или м): ')
name = input('введите имя: ')
age = input('введите возраст: ')

if sex.lower() == 'ж':
    if 9 < int(age) < 21:
        print(f'Её зовут {name}. Ей {age} лет')
    elif age[-1] == '1':
        print(f'Её зовут {name}. Ей {age} год')
    elif age[-1] in '234':
        print(f'Её зовут {name}. Ей {age} года')
    elif age[-1] in '567890':
        print(f'Её зовут {name}. Ей {age} лет')
    else:
        print('неправильно введён возраст')
elif sex.lower() == 'м':
    if 9 < int(age) < 21:
        print(f'Его зовут {name}. Ему {age} лет')
    elif age[-1] == '1':
        print(f'Его зовут {name}. Ему {age} год')
    elif age[-1] in '234':
        print(f'Его зовут {name}. Ему {age} года')
    elif age[-1] in '56789':
        print(f'Его зовут {name}. Ему {age} лет')
    else:
        print('неправильно введён возраст')
else:
    print('неправильно введён пол')