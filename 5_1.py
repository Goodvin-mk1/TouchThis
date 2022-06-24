# Вывести первые N чисел, кратные M и больше K

k = int(input("Enter K: "))
n = int(input("Enter N: "))
m = int(input("Enter M: "))
i = k                           # i начнется от K
counter_before_n = 0
while counter_before_n != n:
    if not i % m and i > k:
        print(i)
        counter_before_n += 1
    i += 1
