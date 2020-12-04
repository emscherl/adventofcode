with open('data.txt') as input:
    lines = [line.rstrip() for line in input]

count = 0
line = 1
trees = 0


def tree_slope(x, y, lines):
    count = 0
    line = 1
    trees = 0

    for i in lines:
        if line % y == 0:
            pass
        print(line, count, i[count])
        if i[count] == '#':
            trees += 1
        count += 3
        if count >= len(i):
            count -= (len(i))
        line += 1
print(trees)