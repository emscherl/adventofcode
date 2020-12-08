import re

with open('data.txt') as f:
    rules = f.readlines()

rule_dict = {}
bag_clr = 'shiny gold'

for i in rules:
    regex = re.match('(.+?) bags', i)
    color_primary = regex.group(1)
    color_inside = re.findall('(\d+) (.+?) bag', i)
    if len(color_inside) > 0:
        color_inside = color_inside
        rule_dict[color_primary] = color_inside
    else:
        rule_dict[color_primary] = [('0', '')]


def shiny_gold(color):
    if color == bag_clr:
        return True
    else:
        if color != '':
            return any(shiny_gold(child) for amount, child in rule_dict[color])


print('part 1: ', sum(shiny_gold(color) for color in rule_dict.keys()) - 1)

def count_bags(color):
    if color == '':
        return 1

    return 1 + sum(int(amount)*count_bags(child) for amount, child in rule_dict[color])

print('part 2: ', count_bags(bag_clr) - 1)