import re

p = re.compile(r'[0-9]*\s*(.*)\s+bag[s]?')


def read_input(filename):
    rel = {}
    with open(filename) as file:
        for line in file:
            item = line.strip()
            if item:
                new_rel = learn_parents(item)
                for child in new_rel:
                    rel.setdefault(child, set()).update(new_rel[child])
    return rel


def color(bag):
    matcher = p.match(bag)
    if matcher:
        return matcher.group(1)
    return None


def learn_parents(line):
    parent_fragment, child_fragment = line.split(' contain ')
    parent = color(parent_fragment)
    if child_fragment.startswith('no other'):
        children = {}
    else:
        children = child_fragment.split(', ')
        children = [color(child) for child in children]
    return {child: {parent} for child in children}


def traverse(child):
    all_parents = set()
    try:
        parents = relationships[child]
        all_parents.update(parents)
        for parent in parents:
            all_parents.update(traverse(parent))
    except KeyError:
        pass
    return all_parents


relationships = read_input('day7/input')
total_parents = traverse('shiny gold')
print(len(total_parents))
