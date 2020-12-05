import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()
highest_seat = 0


def find_row_or_column(letters, possible_seats):
    half_length = int(len(possible_seats)/2)
    if letters[0] in ['F', 'L']:
        possible_seats_new = possible_seats[:half_length]
        if len(letters) == 1:
            return possible_seats_new[0]
        return find_row_or_column(letters[1:], possible_seats_new)
    elif letters[0] in ['B', 'R']:
        possible_seats_new = possible_seats[half_length:]
        if len(letters) == 1:
            return possible_seats_new[0]
        return find_row_or_column(letters[1:], possible_seats[half_length:])


for line in lines:
    line = line.strip()
    row = find_row_or_column(line[:-3], range(128))
    col = find_row_or_column(line[-3:], range(8))
    seat_id = (row * 8) + col
    if seat_id > highest_seat:
        highest_seat = seat_id
print(highest_seat)
