import copy
list1=[]
n=int(input("Enter no of items in list "))
print("Enter Elements ")
for i in range(n):
    list1.append(input())

list2=copy.deepcopy(list1)
list2.append("Appended")

print("List 1 : ",list1)
print("List 2 : ",list2)
