with open('data.txt') as f:
    rules = [line.strip('\n.').replace('contain ', '').replace('bags', 'bag').replace(',', '')
             for line in f]

rule_dict = {}
bag_clr = 'shiny gold'

for rule in rules:
    rule = [r.strip() for r in rule.split('bag')][:-1]
    color_primary = rule[0]
    content = [r.split(' ', 1)[1].replace('other', '') for r in rule[1:]]
    rule_dict[color_primary] = content

def shiny_gold(color):
    if color == bag_clr:
        return True
    else:
        if color != '':
            return any(shiny_gold(child) for child in rule_dict[color])

print(sum(shiny_gold(color) for color in rule_dict.keys())-1)
