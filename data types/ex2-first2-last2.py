my_string = input("Enter a string ")
if len(my_string) < 2:
    print("Empty String")
else:
    first_two = my_string[0]+my_string[1]
    last_two = my_string[-2]+my_string[-1]
    print(first_two+last_two)
