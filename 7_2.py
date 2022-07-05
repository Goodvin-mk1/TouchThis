# Пагинатор

lst: list = ['You', 'are', 'the', 'best', 'man']


def paginator(some_lst: list):
    print(some_lst)
    i: int = 0
    n: str = ''
    print("< or > \nPress \'c\' to close")
    print(some_lst[i])
    while n != 'c':
        n = input(': ')
        if n == '>':
            if i == len(some_lst) - 1:
                i = -1
            i += 1
            print(some_lst[i])
        elif n == '<':
            if i == 0:
                i = len(some_lst)
            i -= 1
            print(some_lst[i])


paginator(lst)
