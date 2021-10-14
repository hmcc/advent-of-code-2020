import re
p = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]*)')


def password_match_policy_one(password, letter, min_count, max_count):
    count = password.count(letter)
    return min_count <= count <= max_count


def password_match_policy_two(password, letter, position1, position2):
    return (password[position1-1] == letter) ^ (password[position2-1] == letter)


def parse(line):
    matcher = p.match(line)
    if matcher:
        return(
            int(matcher.group(1)),
            int(matcher.group(2)),
            matcher.group(3),
            matcher.group(4)
        )
    raise ValueError


def count_matches():
    count = 0
    with open('input') as file:
        for line in file:
            line = line.rstrip()
            try:
                value1, value2, letter, password = parse(line)
                if password_match_policy_two(password, letter, value1, value2):
                    count += 1
            except IndexError:
                print(f'"{line}" cannot be checked against the rule')
            except ValueError:
                print(f'"{line}" does not match the expected format')
    return count


print(count_matches())
