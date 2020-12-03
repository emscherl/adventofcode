f = list(map(int, open('data')))

for i in f:
    for j in f:
        if i + j == 2020:
            print(i)
            print(j)
            print(i * j)

# print ([i * j for i in f for j in f if i + j == 2020])

# print (f)
