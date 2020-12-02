import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

numbers = set()
for line in lines:
    numbers.add(int(line))

for first_number in numbers:
    desired_total = 2020 - first_number
    for second_number in numbers:
        third_number = desired_total - second_number
        if third_number in numbers:
            print(first_number * second_number * third_number)
            exit()
