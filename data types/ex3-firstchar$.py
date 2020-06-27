my_string = input("Enter any string ")
first_char = my_string[0]
result = my_string[1:].replace(first_char, '$')
print(first_char+result)
