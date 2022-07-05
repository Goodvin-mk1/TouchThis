# Перевод десятичного числа в двоичное и обратно

num = int(input("Enter number to converte: "))


def to_binary(n):
    binary_num = ''
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num


def to_numeric(b):
    b = list(map(int, b))
    numeric = 0
    degree = 0
    for i in b[::-1]:
        numeric += (i * (2 ** degree))
        degree += 1
    return numeric


print(to_binary(num))
print(to_numeric(to_binary(num)))
