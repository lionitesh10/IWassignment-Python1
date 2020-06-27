my_string = input("Enter the string ")
newstr = ""
for i in range(len(my_string)):
    if i % 2 == 0:
        newstr += my_string[i]
print("Removed odd strings result :", newstr)
