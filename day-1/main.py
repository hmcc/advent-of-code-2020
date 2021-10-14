def readInput(filename):
    items = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if(item):
                try:
                    items.append(int(item))
                except ValueError:
                    print(f'"{item}" is not an integer')
    return items


def findTwo(items, total):
    for idx1, value1 in enumerate(items):
        for value2 in items[idx1+1:]:
            if value1 + value2 == total:
                return (value1, value2)


expenses = readInput('input')

# Find 2 values satisfying x + y = 2020
value1, value2 = findTwo(expenses, 2020)
print(f'{value1} + {value2} = {value1 + value2}')
print(f'{value1} * {value2} = {value1 * value2}')

# Find 3 values satisfying x + y + z = 2020
for idx1, value1 in enumerate(expenses):
    result = findTwo(expenses[idx1+1:], 2020 - value1)
    if(result):
        value2, value3 = result
        print(f'{value1} + {value2} + {value3} = {value1 + value2 + value3}')
        print(f'{value1} * {value2} * {value3} = {value1 * value2 * value3}')
