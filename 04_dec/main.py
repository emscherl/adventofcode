import re

with open('data.txt') as f:
    passports_ugly = f.read().split('\n\n')


def height_checker(s):
    if s[-2:] == 'cm':
        try:
            h = int(s[:3])
        except ValueError:
            h = int(s[:2])
        if 150 <= h <= 193:
            return True
        else:
            return False
    elif s[-2:] == 'in':
        try:
            h = int(s[:2])
        except ValueError:
            h = int(s[:1])
        if 59 <= h <= 76:
            return True
        else:
            return False
    else:
        return False


values = {'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
          'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
          'eyr': lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
          'hgt': height_checker,
          'hcl': lambda s: re.match(r'#[a-f0-9]{6}', s),
          'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
          'pid': lambda s: len(s) == 9 and s.isdigit()
          }

passports = []

for p in passports_ugly:
    passports.append(p.replace('\n', ' ').split(' '))

counter = 0
counter_call2 = 0

for p in passports:
    d = dict(i.split(':') for i in p)
    if all(v in d for v in values):
        counter += 1
        checker = True
        for i in values:
            fun = values[i]
            if not fun(d[i]):
                checker = False
        if checker:
            counter_call2 += 1

print(counter)
print(counter_call2)
