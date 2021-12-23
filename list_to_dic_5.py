keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = {}
for i in keys:
    for j in values:
        result[i] = j
        values.remove(j)
        break

print(result)
