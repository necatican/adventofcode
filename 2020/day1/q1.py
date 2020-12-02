import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

numbers = set()
for line in lines:
    numbers.add(int(line))

for number in numbers:
    desired_num = 2020 - number
    if desired_num in numbers:
        print(number * desired_num)
        break
