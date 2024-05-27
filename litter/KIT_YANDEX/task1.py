dec = int(input())
sev = ''
while dec > 0:
    sev += str(dec%7)
    dec //= 7
print(sev[::-1])