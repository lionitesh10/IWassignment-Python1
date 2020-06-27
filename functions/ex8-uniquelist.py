list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))
def uniqueList(my_list):
    out=[]
    for i in my_list:
        if i not in out:
            out.append(i)
    return out

print("UNIQUE LIST ELEMENTS ",uniqueList(list1))