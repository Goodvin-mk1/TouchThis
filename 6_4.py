# Оставить в списке из разных типов данных только строки

trash_list = ['str', 'python', [123, 'get', 'set'], 12, ('some', 87), 11.45, {1: 'air'}, 16, 'sky', True, 'works']


def leave_only_str(lst: list):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], str):
            i += 1
            continue
        else:
            lst.remove(lst[i])
    return lst


print(leave_only_str(trash_list))
