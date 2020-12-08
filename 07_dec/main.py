from functools import reduce

with open('data.txt') as f:
    rules = [line.strip('\n.').replace('contain ', '').replace('bags', 'bag').replace(',', '')
             for line in f]

rule_dict = {}
bag_clr = 'shiny gold'

for rule in rules:
    rule = [r.strip() for r in rule.split('bag')][:-1]
    color = rule[0]
    content = [r.split(' ', 1)[1].replace('other', '') for r in rule[1:]]
    rule_dict[color] = content
print(rule_dict)

clrs = []

for color in rule_dict:
    if bag_clr in rule_dict[color]:
        clrs.append(color)
        for c in rule_dict:
            if color in rule_dict[c]:
                clrs.append(c)

for i in range(7):
    for color in rule_dict:
        for clr in clrs:
            if clr in rule_dict[color]:
                clrs.append(color)
    i += 1

clrs = set(clrs)
print(len(clrs))