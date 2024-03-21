di = {}
massiv = []
for i in input().split():
    massiv.append(i)
for i in massiv:
    kod = i[:2]
    if di[kod] != 0:
        di[kod] = i
    else:
        di[kod] = []
        di[kod] += i

print(*sorted(di.items()))