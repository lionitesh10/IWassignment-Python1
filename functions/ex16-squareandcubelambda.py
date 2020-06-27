list1=[]
n=int(input("Enter no of elements in list "))
print("Enter list elements ")
for i in range(n):
    list1.append(int(input()))

def sqandcube(my_list):
    square=list(map(lambda x:x**2,my_list))
    cube=list(map(lambda x:x**3,my_list))
    print(square)
    print(cube)

sqandcube(list1)