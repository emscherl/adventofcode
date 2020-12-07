with open("data.txt") as f:
    g_answers_ugly = f.read().split('\n\n')

g_answers = []
counter = 0


for g in g_answers_ugly:
    g_answers.append(g.split('\n'))

# print(g_answers)

for group in g_answers:
    counter_p = 0
    if len(group) == 1:
        counter += len(group[0])
    else:
        counter_p = len(group)
        group = ''.join(group)
        for i in set(group):
            if group.count(i) == counter_p:
                counter += 1


print(counter)
