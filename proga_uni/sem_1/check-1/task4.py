def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

start_array = input("введите числа: ").split()
if all(isNumber(x) for x in start_array):
    start_array = [float(x) for x in start_array]
    mid_array = []
    for x in start_array:
        if x < 10:
            mid_array.append(x*1.12)
        elif x == 10:
            mid_array.append(x)
        else:
            mid_array.append(x * 0.25)
    mid_array.sort()
    final_array = [round(x, 2) for x in mid_array]
    print(final_array)

    with open('file_task4.txt', 'a', encoding='utf-8') as f: #я умею работать только с txt файлами =)
        f.writelines("\n".join(map(str, final_array)))
        f.close()
else:
    print("Вы должны были ввести числа!")