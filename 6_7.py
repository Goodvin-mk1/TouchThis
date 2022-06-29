# Посчитать сумму соседей для каждого элемента в списке

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(num_list):
    if i == 0:
        summ = num_list[i + 1] + num_list[-1]
        print('For ', num_list[i], ' sum of nearest: ', summ)
        i += 1
    elif i == num_list.index(num_list[-1]):
        summ = num_list[i - 1] + num_list[0]
        print('For ', num_list[i], ' sum of nearest: ', summ)
        i += 1
    else:
        summ = num_list[i - 1] + num_list[i + 1]
        print('For ', num_list[i], ' sum of nearest: ', summ)
        i += 1
