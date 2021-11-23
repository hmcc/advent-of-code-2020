def read_input(filename):
    values = []
    with open(filename) as file:
        for line in file:
            values.append(int(line.strip()))
    return values


def windows(all_values, size):
    current_window = []
    for number in all_values:
        current_window.append(number)
        while len(current_window) > size:
            del current_window[0]
        if len(current_window) == size:
            yield current_window


def find_two(items, total):
    for idx1, value1 in enumerate(items):
        if total - value1 in items[idx1+1:]:
            return True
    return False


input_values = read_input('day9/input')
window_size = 25
generator = windows(input_values, window_size+1)
window = []
for window in generator:
    if not find_two(window[:window_size], window[window_size]):
        break

target = window[window_size]
print(target)

for window_size in range(2, len(input_values)):
    generator = windows(input_values, window_size)
    for window in generator:
        if sum(window) == target:
            print(window)
            print(f'{min(window)} + {max(window)} = {min(window) + max(window)}')
            break
