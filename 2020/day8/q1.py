import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, 'input'), 'r')
lines = input_file.readlines()


commands = []
for line in lines:
    command_parts = line.strip().split(' ')
    command_int = int(command_parts[1])
    command_executed = False

    commands.append(
        (command_parts[0], {'value': command_int, 'status': command_executed}))

accumulator = 0
cursor = 0
while cursor in range(len(commands)):
    command_tuple = commands[cursor]
    command = command_tuple[0]
    is_executed = command_tuple[1]['status']
    command_value = command_tuple[1]['value']
    if is_executed:
        break

    commands[cursor][1]['status'] = True

    if command in ['nop', 'acc']:
        cursor += 1
    if command == 'acc':
        accumulator += command_value
    elif command == 'jmp':
        cursor += command_value
print(accumulator)
