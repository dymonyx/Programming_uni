import itertools
a = []
k = '123456'
for i in itertools.permutations('123456'):
    s = ''.join(i)
    flag = 0
    for i in range(6):
        if k[i] == s[i]:
            flag += 1
    if flag == 2:
        a.append(s)

for i in itertools.permutations('123456'):
    s = ''.join(i)
    flag = 0
    for i in range(6):
        if k[i] == s[i]:
            flag += 1
    if flag == 3:
        a.append(s)

print(len(a), a[-5:])
# проверка связи