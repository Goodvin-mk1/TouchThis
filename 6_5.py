# Развернуть список, без использования метода .reverse,
# функции reversed, без дополнительного списка и без среза

num_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]


def new_reverse(lst: list):
    i = 0
    while i < len(lst):
        lst.insert(0 + i, lst.pop(len(lst) - 1))
        i += 1
    return lst


print(new_reverse(num_list))
