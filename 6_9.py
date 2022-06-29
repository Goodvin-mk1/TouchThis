# Вывести тех, у кого не ключа email,
# или значение этого ключа отсутствует

users_id = {
    'id1': {
        'fname': 'Nikita',
        'lname': 'Matyushonok',
        'phone': '232323',
        'email': 'Nikita@mail.ru'
    },
    'id2': {
        'fname': 'Pasha',
        'lname': 'Turkov',
        'phone': '767676',
        'email': 'Pasha@mail.ru'
    },
    'id3': {
        'fname': 'Nastya',
        'lname': 'Gorbacheva',
        'phone': '414141',
        'email': ''
    },
    'id4': {
        'fname': 'Veniamin',
        'lname': 'Leadsman',
        'phone': '909090'
    }
}
for u_id in users_id.values():
    if 'email' not in u_id:
        print(u_id['fname'])
    elif u_id['email'] == '':
        print(u_id['fname'])
