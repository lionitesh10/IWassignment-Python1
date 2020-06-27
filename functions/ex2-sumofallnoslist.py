list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))

def sumOfLists(my_list):
    return sum(my_list)

print(sumOfLists(list1))