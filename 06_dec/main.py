with open("data.txt") as f:
    g_answers_ugly = f.read().split('\n\n')

g_answers = []
counter = 0

for g in g_answers_ugly:
    g_answers.append(g.replace('\n', ''))

for g in g_answers:
    counter += (len(set(g)))

print(counter)