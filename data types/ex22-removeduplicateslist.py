list1=[]
out=[]
n=int(input("Enter no of items in list "))
print("Enter list items ")
for i in range(n):
    list1.append(input())
for i in list1:
    if i not in out:
        out.append(i)
list1=out
print("After removing duplicates ",list1)