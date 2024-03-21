res = []
for i in range(1, 10000 + 1):
    if all([i%2 != 0, i%4!=0, i%5 != 0, i%9 != 0]):
        res.append(i)

print(len(res), res[-5:])
