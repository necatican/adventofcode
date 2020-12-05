import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()
seats = set()


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
    seats.add(seat_id)

cursor = 0
while cursor <= max(seats):
    # `Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.``
    # My ID shouldn't be on the list but it's a number between two numbers
    desired_number = min(seats) + cursor
    if desired_number not in seats:
        print(desired_number)
        break
    cursor += 1
