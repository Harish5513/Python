list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

print("Original list 1 : " + str(list1))
print("Original list 2 : " + str(list2))

con_list = []
for i in range(0, len(list1)):
    con_list.append(list1[i] + list2[i])

print("Resultant list is : " + str(con_list))