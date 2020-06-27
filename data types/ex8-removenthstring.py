my_string = input("Enter string ")
n = int(input("Enter index of character to remove "))
if len(my_string) > 0:
    first = my_string[:n]
    second = my_string[n+1:]
    print(first+second)
else:
    print("String is empty")
