my_dict={}
print("Enter key and value to add in dictionaray or -1 to end on key term: ")
while True:
    key=int(input("Enter key : "))
    if key==-1:
        break
    else:
        value=int(input(("Enter value :")))
        my_dict[key]=value
print("Before Dictionary ",my_dict)
print("Add key , value to dictionary : ")
key=int(input("enter key "))
value=int(input("enter value "))
my_dict[key]=value

print("After Dictionary : ",my_dict)