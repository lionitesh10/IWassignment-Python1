def Intersection(list1, list2):
    result = list(filter(lambda x: x in list1, list2))
    return result


list1, list2 = [], []


def createList(list1, n):
    print("Enter list elements ")
    for i in range(n):
        list1.append(int(input()))


n = int(input("Enter no of elements in list1 "))
createList(list1, n)
n = int(input("Enter no of elements in list2 "))
createList(list2, n)

print(Intersection(list1, list2))
