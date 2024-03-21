time = int(input('введите секунды:'))
days = time // 86400
hours = (time - days*86400)//3600
minutes = (time - days*86400 - hours*3600)//60
seconds = time - days*86400 - hours*3600 - minutes*60
print(f'{time} секунд - это {days} дней {hours} часов {minutes} минут {seconds} секунд')