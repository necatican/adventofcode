import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

answers = set()
total_answer_count = 0
first_line = ''
for line in lines:
    if line == '\n':
        total_answer_count += len(answers)
        answers = set()
        first_line = ''
        continue

    if not answers:
        if first_line:
            continue
        first_line = list(line.strip())
        answers.update(first_line)
    else:
        for char in first_line:
            if char not in line and char in answers:
                answers.remove(char)

print(total_answer_count)
