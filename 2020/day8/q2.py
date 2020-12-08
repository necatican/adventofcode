import os
import copy
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, 'input'), 'r')
lines = input_file.readlines()


def execute_commands(commands):
    accumulator = 0
    cursor = 0
    while cursor in range(len(commands)):
        command_tuple = commands[cursor]
        command = command_tuple[0]
        is_executed = command_tuple[1]['status']
        command_value = command_tuple[1]['value']
        if is_executed:
            return 0
        commands[cursor][1]['status'] = True
        if command in ['nop', 'acc']:
            cursor += 1
        if command == 'acc':
            accumulator += command_value
        elif command == 'jmp':
            cursor += command_value
    return accumulator


commands = []
for line in lines:
    command_parts = line.strip().split(' ')
    command_int = int(command_parts[1])
    command_executed = False

    commands.append(
        (command_parts[0], {'value': command_int, 'status': command_executed}))

i = 0
while i in range(len(commands)):
    command = commands[i][0]
    if command not in ['jmp', 'nop']:
        i += 1
        continue

    command_list = copy.deepcopy(commands)
    if command == 'jmp':
        command_list[i] = ('nop', command_list[i][1])
    else:
        command_list[i] = ('jmp', command_list[i][1])
    result = execute_commands(command_list)
    if result != 0:
        print(result)
        break
    i += 1
