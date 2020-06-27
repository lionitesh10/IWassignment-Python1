dic1={1:10,2:20,3:30,4:40,5:50,6:60}
key=int(input("Enter key to see if it already exists : "))
if key in dic1.keys():
    print("Key already exists ")
else:
    print("Key does not exists ")