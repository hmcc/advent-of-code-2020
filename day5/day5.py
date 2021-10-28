def read_input(filename):
    items = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if item:
                try:
                    items.append(item)
                except ValueError:
                    print(f'"{item}" is not an integer')
    return items


def get_row(seat_code_fragment):
    return int(seat_code_fragment.replace('F', '0').replace('B', '1'), 2)


def get_column(seat_code_fragment):
    return int(seat_code_fragment.replace('L', '0').replace('R', '1'), 2)


def decode(seat_code):
    return (get_row(seat_code[:7]), get_column(seat_code[7:]))


def seat_id(seat_code):
    decoded = decode(seat_code)
    return decoded[0] * 8 + decoded[1]


seat_codes = read_input('day5/input')
seat_ids = [seat_id(seat_code) for seat_code in seat_codes]
print(max(seat_ids))
