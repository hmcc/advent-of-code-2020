def process_input(filename):
    answer_sets = []
    answer_sets.append(set())
    taken_newline = True
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if not item:
                taken_newline = True
            elif taken_newline:
                answer_sets.append(set(item))
                taken_newline = False
            else:
                answer_sets[-1] = answer_sets[-1].intersection((set(item)))
    return answer_sets


answers = process_input('day6/input')
total = sum([len(x) for x in answers])
print(total)
