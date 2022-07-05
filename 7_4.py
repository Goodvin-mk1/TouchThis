# Отсортировать список чисел,
# не используя sort и sorted

lst: list = [8, 2, 2, 2, 6, 12, 4, 9, 999, 55, 32, 7, 3, 76]


def my_sort(some_lst: list) -> list:
    sorted_list = []
    for i in range(len(some_lst)):
        sorted_list.append(some_lst.pop(some_lst.index(min(some_lst))))
    return sorted_list


print(my_sort(lst))
