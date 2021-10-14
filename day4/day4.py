import re

hgt_pattern = re.compile(r'^(\d+)((cm|in))$')
hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
pid_pattern = re.compile(r'^[0-9]{9}$')


def to_dict(raw_passport):
    items = raw_passport.split()
    return {item.split(':')[0]: item.split(':')[1] for item in items}


def is_valid_year_range(value, start, end):
    try:
        int_value = int(value)
        return start <= int_value <= end
    except ValueError:
        return False


def is_valid_byr(byr):
    return is_valid_year_range(byr, 1920, 2002)


def is_valid_iyr(iyr):
    return is_valid_year_range(iyr, 2010, 2020)


def is_valid_eyr(eyr):
    return is_valid_year_range(eyr, 2020, 2030)


def is_valid_hgt(hgt):
    try:
        matcher = hgt_pattern.match(hgt)
        if matcher:
            value = int(matcher.group(1))
            units = matcher.group(2)
            if units == 'cm':
                return 150 <= value <= 193
            elif units == 'in':
                return 59 <= value <= 76
        return False
    except ValueError:
        return False


def is_valid_hcl(hcl):
    return hcl_pattern.match(hcl) is not None


def is_valid_ecl(ecl):
    valid_values = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return ecl in valid_values


def is_valid_pid(pid):
    return pid_pattern.match(pid) is not None


def is_valid(passport):
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return all([key in passport.keys() for key in required_keys]) \
        and is_valid_byr(passport['byr']) \
        and is_valid_iyr(passport['iyr']) \
        and is_valid_eyr(passport['eyr']) \
        and is_valid_hgt(passport['hgt']) \
        and is_valid_hcl(passport['hcl']) \
        and is_valid_ecl(passport['ecl']) \
        and is_valid_pid(passport['pid']) \



def count_matches(filename):
    with open(filename) as file:
        data = file.read()
    passports = [to_dict(passport) for passport in data.split('\n\n')]
    return sum(is_valid(passport) for passport in passports)


print(count_matches('day4/input'))
