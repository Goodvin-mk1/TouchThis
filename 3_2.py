#
# Найти среднее арифметическое из трех чисел,
# оставив 3 знака после точки
#
print("Enter a, b, c")
num_a = int(input("a="))
num_b = int(input("b="))
num_c = int(input("c="))
average = (num_a + num_b + num_c) / 3
print(round(average, 3))
