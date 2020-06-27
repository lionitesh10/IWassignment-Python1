my_string=input("Enter your String ")
ch=input("Enter character to check ")

checkStart = lambda x: True if x.startswith(ch) else False
print(checkStart(my_string))
