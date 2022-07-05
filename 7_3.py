# Количество совпавших букв на одном индексе

str_a: str = input("Str a: ")
str_b: str = input("Str b: ")


def match(a: str, b: str) -> int:
    count: int = 0
    i: int = 0
    if len(a) >= len(b):
        min_len = len(b)
    else:
        min_len = len(a)
    while i < min_len:
        if a[i] == b[i]:
            count += 1
        i += 1
    return count


print(match(str_a, str_b))
