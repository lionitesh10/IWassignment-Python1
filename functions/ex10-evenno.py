list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))

def Even(my_list):
    evn=[]
    for i in my_list:
        if i%2==0:
            evn.append(i)
        
    return evn

print("Even no list : ",Even(list1))