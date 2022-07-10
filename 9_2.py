# Найти сумму модулей отрицательных нечетных элементов.
from pprint import pprint
from random import randint


def modul_sum(array: list) -> int:
    result = 0
    for row in array:
        for el in row:
            is_negative = el < 0
            is_odd = el % 2

            if is_negative and is_odd:
                result += el
    return abs(result)


input_array = [[randint(-5, 5) for _ in range(5)] for _ in range(5)]
pprint(input_array)
print(modul_sum(input_array))
