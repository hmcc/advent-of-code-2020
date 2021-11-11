def windows(filename, window_size):
    window = []
    with open(filename) as file:
        for line in file:
            number = int(line.strip())
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


size = 25
generator = windows('day9/input', size+1)
for window in generator:
    if not find_two(window[:size], window[size]):
        print(window[size])
        break
