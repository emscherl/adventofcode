with open('data.txt') as f:
    adapters = [int(i) for i in f]

adapters.append(max(adapters) + 3)


def get_3_larger(idx: int):
    return [idx+1, idx+2, idx+3]


cur_adapt = 0
count_1 = 0
count_3 = 0

for i in range(len(adapters)):
    nxt_3_adapt = get_3_larger(cur_adapt)
    nxt_adapt = min(adapters)

    if nxt_adapt == nxt_3_adapt[0]:
        count_1 += 1

    if nxt_adapt == nxt_3_adapt[2]:
        count_3 += 1

    cur_adapt = nxt_adapt
    adapters.remove(cur_adapt)

print('1-jolt:', count_1, '  3-jolt:', count_3)
print('Result:', count_1 * count_3)