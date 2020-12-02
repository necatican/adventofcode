import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()
correct_password_count = 0

for line in lines:
    occurrence_count = 0
    # Exactly one of these positions must contain the given letter.
    parts = line.split(':')
    rule_parts = parts[0].split(' ')
    positions = rule_parts[0].split('-')
    letter = rule_parts[1]
    password = parts[1].strip()

    for position in positions:
        # Be careful; Toboggan Corporate Policies have no concept of "index zero"!
        if password[int(position) - 1] == letter:
            occurrence_count += 1

    if occurrence_count == 1:
        correct_password_count += 1
print(correct_password_count)
