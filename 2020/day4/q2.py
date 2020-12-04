import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

passports = []
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0


def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    year_rules = {'byr': [1920, 2002], 'iyr': [
        2010, 2020], 'eyr': [2020, 2030], 'hgt': {'cm': [150, 193], 'in': [59, 76]}}
    allowed_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for field in required_fields:
        field_value = passport.get(field)
        if not field_value:
            return 0

        if field in ['byr', 'iyr', 'eyr', 'hgt']:
            rule = year_rules[field]
            if field == 'hgt':
                hgt_unit = field_value[-2:]
                if hgt_unit not in ['cm', 'in']:
                    return 0
                rule = rule[hgt_unit]
                field_value = field_value[:-2]
            if not rule[0] <= int(field_value) <= rule[1]:
                return 0
        elif field == 'hcl':
            hcl_val = field_value[1:]
            if not field_value[0] == '#' or len(hcl_val) != 6 or not hcl_val.isalnum():
                return 0
        elif field == 'ecl':
            if field_value not in allowed_eye_colors:
                return 0
        elif field == 'pid':
            if len(field_value) != 9 or not field_value.isnumeric():
                return 0
    return 1


for line in lines:
    if line == '\n':
        passport_fields = ' '.join(passports).split(' ')
        passport = {}
        for field in passport_fields:
            field_key_pair = field.split(':')
            passport[field_key_pair[0]] = field_key_pair[1]
        valid_count += validate_passport(passport)
        passports = []
        continue
    passports.append(line.strip())

print(valid_count)
