import re
p = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]*)')

def passwordMatchPolicyOne(password, letter, minCount, maxCount):
    count = password.count(letter)
    return count >= minCount and count <= maxCount

def passwordMatchPolicyTwo(password, letter, position1, position2):
    return (password[position1-1] == letter) ^ (password[position2-1] == letter)

def parse(line):
    m = p.match(line)
    if m:
        return(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))
    raise ValueError


correct = 0
with open('input') as file:
    for line in file:
        line = line.rstrip()
        try:
            value1, value2, letter, password = parse(line)
            if passwordMatchPolicyTwo(password, letter, value1, value2):
                correct += 1
        except IndexError:
            print(f'"{line}" cannot be checked against the rule')
        except ValueError:
            print(f'"{line}" does not match the expected format')

print (correct)