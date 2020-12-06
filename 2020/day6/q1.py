import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

answers = set()
total_answer_count = 0
for line in lines:
    if line == '\n':
        total_answer_count += len(answers)
        answers = set()
        continue
    answers.update(list(line.strip()))

print(total_answer_count)
