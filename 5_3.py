# Вывести четные числа от 2 до N по 5 в строку

n = int(input("Enter N: "))
for i in range(2, n + 1, 2):
    print(i, end=' ')
    if i % 5 == 0:
        print('')
