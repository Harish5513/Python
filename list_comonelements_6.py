a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in a:
    for y in b:
        if x == y:
            c.append(x)

for x in c:
    if c.count(x) > 1:
        c.remove(x)
print(c)
