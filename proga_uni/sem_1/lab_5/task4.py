
def code(string, key):
    result = ""
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    return result

def decode(string, key):
    return (code(string, key))


if __name__ == "__main__":
    string = input('введите строку: ')
    while string != "Q":
        key = input('введите шифр: ')
        ans= input('вы хотите дешифровать или зашифровать? (d, z): ')
        if ans == "d":
            print(decode(string, key))
        elif ans == 'z':
            print(code(string, key))
        else:
            print('вы не то ввели')
        string = input("введите строку: ")