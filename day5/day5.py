def read_input(filename):
    items = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if item:
                items.append(item)
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
seat_ids.sort()
print(seat_ids[-1])

expected_seat_ids = list(range(seat_ids[0], seat_ids[-1]))
diff = [x for x in expected_seat_ids if x not in seat_ids]
print(diff[0])
