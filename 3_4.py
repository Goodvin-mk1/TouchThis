# Посчитать кол-во положительных
# и отрицательных чисел
print("Enter three nums: ")
num_a = input("a=")
num_b = input("b=")
num_c = input("c=")
num_count = 3
cash_string_nums = str([num_a, num_b, num_c])
negative = cash_string_nums.count('-')
print(f"You have {num_count - negative} positive and {negative} negative nums")
