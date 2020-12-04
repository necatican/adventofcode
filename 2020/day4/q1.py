import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()

passports = []
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0

for line in lines:
    if line == '\n':
        passport = ' '.join(passports)
        for field in required_fields:
            if passport.find(field) == -1:
                break
        else:
            valid_count += 1
        passports = []
        continue
    passports.append(line.strip())

print(valid_count)
