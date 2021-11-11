def read_input(filename):
    input = []
    with open(filename) as file:
        for line in file:
            input.append(int(line.strip()))
    return input


def windows(input, window_size):
    window = []
    for number in input:
        window.append(number)
        while len(window) > window_size:
            del window[0]
        if len(window) == window_size:
            yield window


def find_two(items, total):
    for idx1, value1 in enumerate(items):
        if total - value1 in items[idx1+1:]:
            return True
    return False


input = read_input('day9/input')
window_size = 25
generator = windows(input, window_size+1)
for window in generator:
    if not find_two(window[:window_size], window[window_size]):
        break


target = window[window_size]
print(target)

for size in range(2, len(input)):
    generator = windows(input, size)
    for window in generator:
        if sum(window) == target:
            print(window)
            print(f'{min(window)} + {max(window)} = {min(window) + max(window)}')
            break
