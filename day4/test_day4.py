from day4 import day4


def test_is_valid_byr_too_low():
    assert day4.is_valid_byr(1919) is False


def test_is_valid_byr_too_high():
    assert day4.is_valid_byr(2003) is False


def test_is_valid_byr_just_right():
    assert day4.is_valid_byr(1920) is True
    assert day4.is_valid_byr(2002) is True


def test_is_valid_iyr_too_low():
    assert day4.is_valid_iyr(2009) is False


def test_is_valid_iyr_too_high():
    assert day4.is_valid_byr(2021) is False


def test_is_valid_iyr_just_right():
    assert day4.is_valid_iyr(2010) is True
    assert day4.is_valid_iyr(2020) is True


def test_is_valid_eyr_too_low():
    assert day4.is_valid_eyr(2019) is False


def test_is_valid_eyr_too_high():
    assert day4.is_valid_eyr(2031) is False


def test_is_valid_eyr_just_right():
    assert day4.is_valid_eyr(2020) is True
    assert day4.is_valid_eyr(2030) is True


def test_is_valid_height_cm_too_low():
    assert day4.is_valid_hgt('149cm') is False


def test_is_valid_height_cm_too_high():
    assert day4.is_valid_hgt('194cm') is False


def test_is_valid_height_cm_just_right():
    assert day4.is_valid_hgt('150cm') is True
    assert day4.is_valid_hgt('193cm') is True


def test_is_valid_height_in_too_low():
    assert day4.is_valid_hgt('58in') is False


def test_is_valid_height_in_too_high():
    assert day4.is_valid_hgt('77in') is False


def test_is_valid_height_in_just_right():
    assert day4.is_valid_hgt('59in') is True
    assert day4.is_valid_hgt('76in') is True


def test_is_valid_height_wrong_units():
    assert day4.is_valid_hgt('5ft') is False


def test_is_valid_hcl_false():
    assert day4.is_valid_hcl('#123abz') is False
    assert day4.is_valid_hcl('123abc') is False


def test_is_valid_hcl_true():
    assert day4.is_valid_hcl('#123abc') is True


def test_is_valid_ecl_false():
    assert day4.is_valid_ecl('wat') is False


def test_is_valid_ecl_true():
    assert day4.is_valid_ecl('brn') is True


def test_is_valid_pid_false():
    assert day4.is_valid_pid('0123456789') is False


def test_is_valid_pid_true():
    assert day4.is_valid_pid('000000001') is True
