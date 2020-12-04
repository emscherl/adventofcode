import re

count = 0

pattern = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'

with open('data.txt') as f:
    lines = f.readlines()

for i in lines:
    match = re.search(pattern, i)
    min_val = int(match.group(1))
    max_val = int(match.group(2))
    char = match.group(3)
    pword = match.group(4)

    if pword[min_val-1] == char and not pword[max_val-1] == char:
        count += 1
    if pword[max_val - 1] == char and not pword[min_val - 1] == char:
        count += 1
print(count)
