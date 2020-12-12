with open('data.txt') as f:
    xmas = [int(i) for i in f]

lst_elem = 25
inv_num = int


def get_prev(idx: int, lst: list, num_elem: int) -> list:
    return lst[idx - num_elem:idx]


def check_sum(num: int, lst: list) -> bool:
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
    if i < lst_elem:
        continue
    prev_5 = get_prev(i, xmas, lst_elem)
    if not check_sum(xmas[i], prev_5):
        inv_num = xmas[i]
        print(xmas[i], 'at idx', i)
        break


def get_en_weak(lst: list, num: int) -> list:
    for i in range(len(lst)):
        en_weak = [lst[i]]
        for e in range(1, len(lst)):
            if i + e == len(lst):
                break
            en_weak.append(lst[i + e])
            if sum(en_weak) == num:
                return en_weak


en_weak_lst = get_en_weak(xmas, inv_num)

print('contiguous set: ', en_weak_lst, ' Solution: ', min(en_weak_lst) + max(en_weak_lst))