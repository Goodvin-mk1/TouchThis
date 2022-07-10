# Симметричени ли список

def is_symmetric(lst: list) -> bool:
    list_size = len(lst)
    for i in range(list_size // 2):
        if lst[i] != lst[list_size - i - 1]:
            return False
    return True

kek = 3 if j == i else 2 if j > i else 1
