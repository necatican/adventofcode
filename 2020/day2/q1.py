import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()
correct_password_count = 0

for line in lines:
    parts = line.split(':')
    rule_parts = parts[0].split(' ')
    policy_range = rule_parts[0].split('-')
    letter = rule_parts[1]

    letter_count = parts[1].strip().count(letter)
    if int(policy_range[0]) <= letter_count <= int(policy_range[1]):
        correct_password_count += 1
print(correct_password_count)
