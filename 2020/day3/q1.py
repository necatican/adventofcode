import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

cursor = 0
tree_count = 0
column = []

for line in lines:
    column.append(list(line.strip()))

for i in range(len(column) - 1):
    row = column[i]
    row_length = len(row)
    cursor += 3
    cursor %= row_length

    if column[i + 1][cursor] == '#':
        tree_count += 1

print(tree_count)
