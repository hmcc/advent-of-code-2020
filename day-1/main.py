def read_input(filename):
    items = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if item:
                try:
                    items.append(int(item))
                except ValueError:
                    print(f'"{item}" is not an integer')
    return items


def find_two(items, total):
    for idx1, value1 in enumerate(items):
        for value2 in items[idx1+1:]:
            if value1 + value2 == total:
                return (value1, value2)
    raise IndexError

def find_three(items, total):
    for idx1, value1 in enumerate(items):
        try:
            value2, value3 = find_two(expenses[idx1+1:], total - value1)
            return (value1, value2, value3)
        except IndexError:
            pass


expenses = read_input('input')

# Find 2 values satisfying x + y = 2020
answer1, answer2 = find_two(expenses, 2020)
print(f'{answer1} + {answer2} = {answer1 + answer2}')
print(f'{answer1} * {answer2} = {answer1 * answer2}')

# Find 3 values satisfying x + y + z = 2020
answer1, answer2, answer3 = find_three(expenses, 2020)
print(f'{answer1} + {answer2} + {answer3} = {answer1 + answer2 + answer3}')
print(f'{answer1} * {answer2} * {answer3} = {answer1 * answer2 * answer3}')
