my_string = input("Enter a string ")
if len(my_string) < 3:
    print(my_string)
else:
    if my_string[-3:] == "ing":
        print(my_string+"ly")
    else:
        print(my_string+"ing")
