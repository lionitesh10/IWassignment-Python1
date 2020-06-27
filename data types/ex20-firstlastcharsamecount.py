list1 = ['abc', 'xyz', 'aba', '1221']
c = 0
for i in list1:
    if len(i) >= 2:
        if i[0] == i[-1]:
            c += 1
print("Count = ", c)
