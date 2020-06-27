dic1={1:10,2:20,3:30,4:40,5:50,6:60}
print(dic1)
key=int(input("Enter key to remove : "))
dic1.pop(key,"No key found")
print(dic1)