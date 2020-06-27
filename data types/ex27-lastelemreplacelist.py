list1=[]
list2=[]
print("Enter lengths for main list and sublist ")
n1=int(input())
n2=int(input())
print("Enter main list items : ")
for i in range(n1):
    list1.append(int(input()))
print("Enter sublist elements : ")
for i in range(n2):
    list2.append(int(input()))
list1.pop()
list1.extend(list2)
print(list1)