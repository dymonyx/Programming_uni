s1, s2 = input("Введите первую строку: ").lower(), input("введите вторую строку: ").lower()
arr1 = [i in s2 for i in s1]
arr2 = [i in s1 for i in s2]
print(all(arr1+arr2))