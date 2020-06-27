list1=[]
n=int(input("Enter no of items in list "))
print("Enter Elements ")
for i in range(n):
    list1.append(input())
if len(list1)==0:
    print("List is empty ")
else:
    print("List is not empty")
