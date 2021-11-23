from functools import reduce
from operator import mul


def read_input(filename):
    values = []
    with open(filename) as file:
        for line in file:
            values.append(int(line.strip()))
    return values


def path_count(n):
    """
    Given the length of a sorted list of joltages with joltage difference 1,
    calculate the number of ways to combine them.
    e.g. [4, 5, 6, 7] can be combined as
    [4, 5, 6, 7]
    [4, 6, 7]
    [4, 5, 7]
    [4, 7]
    = 4 ways
    The answers to the first few are known:
    n   | Paths
    --- | ---
    1   | 1
    2   | 1
    3   | 2
    4   | 4
    After this, the answer is double the previous answer, minus the answer
    from 4 answers ago
    n   | Paths
    --- | ---
    5   | 7 (4 * 2 - 1)
    6   | 13 (7 * 2 - 1)
    7   | 24 (13 * 2 - 2)
    8   | 44 (24 * 2 - 4)
    """
    if n < 5:
        return pow(2, max(n - 2, 0))
    return path_count(n - 1) * 2 - path_count(n - 4)


def sublists(input_list):
    """
    Given a sorted input list of joltages, where the difference between each
    joltage is either 1 or 3, return all the sections where the joltage
    difference is 1, as a new list.
    e.g. [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19] ->
    [1], [4, 5, 6, 7], [10, 11, 12], [15, 16], [19]
    """
    sublist = [input_list[0]]
    for item in input_list[1:]:
        if item - sublist[-1] == 1:
            sublist.append(item)
        if item - sublist[-1] == 3:
            yield sublist
            sublist = [item]
    yield sublist


# sort the adapters from the bag
input_values = read_input('day10/input')
input_values.sort()

# add the charging outlet and the device
input_values.insert(0, 0)
input_values.append(input_values[-1] + 3)

# count the possible paths for each block with joltage differences of 1
# and multiply the answers together
answer = reduce(mul, (path_count(len(s)) for s in sublists(input_values)))
print(answer)
