from pprint import pprint

n = int(input("N = "))

# Диагональ слева на право
input_array = [[3 if col == row else 2 if col > row else 1 for col in range(n)] for row in range(n)]
pprint(input_array)

# Диагональ справа на лево
input_array = [[3 if col == n - row - 1 else 2 if col < n - row - 1 else 1 for col in range(n)] for row in range(n)]
pprint(input_array)
