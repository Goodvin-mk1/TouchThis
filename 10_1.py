# Дан многострочный файл txt

num = int(input("Enter n: "))


def option_a(n: int):
    # Разбить файл на N файлов построчно
    # в последний записывается все до конца
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    i = 0
    while i < n:
        if i == n - 1:
            new_file = open('file' + str(i + 1) + '.txt', 'w', encoding='utf-8')
            new_file.write('\n'.join(lines[i:]))
            break
        new_file = open('file' + str(i + 1) + '.txt', 'w', encoding='utf-8')
        new_file.write(lines[i])
        i += 1


def option_b(n: int):
    # Разбить файл на несколько файлов по N строк
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    file_name = 1
    i = 0
    while i < len(lines):
        with open('file' + str(file_name) + '.txt', 'w', encoding='utf-8') as new_file:
            new_file.write('\n'.join(lines[i:i + n]))
            i += n
            file_name += 1
