s1 = input("Введите строку: ")
s1 = "".join(c for c in s1 if c.isalpha())
name = ''
while s1 != "":
    name += s1[-1]
    s1 = input("Введите строку: ")
    s1 = "".join(c for c in s1 if c.isalpha())
print("ваше имя: ", name)

"""я сижу сегодня и горюю,
положу-ка я ложку на стол.
как прекрасна земля!"""