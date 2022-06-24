# Зацикленный простой калькулятор, пользователь
# вводит число (получится ввести только число),
# выбирает операцию (только из предложенного списка)
# и еще одно число (по принципу первого)

while True:                     # После получения результата, калькулятор начнет работу сначала
    num_a = input("Enter a: ")
    while not num_a.isdigit():
        num_a = input("\"a\" must be a digit. Try again: ")
    num_a = int(num_a)
    operation_list = ['+', '-', '*', '/', '**', '//', '%']
    operation = input("Select operation: +   -   *   /   **   //   %\n: ")
    while operation not in operation_list:
        operation = input("Select operation, ONLY: +   -   *   /   **   //   %\n: ")
    num_b = input("Enter b: ")
    while not num_b.isdigit():
        num_b = input("\"b\" must be a digit. Try again: ")
    num_b = int(num_b)
    if operation == '+':
        result = num_a + num_b
    elif operation == '-':
        result = num_a - num_b
    elif operation == '*':
        result = num_a * num_b
    elif operation == '/':
        result = num_a / num_b
    elif operation == '**':
        result = num_a ** num_b
    elif operation == '//':
        result = num_a // num_b
    else:
        result = num_a % num_b
    print(result, '\n')
