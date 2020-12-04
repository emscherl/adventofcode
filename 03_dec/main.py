with open('data.txt') as input:
    lines = [line.rstrip() for line in input]

def tree_slope(x, y, tree_list):
    count = 0
    line = 0
    trees = 0

    while line < len(tree_list):
        f = tree_list[line]
        if f[count] == '#':
            trees += 1
        line += y
        count += x
        if count >= len(f):
            count -= len(f)

    return trees

trees_1 = tree_slope(1, 1, lines)
print(trees_1)

trees_2 = tree_slope(3, 1, lines)
print(trees_2)

trees_3 = tree_slope(5, 1, lines)
print(trees_3)

trees_4 = tree_slope(7, 1, lines)
print(trees_4)

trees_5 = tree_slope(1, 2, lines)
print(trees_5)

print(trees_1 * trees_2 * trees_3 * trees_4 * trees_5)
