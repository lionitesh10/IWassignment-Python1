list1 = []
n = int(input("Enter no of words to be entered "))
for i in range(n):
    list1.append(input("Enter word "))


def listlongest(list1):
    max1 = len(list1[0])
    for i in list1:
        if len(i) > max1:
            max1 = len(i)
    return max1


print("The length of the longest one is ", listlongest(list1))
