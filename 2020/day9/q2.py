import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, 'input'), 'r')
lines = input_file.readlines()

# `The final step in breaking the XMAS encryption relies on the invalid number you just found`
target_number = 1124361034
numbers = []

for line in lines:
    current_number = int(line.strip())
    numbers.append(current_number)
numbers.remove(target_number)

cursor = 0
while cursor in range(len(numbers)):
    slice_cursor = cursor
    number_slice = []
    while sum(number_slice) < target_number:
        number_slice.append(numbers[slice_cursor])
        slice_cursor += 1
    if sum(number_slice) == target_number:
        print(min(number_slice) + max(number_slice))
        break
    cursor += 1
