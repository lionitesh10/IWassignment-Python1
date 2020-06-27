list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def assending(listdata):
    return listdata[1]
list1.sort(key=assending)
print(list1)