def read_input(filename):
    values = []
    with open(filename) as file:
        for line in file:
            values.append(int(line.strip()))
    return values


def paths(values, path_so_far, idx):
    for offset in range(1, 4):
        if idx + offset == len(values) - 1:
            if values[idx + offset] - values[idx] < 4:
                yield path_so_far + [values[-1]]
            break
        elif values[idx + offset] - values[idx] < 4:
            for path in paths(values, path_so_far + [values[idx+offset]], idx+offset):
                yield path


# sort the adapters from the bag
input_values = read_input('day10/input_sample')
input_values.sort()

# add the charging outlet and the device
input_values.insert(0, 0)
input_values.append(input_values[-1] + 3)

possible_paths = paths(input_values, input_values[:1], 0)
print(sum(1 for ignore in possible_paths))
