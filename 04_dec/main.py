with open('data.txt') as f:
    passports_ugly = f.read().split('\n\n')

def height_checker(s):
    if s[-2:] == 'cm':
        if 150 <= int(s[:2]) <= 193:
            return True
        else:
            return False
    elif s[-2:] == 'in':
        if 59 <= int(s[:1]) <= 76:
            return True
        else:
            return False
    else:
        return False


values = {'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
          'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
          'eyr': lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
          'hgt': height_checker, 'hcl', 'ecl', 'pid']


passports = []

for p in passports_ugly:
    passports.append(p.replace('\n', ' ').split(' '))

counter = 0

for p in passports:
    d = dict(i.split(':') for i in p)
    if all(v in d for v in values):
        counter += 1

print(counter)
