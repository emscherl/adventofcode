with open('data.txt') as f:
    xmas = [int(i) for i in f]


def get_prev_5(idx: int, lst: list) -> list:
    return lst[idx - 25:idx]


def check_sum(num: int, lst: list):
    checklist = []
    for i in range(len(lst)):
        for x in lst:
            if x + lst[i] == num:
                checklist.append(True)
    if not checklist:
        return False
    else:
        return True


for i in range(len(xmas)):
    if i < 25:
        continue
    prev_5 = get_prev_5(i, xmas)
    if not check_sum(xmas[i], prev_5):
        print(xmas[i], 'at idx', i)
        break
