with open('data.txt') as f:
    seats = f.readlines()


def seat_id(r, c):
    return r * 8 + c


id_lst = []

for s in seats:
    r_ges = 128
    r = range(127)
    c_ges = 8
    c = range(8)

    for i in range(7):
        r_ges = int(r_ges / 2)
        if s[i] == "F":
            r = r[:r_ges]
        elif s[i] == "B":
            r = r[r_ges:]
    r = r[0]

    for i in range(7, 10):
        c_ges = int(c_ges / 2)
        if s[i] == "L":
            c = c[:c_ges]
        elif s[i] == "R":
            c = c[c_ges:]
    c = c[0]

    id_lst.append(seat_id(r, c))

print(id_lst)

all_ids = []

for r in range(127):
    for c in range(8):
        all_ids.append(seat_id(r, c))

print(all_ids)

ls = [x for x in all_ids if x not in id_lst]
print(ls)

id = [x for x in ls if x-1 in id_lst and x+1 in id_lst]
print(id)
