start = input('Введите строку: ')
end = ''
for i in range(len(start)):
    if start[i] == start[i].lower():
        end+=start[i].upper()
    else:
        end+=start[i].lower()

print(end, len(end))