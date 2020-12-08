with open('data.txt') as f:
    boot = [i.strip().split(' ') for i in f]

acc_counter = 0
counter = 0
done = []

while counter not in done:
    done.append(counter)
    action = boot[counter][0]
    steps = int(boot[counter][1])

    if action == 'nop':
        counter += 1
        continue
    elif action == 'acc':
        acc_counter += steps
        counter += 1
    elif action == 'jmp':
        counter += steps

print(acc_counter)