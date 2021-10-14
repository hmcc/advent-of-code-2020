from day4 import day4

def test_is_valid_byr_too_low():
    assert day4.is_valid_byr(1919) == False


def test_is_valid_byr_too_high():
    assert day4.is_valid_byr(2003) == False


def test_is_valid_byr_just_right():
    assert day4.is_valid_byr(1920) == True
    assert day4.is_valid_byr(2002) == True


def test_is_valid_iyr_too_low():
    assert day4.is_valid_iyr(2009) == False


def test_is_valid_iyr_too_high():
    assert day4.is_valid_byr(2021) == False


def test_is_valid_iyr_just_right():
    assert day4.is_valid_iyr(2010) == True
    assert day4.is_valid_iyr(2020) == True


def test_is_valid_eyr_too_low():
    assert day4.is_valid_eyr(2019) == False


def test_is_valid_eyr_too_high():
    assert day4.is_valid_eyr(2031) == False


def test_is_valid_eyr_just_right():
    assert day4.is_valid_eyr(2020) == True
    assert day4.is_valid_eyr(2030) == True


def test_is_valid_height_cm_too_low():
    assert day4.is_valid_hgt('149cm') == False


def test_is_valid_height_cm_too_high():
    assert day4.is_valid_hgt('194cm') == False


def test_is_valid_height_cm_just_right():
    assert day4.is_valid_hgt('150cm') == True
    assert day4.is_valid_hgt('193cm') == True


def test_is_valid_height_in_too_low():
    assert day4.is_valid_hgt('58in') == False


def test_is_valid_height_in_too_high():
    assert day4.is_valid_hgt('77in') == False


def test_is_valid_height_in_just_right():
    assert day4.is_valid_hgt('59in') == True
    assert day4.is_valid_hgt('76in') == True

def test_is_valid_height_wrong_units():
    assert day4.is_valid_hgt('5ft') == False


def test_is_valid_hcl_false():
    assert day4.is_valid_hcl('#123abz') == False
    assert day4.is_valid_hcl('123abc') == False


def test_is_valid_hcl_true():
    assert day4.is_valid_hcl('#123abc') == True


def test_is_valid_ecl_false():
    assert day4.is_valid_ecl('wat') == False


def test_is_valid_ecl_true():
    assert day4.is_valid_ecl('brn') == True


def test_is_valid_pid_false():
    assert day4.is_valid_pid('0123456789') == False


def test_is_valid_pid_true():
    assert day4.is_valid_pid('000000001') == True