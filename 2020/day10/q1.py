import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, 'input'), 'r')
lines = input_file.readlines()

jolts = set()
one_jolt_diff_count = 0
# Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).
three_jolt_diff_count = 1

for line in lines:
    jolts.add(int(line.strip()))

previous_jolt = 0
for jolt in jolts:
    if jolt - previous_jolt == 1:
        one_jolt_diff_count += 1
    elif jolt - previous_jolt == 3:
        three_jolt_diff_count += 1
    previous_jolt = jolt

print(one_jolt_diff_count * three_jolt_diff_count)
