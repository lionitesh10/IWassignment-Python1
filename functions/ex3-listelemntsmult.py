list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))

def mulItems(my_list):
    mul=1
    for i in my_list:
        mul*=i
    return mul

print("Multiplication result is ",mulItems(list1))