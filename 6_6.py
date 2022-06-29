# Отсортировать список чисел, сначала четные, потом нечетные

num_list = [1, 3, 6, 11, 8, 4, 3, 5, 11, 16, 32, 99, 54, 17, 82]


def even_odd(lst: list):
    i = 0
    while i < len(lst):
        if not lst[i] % 2:
            lst.insert(0, lst.pop(i))
            i += 1
        else:
            i += 1
    return lst


print(even_odd(num_list))
