def dup(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y
x = [1,2,3,4,3,2,1]

print(dup(x))