stats_arr = []

s = input('Введите число: ')
while s!='Q':
    stats_arr.append(float(s))
    s = input('Введите число: ')

maxx = max(stats_arr)
minn = min(stats_arr)
max_i = stats_arr.index(maxx)
min_i = stats_arr.index(minn)

def mno(starts_arr):
    if abs(min_i - max_i) == 1:
        mn = 'чисел в этом диапазоне нет'
        return mn
    mn = 1
    if min_i < max_i:
        for i in range(min_i + 1, max_i):
            mn*=starts_arr[i]
    else:
        for i in range(max_i + 1, min_i):
            mn*=starts_arr[i]
    return mn


print(f'Кол-во элеменов: {len(stats_arr)}, Ср.арифм: {sum(stats_arr)/len(stats_arr)}, Сумма: {sum(stats_arr)}')
print(f'Макс.эл и индекс: {[maxx, max_i]}, Мин.эл и индекс: {[minn, min_i]}')
print(f'Произведение: {mno(stats_arr)}')