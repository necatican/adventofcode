import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, 'input'), 'r')
lines = input_file.readlines()

preamble = 25
preamble_done = False
numbers = []

for line in lines:
    current_number = int(line.strip())
    if preamble_done:
        is_found = False
        for number in numbers[:-1]:
            desired_num = abs(current_number - number)
            if desired_num in numbers:
                is_found = True
        if not is_found:
            print(current_number)
            break
        numbers.pop(0)
    numbers.append(current_number)
    preamble_done = len(numbers) == preamble
