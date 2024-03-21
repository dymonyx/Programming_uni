line = input('Ввведите строку: ')

def summ(line):
    summa = 0
    for i in range(len(line)):
        try:
            summa += int(line[i])
        except:
            pass
    return summa

print(summ(line))