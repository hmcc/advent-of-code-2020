from collections import defaultdict
from functools import reduce


def read_input(filename):
    values = []
    with open(filename) as file:
        for line in file:
            values.append(int(line.strip()))
    return values


def diff(a, b):
    return b - a


def tally(a, b):
    a[b] += 1
    return a


# sort the adapters from the bag
input_values = read_input('day10/input')
input_values.sort()

# add the charging outlet and the device
input_values.insert(0, 0)
input_values.append(input_values[-1] + 3)

# find the difference between each pair, and tally them up
differences = map(diff, input_values[:-1], input_values[1:])
counts = reduce(tally, differences, defaultdict(int))

print(counts)
