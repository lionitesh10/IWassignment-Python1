my_string = input("Enter comma separated words ")
words = my_string.split(",")
list2 = []
for i in words:
    if i not in list2:
        list2.append(i)
list2.sort()
output = ",".join(list2)
print(output)
