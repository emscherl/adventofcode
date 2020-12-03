f = list(map(int, open('data')))

for i in f:
    for j in f:
        for k in f:
            if i + j + k == 2020:
                print(i)
                print(j)
                print(k)
                print(i * j * k)

# print ([i * j for i in f for j in f if i + j == 2020])

# print (f)
