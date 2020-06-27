list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))

def filterlist(my_list):
    positive=list(filter(lambda x:x>=0,my_list))
    return positive

print("Filtered positive list of integers ",filterlist(list1))