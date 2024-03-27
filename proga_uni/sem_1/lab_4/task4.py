
ff = open('file_task4.txt')
main_arr = list(ff.readline().split(','))

print(main_arr)

login = input('Введите логин: ')

def log_in(login):
    if login.lower() in main_arr:
        return ('Доступ разрешён.')
    else:
        print('Логин не найден, хотите создать новый логин?')
        ans = input('Ввведите ответ (да/нет): ')
        if ans.lower() == 'да':
            with open('file_task4.txt', 'a', encoding='utf-8') as f:
                f.write(',' + login)
                f.close()
            return ('Доступ разрешён.')
        else:
            return ('Доступ запрещён.')

# check


print(log_in(login))