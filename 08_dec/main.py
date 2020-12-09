def get_input():
    with open('data.txt') as f:
        boot = [i.strip().split(' ') for i in f]
    return boot


boot = get_input()

lst_jmp = []
lst_nop = []


def get_op_idx(op):
    boot = get_input()
    op_idx = []
    for i in range(len(boot)):
        if boot[i][0] == op:
            op_idx.append(i)
    return op_idx


jmp_idx = get_op_idx('jmp')
nop_idx = get_op_idx('nop')

#print(jmp_idx)
#print(nop_idx)

change_id = 0

for e in jmp_idx:
    done = []
    c = 0
    boot = get_input()
    if boot[e][0] == 'jmp':
        boot[e][0] = 'nop'
        while c not in done:
            done.append(c)
            if c == len(boot) - 1:
                change_id = e
            elif c > len(boot) - 1:
                continue
            elif boot[c][0] == 'jmp':
                c += int(boot[c][1])
            else:
                c += 1


print('change id: ', change_id)

boot = get_input()
boot[change_id][0] = 'nop'

acc_counter = 0
counter = 0
done = []

while counter not in done:
    done.append(counter)

    if counter == len(boot) - 1:
        break
    action = boot[counter][0]
    steps = int(boot[counter][1])

    if action == 'nop':
        counter += 1
    elif action == 'acc':
        acc_counter += steps
        counter += 1
    elif action == 'jmp':
        counter += steps


print(acc_counter)

# print(done)
# print(acc_counter)
