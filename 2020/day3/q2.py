import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

column = []
rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
final_result = 1

for line in lines:
    column.append(list(line.strip()))

for rule in rules:
    right_steps = rule[0]
    down_steps = rule[1]
    print(right_steps, down_steps)
    cursor = 0
    tree_count = 0
    i = 0
    while i in range(len(column) - down_steps):
        row = column[i]
        row_length = len(row)
        cursor += right_steps
        cursor %= row_length
        i += down_steps
        if column[i][cursor] == '#':
            tree_count += 1
    final_result *= tree_count
print(final_result)
