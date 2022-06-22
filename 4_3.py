count_users = int(input('Enter count of new users: '))
my_dict = {i: {'name:' + input(f'{i} user name: '), 'email:' + input(f'{i} user email: ')} for i in
           range(1, count_users + 1)}
print(my_dict)
