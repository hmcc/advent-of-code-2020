import re

p = re.compile(r'[0-9]*\s*(.*)\s+bag[s]?')
p2 = re.compile(r'([0-9]+)\s*(.*)\s+bag[s]?')


def read_input(filename):
    rel = {}
    with open(filename) as file:
        for line in file:
            item = line.strip()
            if item:
                new_rel = learn_children(item)
                for child in new_rel:
                    rel.setdefault(child, set()).update(new_rel[child])
    return rel


def color(bag):
    matcher = p.match(bag)
    if matcher:
        return matcher.group(1)
    return None


def color_and_count(bag):
    matcher = p2.match(bag)
    if matcher:
        return (matcher.group(2), int(matcher.group(1)))
    return None


def learn_children(line):
    parent_fragment, child_fragment = line.split(' contain ')
    parent = color(parent_fragment)
    if child_fragment.startswith('no other'):
        children = {}
    else:
        children = child_fragment.split(', ')
        children = {color_and_count(child) for child in children}
    return {parent: children}


def learn_parents(line):
    parent_fragment, child_fragment = line.split(' contain ')
    parent = color(parent_fragment)
    if child_fragment.startswith('no other'):
        children = {}
    else:
        children = child_fragment.split(', ')
        children = [color(child) for child in children]
    return {child: {parent} for child in children}


def traverse_up(child):
    all_parents = set()
    try:
        parents = relationships[child]
        all_parents.update(parents)
        for parent in parents:
            all_parents.update(traverse_up(parent))
    except KeyError:
        pass
    return all_parents


def traverse_down(parent):
    cost = 0
    try:
        children = relationships[parent]
        for child in children:
            cost = cost + child[1]
            cost = cost + child[1] * traverse_down(child[0])
    except KeyError:
        pass
    return cost


relationships = read_input('day7/input')
print(traverse_down('shiny gold'))
