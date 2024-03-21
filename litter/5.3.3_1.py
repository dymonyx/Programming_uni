import itertools
a = []
k = '1234567'
for i in itertools.permutations('1234567'):
    s = ''.join(i)
    flag = 0
    for i in range(7):
        if k[i] == s[i]:
            flag += 1
    if flag == 2:
        a.append(s)

for i in itertools.permutations('1234567'):
    s = ''.join(i)
    flag = 0
    for i in range(7):
        if k[i] == s[i]:
            flag += 1
    if flag == 4:
        a.append(s)

print(len(a), a[-5:])